import pulumi

front_end_port = '3000'
pulumi.export('url', pulumi.Output.format(
    'https://localhost:{0}', '3000'))
