## Learning Objective

Students will learn foundational knowlege on AWS and how to create and leverage AWS services like EC2 engine, S3 bucket, and EBS volumes.


## Link to step-by-step instructions

Follow these links if you just need the links to instructions to create resources on AWS. The appropriate sections below also provide these links with elaborate discussion.

- [Open an AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
- [Create IAM user and groups](../docs/iam.md)
- [Create a free-tier EC2 instance](https://medium.com/@GalarnykMichael/aws-ec2-part-1-creating-ec2-instance-9d7f8368f78a) 
- [Create a S3 bucket](https://docs.aws.amazon.com/quickstarts/latest/s3backup/welcome.html)
- [Attach an EBS volume to EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html)
- [Install AWS CLI](https://docs.amazonaws.cn/en_us/cli/latest/userguide/install-cliv2.html)


## Contents
[1. What is cloud computing?](#what-is-cloud-computing?)

[2. Why cloud computing skills are becoming essential for data scientists?](#why-cloud-computing-skills-are-becoming-essential-for-data-scientists)

[3. Why AWS](#why-aws)?

[4. AWS resources](#aws-resources)<ul><li>[4.1. Create an AWS Account](#create-an-aws-account) <br><li>[4.2. AWS IAM](#aws-iam) <br><li> [4.3. AWS EC2](#aws-ec2)<br><uL><li>[4.3.1. Launch your own EC2 instance](#launch-your-own-instance)<br><li>[4.3.2. Connect to your instance](#connect-to-your-instance)<br><li>[4.3.3. Terminate instance](#terminate-instance)<br></ul><li>[4.4. S3 Services](#s3-services)<br><ul><li>[4.4.1. S3 data model](#s3-data-model)<br><li>[4.4.2. S3 pricing](#s3-pricing)<br><li>[4.4.3 Creating a S3 bucket](#creating-a-s3-bucket)<br></ul><li>[4.5. Elastic Block Storage (EBS)](#ebs)<br><ul><li>[4.5.1. General difference between S3 and EBS](#general-difference-between-s3-and-ebs)<br><li>[4.5.2. How to create an EBS volume](#how-to-create-an-ebs-volume)</ul></ul>

[5. Three ways to connect to AWS resources](#three-ways-to-connect-to-aws-resources)<ul><li>[5.. AWS CLI](#aws-cli)<br><li>[5.2. AWS SDK for Python](#aws-sdk-for-python)</ul>


## What is cloud computing?

Cloud computing is the use of IT resources over the Internet to store, manage, and process data. Cloud providers like Amazon Web Service (AWS) and Google Cloud provides access to technology services, such as computing power, storage, and databases as needed and on pay-per-use basis as an alternative to buying, owning, maintaining physical data centers and servers.

***Benefits***
- Reduced: <ul> 
- _Hardware cost_ 
- _Operational cost_
- _Deployment cost_</ul>
- Increased: <ul> 
- _Resiliency_ <br>
  Recoverability from failure
- _Performance_<br>
  Scale up or down the resources on a need basis
- _Capacity_ <br>
  Any resources such as compute and storage can grow seamlessly</ul>

***Cloud Computing Model***<br>
- _Full cloud deployment_ <br>
All components such as database, processing, storage in the cloud
- _Hybrid deployment_<br>
E.g., some processing on-premises, and others in the cloud

_Other way of defining cloud models_<br>
- `Infrastructure as a service (IaaS)`
<br> Entire infrastructures in the cloud: e.g., all server and network components <br>
Users manage the infrastructure themselves
- `Platform as a service (PaaS)`
<br>Cloud providers manage the infrastructure
<br> Users only manage the applications deployed on platforms
- `Software as a service (SaaS)`
<br> Just use the software developed and managed by others

## Why cloud computing skills are becoming essential for data scientists?

I want to share my own little story here with the hope to best illustrate how cloud computing is becoming mainstream in data science space. Before Wells Fargo, I worked as data scientists at Monsanto, Equifax, and PrecisionHawk. The latter was a pioneer company on commercial drones and imagery services supported by advanced robotics and software. All its data processing and web services were hosted on AWS cloud. I joined the company right after my research positions at universities, and lack of any previous cloud experience was one of the factors for my difficult time over there. When I joined Monsanto (now Bayer) in 2016, the company was undergoing full digital transformation and migrating all its data and computing resources to AWS. I needed to fully dedicate my initial few months to learn a whole host of AWS related tools and web services. Equifax, despite being a company in financial sector that is more hesitant towards cloud, recently moved to Google cloud too.

As more and more companies across industries are migrating their data centers and servers towards cloud, data scientists and machine learning engineers have no other option but to embrace the change. I had the liberty to spend quite a time learning about the technologies as those companies were just transitioning into cloud, but I suspect, they will look for at least some prior experience in cloud technologies these days while hiring their prospective data scientists.


## Why AWS?

The primary reason is due to my own lack of sufficient experience in other cloud services. However, AWS is a major player and a leading cloud service provider especially in data science and machine learning space. Once you are trained on AWS, it would not take a lot of effort to transition to other service providers, if needed, as the technologies and basic concepts overlap.


## AWS resources

There are whole host of services provided by AWS, but they generally fall into the following broad categories. In this course, we will only cover IAM (security and permission), EC2 (compute service), S3, and EBS (storage), which will be minimum for you to get started with a data science project in the cloud.

- Compute
- Storage and Content Delivery
- Database
- Networking
- Management Tools
- Security and Identity
- Application Services


### Create an AWS account


To get started with AWS, you need to create an AWS account. The account creation is free, but you need to provide your credit card information. Go ahead and create an account by following the instructions on [AWS site](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/). 

### AWS IAM

AWS identity and access management (IAM) controls authentication and authorization in an AWS account. There are four key terms of IAM: 

`User`: anyone who will use an AWS  account 

`Group`: a collection of users with shared permissions  

`Roles`: specific permission to use specific AWS resources 

`Policies`: containers for security or permission 

The intuitive way to understand these terms is to directly start working with them in AWS console. Follow the step-by-step guidelines [here](../docs/iam.md) for creating users and groups and attaching security policies to them. 

### AWS EC2

Elastic compute cloud (EC2) is the compute service and is one of the core offerings by AWS. The EC2 instances are customizable and scalable (based upon the computing requirements) and thus referred to as elastic. An EC2 instance is a virtual server in EC2 for running applications on the AWS infrastructure.

EC2 instances come in the following flavors:

- `General Purpose`: the most popular one and provides a balance of performance and cost; are ideal for applications that use these resources in equal proportions such as web servers, email servers.

- `Compute Optimized`:  ideal for compute-intensive applications that benefit from high performance processors; well suited for compute-intensive applications such as some scientific modeling or high-performance web servers, machine learning interface etc.

- `Memory Optimized`: used for workloads that process large data sets in memory such as real-time big data analytics, or running Hadoop or Spark

- `Accelerated Computing`: uses additional hardware (GPUs, FPGAs) co-processors to provide for efficient and parallel processing for tasks such as graphics rendering and deep learning.

- `Storage Optimized`: designed for low latency workloads that require sequential read and write access on large amount of datasets on local storage such as transactional database

#### Launch your own EC2 instance

-----

`T2.micro` is a `free-tier` eligible EC2 instance, which provides free 750 hours of Linux and Windows each month for one year for new AWS customers. The instance serves the learning objective of this course. If you plan to undertake your final project in AWS environment, then you might need to choose a suitable one in the future that meets the compute and memory requirements of the project. We will get back to this once you finalize your project topic.


You can find step by step instructions to create a window instance [here](https://towardsdatascience.com/aws-ec2-for-beginners-56df2e820d7f) and linux instance [here](https://medium.com/@GalarnykMichael/aws-ec2-part-1-creating-ec2-instance-9d7f8368f78a) 

####  Connect to your instance

After you launch your instance, you can connect to it and use it the way that you'd use a computer sitting in front of you. To connect to your instance using the browser-based client from the Amazon EC2 console, follow the steps below:

* Select the EC2 instance you created and choose "Connect"
* Choose EC2 Instance Connect (browser-based SSH connection), Connect.


You can also connect to a linux instance via [SSH client](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html) of your choice in your computer. In mac computer, SSH client is built in the terminal. You can use MobaXterm or PuTTY to SSH if you are using windows. Click [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html) to learn more about that.

Follow steps [here](https://gist.github.com/djsegal/9f894093165795c9350a0fedd7a8d1f5) if you want to install anaconda in the newly created instance and serve a jupyter notebook from your instance.

#### Terminate Instance

Amazon EC2 is free to start (learn more), but you should terminate your instances to prevent additional charges after exceeding the usage limit (750 hours). When you terminate the EC2 instance, all associated data will also be deleted. Select the EC2 instance, choose "Actions", select "Instance State", and "Terminate". 

You can stop the instance instead of terminating if you attach an EBS volume to EC2 and don't want the data on the volume to be deleted. We will discuss more on EBS later. The data on your EBS volume will remain after stopping while all information on the local (ephemeral) hard drive will be lost as usual. However, there will be standard charges for EBS volume. Therefore, you should only stop an instance if you plan to start it again within a reasonable timeframe. Otherwise, you might want to terminate an instance instead of stopping it for cost saving purposes.


### S3 Services

`S3` (simple storage service) is the mostly commonly used AWS service. S3 can be thought of as similar to Dropbox or Google drive, but a more scalable storage system accessible to codes and applications. AWS provides encryption to the data stored in S3 and considered secure. S3 is durable due to provision of data versioning by making multiple copies across different data centers. It automatically scales according to storage requirement, and the user pay for the storage they use.

#### S3 data model

S3 storage of objects revolves around the concept of buckets and keys. Data is stored as an object inside a S3 bucket. Each S3 object has data, a key, and metadata such as name of the object, size, and date. The object key (or key name) uniquely identifies the object in a bucket. It is helpful to think of a bucket as similar to root directory and keys as similar to subfolder and files. But it is useful to remember that data is stored in S3 as objects (not files). Learn more about the difference [here](https://www.netapp.com/us/info/what-is-object-storage.aspx). So, the S3 data model is a flat structure: there is no hierarchy of sub-buckets or subfolders. However, the logical hierarchy can be infered using key name prefixes and delimiters as the S3 console does. 

If a file named /myfiles/my_file.txt is stored inside my_s3_bucket, then myfiles/my_file.txt is the key to that file. This is important to know since APIs will ask for the bucket and key separately when you want to retrieve your file from s3.

#### S3 pricing

The rate AWS charge for s3 storage depends upon the object size, duration of storage, and frequency of access. The cost starts at $0.023 per GB per month for standard access. See Amazon S3 Pricing [here](https://aws.amazon.com/s3/pricing/) for more information.

#### Creating a s3 bucket

To create a S3 bucket, and transfer files to and from the computer, follow the instructions [here](https://docs.aws.amazon.com/quickstarts/latest/s3backup/welcome.html) on AWS site

### EBS

Elastic Block Storage (EBS) is an external disk like storage to be used with EC2 instances. The local storage that comes with EC2 instances shuts down with instances, and the data in the local storage gets lost. EBS is the answer if we need to data to live beyond the life of an EC2 instance. 

Amazon EBS volumes range from 1 GB to 16 TB in size. The storage on a volume is limited to the provisioned size and cannot be changed. The volume can be attached to any Amazon EC2 instance in the same availability Zone. Once attached, it will appear as a mounted device similar to any hard drive or other block device. At that point, the instance can interact with the volume just as it would with a local drive, formatting it with a file system or installing applications on it directly.

A volume can only be attached to one instance at a time, but many volumes can be attached to a single instance. This means that you can attach multiple volumes and stripe your data across them for increased I/O and throughput performance. This is particularly helpful for database style applications that frequently encounter many random reads and writes across the dataset. If an instance fails or is detached from an Amazon EBS volume, the volume can be attached to any other instance in that Availability Zone.


#### General difference between S3 and EBS


|    | *S3* | *EBS*|
|--- | :---: | ---: |
|*Type* | External storage | Volumes mounted on EC2 instance|
|*Storage Limit* | 1 GB to 16 TB | Unlimited|
|*Durability* | 1 in 200 to 1-in-1000 | Multiple copies|
|*EC2 Accessibility* | Same availability zone| Any availability zone|
|*Performance*| Higher latency| Lower latency
|*File listing and searching*| Slow | Fast|



#### How to create an EBS volume

An EBS volume can be created at the time of EC2 instance launch or can be created separately and mounted to a running instance. The detail instructions to create and attach different types of volumes from AWS management console can be found [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html)


## Three ways to connect to AWS resources

![](aws_3ways.png)

Most of the above discussed topics related to creating and interfacing with AWS resources were based upon using AWS management console. The other two ways include using AWS CLI and AWS SDK.

### AWS CLI

It is an open source tool to interact with AWS programmatically. Different features of AWS resources can be accessed in command line using the AWS CLI.

#### Installing AWS CLI: 

Follow the instructions on the Amazon documentation [here](https://docs.amazonaws.cn/en_us/cli/latest/userguide/install-cliv2.html) to install AWS CLI. For this course, you might want to install AWS CLI version 2. The version is still under testing and evaluation, and Amazon recommend not to use the version as of now in the production environment. But for this course, we probably don't care about that.

#### Configuring the AWS CLI


After installation, you need to configure the CLI with your amazon account. For this, type aws2 configure command in the command line. AWS CLI promts you to supply the following four parameters. The AWS CLI stores this information in a profile (a collection of settings) named default. The information in the default profile is used any time you run an AWS CLI command that doesn't explicitly specify a profile to use.

```shellscript
$ aws2 configure
```
- AWS Access Key ID [None]: 

-  Secret Access Key [None]:

-  region name [None]: 

- Default output format [None]: 

 You previously created the access keys and secret in the [AWS IAM](#aws-iam) and saved it to a secure locaiton. You could only download the keys right after they are created. They can't be recovered later though you can create a new access key again.
 

AWS CLI is the official tool from AWS. One limitation of it is that there is no tab-completion feature. There is a tool callled `aws-shell` that offers similar functionalities as AWS CLI but with tab-completion of the typed commands. It is hard to remember all the aws commands and the tab-completion feature is very useful. So if you are interested, go to the github page of the tool [here](https://github.com/awslabs/aws-shell).

Once installed and configured, You can use AWS CLI to talk to and manipulate AWS resources. Here are some examples.


**Example commands for EC2**

View Current Status of an Instance

```shellscript
aws ec2 describe-instances
```
Start a new instance

```shellscript
aws ec2 start-instances --instance-ids instnace_id
```

Stop an EC2 instance
```shellscript
aws ec2 stop-instances --instance-ids instance_id

```
**Example commands for S3**

list files in a S3 bucket

```shellscript
aws s3 ls
```

Create a new bucket
```shellscript
aws s3 mb s3://bucket-name
```

Sync the current folder and S3 
```shellscript
aws s3 sync . s3://my-bucket/path
```


## AWS SDK for Python 

Boto3 is the AWS sdk for python. Boto3 makes it easy to integrate Python application, library, or script with AWS services.

If you had already installed Anaconda, Type the following in the terminal or command line to install Boto3 on your computer.


```python
pip install boto3
```

or
```python
conda install boto3
```

if you are already familiar with python and wants to take a deep dive on boto3, follow this tutorial [here](https://realpython.com/python-boto3-aws-s3/#client-versus-resource) 


```python

```
