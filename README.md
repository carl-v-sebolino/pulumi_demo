# Introduction to Pulumi
A demo project to get you started with the basics of Pulumi

- Pulumi is an IaC library, enabling you to manage your infrastructure in your favorite language. It is available across all common languages, such as Python, Go, Javascript, C#, Typescript, etc., and supports all major cloud providers, like AWS, Azure, and GCP.

## Installation
- For installation please refer to this <a href="https://www.pulumi.com/docs/install/" target="_blank">link.</a>

## Creating a Pulumi Project
* Infrastructure in Pulumi is organized into *projects*
* Project
    * A project represents a Pulumi program that, when run, declares the desired infrastructure for Pulumi to manage.
* Stacks
    * The program has corresponding stacks, or isolated, independently configurable instances of your Pulumi program.

### Create a Directory For Your Project
* Each Pulumi project lives in its own directory. Create one now and change into it by running these commands in your terminal:
```
mkdir pulumi_demo_app
cd pulumi_demo_app
```

### Initialize your project


### Inspect Files
**``__main__.py``** - will serve as the main entry point of your Pulumi program.

**``Pulumi.yaml``** - represents the main cofiguration file of the project itself.