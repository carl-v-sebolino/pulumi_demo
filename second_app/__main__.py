import pulumi

config = pulumi.Config()
stack = pulumi.get_stack()

# org is set to the organization associated with your account
# if you have an individual account, the org is your account name
org = config.require('org')

stack_ref = pulumi.StackReference(f'{org}/pulumi_demo/{stack}')
pulumi.export('shop_url', stack_ref.get_output('url'))
