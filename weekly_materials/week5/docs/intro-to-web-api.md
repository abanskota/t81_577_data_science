### Into to web API


Data is being increasingly served from the web using APIs. Digital data companies like Twitter, Facebook, or Google have tons of new and changing data everyday, and serving  via API makes data easily accessible to their users. API also allow users to efficiently retrieve a small subset of relevant data from a large database hosted on the web. This is not only true for the big Silicon Valley companies but also for the others who host their enterprise data on cloud. For example, Bayer crop science (formerly Monsanto and my former employer) used to serve its products, customers, and geospatial data almost entirely via APIs to internal users.


#### What is API?

An application programming interface (API) is a set of rules for building software and applications. The rules determine how an  client application can access and consume the service (data and functionality) from a layer exposed by a server application. 

In the final week of this course, you are going to learn how to serve the model you built via a web API so that others can consume the service of your model. A user does not need to know all the intricacies of your machine learning model, they can just send a query with model inputs to the API endpoint (URL) and receive the prediction in a predetermined format. That is what API is for. Encapsulating all the inner workings and only exposing the services to a client.

As the name suggests, Web API is the one that can be accessed and interacted with over the web using HTTP protocol. Users make requests to specific web services and retrieve relevant resources back as response. While visiting a website through a browser (a client) such as Chrome, we implicitely make a request to a server to serve the page in HTML format, and the browser formats and presents the response as a nice-looking web page. Web API is different in a sense that the request is made for only a specific service (or data), and the server would just return the specific response likely in JSON or XML format.

REST(Representational state transfer) API uses HTTP (Hyper Text Transfer Prototocal) for communication between server and client. Most common WEB APIs in the present days are built with REST architecture. Visit this [site](https://restfulapi.net/)if you want to learn more about REST architecture and APIs.


A client can make the following four main types of HTTP requests to interact with a web API. We will learn in the next section what a HTTP request looks like and how to format and send one.

<ul><li> 

**GET**:  to get information, data, metadata,etc. GET does not modify the resources, and normally, this is the only request a service consumer of an API makes. <li>
    
**POST**: to create a new resource into the collection of resources.
<li>
    
**PUT**:  to changes existing information
<li>
    
**DELETE**: to delete existing information
</ul>

Clients not necessarily always receive intended response for their requests. A request might fail for several reasons such as invalid request, lack of existence of service, or problem on server. All responses to client’s requests consist of HTTP status codes such as:

Status code `200` (**success**):  The request is valid and the clients retrieve what they requested.<br>
Status code `400`(**bad request**): Something went wrong such as due to badly formatted requests or authentication issue. <br>
Status code `500`(**server error**) : There was nothing wrong with the request but something with the server.<br>

An application client such as python program to interact with an API should always check the HTTP status code before trying to do any other things with the response. Now that you have a general idea of API, methods to talk to API and status codes of the response, we will start learning how to make requests to APIs first with a software client named `POSTMAN` and then with  python library named `requests`.
