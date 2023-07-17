# Stack
* When you bootstrap a project, you have to initialize a stack
* Every program has corresponding stacks, or isolated, independently configurable instances of your Pulumi program.
* The default is **``dev``**
* You can set up a config for each stack
* You can also copy config between stacks

Create a stack
```
pulumi stack init <stack_name>
```
Show the different stacks that are available
```
pulumi stack ls
```

Select a stack
```
pulumi stack select <stack_name>
```

Delete a stack
```
pulumi stack rm <stack_name>
```
## Stack Output
We can also get this value by running **``pulumi stack output <key>``** on any particular stack.

## Stack References
* You can retrieve exported outputs and use them in new projects
* Allow you to access the outputs of one stack from another stack.

Example code:
```
stack = pulumi.get_stack()
org = 'foo_organization'
stack_ref = pulumi.StackReference(f'{org}/stack_sample/{stack}')
exported_value_from_other_stack = stack_ref.get_output('exported_value')
```
* **``exported_value``** - This string is the output variable from the other stack within your project.

## Making a stack configurable
* One of the main reasons to use stacks is to have different configurations between them.
* For example you can set a different configuration for a **`dev`** and a **`staging`** stack

## Working with Secrets
* To encrypt a configuration setting before runtime, you can use the CLI command **``pulumi config``** set command with a **``--secret``** flag. All these encrypted values are stored in your state file.
```
pulumi config set --secret <key> <value>
```
* If we would like to get the plain-text value, we can do it with this command:
```
pulumi stack output <key_name> --show-secrets
```