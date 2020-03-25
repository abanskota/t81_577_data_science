## Common machine learning algorithms: Part I

In [Week 4](https://github.com/abanskota/t81_577_data_science/blob/master/weekly_materials/week4/docs/types-by-framework.md), we learnt some distinctions between statistical modelling and machine learning framework. We also learnt that machine learning models could be broadly categorized into supervised, unsupervised, and reinforcement learning models. In this section you will have a high level overview on some of the most common machine learning algorithms. This is the part I of the introduction to the machine learning algorithms. In the next week, we will cover some additional algorithms.

[1. Linear regression?](#linear-regression?)<ul><li>[1.1. Ordinary least-square regressions](#ordinary-least-square-regression) <br><li>[1.2. Linear regression with regularization](#linear-regression-with-regularization) <ul><li>[1.2.1 Ridge regression](#ridge-regression)<br><li>[1.2.2. Lasso regression](#lasso-regression)</ul></ul><li> [2. Logistic regression](#logistic-regression)<br><li>[3. Naïve Bayes classifier algorithm](#naïve-bayes-classifier-algorithm)<br><li>[4.Tree based algorithms](#tree-based-algorithms)<ul><li>[4.1 Bagging](#bagging)<br><li>[4.2 Random Forests](#random-forests)<br><li>[4.3 Boosting](#boosting)</ui><li>[5. K-means clustering](#k-means-clustering)
    
## Linear Regression

In supervised learning, the goal is to learn a function f : X → Y given data so that f(x) is a “good” predictor for the corresponding value of y. When the target variable that we’re trying to predict is continuous, the learning problem becomes a regression problem. 

Linear regression consists of a family of linear techniques to build regression models. In a univariate regression, a regression line describes how a response variable linearly changes as explanatory variable changes. In higher dimensions with multiple explanatory variables, linear regression problem amounts to finding a plane or a hyper-plane. 

### Ordinary least squares regression

Linear regression between a continuously valued response (target variable y) and a set of explanatory variables (x0, x1, x2…...xm) can be defined as follows:

![](../files/eq1.png)

,where b is the y axis intercept, and w<sup>1</sup> ... w<sup>m</sup> are the coefficients of the corresponding explanatory variables. The goal of a learning algorithm is to learn the set of coefficients or weights that best describe the linear relationship between X and y variables in the training data that can be accurately used to predict the value of y in future data.

When the best line is determined using a technique called least square, the linear regression is known as the least square regression or ordinary least square regression. The least square regression fitting procedure involves a loss function, known as residual sum of squares or RSS of the differences between true y value and estimated values. 

![](../files/loss.png)

The coefficients are chosen, such that they minimize this loss function.

**Note:** _It is common in machine learning to refer to the error between yhat and y of a single training observation as loss function, and the cumulative error over the entire dataset as cost function._

![](../files/argmin.png)

The least square problem can be analytically solved with the following equation:

![](../files/xtx.png)

However, when there are a very large number of predictor variables in the order of tens of thousands, optimization algorithms such as gradient descent provide faster and stable solutions to the least square problems. 


### Linear regression with regularization

When there are a large number of explanatory variables, a supervised learning problem tends to suffer from overfitting. Overfitting happens when a model in consideration works perfectly with training data but is unable to generalise to unseen datasets. 
Regularisation is a process of adding a penalty term that shrinks the weight parameters towards zero in order to prevent overfitting. The regularisation terms are ‘constraints’ by which an optimisation algorithm must ‘adhere to’ when minimising the loss function, apart from having to minimise the error between the true y and the predicted ŷ.

### Ridge regression

Ridge regression  adds “square  value of magnitude” of weight parameters (L2 norm) to the loss function of a model to regularize a linear regression.

![](../files/ridge-loss.png)

The loss function is modified by adding the shrinkage quantity as a penalty term.  The weight parameters are then estimated by minimizing the modified loss function. λ is the tuning parameter that decides how much we want to penalize the flexibility of our model. Greater the value of the lambda, more shrinkage would occur and the weight parameter tends to take small values leading to less overfitting. However, if lambda is very large then it will introduce bias (underfitting). Ridge regression is sensitive to scale and hence requires all explanatory variables to be in a similar scale.

#### Lasso regression 

LASSO  adds “absolute value of magnitude” of weight parameters (L1 norm) scaled by a regularization parameter as penalty term to the loss function.

![](../files/lasso-loss.png)

Lasso regression tends to shrink the weight of less important features to zero, thereby removing some features altogether. Ridge regression on the other hand tends to minimize the larger weight parameter into small values due to the squared term in the loss function.

### Logistic regression 

In spite of its name, logistic regression is a model for classification, not regression. It is one of the most widely used machine learning models for binary and multiclass classification.
In case of binary classification of class 1 and 0, logistic regression computes the natural log of the odds that Y is equal to 1 (logit odds), which is simply the ratio of the probability that Y is 1 divided by the probability that Y is 0. 

 ![](../files/logistic.png)
 
,Where p = probability of y being class 1. This formula shows that the logistic regression model is a linear model for the log odds.
Instead of the log odds, we are actually interested in the quantity p, which is estimated by applying a sigmoid or logistic function (inverse form of the logit function) to the quantity in the right hand side of the above equation. The estimated probability of an observation belonging to class 1 is then given by,

![](../files/sigmoid.png)

Since the output of the sigmoid function always ranges between 0 and 1, the output value can be interpreted as the conditional probability of an observation belonging to the class. The loss function used in logistic regression is called log loss function, which takes the following form:

![](../files/logloss.png)

And the cost function over all training examples is given by,

![](../files/logcost.png)

Logistic regression can also be extended from binary classification to multi-class classification. Then it is called Multinomial Regression. Logistic regression is widely used in the industry setting when the interpretability of the model coefficients is the necessity. 

### Naïve Bayes Classifier Algorithm

A Naive Bayes classifier machine learning model is used for classification tasks and based upon Bayes theorem. Bayes theorem from a classification standpoint can be specified in the following form:

![](../files/bayes.png)

,Where the term in the left side is the probability of a certain class variable (yj) given predictor variables X .


After assuming the independence of all xi variables for a given class, the class probability for class yj can be computed as joint probability of all xi given yj as follows:

![](../files/posterior.png)
 
Based upon the above, an observation will be assigned a class label that has the greatest conditional probability. Naive Bayes classifiers have found success in problems related to text classification and have been  used in email spam filtering and sentiment analysis problems.

## Tree based algorithms

Tree-based methods are used for both regression and classification problems. Tree based methods recursively stratify or segment the feature space into a number of simple regions ( classes or real value output) using some decision rules •  Since the set of splitting rules used to segment the predictor space can be summarized in a tree, these types of approaches are known as decision-tree methods.

Tree-based methods are simple and useful for interpretation. However,  their  predictive ability is typically inferior compared to more advanced machine learning approaches. Ensemble methods  combine multiple trees to yield a single consensus prediction that can often result in major improvements in prediction accuracy, at the expense of some loss interpretation. 

![](../files/tree.png)

[Source]( https://www.kdnuggets.com/2020/01/decision-tree-algorithm-explained.html)