## Exploratory Data Analysis 

Exploratory data analysis (EDA) is a process of critical scrutiny of data in relation to the problem at hand. Generally speaking, any method of looking at data before fitting the model falls under the realm of exploratory data analysis. 

EDA helps us:<br>

- understand the quality, quantity, and the utility of data <br>
- get familiar with data distribution <br>
- devise a plan for data massaging<br>
- formulate and test preliminary hypothesis about the relationship among features<br>
- understand the need for creating more features<br>


Data for predictive modelling generally comes in the form of a rectangular array with rows representing records or observations on subjects. Columns typically represent one outcome variable and one or many predictor variables (features), which contain either numeric values (ratio and interval) for quantitative features or nominal and ordinal values for categorical ones.

Each of the features and target variables can be explored  individually or in relation to each other. The techniques might vary depending upon whether the features are of categorical or numeric types. EDA could involve  statistical summaries, tabular analysis, and graphical methods.

EDA should be done with the following questions in mind:

#### 1. What kind of features (variables or columns) are there? Is there any need for type conversion?
#### 2. How is data distributed across different features? Are there any outliers you need to be concerned about?
#### 3. Is there any need for data cleaning? Are there any missing values?
#### 4. How do  feature vary in relation to each other and target variable?
#### 5. Are there any observable trends, patterns, and  anomaly visible in the graphical analysis of data?

In the upcoming lectures of this week, we will try to work with one open source dataset and perform EDA by treating those questions seperately or in combination.

[Next: Univariate EDA](https://github.com/abanskota/t81_577_data_science/blob/master/weekly_materials/week7/notebooks/eda-univariate.ipynb)
