import pulumi
import pulumi_aws as aws
import mimetypes
import os

# set configuration
config = pulumi.Config()
site_dir = config.require('site_dir')


# create an S3 bucket
bucket = aws.s3.Bucket('my-pulumi-bucket', website={
    'index_document': 'index.html',
})

file_path = os.path.join(site_dir, 'index.html')  # add file to the bucket
mime_type, _ = mimetypes.guess_type(file_path)

# read file
obj = aws.s3.BucketObject('index.html', bucket=bucket.bucket,
                          source=pulumi.FileAsset(file_path),
                          acl='public-read',
                          content_type=mime_type,
                          )

pulumi.export('bucket_name', bucket.bucket)  # output the bucket name
# export the bucket endpoint (the full url)
pulumi.export('bucket_endpoint', pulumi.Output.concat(
    'http://', bucket.website_endpoint))
