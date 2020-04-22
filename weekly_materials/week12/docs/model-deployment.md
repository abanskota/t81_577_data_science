
## Model deployment

Let's say you developed a cool model and determined that it adds a lot of business value. Now what? It's the time for model deployment. 

What is the deployment of machine learning models?

- Putting models into production <br>
- The action of making your models available to customers.<br>
- One of the most important steps in the machine learning pipeline. Business can extract more value from a model when it is fully integrated with the business systems. <br>

Like any other software product, deployment of a machine learning model is a collaborative work that requires coordination among data scientists, IT teams, and business professionals. 

## Factors affecting deployment

There are no single, optimal, one-size-fits-all deployment approaches. Apart from the people aspect (because of being highly collaborative in nature), the process is driven by various factors as below.

### Relationship with other applications

A model can typically be deployed in two ways:

**embedded model:**  <br>
Treat the model as a dependency that will be integrated within a consuming application
Model deployed as a separate service:

** Model as a service** <br>
Model is deployed as a service independently of the consuming applications

### Model characteristics

Deployment resources and workflow vary with how often and what way your model needs to be retrained.

- Does the model need to be retrained once in a while when the performance dips or gets unstable (offline training)? Or, does the model need to be continuously retrained as new data arrives (online training)?

- It can also vary the way output of the prediction is calculated. Does the prediction need to be delivered for a batch of input with lag in time or it needs to be done real-time?

- Is the model being deployed as a replacement for a legacy one? 
What time of input data and in what shape the model will consume  as input (high-res/low-res image,small text vs corpus of text etc).

### Business needs

- What is the expected volume of the requests in a given time (throughput)
- What should be the optimal response time of the model? 
- Does the model need to be highly scalable?

### Enterprise infrastructure

- Is there current language support for your model deployment or it needs to be re-coded into another language?

- Does your organization often involve reinventing infrastructure for individual projects or has developed capacity to deploy with minimum latency? 








