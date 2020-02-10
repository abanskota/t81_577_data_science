## Learning objective: Learn how to fetch data from a table in a relational database (PostgreSQL) using psycopg2 library




## Install PostgreSQL 

PostgreSql (aka Postgres) is a popular open-source relational database management system (DBMS). A relational DBMS employs the relational data model in which data are organized into table-like(row-column) structure. Postgres allows us to perform tasks such as control access to a relational database, read and write data into database and run queries. 

 In order to learn how to connect to the databases and read data into python, it is necesary to have Postgres installed on your working computer or have access to one on Web or server. Visit this [link](https://www.2ndquadrant.com/en/blog/pginstaller-install-postgresql/) for a step-by-step instruction to install Postgres in your machine.

Once installed, we need to start the server. Go to this [link](https://tableplus.com/blog/2018/10/how-to-start-stop-restart-postgresql-server.html) to configure and start the server in Windows or to this [link] for Mac.

Once the server is started, type `psql` in your command line. `psql` enables us to send queries interactively, issue them to Postgres, and see the query results.

Type the following in the `psql` prompt to create a new database named `t81577`:

```bash
CREATE DATABASE t81577;
```

### Connect to the database using psycopg2

To connect to the database we just created, we will use a python library named `psycopg2`. The library has connect() method that takes in some parameters to connect to Postgres server and returns a Connection object. The default value for the `username` and `password` parameters is `postgres`. Pass in the right parameters in case you changed them after installation.

```python
import psycopg2
conn = psycopg2.connect(host="localhost",database="t81577", user="postgres", password="postgres")
```

The connection object creates a client session with the database server. To execute commands and queries against the database, you will also need to create another object called the Cursor object, which is created by the Connection object.

```python
cur = conn.cursor()
```

### Load a csv data into postgres


TODO: COMPLETE THIS SECTION


CSV_TABLE = '/home/asimbanskota/t81_577_data_science/weekly_materials/week5/files/city.csv'. The table has five columns: `id`, `lat`, `lon`, `city`, and `state` as shown below. 


![](../files/tables.png)

To load the table in Postgres, we first need to create an empty table with schema describing data types for all columns in the table. We learnt earlier how to create a cursor object from a connection to Postgres. To execute any command, you need to call the execute method of the cursor by passing the Postgresql command as below for creating a table:

```python
import psycopg2
conn = psycopg2.connect(host="localhost",database="t81577", user="postgres", password="postgres")
cur = conn.cursor()
cur.execute("""
CREATE TABLE cities(
id integer PRIMARY KEY,
lat text,
lon text,
city text,
state text)
""")
conn.commit()
cur.close()
conn.close()
```

The psycopg2 command copy_from can be used to directly load data from a file like .csv into a Postgres table. We just created a table named `cities` inside the `t81577` database, in which we will copy the contents from the CSV_TABLE 

```python
import psycopg2
CSV_FILEPATH = '/home/asimbanskota/t81_577_data_science/weekly_materials/week5/files/city.csv'
conn = psycopg2.connect(host="localhost",database="t81577", user="postgres", password="postgres")
cur = conn.cursor()
with open(CSV_FILEPATH, 'r') as f:

    next(f) # Skip the header row.
    cur.copy_from(f, 'cities', sep=',')
conn.commit()
cur.close()
conn.close()
```


## Fetch data into Python

In this section we will learn about how to fetch data from PostgreSQL database into a python application using `psycopg2` library. 
Note that even though we are focusing here on accessing data from PostgreSQL, the methods and the syntax would be the same for other relational databases as well. As a reminder,

- Use the `connect()` method of `psycopg2` to connect to a database
- Create a cursor object using the connection object returned by the connect method
- Use the cursor object to execute PostgreSQL queries from Python.
- Close the cursor and object connection after the completion of the work

The cursor object has methods such as `fetchall()` to grab entire data from a database table.

```python
conn = psycopg2.connect(host="localhost",database="t81577", user="postgres", password="postgres")
cur = conn.cursor()
sql = """SELECT * from cities"""
cur.execute(sql)
records = cur.fetchall()
cur.close()
conn.close()
```

As some tables could be huge in size and grabbing the entire data might be neither realistic nor necessary, other two cursor methods `fetchmany()`, `fetchone()` can be used to retrieve selected rows from the table. 

For example, to fetch just 10 rows, run the following command after opening connection and executing the sql query as before:

```python
records = cur.fetchmany(10)
```
If the cur.fetchmany(10) is called again with the previous cursor open, the next 10 rows will be returned.

### Querying data


As with other DBMS, we query information from Postgres by using "select" statements. Here is the general syntax:

`SELECT columns FROM table;`

In order to select only `city` and `states` columns from the cities table, create a sql string as below:


```python
sql = """SELECT city,state FROM cities"""
cur.execute(sql)
cur.fetchall()
```
To select only those rows that meet certain criterion, for example, `lat` column value less than 80 degree:

```python
sql = """SELECT city,state FROM cities WHERE lon <80"""
cur.execute(sql)
cur.fetchall()

```
And off course, we can add more filtering criteria using conditional
```python
sql = """SELECT ncity,state FROM cities WHERE lon <80 AND lat >30 ORDER BY city"""
cur.execute(sql)
cur.fetchall()
```

These were the basic illustrations of grabbing data from Postgres into Python. The query can get complicated when our data resides across different tables, however, these simple examples are sufficient to get started and get many things done. Finally, as with everything, don't forget to catch and raise exceptions that may occur during the process:

Here is a simple example for that:

```python
import psycopg2

def get_city_data(sql):
    try:
        conn = psycopg2.connect(host="localhost",database="t81577", user="postgres", password="postgres")
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL table", error)

    finally:
        if (conn):
            cur.close()
            conn.close()
            
sql = """SELECT city,state FROM cities WHERE lon <80 AND lat >30 ORDER BY city"""
get_city_data(sql)
```



### References:

[Loading data into postgres](https://www.dataquest.io/blog/loading-data-into-postgres/)

[Select data from table](https://pynative.com/python-postgresql-select-data-from-table/)








