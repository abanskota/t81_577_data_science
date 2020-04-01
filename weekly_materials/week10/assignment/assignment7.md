### Assignment 7

In this assignment, you will work with the Iris Flower dataset that you can load from sklearn.datasets. You will build predictive models using different classification algorithms and compare their predictive performances.

```python
from sklearn.datasets import load_iris
iris = load_iris()
```

The data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length, stored in a 150x4 numpy.ndarray inside a dictionary in a pickled format. The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.

Perform your analysis on Jupyter notebook. Submit your Notebook to OK for grading!

1. Split the datasets into training (80%) and testing (20%) - 1 Point

2. Create a pipline of the following steps: ( 4.5 Points)

- Impute missing values 
- Create polynomial features (degree 3) from Sepal Length and Sepal Width columns
- Apply feature scaling so that all features have values between 0 and 1.

3. Fit 3 different classification algorithms of your choice on the training data preprocessed through the pipeline from step 2. ( 3 Points)

4. Report the overall accuracy of the three models on the test dataset (1.5 Points)

Good luck!

