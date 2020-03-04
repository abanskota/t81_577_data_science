## A very brief introduction to Scikit-Learn 

Scikit-learn is a Python package for machine learning with a wide selection of learning algorithms. It is built on top of Scipy( scientific Python), Numpy, and Matplotlib libraries. As with Numpy and Pandas, it leverages c-libraries and the use of cython to improve performance. It integrates very well with many Pandas and Numpy including many others commonly used in data analysis and visualization. 


Scikit-learn comes with Anaconda Python distribution. As always, to install in a different or virtual environment, use 
```bash 
pip install scikit-learn
``` 
or 

```bash 
conda install scikit-learn
```

To import the library, use:

```python
import sklearn
```
Note that it is `sklearn` that you need to type in Python interpreter not scikit-learn.

Scikit-learn is focussed on building machine learning models. That is why we learnt Numpy and Pandas for loading data and exploratory data analysis in the past weeks but not Scikit-learn. In the next few weeks, we will learn more about Scikit-learn APIs for modelling algorithms. This week, we will use sklearn's preprocessing module that provides several common utility functions and transformer classes for preprocessing data in a format suitable to building models. For many data science works, a typical workflow consists of using Pandas to do EDA followed by scikit-learn for preprocessing and machine learning. In the ensuing lessons on preprocessing, we will use various functions and classes from scikit-learn to standardize, normalize, discretize, impute missing values, encode categorical variables, transform, and generate new features. 


To import the preprocessing module, type:

```python
from sklearn import preprocessing
```

**Data Type**: array-like object is the most common data type for scikit-learns- array-like being any object compatible to numpy.array() method such as a numpy array, a list of numbers, pandas dataframe and series etc.

References:


[A Gentle Intoduction to Scikit-Learn](https://machinelearningmastery.com/a-gentle-introduction-to-scikit-learn-a-python-machine-learning-library/)

[Next: Imputation of missing values](https://github.com/abanskota/t81_577_data_science/blob/master/weekly_materials/week8/docs/missing-value.md)