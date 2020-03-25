We saw in the previous week that real world data might contain missing values. These misisng values are often encoded as blanks, NaNs or other placeholders. Such datasets are normally incompatible with learning algorithms for predictive models, which generally assume dataset contains meaningful values represented as numerical types. 


### 1. Dropping rows and columns

The most basic strategy with incomplete dataset is to drop entire rows and/or columns containing missing values when:

- there are very few missing values, and

- if the distribution of missing values are completely at random.


[This](https://towardsdatascience.com/all-about-missing-data-handling-b94b8b5d2184) article describes what missing values at random mean with examples. 

When the values are missing completely at random, the rows can be dropped when the dataset is significantly large with respect to the number of rows to be dropped and thus does not lead to information loss.

A feature could potentially be dropped if it contained a large number of missing data points. However, a decision of dropping columns is only justified if it improves the performance of a model and thus should be done in conjuction with the model building process.

### Creating a feature out of missing values

When data are not missing completely at random, the information could be captured by creating another feature with binary flags for missing values. A scikit-learn method `MissingIndicator` from `impute` module can be used to create such boolean flags for missing values. The missing data points is then replaced by either mean/median value. 

```python
from sklearn.impute import MissingIndicator 
import numpy as np
INPUT_FILE = "beer_reviews.csv"
df = pd.read_csv(INPUT_FILE)
indicator = MissingIndicator(missing_values=np.NaN)
indicator = indicator.fit_transform(df)
```

In the above dataset, there were three columns with missing values, and hence the resultant indicator array has three columns with boolean values.

**_Note_:** we will use sklearns' fit() , transform(), and fit_transform() methods later in the course. But it is helpful to remember at this point is that fit() calculates the parameters of a transformation and saves them as an internal objects state. Afterwards, transform() method can be called to apply the transformation to a dataset. If the dataset for both fit and trasform is the same, we can simply use fit_transform() method. Internally, it just calls first fit() and then transform() on the same data.

## Imputation

Imputation is a better approach for handling dataset with missing values than to just drop rows and columns. Imputation means filling in the missing value using the most probable value.


### Replacing with central tendencies

Replacing missing data with mean the quickest and easy approach. However, it might bias the model when the missing values are not missing at random, and it also fails to take into account of the information from other columns. Median can be used to substitute the missing values when variable has a skewed distribution, and mode (or most frequent) can be used for catagorical features.

```python
from sklearn.impute import SimpleImputer
imp_float = SimpleImputer(missing_values=np.nan, strategy='mean')
array_df_float = imp_float.fit_transform(df.select_dtypes(include=['float64']))

df1 = pd.DataFrame([["a", "x"],[np.nan, "y"],["a", np.nan], ["b", "y"]], dtype="category")
imp_category = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
array_df1 = imp_category.fit_transform(df1)
```

### Multivariate feature imputation

A more sophisticated approach is to use multivariate approach such as using k-nearest neighbor (KNN) algorithm or fitting a regression function. 


Sklearn's IterativeImputer class models each feature with missing values as a function of other features, and uses that estimate for imputation. A feature column is designated as output y and the other feature columns are treated as inputs X. A regressor is fit on (X, y) for known y. Then, the regressor is used to predict the missing values of y.

```from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp = IterativeImputer(max_iter=5, random_state=0)
df = pd.DataFrame([[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]])
print(np.round(imp.fit_transform(df)))
[[ 1.  2.]
 [ 3.  6.]
 [ 4.  8.]
 [ 2.  3.]
 [ 7. 14.]]
 ```

**_Note_** This estimator is in the experimental stage, import enable_iterative_imputer must be imported prior to importing the estimatorv .

