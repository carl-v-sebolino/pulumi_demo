# Laboratory 1
This example will demonstrate how to easily deploy a static website.

Before you get started using Pulumi, let’s run through a few quick steps to ensure your environment is set up correctly.

## Install Pulumi
- Follow this installation [guide](https://www.pulumi.com/docs/install/)

## Install Language Runtime
- In this example will be using Python
- Install [Python version 3.7 or later](https://www.python.org/downloads/). To reduce potential issues with setting up your Python environment on Windows or macOS, you should install Python through the official Python installer.
-
If you're having trouble setting up Python on your machine, see [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/) for detailed installation instructions on various operating systems and distributions.

## Configure Pulumi to access your AWS account
- Pulumi requires cloud credentials to manage and provision resources. You must use an IAM user account that has **Programmatic access** with rights to deploy and manage resources handled through Pulumi.
- Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Configure [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- If you have previously installed and configured the AWS CLI, Pulumi will respect and use your configuration settings.
- For additional information on setting and using AWS credentials, see [AWS Setup](https://www.pulumi.com/registry/packages/aws/installation-configuration/)

For code example checkout the branch **`lab1`**

To set the value for **``site_dir``** config

Type the following command in your terminal:
```
pulumi config set pulumi_demo: site_dir <site_directory_name>
```
To run the program type **``pulumi up``** in your terminal