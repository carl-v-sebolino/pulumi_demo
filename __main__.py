import pulumi
from pulumi import automation as auto
from pulumi_aws import s3

""" A simple Automation API program """

def pulumi_program():
    # Create a bucket and expose a website index document
    site_bucket = s3.Bucket('s3-website-bucket', website=s3.BucketWebsiteArgs(index_document='index.html'))
    index_content = """
    <html>
        <head><title>Hello S3</title><meta charset="UTF-8"></head>
        <body>
            <p>Hello, world!</p>
        </body>
    </html>
    """
    # Write our index.html into the site bucket.
    s3.BucketObject("index",
                    bucket=site_bucket.id,  # Reference to the s3.Bucket object.
                    content=index_content,
                    key="index.html",  # Set the key of the object.
                    content_type="text/html; charset=utf-8")  # Set the MIME type of the file.

    # Set the access policy for the bucket so all objects are readable.
    s3.BucketPolicy("bucket-policy", bucket=site_bucket.id, policy={
        "Version": "2012-10-17",
        "Statement": {
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            # Policy refers to bucket explicitly.
            "Resource": [pulumi.Output.concat("arn:aws:s3:::", site_bucket.id, "/*")]
        },
    })

    # Export the website URL.
    pulumi.export("website_url", site_bucket.website_endpoint)

project_name = 'simple_automation_api_demo'
stack_name = 'dev'

stack = auto.create_or_select_stack(stack_name=stack_name, project_name=project_name, program=pulumi_program)

stack.workspace.install_plugin('aws', 'v4.0.0')
stack.set_config('aws:region', auto.ConfigValue(value='ap-southeast-1'))
# stack.destroy()
up_res = stack.up(on_output=print)