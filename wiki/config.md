# Configuration

## Setting Configuration
* **``pulumi config``** - command manages configuration for your stack
* **``pulumi config set``** - writes values to a stack configuration

* **``Pulumi.<stack_name>.yaml``** - represents the configuration the current stack.

## Retrieving Configuration
* You can retrieve this configuration value in your code
* You can also retrieve them from the CLI
* You can mark configuration values as secret using the **``--secret``** flag. This stops the value being stored in plaintext in any stack file or state


Set config in your code editor
```
config = pulumi.Config()
```

Setting a required config value
```
required_value = config.require('required_value')
```

To set the required config value in your terminal to set the value
```
pulumi config set required_value 'this-is-a-required-value'
```

Set an optional value
```
optional_value = config.get('optional_value')
```

Set secret value
```
secret_value = config.require_secret('secret_value')
```

To set the secret config value in your terminal to set the value
```
pulumi config set secret_value 'this-is-a-secret-value' --secret
```
