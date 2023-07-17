import pulumi

config = pulumi.Config()
REQUIRED_VALUE = config.require('required_value')
OPTIONAL_VALUE = config.get('optional_value')
SECRET_VALUE = config.require_secret('secret_value')

print(REQUIRED_VALUE)
print(OPTIONAL_VALUE)
print(SECRET_VALUE)

front_end_port = '3000'
pulumi.export('url', pulumi.Output.format(
    'https://localhost:{0}', front_end_port))
