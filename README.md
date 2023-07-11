# Introduction to Pulumi
A demo project to get you started with the basics of Pulumi

- Pulumi is an IaC library, enabling you to manage your infrastructure in your favorite language. It is available across all common languages, such as Python, Go, Javascript, C#, Typescript, etc., and supports all major cloud providers, like AWS, Azure, and GCP.

## Terminology
* Pulumi Project
    * A project is a folder containing Pulumi code
    * Projects must contain a Pulumi.yaml file, which has information Pulumi needed
    * Info such as the chosen language runtime, a name and description are stored here

* Pulumi Resource
    * A resource is any object or "thing" managed by Pulumi
    * Depending on your chosen provider and language, a resource could be anything from
    an S3 bucket to Kubernetes cluster
    * You define resource in code with Pulumi and the Pulumi engine makes that code declarative

* Pulumi Program
    * Is a collection of resources
    * Programs are used to group resources together. All the resources in a program are evaluated when you run **``pulumi up``**
    * Your programs can contain as many resources as you like, It's often good practice to group related resources together.

* Pulumi Stack
    * A stack is an uniquely configured instances of a Pulumi program
    * Stacks are very flexible, but are often used to make programs have different configuration values depending on how they're deployed.
    * A common usage of stacks is to switch values between environments (such as dev, stg, and prod)

* Pulumi Provider
    * A provider interacts with an infrastructure an Pulumi's behalf
    * Pulumi has providers for many of the popular cloud providers such as AWS, Azure, Google Cloud, and Kubernetes
    * A provider has 2 components
        - The language SDK
        - A binary (or plugin)
        - Both must be installed to use Pulumi with a specific cloud

* Pulumi Output
    * Output is a special value in Pulumi
    * It holds a computed value which Pulumi does not know at runtime. This is usually a value returned by a cloud provider's API
    * An example of this might be an instance ID when creating an EC2 instance or a container ID when creating a Docker container
    * Example: ``` pulumi.export('bucket_name', bucket.id) ```

* Pulumi State
    * State is where Pulumi stores the result of its execution
    * The default state is the Pulumi Saas, which is configured when you login to Pulumi
    * It's possible to store your state in other place. By default it is stored in Pulumi.

* Pulumi Console
    * Is the key to your interaction with Pulumi

## Create an Account
* Pulumi requires a way to store your state
* Pulumi offers a free account for individuals
* Paid plans for teams
* Create an account [here](https://app.pulumi.com/signup)

## Installation
- For installation please refer to this <a href="https://www.pulumi.com/docs/install/" target="_blank">link.</a>

## Logging In
- Logging in sets up your *state*
- Logging in is a global operation
- When logging in you select your *backend*
- Type the ``` pulumi login ``` command to login

## You Can Choose a Programming Language
- In this case we will use Python
- You can download the Python installer [here](https://www.python.org/downloads/)


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

### Initialize Your Project
* By typing the **```pulumi new```** command it will give you a list of the different templates that are available depending on your cloud provider and depending on what you need to do.
* In this case we're gonna use **``pulumi new aws-python``**


### Inspect Files
* **``__main__.py``** - will serve as the main entry point of your Pulumi program.
* **``Pulumi.yaml``** - represents the main cofiguration file of the project itself.
* **``venv``** - a virtualenv for your project.
* **``requirements.txt``** - your project's Python dependency information.
