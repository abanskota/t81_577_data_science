### Into to web API

``` I had a hard time figuring out what API was. I met a lot of people talking about APIs without them telling me what actually it was. My impression was that the most people pretended to know what API was, and I started doing the same.```

Data is being increasingly served from the web using APIs. Digital data companies like Twitter, Facebook, or Google have tons of new and changing data everyday, and serving  the data via API makes it easily accessible to users. API will also allow users to efficiently retrieve  a small subset of relevant data from a large database hosted on the web.

This is not only true for the big Silicon Valley companies; many others, who host their enterprise data on cloud, also routinely leverage API. For example, Bayer crop science (formerly Monsanto and my former employer) used to serve data such as those related to their products, customers, and agricultural fields almost entirely via APIs to its internal users.

What are APIs? An application programming interface (API) is a set of rules for building software and applications. The rules determine how an application client  can access and consume the service from an exposed layer by the service provider. API can serve both data and functionality. In the final week of  this course,  you are going to learn how to serve the model you built as a web API for others to consume the service of your model. A user does not need to know intricacies of your machine learning model, they can just send a query with model inputs to the API endpoint (URL) and receive the prediction in a predetermined format. That is what API is for. Encapsulating all the inner workings and only exposing the service to a client.

Web API as the name suggests, is an API that can be accessed and interacted with over the web using HTTP protocol. Users make requests to specific web services and retrieve relevant resources back as a response. Such API that uses HTTP requests for communication with web services are called REST (Representational state transfer) API. Visit this [site](https://restfulapi.net/) if you want to learn more about REST architecture and APIs.

A client can make the following four main types of HTTP requests to interact with a web API. We will learn in the next section what the HTTP requests look like and how to format and send them.

`GET`:  to get information, data, metadata,etc. GET does not modify the resources, and normally,  this is the only request a service consumer of an API makes. 
`POST`: to create a new resource into the collection of resources.
`PUT`:  to changes existing information
`DELETE`: to delete existing information

Obviously, clients don’t always receive what they request for. A request might fail for several reasons such as invalid request, lack of service existence, or problem on server. All responses to client’s requests consist of HTTP status codes such as:

Status code `200` (**success**):  The request is valid and the clients retrieve what they requested.
Status code `400`(**bad request**): Something went wrong such as due to badly formatted requests or authentication issue. 
Status code `500`(**server error**) : There was nothing wrong with the request but something with the server.

An application client such as python program to interact with an API should always check the HTTP status code before trying to do any other things with the response. Now that you have a general idea of API, methods to talk to API and status codes of the response, we will start learning how to make requests to APIs first with a software client named `POSTMAN` and then with  python library named `requests`.
