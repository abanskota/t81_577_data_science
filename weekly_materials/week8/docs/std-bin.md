# Standardization and binning


## Standardization

Standardization of datasets is a common requirement for many machine learning algorithms to behave optimally. Standardization is a transformation that makes the data to be centered at zero.

Some families of algorithms are scale invariant and don't care whether the features are mean centered or not. However, for many algorithms, the standardization process improves the numerical stability of the model, speeds up training process, and enables all features to contribute in the learning process.

Sklearn provides different ways of scaling features:

### StandardScaler

It standardizes features such that the feature has zero mean and unit variance as below:

```bash
x_scaled = (x — u) / s
```
where, u is the mean and s is the standard deviation. The standard scaler tends to work better when the features have normal (Gaussian) distribution.

Example of using StandardScaler in sklearn:

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X  = np.array([[ 1., -3.,  4.],
               [ 2.,  2.,  3.],
                [ 3.,  3., 2.]])
X_scaled = scaler.fit_transform(X)
```

### MinMaxScaler

The MinMaxScaler transforms features by scaling each feature to a given range typically between 0 and 1. This scaler works better for cases where the distribution is not Gaussian or the standard deviation is very small but is sensitive to outliers.

```bash
x_scaled = (x-min(x)) / (max(x)–min(x))
```
Example of using MinMaxScaler in sklearn:

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
X_scaled = scaler.fit_transform(X)
```

### MaxAbsScaler

MaxAbsScaler works in a very similar fashion, but scales in a way that the training data lies within the range [-1, 1] by dividing through the largest maximum value in each feature. It is meant for data that is already centered at zero or sparse data.

```bash
x_scaled = x / max(abs(x))
```

Example of using MaxAbsScaler in sklearn:
```python
from sklearn.preprocessing import MaxAbsScaler
scaler = MaxAbsScaler()
X_scaled = scaler.fit_transform(X)
```
## Binning

Data binning or discretization is a  pre-processing technique used to minimize the impact of small fluctuation in the dataset by converting the continuous features into categorical ones. This is the process of “smoothing”, wherein each bin smoothens fluctuations, thus reducing noise in the data. 

The original data values are divided into small intervals known as bins and then they are replaced by a categorical value for that bin. Discretization is similar to constructing histograms for continuous data. However, histograms focus on counting features which fall into particular bins, whereas discretization focuses on assigning feature values to these bins.

Binning might help to improve accuracy of a predictive model by reducing noise and non-linearity and also allows easy identification of outliers and invalid values for a feature. Disadvantage of binning is that it increases the number of features and can thus lead to learning problems (overfitting) with small dataset.

We looked at how to bin  a feature using `cut` and `cut` methods in Pandas last week. Sklearn also provides methods for binning with different strategies.


Separating values into ‘N’ number of bins with equal width. 
```bash
width = (max - min) / N
```
Example of using equal width binning in sklearn:

```python
ffrom sklearn.preprocessing import KBinsDiscretizer
X = np.array([[ -3., 5., 15 ],
             [  0., 6., 14 ],
             [  6., 3., 11 ]])
X_binned = KBinsDiscretizer(n_bins=5, encode='ordinal').fit_transform(X)

print(X_binned)
print(X_binned)
[[0. 2. 4.]
 [2. 4. 2.]
 [4. 0. 0.]]
 ```
 
KBinsDiscretizer implements different binning strategies, which can be selected with the strategy parameter. The ‘uniform’ strategy uses constant-width bins. The ‘quantile’ strategy uses the quantiles values to have equally populated bins in each feature. The ‘kmeans’ strategy defines bins based on a k-means clustering procedure performed on each feature independently.

Binning can also be done in a supervised manner so as to maximize information for the target variables in a predictive model.

[Next:Categorical Encodings](https://nbviewer.jupyter.org/github/abanskota/t81_577_data_science/blob/master/weekly_materials/week8/notebooks/categorical-encoding.ipynb)