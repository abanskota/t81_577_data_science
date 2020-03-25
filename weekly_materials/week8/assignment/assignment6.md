### Assignment 6

In this assignment, you will work with the `Iris Flower` dataset that has been slightly revised for the assignment purpose. The dataset is saved in the week8 assignment folder.

The data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length, stored in a 150x4 numpy.ndarray inside a dictionary in a pickled format. The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.

To load the dataset as dictionary into Python, type the following lines of codes:

```
python
with open('iris.pickle', 'rb') as handle:
    iris = pickle.load(handle)
```

Check the dictionary keys and values to find out diffferent features in the dataset. See [here](https://en.wikipedia.org/wiki/Iris_flower_data_set) for more information on this dataset.


Perform your analysis on Jupyter notebook to answer the following questions. Submit your Notebook to OK for grading!

1. Create a Pandas dataframe from the `iris` dictionary you loaded. The dataframe should at least contain one target variable from items inside 'target' keys and four other features i.e. Sepal Length, Sepal Width, Petal Length and Petal Width. (Point 1)
    
2. Determine which column has missing values missing at random? State your reason (Point 1). Impute the values for the column using an univariate algorithm from sklearn.impute and add back the imputed feature to the dataframe (Point 1) 
    
3. Add an indicator feature to the dataframe to denote the missing values of a column that are not missing at random (Point 1.5). Impute the values for the column using an instance of IterativeImputer class of sklearn. Either use default arguments or feel free to experiment with the choice of available set of arguments. (Point 1.5)
    
4. Standardize the values of each column using one of the scaler class from sklearn.preprocessing and state you reason for using the particular scaler. Add the standardized features to the dataframe.[Point 2]

5. Create polynomial features of order two including interaction features and add the new features back to the dataframe. (Point 2)
    


Good luck!

