## Docker in data science

### What is Docker?

- It can be though of as lightweight virtual machines that contain everything required for running an application. 

- Unlike VM, docker is much faster to spin up and can re-use layers from other containers making it much faster to build and share.

- A docker container can capture a snapshot of the state of your system so that someone else can quickly re-create your compute environment.

### Why docker is valuable for data scientists?

- You most like colloborate with fellow data scientists during development of the model and IT people for deployment. You almost certainly require the same major (and maybe minor) version of Python and library versions and probably similiar OS to share your work seamlessly. Wrapping everything in a Docker container reduces the burden on others of recreating your environment and makes your work more accessible. 

- Docker makes the process of porting your environment (all of your libraries, files, etc.) very easy. It can be used on your local machine, your coworker’s machine, or a cloud provider’s servers. 

- Being comfortable with Docker can allow you to deploy your models or analyses as applications (for example as a REST API endpoint that can serve predictions) that make your work accessible to others. Furthermore, other applications that you may need to interact with as part of your data science workflow may exist in a Docker container such as a database or other application.

### Basic docker terminology to get started

**Image**

A blueprint for what you want to build. It contains the Dockerfile, libraries, and code your application needs to run, all bundled together.Ex: Ubuntu + TensorFlow +  a running Jupyter Server.

**Container**

An instantiation of an image, multiple containers can be run on top of the same image running. You can think of an image as the executable file, and the running process spawned by that file as the container.

**Dockerfile**

A Dockerfile is a file with instructions for how Docker should assemble your image.

**Container Registry**
Docker containers offer version control, and hence the change at any stage can be committed. If you want other people to be able to make containers from your image, you send the image to a container registry. Docker Hub is the largest registry and the default.

**Layer** modification to an existing image, represented by an instruction in the Dockerfile. Layers are applied in sequence to the base image to create the final image.

### How to install

Download and install docker from [here](https://www.docker.com/products/container-runtime#/download). If you happen to have chromebook like me, follow the instructions [here](https://willschenk.com/articles/2019/setting_up_chromebook/)


You can get started with docker by following the tutorials for begeniers from [here](https://docker-curriculum.com/#getting-started). In the following section, you will see examples of creating a docker container to spin up a jupyter notebook server and to serve the flask app we created in the last section as web api.


In order to run the Flask app you created with Docker container, you first need to build a docker image. For that you need a dockerfile, It is a plain text file with instructions and arguments. Here is the description of the instructions we’re going to use in our next example:


FROM — set base image
RUN — execute command in container
ENV — set environment variable
WORKDIR — set working directory
VOLUME — create mount-point for a volume
CMD — set executable for container


create a text file `Dockerfile` without extension. Edit the file with the following parameters, change the python matching the version in your local, not mandatory though because Docker will get it from registry if you don't have that version.

```bash
FROM python:3.7.4
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
```

Being inside the directory, run the following command to build your docker image. Don't miss the `.` , whihc means build in the current directory.

```bash
docker build -t docker_flask:latest .
```

You will see bunch of messages with final two lines showing this:

```bash
Successfully built f5dc09ab1765
Successfully tagged docker_flask:latest
```

Run the build you just created using the following command:

```bash
docker run -d -p 5000:5000 docker_flask:latest
```

Follow [this](https://medium.com/@doedotdev/docker-flask-a-simple-tutorial-bbcb2f4110b5
) tutorial based on which I created this lecture for more dicsussion on those commands.



