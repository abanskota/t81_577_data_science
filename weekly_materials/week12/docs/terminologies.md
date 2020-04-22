## Overview of some deployment related terminologies

### Web-APIs

In the second week of the course, we learned about what web-API is and how to interact with them. As a reminder, an API is a set of rules for building software and applications. The rules determine how an client application can access and consume the service (data and functionality) from a layer exposed by a server application. As the name suggests, web-API is the one that can be accessed and interacted with over the web using HTTP protocol. A machine learning model can be served as a web API so that others use the functionality of the model. A user does not need to know all the intricacies of your machine learning model, they can just send a query with model inputs to the API endpoint (URL) and receive the prediction in a predetermined format. That is what API is for. Encapsulating all the inner workings and only exposing the services to a client.


### Production vs stage vs development environment

" An environment can be thought of as a specific machine (physical or virtual), running a specific operating system and version, that is configured in a very specific way, along with having a specific, versioned set of software, programming languages (e.g., Python), and packages installed." [Source](https://www.innoarchitech.com/blog/development-vs-or-production-batch-offline-online-automated-artificial-intelligence-ai-machine-learning)

#### Development environment 
Development environments is where you developed, optimized, and tested your machine learning model. It could be your local machine, or a remote machine on a server or distributed environment. The general requirement is that that development environment shouldn't exceed the resources permitted in the environment where the model finally sits in. In one of the organizations I worked, governmental data were allowed to be used for research in development environments but not in production. Similarly, the spark compute services were available in the development but not in the production. The mismatch of the environment and their implications needs to be given due consideration by the data scientists during model development 

The other requirement is that the code in development absolutely should be tracked and managed using a version control system.


#### Staging environment

Staging environment is a setup that mimics a production environment so data availability, software and hardware do not differ significantly. It is as close as to the real thing so that models can be tested and implemented in a stable, isolated environment. In reality, however, either the staging environment doesn’t mirror a production, or the step of moving the model into the staging environment is skipped and deployed directly into the production environment.


#### Production environment

Production environment normally has machines that are highly optimized to meet expected load and demand (scalability), and are also expected to be continuously running and working properly (availability and reliability). Once your model is deemed valuable to business, successfully meets all requirements and passes all tests where applicable, it is deployed to a production environment. The production environment is where the model runs constantly and is available to consumers or end users. 


### Online learning

Online learning means that your model learns, improves and updates itself while in production. The learning algorithm is hooked to a data stream and continuously trains itself as new data comes in. A constantly updated model is immediately accessible as a web service. Technically, this is the most challenging setup to achieve, and it has mostly been used by the big players so far.

### Automated machine learning

An even more sophisticated version of online learning is automated machine learning. Instead of updating the model, you can run an entire machine learning pipeline of training and tuning  and model selection process online in production. There are some tools such as Amazon SageMaker and DataRobot that can also automatically deploy a model to production.
