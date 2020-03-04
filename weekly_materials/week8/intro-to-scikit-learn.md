## A brief Intoduction to Scikit-Learn Library

Scikit-learn is a Python package for machine learning with wide selection of learning algorithms. It is built on top of Scipy( scientific Python), Numpy, and Matplotlib libraries. As with Numpy and Pandas, it leverages c-libraries and the use of cython to improve performance. It integrates very well with many Pandas and Numpy including many others commonly used in data analysis and visualization. 


Scikit-learn comes with Anaconda Python distribution. As always, to install in a different or virtual environment, use ```bash pip install scikit-learn``` or ```bash conda install scikit-learn```. 

To import the library, use:

```python
import sklearn
```
Note that it is `sklearn` that you need to type in Python interpreter not scikit-learn.

Scikit-learn is focussed on building machine learning models. That is why, we learnt Numpy and Pandas for loading data and exploratory data analysis but not Scikit-learn. In the next few weeks, we will learn more about Scikit-learn APIs for modelling algorithms. In this week, we will use sklearn's preprocessing module that provides several common utility functions and transformer classes for preprocessing data in a format suitable to building models. For many data science works, a typical workflow consists of using Pandas to do EDA followed by scikit-learn for preprocessing and machine learning. In the ensuing lessons on preprocessing, we will use various functions and classes from scikit-learn to standardize, normalize, discretize, impute missing values, encode categorical variables, transform, and generate new features. 


To import the preprocssing module, type:

```python
from sklearn import preprocessing
```


References:

[A Gentle Intoduction to Scikit-Learn](https://machinelearningmastery.com/a-gentle-introduction-to-scikit-learn-a-python-machine-learning-library/)