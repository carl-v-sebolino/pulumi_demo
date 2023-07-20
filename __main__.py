import pulumi
import pulumi_aws as aws


ami = aws.ec2.get_ami(
    most_recent=True,
    owners=["137112412989"],
    filters=[{"name":"name","values":["amzn-ami-hvm-*-x86_64-ebs"]}]
)

# Get the default VPC
vpc = aws.ec2.get_vpc(default=True)

# Create a security group
group = aws.ec2.SecurityGroup(
    "web-secgrp",
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'icmp', 'from_port': 8, 'to_port': 0, 'cidr_blocks': ['0.0.0.0/0'] },
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] },
    ],
    egress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] },
    ]
)

"""
Adding a load balancer
    Add a load balancer in order to distribute the load evenly.
    We will have just a single URL that we can go to and the load balancer will
    automatically the load balancer will determine which availability zone to
    get the data from. Very helpful when dealing with large users the data can
    be loaded depending on where the load is the lowest
    so that it can balance the load across the servers.
"""

# CREATE A VPC SUBNETS
vpc_subnet = aws.ec2.get_subnet_ids(vpc_id=vpc.id)

# CREATE LOAD BALANCER
lb = aws.lb.LoadBalancer(
    'loadbalancer',
    internal=False,
    security_groups=[group.id],
    subnets=vpc_subnet.ids,
    load_balancer_type='application',
)

target_group = aws.lb.TargetGroup(
    'target-group',
    port=80,
    protocol='HTTP',
    target_type='ip',
    vpc_id=vpc.id,
)

listener = aws.lb.Listener(
    'listener',
    load_balancer_arn=lb.arn,
    port=80,
    default_actions=[{'type': 'forward', 'target_group_arn': target_group.arn}],
)

# CREATING A SIMPLE WEB SERVER
# server = aws.ec2.Instance(
#     'web-server',
#     instance_type='t2.micro',
#     vpc_security_group_ids=[group.id],
#     ami=ami.id,
#     user_data="""
# #!/bin/bash
# echo "Hello, World" > index.html
# nohup python -m SimpleHTTPServer 80 &
# """,
#     tags={
#         'Name': 'web-server',
#     }
# )
# pulumi.export('ip', server.public_ip)
# pulumi.export('hostname', server.public_dns)

"""
Create more EC2 instances each running the same Python webserver
and we're gonna make them across the aws availability zones in the region
"""
ips = []
hostnames = []

for az in aws.get_availability_zone().names:
    server = aws.ec2.Instance(
        f'web-server-{az}',
        instance_type='t2-micro',
        # vpc_security_group_ids=[group.id],
        security_groups=[group.name], # for load balancing
        ami=ami.ida,
        availability_zone=az,
        user_data="""
    #!/bin/bash
    echo \"Hello World! -- from {} \" > index.html
    nohup python -m SimpleHTTPServer 80 &
    """.format(az),
        tags={
            'Name': 'web-server',
        }
    )
    ips.append(server.public_ip)
    hostnames.append(server.public_dns)
    attachment = aws.lb.TargetGroupAttachment(
        f'web-server-{az}',
        target_group_arn=target_group.arn,
        target_id=server.private_ip,
        port=80,
    )

pulumi.export('ips', ips)
pulumi.export('hostnames', hostnames)
pulumi.export('url', lb.dns_name)
