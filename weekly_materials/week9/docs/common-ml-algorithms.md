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


