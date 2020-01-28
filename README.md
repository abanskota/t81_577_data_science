# T81 577 Applied Data Science for Practitioners

[Washington University in St. Louis](https://wustl.edu/)

Instructor: Asim Banskota

Spring 2020, Wednesday, 6:00 PM - 9:00 PM , Cupples II, Room L015

# Course Description

Organizations are rapidly transforming the way they ingest, integrate, store, serve data, and perform
analytics. In this course, students will learn the steps involved with designing and implementing data
science projects. Topics addressed include: ingesting and parsing data from various sources, dealing with
messy and missing data, transforming and engineering features, building and evaluating machine learning models, and
visualizing results. Using Python based tools such as Numpy, Pandas, and Scikit-learn, students will
complete a practical data science project that addresses the entire design and implementation process.
Students will also become familiar with the best practices and current trends in data science including
code documentation, version control, reproducible research, pipeline automation, and cloud computing. Upon completion of the course, students will emerge equipped with data science knowledge and skills that can be applied from day one on the job.

# Syllabus

Week|Content
----|----
Week 1 <br> **1/15/2020** |**Introductions** <ul><li>1.1. [Data science in practice](weekly_materials/week1/docs/data-science-in-practice.md) <li> 1.2. Introduction to Python Programming Language <ul> <li> 1.2.1. [Python introduction and set up](weekly_materials/week1/docs/python-introduction-and-set-up.md) <li> 1.2.2. [Jupyter Notebook and Lab](weekly_materials/week1/docs/jupyter-notebook-and-lab.md)  </ul> 1.3. [An introduction to Amazon Web Service (AWS)](weekly_materials/week1/docs/an-introduction-to-aws.md) </ul>**Assignment 1.1:** [Install anaconda and test Jupyter notebook](weekly_materials/week1/assignments/assignment-1.md) <br>**Assignment 1.2:** [AWS fundamentals](weekly_materials/week1/assignments/assignment-2.md) </ul>
Week 2 <br> **1/22/2020** |**Python Fundamentals** <ul><li> 2.1. [Basic data types](weekly_materials/week2/notebooks/basic-data-types.ipynb) <li> 2.2. [Data structure and iterables](weekly_materials/week2/notebooks/data-structure-and-iterables.ipynb)<li> 2.3 [Conditional, iteration, and function in Python](weekly_materials/week2/notebooks/conditional_iteration_function.ipynb)<li>2.4. [Map, filter, reduce, comprehension](weekly_materials/week2/notebooks/map-filter-reduce-comprehension.ipynb) </ul>**Assignment 2:** [Programming practice assignment](weekly_materials/week2/assignments/assignment2.ipynb)</ul>
Week 3 <br> **1/29/2020** |[**Coding Best Practices in Data Science** ](weekly_materials/week3/docs/coding-best-practices-in-data-science.md)<ul><li> 3.1. [Top nine best-practices](weekly_materials/week3/docs/top-nine-best-practices.md) <li> 3.2. [Style guide for python code](weekly_materials/week3/docs/style-guide-for-python-code.md) <li>3.3. [Documenting python code](weekly_materials/week3/docs/documenting-python-code.md) <li>3.4. [Version control](weekly_materials/week3/docs/version-control.md) <li>  3.5. [Code linting](weekly_materials/week3/notebooks/linting.ipynb) <li> </ul>**Assignment 3.:** [Version control, project structure, and code documentation](weekly_materials/week3/assignments/assignment3.md) </ul>
Week 4 <br> **2/5/2020** |**Modeling Overview** <ul><li> 4.1. Types of models <ul><li> 4.1.1. Descriptive/Prescriptive/Predictive <li> 4.1.2. Statistical vs Machine learning <li> 4.1.3. Blackbox vs Explainable </ul> 4.2. Model development steps <ul><li> 4.2.1. Framing questions <li> 4.2.2. Data ingestion and wrangling <li> 4.2.3. Data Preprocessing <li> 4.2.4. Model fitting and evaluation <li> 4.2.5 Model deployment <li> 4.2.6. Performance monitoring and redevelopment </ul></ul> **Quiz** Modeling Overview </ul>
Week 5 <br> **2/12/2020**| **Accessing Data** <ul><li> 5.1. Introduction to RESTful APIs <li> 5.2. Accessing data from API using request module and Postman <li> 5.3. Overview of JSON-formatted data <li> 5.4. Parsing JSON data <li> 5.5. Importing commonly used files formatted data <li> 5.6. Reading data from PostgreSQL database </ul> **Assignment 4:** Finalization of final project topic and data set (Not graded)</ul>
Week 6 <br> **2/19/2020**| **Numpy/Pandas for Data Munging/Wrangling** <ul><li> 6.1. Pandas and numpy data structure <li> 6.2. Querying and reading data <li> 6.3. Reshaping, Indexing, slicing, and filtering data <li> 6.4. Join, Merge, and Aggregation <li> 6.5. Vectorization <li> 6.6. Basic statistics and plotting </ul> **Assignment 5:** Data wrangling with Numpy and Pandas </ul>
Week 7 <br> **2/26/2020**| **Exploratory Data Analysis (EDA)** <ul><li> 7.1. Categorical vs numeric features <li> 7.2. Datatype conversion <li> 7.3. Sampling <li> 7.4. Data summary and distribution <li> 7.5. Patterns in data <li> 7.6. Data visualization using matplotlib, seaborn, and Bokeh <li> 7.7 Anomaly/outlier detection </ul> **Assignment 6:** Patterns in data: Vizualization and data summary </ul>
Week 8 <br> **3/4/2020**| **Data Preprocessing** <ul><li> 8.1. Basics (select, filter, removal of duplicates)<li> 8.2. Data Transformation <li> 8.3. Standardization, Binning, Missing value treatments <li> 8.4 Balancing dataset </ul> **Assignment 6:** Data preprocessing </ul>
Week 9 <br> **3/18/2020** | **Feature Transformation and Engineering** <ul><li> 9.1. Categorical encodings <li> 9.2. Feature creation/engineering <li> 9.3. Feature extraction </ul> **Assignment** Transformation of categorical and continuous features </ul>
Week 10 <br> **3/25/2020** |**Building and Evaluating Models** <ul><li>10.1. Tour of machine learning algorithms using scikit learn <li> 10.2. Introduction to Scikit-learn model development API <li> 10.3. Amazon SageMaker <li> 10.4. Training and fitting classification models <li> 10.5.Training and fitting regression models <li> 10.6. Performance evaluation metrics and curves </ul> **Assignment:** Model building and evaluation using Scikit-Learn </ul>
Week 11 <br> **4/1/2020** | **Best practices in Machine Learning** <ul><li> 11.1. Bias vs variance tradeoff <li> 11.2. Train/dev/test dataset <li> 11.3. Regularization <li> 11.4. Learning vs validation curves <li> 11.5. Hyperparameter tuning <li> 11.6. Ensemble learning <li> 11.7. Streamlining workflows with pipelines </ul> **Assignment:** Regularization, cross validation and hyperparameter tuning </ul>
Week 12 <br> **4/8/2020** | **1. Guest Lecture: Data Science at Wells Fargo** <br> **2. Discussion on final project status** <br> **Quiz 2:** Best practices on machine learning 
Week 13 <br> **4/15/2020** | **Productionize a Machine Learning model** <ul><li> 13.1. Dev/Stage/Prod environment <li> 13.2 Docker , Docker Files, Docker Containers <li> 13.3. Deploy a machine learning model as a Flask app <li> 13.4 Introduction to Airflow </ul> **Assignment:** Build and deploy a model using Docker and Heroku app </ul>
Week 14 <br> **4/22/2020** | **Final Project Demo** <br> Short 5 minutes long individual project demo
