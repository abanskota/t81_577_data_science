### Learning objective: Explore and familiarize with the steps of machine-learning model development on a high level. 


Here we will briefly discuss the major steps of model development in machine learning. From here onwards, our focus will be on building a predictive model using supervised machine learning techniques. Each step discussed here will be subsequently treated in detail later in the course.

### Framing questions

Understanding and clearly defining business problems is the first and most critical aspect in the model building process. Usually, the request for a machine learning based product or solution comes from people who have better grasp on business domain. Engaging with the customers right from the beginning and asking a series of questions will allow data scientists to deliver products according to the need of customers. Formulating and asking right questions will help fully understand the business need without making assumptions about what others are thinking.

Example of some questions:

- What are the requirements of the problem? 
- What are the assumptions and constraints?
- Is the problem solvable?
- How should the questions be prioritized to derive the most value?
- What resources are available? 
- What risks are there in pursuing the project?
- What are the different data sources, which variables do I need, and how much data will I need to get from each one? 
- How will the results be used? 

Additionally, one important question that needs to be asked at the outset is whether **machine learning is the right tool  for the problem or not**. In most instances, simple heuristics such as averages or ranks might provide the quick answer business is looking for. Don’t shy away from offering such a solution unless and until you have reasons to believe that machine learning solution can provide better answers and the necessary data is available. 

### Data collection:

The goal of the data collection is to gather datasets that can be used to build and evaluate machine learning models. Having already asked the right questions in relation to the need of and accessibility to data makes the acquisition process a lot smoother. However, this step is very critical as the quality and quantity of gathered data will directly determine how good the final model is going to be. The collection may require integrating data from various sources and possibly involving augmentation (where existing datasets are enhanced by adding more external or synthetic data). Some teams make a cardinal mistake of spending months and months of their time collecting and enriching dataset thinking a machine learning model would only work when fed with large amounts of data. Machine learning is an iterative process: quickly prototyping ideas on the readily available dataset is very important for gaining foresight on product viability, setting up benchmarks and future roadmap, and understanding the required level of  further data collection.


### Data preprocessing

Raw data rarely comes in a form suitable to readymade analysis. Many data scientists complain that they spend eighty percent of the time gathering and preprocessing data. As data quality is one of the major determinants of model accuracy, preprocessing data for improving quality is an inherent part of model development life-cycle. The poor quality could be due to inaccuracy and inconsistency in data, or incompleteness in values. Preprocessing takes raw data and transforms them into one with increased quality. Additionally, preprocessing also involves transforming raw data into different shapes by means of engineering more features (variables) or transforming existing features into different value ranges. 

Preprocessing types:

- Correcting inconsistency
- Identifying outliers
- duplicate removals
- Data type conversion and encoding categorical features
- Standardization, Aggregation, Binning, Missing value treatments
- Balancing dataset
- Creation of new features 
- Splitting data into train-test-val


### Model training 

Training a model is the core part of a model development endeavor. Training a model means teaching a machine learning algorithm to learn the functional (mathematical) relationship between input and output variables. The end goal is to come up with a model that can accurately predict values for output variables given some values for a set of input variables. Depending upon the type of output variable, the training process is called either classification (categorical labels) or regression ( a real value). A variety of machine learning algorithms exist for accomplishing both tasks. It is not entirely clear at the outset which algorithm should be used for a given task: the common approach is to compare model performance with many different techniques and pick one that provides the greatest predictive accuracy. Though other factors such as time taken to train models and the level of complexity required to deploy in production are also considered in finally selecting the best model. 

### Model Evaluation

As already implied, predictive models are judged based upon their ability to predict output values for inputs that were not seen by model during training. It means that the candidate models should be evaluated against the data set that were not used during training. Such a process of evaluating models is called cross-validation. During preprocessing, data is split randomly between training and test dataset for that purpose. Some modelling algorithms such as random forest and neural network require selecting not only the model parameters ( coefficients of equations) but also hyperparameters that define the model architecture. Training models with such algorithms require another independent dataset for selecting hyperparameters during training.


### Model deployment

### Performance monitoring and redevelopment


References:


[How to ask right questions](https://towardsdatascience.com/how-to-ask-the-right-questions-as-a-data-scientist-913621907411)