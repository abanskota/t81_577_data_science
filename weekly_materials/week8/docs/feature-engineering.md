### Feature Engineering

It is the process of generating additional features from raw data in order to improve the performance of machine learning algorithms relying on domain knowledge, intuition, and data manipulation.

It is generally believed that feature engineering plays the most important part of a machine learning project's success or failure. This is because a machine learning algorithm learns from the data fed into it, and features that are relevant to a task improve the learning process. Simple models with better features always tend to outperform complex model with no so goo feature set.

Feature engineering process could be data-specific. The categorical encodings discussed earlier is one type of a feature engineering process for text data. Similarly, a wide array of techniques of extracting features from imagery exist in the image processing domain. For tabular data, feature engineering typically involves either transformation or aggregation. 

**Transformation**: Creating new features out of one or more of the existing columns in a row wise manner i.e. transformation of one row is independent of another row in an array or a dataframe.

**Aggregation**: Creating new features from existing data from one or more existing columns by grouping observations over one or more other columns. 

Domain knowledge plays a huge role in feature engineering. As we saw in EDA in the previous week, spending more time and exploring the nature of the data can give us insight about the direction of the trasformation and aggregation of data needed. Apart from that, talking to domain expert and reading literature on similar works can also help come up with intuition for generating better features. 

As with other predictive modelling steps, feature engineering is an iterative process:

- Deciding what features to create
- Creating features
- Checking the performance of model with new features
- Generating more relevant features until the work is done.

Additional features can improve the performance of the model if they are strongly or even weakly related to target variables. But having a large number of features can also lead to performance deterioration due to overfitting that needs to be handled separately.

While feature engineering is usually a manual iterative process, scikit-learn provides an automated way of generating polynomial features of high-order and interaction terms. These polynomial features can enable even simple linear techniques to model complex non-linear relationships between target and predictor features. Different features of higher order polynomial (square and cube) and features capturing interaction between columns can be created with scikit-learn as follows:


```python
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
X = np.arange(6).reshape(3, 2)
poly = PolynomialFeatures(degree=3)
poly.fit_transform(X)

array([[  1.,   0.,   1.,   0.,   0.,   1.,   0.,   0.,   0.,   1.],
       [  1.,   2.,   3.,   4.,   6.,   9.,   8.,  12.,  18.,  27.],
       [  1.,   4.,   5.,  16.,  20.,  25.,  64.,  80., 100., 125.]])
```


