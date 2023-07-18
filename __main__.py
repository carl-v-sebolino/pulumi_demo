import pulumi
import pulumi_aws_native as aws_native
import pulumi_aws as aws_classic
import json

# bucket = aws_native.s3.Bucket(
#     'my-bucket',
#     public_access_block_configuration=aws_native.s3.BucketPublicAccessBlockConfigurationArgs(
#         block_public_policy=False,
#     )
# )

# bucket_policy = aws_classic.s3.BucketPolicy(
#     'my-bucket-policy',
#     bucket=bucket.id,
#     policy=bucket.arn.apply(
#         lambda arn: json.dumps(
#             {
#                 'Version': '2012-10-17',
#                 'Statement': [
#                     {
#                         'Effect': 'Allow',
#                         'Principal': "*",
#                         'Action': ['s3.GetObject'],
#                         'Resource': [f'{arn}/*'],
#                     }
#                 ]
#             }
#         )
#     ),
#     opts=pulumi.ResourceOptions(parent=bucket)
# )

# pulumi.export('bucket', bucket.bucket_name)

"""
Let's encapsulate the code into something more reusable. We could start out by creating a resource grouping for the kind of resource we wanted to use:
"""

# class OurBucketClass:
#     _POLICIES = {
#             "default": {
#                 "Effect": "Allow",
#                 "Principal": "*",
#                 "Action": ["s3:GetObject"],
#             },
#             "locked": {
#                 # ...
#             },
#             "permissive": {
#                 # ...
#             },
#         }

#     def __init__(self, name: str, policy_type: str) -> None:
#         self._bucket = aws_native.s3.Bucket(
#             name,
#             public_access_block_configuration=aws_native.s3.BucketPublicAccessBlockConfigurationArgs(
#                 block_public_policy=False,
#             )
#         )

#         self._bucket_policy = aws_classic.s3.BucketPolicy(
#             f'{name}-policy',
#             bucket=self._bucket.id,
#             policy=self._get_bucket_policy(policy_type),
#             opts=pulumi.ResourceOptions(parent=self._bucket)
#         )

#     def _get_bucket_policy(self, policy_type: str) -> pulumi.Output:
#         try:
#             statement = self._POLICIES[policy_type]
#         except KeyError as e:
#             add_note = "Policy type needs to be 'default', 'locked', or 'permissive'"
#             raise ValueError(f'{add_note}. You used {policy_type}.') from e
#         return self._bucket.arn.apply(lambda arn: json.dumps(
#             {
#                 'Version': '2012-10-17',
#                 'Statement': [
#                     {**statement, 'Resource': [f'{arn}/*']},
#                 ]
#             }
#         ))

# bucket = OurBucketClass('my-bucket', 'default')

"""
Create a class that encapsulates the functionality while subclassing the ComponentResource class (using the ComponentResource class as a template).

"""
class OurBucketComponent(pulumi.ComponentResource):
    def __init__(self, name_me, policy_name='default', opts=None) -> None:
        """
        By calling super(), we ensure any instantiation of this class inherits
        from the ComponentResource class so we don't have to declare all the
        same things all over again
        """
        super().__init__('pkg:index:OurBucketComponent', name_me, None, opts)
        """
        This definition ensures the new component resource acts like anything
        else in the Pulumi ecosystem when being called in code.
        """
        child_opts = pulumi.ResourceOptions(parent=self)
        self.name_me = name_me
        self.policy_name = policy_name
        self.bucket = aws_native.s3.Bucket(f'{self.name_me}')
        self.policy_list = {
            "default": {
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject"],
            },
        }
        """
        We also need to register all the expected output for this component
        resource that will returned by default
        """
        self.register_outputs({
            'bucket_name': self.bucket.bucket_name
        })

    def define_policy(self):
        policy_name = self.policy_name
        try:
            json_data = self.policy_list[f"{policy_name}"]
            policy = self.bucket.arn.apply(
                lambda arn: json.dumps(
                    {
                        'Version': '2012-10-17',
                        'Statement': [
                            {**json_data, 'Resource': [f'{arn}/*']},
                        ]
                    }
                )
            )
            return policy
        except KeyError as err:
            add_note = "Policy name needs to be 'default', 'locked', or 'permissive'"
            print(f"Error: {add_note}. You used {policy_name}.")
            raise

    def set_policy(self):
        bucket_policy = aws_classic.s3.BucketPolicy(
            f"{self.name_me}-policy",
            bucket=self.bucket.id,
            policy=self.define_policy(),
            opts=pulumi.ResourceOptions(parent=self.bucket)
        )
        return bucket_policy

bucket1 = OurBucketComponent('test-bucket-1', 'default')
bucket1.set_policy()
pulumi.export('bucket_name', bucket1.bucket.id)