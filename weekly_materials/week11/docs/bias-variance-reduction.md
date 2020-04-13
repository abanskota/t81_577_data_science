## How to reduce bias and variance

In week9 here, we briefly discussed the tradeoff between bias and variance. To recap, a model that performs well on training data is said to have low bias, and a model that performs well on future data set is said to have low variance. Doing well on the training set is easy by just memorizing the examples. As the goal of a predictive model is to generalize beyond the examples in the training set, we want the model to have low variance. However, the model can only be learned by training and performing well on training data. Hence, during training, we also keep track of variance by validating the subsequent model on an independent validation or dev set. The model performance on training data would tell us about the bias in the model, and the model performance on the validation set indicates variance. Ideally, we would like to keep both bias and variance low.

Increasing model flexibility such as making a model highly non-linear might lead to a low bias high variance situation when the model highly overfits training data. Simple models on the other hand have low variance but they typically underfit i.e they struggle to learn the underlying patterns in the data resulting in high bias. This is known as bias-variance tradeoff. We need to find the right balance. However, it should be noted that the tradeoff is less of a concern in modern machine learning with enough data and computational power. With enough data, it is possible to decrease the variance without impacting bias. 

You can take a look at the error rate of a model to obtain information on whether a model is underfitting (low-bias) or overfitting (high variance) and then take proper action. Suppose, you are undertaking a classification task that human can achieve almost perfect performance. In such cases, if you are obtaining 1% error rate on your training data and 5% on your validation data, you know your model has high variance. But, if your error rate is 10% on test data, and 11% on your validation data, you know your model is underfitting. 

Some algorithms such as neural network runs in an iterative manner either until convergence or until user-provided limit is exceeded. Looking at the learning curves that shows the behaviour of training and validation error rate over time can provide guidance on optimizing bias and variance. Typically, the error rate in learning curves goes down for both training and validation set, but at one point the training error rate keeps going down but validation error rate starts increasing. At that point, you will recognize that the model starts overfitting.


### Techniques for reducing bias


- `Increase the model complexity`
Increase the model complexity such as increasing the depth of the tree in a tree based algorithms, selecting radial kernel over linear or polynomial kernel in SVM, and using more hidden layers and nodes in neural network can decrease the model bias. If such increase in model flexibility increases the variance, use regularization techniques in tandem. If you include a well-designed regularization method, then you can usually safely increase the size of the model without increasing overfitting.


- `Error analysis` You can sample the examples with high prediction error to figure out the potential causes for the greater error rate. That might lead you to some insights and actions such as correcting labelling errors or generating features to specifically address such gross errors.


- `Tune or eliminate regularization`

This will reduce avoidable bias, but increase variance.


### Variance reduction techniques:

- `Add more training data`

If you have more data and enough computation power. Having more data normally would have no significant effect on bias.

- `Add regularization`

Adding regularization reduces variance but increases bias.

- `Feature selection`

It can reduce variance but can also increase bias. In modern machine learning, little emphasis is given to feature selection when the data is plenty and no shortage of complexity power. But the feature selection can be helpful when the training data size is small.

- `Decrease the model complexity`

Making a model simpler reduces the variances but also increase bais. So this step should be avoided unless there are other tradeoffs related to training speed and data. 

- `Add early stopping`




