Resampling of imbalanced data


In the predictive modelling task, imbalanced data refers to the situation when the distribution of target variable Y is highly skewed. I

It is a common problem in classification taks, when the classes are not represented equally. For example, when building model for fraud detection, loan deafult, spam detection etc, number of examples avaialble for positive classes are normally way fewer than negative classes.

Imabalanced dataset is problematic because the learning by learning algorithms will be biased towards the ovderly represented class. A machine learning algorithm learrns by trying to make fewer mistakes: since there are fewer examples in one class, it tends to focus on not making mistakes in the overly represented class. In a fraud dection task fraught with large number of negative examples, the learning algorithm might try very hard to be right with all examples in negative class that defeats our primary purpose. 

There are some recommended ways of dealing with imabalanced data especially during model training and evaluation such as weighted training, penalizing model with adjusted cost function, and selecting metrics insensitive to class imbalance. We will cover those in Week 11 lecture of the best practices in machine learning.

Here, we will discuss about easy to implement resampling techniques to balance dataset before training a model

There are two main approaches to even-up classes in an imbalanced data:

- **oversampling:** Increase the number of instances from the under-represented class ( sampling with replancement)

<ui><li> _Disadvantage_: It can lead to overfitting (doing will with the model data but no so with the future dataset)
   

- **undersampling:** Remove instances from the over-represented class, called under-sampling.
    
<ui><li> _Disadvantage_: It can cause loss of information.

These approaches are often very easy to implement and fast to run. They are an excellent starting point.

Some Rules of Thumb
Consider testing under-sampling when you have an a lot data (tens- or hundreds of thousands of instances or more)
Consider testing over-sampling when you don’t have a lot of data (tens of thousands of records or less)
Consider testing random and non-random (e.g. stratified) sampling schemes.
Consider testing different resampled ratios (e.g. you don’t have to target a 1:1 ratio in a binary classification problem, try other ratios)

