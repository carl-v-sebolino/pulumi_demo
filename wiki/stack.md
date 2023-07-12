# Stack
* Every program has corresponding stacks, or isolated, independently configurable instances of your Pulumi program.
* The default is **``dev``**
* You must set up a config for each stack

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