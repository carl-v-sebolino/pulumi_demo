"""An AWS Python Pulumi program"""

import pulumi

config = pulumi.Config()
required_value = config.require('required_value')
optional_value = config.get('optional_value')
secret_value = config.require_secret('secret_value')


print(required_value)
print(optional_value)
print(secret_value)
