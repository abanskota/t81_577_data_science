In this lecture, you will learn:


- How an analytical model that needs to be updated frequently can be converted into an Airflow workflow. 


In [week10](https://github.com/abanskota/t81_577_data_science/blob/master/weekly_materials/week10/notebooks/scikit-learn-pipeline.ipynb), we learn about how to streamline a machine learning workflow using a pipeline. We saw that a pipeline allows us to chain multiple preprocessing, model fitting, evaluation, and prediction steps into an automated workflow. If your model doesn't need to be trained on new dataset frequently and periodically, the deployment solution similar to what we learnt last week (pipeline + pickled model + flask) might serve well for the purpose. However, if the model needs to be trained online with peridic stream of data, then we need to consider various things:

- how to ingest the incoming data
- how to combine and transform the newly ingested data
- how to schedule periodic training
- how to efficiently handle error
- how to automatically try more attempts in case of error
- how to monitor and communicate updated status and performance of model

Apache Airflow can be your friend in such situation to automate the end to end ML process from data ingestion to deployment and monitoring. Airflow is a platform to programmatically author, schedule and monitor workflows. One of the main advantages of using a workflow system like Airflow is that all is code, which makes your workflows explicit, maintainable, versionable, testable, and collaborative.

- Integrates with a number of sources (databases, filesystems)
- Tracks failure, retries, success
- Enable identify the dependencies and execution
- Provides built-in support for scheduling using schedulers
- Provides web interfaces


### Basic Airflow concepts

**Task**: a defined unit of work (these are called operators in Airflow)
**Task instance**: an individual run of a single task. Task instances also have an indicative state, which could be “running”, “success”, “failed”, “skipped”, “up for retry”, etc.
**DAG**: Directed acyclic graph, a set of tasks with explicit execution order, beginning, and end
**DAG run**: individual execution/run of a DAG

<img src="https://airflow-tutorial.readthedocs.io/en/latest/_images/DAG.png" alt="_images/DAG.png"/>


### Example

While any ML model can be deployed as workflow, the benefit would be more obvious with the example we follow here.


Let's first understand the problem situation of the example. Imagine you need to monitor the company's database to identify duplicate records and remove them peridically. The records might contain fields like name and address of people, which might not always entered similarly. So finding the duplicates mean you need to employ some fuzzy matching techniques. so the core model comprise of periodically ingesting new records into your database, if those records don't match with the existing one using fuzzy techniques.

The workflow consist of:

- Ingest new data periodically 
- Fuzzy match data with the current records in the database 
- Insert new data into database if not matched

Here, we will use fake data generated from python library to create a table in Postgres.
- The new data will also be created by the same library. 
- The first name, last name, and address of the fields of the new record are cleaned (preprocessed)
- that are comnew record will be run against all the records in the database to compute Jaro distance (a fuzzy matching) between first name, last name, score by an al

In order for the examples workflow in this tutorial to run, you need to have postgress installed in the computer by following the instruction [here](https://github.com/abanskota/t81_577_data_science/blob/master/weekly_materials/week5/docs/accessing-data-from-postgres.md) or from [here](
https://blog.crunchydata.com/blog/easy-postgresql-10-and-pgadmin-4-setup-with-docker) if you prefer to install from docker.

Airflow can also be installed both locally and using docker. However, local installation can be very problematic compared to docker installation. In this tutorial, we will use the pre-built docker image named `puckel/docker-airflow`. We previously learnt how to install docker and register to docker hub. All you need to do is to run the following command to pull a docker image for airflow.

```bash
docker pull puckel/docker-airflow
```

 Run the following command to create a running container from the pulled image.

```bash
docker run -d -p 8080:8080 puckel/docker-airflow webserver

You can now paste localhost:8080 in your local browser to access airflow UI.

```
On the command line, you can find the container name by running:

```bash
docker ps
```

You can jump into your running container’s command line using the command:
```bash
docker exec -ti <container name> bash
```

### Instantiate a DAG
We'll need a DAG object to nest our tasks into. 

`dag_id` serves as a unique identifier for your DAG. We also pass the default argument dictionary named `dag_params` as a default set of arguments to each task's constructor.

```python dag_params = {
    'dag_id': 'Jaro_dag',
    'start_date': datetime(2019, 10, 7),
    'email': email_list,
    'schedule_interval': None
}
dag = DAG(dag_id = 'jaro_dag',default_args = dag_params)
```

### Defining tasks

Tasks are defined as abstraction of relevenat Operators. Following are the examples of defining a taks of email notification with EmailOperator and a task of running a python function using  PythonOperator.The first argument task_id acts as a unique identifier for the task.

```python
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import PythonOperator

email_list = ["asimbanskota@gmail.com", ""]

email_success = EmailOperator(
        task_id='email_success',
        to=email_list,
        subject='Airflow Alert Success',
        html_content=""" <h3>new data insertion success</h3> """,
        dag=dag
)

run_analysis = PythonOperator(task_id = 'run_analysis', python_callable = run_analysis, dag = dag)
```

### Setting up Dependencies
run_analysis >> email_success


### DAG definition file

In Airflow, DAGs definition files are python scripts (“configuration as code” is one of the advantages of Airflow). You create a simple DAG by with dag object, task definitions, and their dependencies as above described. The DAG defnition file need to go inside the `/usr/local/airflow/dags` directory. But as we are working inside docker container, we don't want to add the DAG definition files directly in there and use a `volumne` to mount to share a directory between local machine and the Docker container. In order to map the local directory to container, we need to run the docker container as follows with flag `-v`.

```bash
docker run -d -p 8080:8080 -v /home/asimbanskota/airflow/dags:/usr/local/airflow/dags puckel/docker-airflow webserver
```

In order to install the extra python packages, you can create a requirments.txt and map the file simiilar way as for dags folder.
```bash
docker run -d -p 8080:8080 -v /home/asimbanskota/airflow/dags:/usr/local/airflow/dags -v $(pwd)/requirements.txt:/requirements.txt  puckel/docker-airflow webserver
```

you need to run docker container as root user as below.
```bash
docker exec -ti  --user root <container_name>  bash
```

To be continued......


netstat -ano | grep :5432

