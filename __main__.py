"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
# create an instance of the aws s3 bucket
bucket = s3.Bucket('my-bucket')
"""
The same as
s3.Bucket('my-bucket')
"""

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
