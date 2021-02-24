### What is model interpretability

In the earlier discussions, we learned that some models are interpretable while others are black box. Interpretability is closely connected with the ability of users to understand the model. Usually, there is a tradeoff between interpretability and predictive ability. Predictive models embrace complexity to gain greater predictive accuracy at the expense of interpretability.

### Interpretability of a simple linear regression model

Simple statistical models are normally considered interpretable. Let's take a look at the previous example of a simple linear regression:

<img src="http://www.sciweavers.org/tex2img.php?eq=y%20%3D%20%20%20%5Cbeta_0%20%20%2B%20%20%5Cbeta_1%20%2A%20%20%5Csum_1%5En%20x_i%20%2B%20%20%20%5Cxi_i&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="y =   \beta  +  \beta_1 *  \sum_1^n x_i +   \xi_i" width="183" height="50" />

The interpretability of the above model is attributed to the model being linear in coefficients and thus exhibiting monotonicity (the relationship between x and y always stays either positive or negative). Let's assume that we estimated the two coefficients to be 0.1 and 2, which  makes the estimated equation: 
```bash 
y = 0.1 + 2*x
```
The model could be interpreted as: `for every 1 unit increase in x, y increases with 2 unit`. 


### Interpretability of a ML model

Recently, the concern of interpretability of machine learning, or lack thereof, has been gaining a lot of attention.

- More and more decisions that impact people in their daily lives are being developed using machine learning. People are curious and wants to know why such and such decision are being made.

- Interpretable models are required when making adverse-action decision in highly regulated industry like finance

- Blindly trusting the prediction undermines the scientific method; creates little room for fixing bugs and errors in the model; and perhaps can further fuel people's suspicion towards AI technologies.

Some Machine learning models such as a single tree based model and lasso regression are interpretable. However, such models are not known for high predictive accuracy.

Several techniques have recently surfaced that help interpret a complex non-linear ML model. Local interpretable model-agnostic explanations (LIME) is one of the widely known, which computes explainable linear models locally to approximate a global non-linear one. Visit this [site](https://christophm.github.io/interpretable-ml-book) to know more such techniques in an online book for interpretable machine learning.



**References**

https://github.com/jphall663/GWU_data_mining/blob/master/10_model_interpretability/notes/MLI_good_bad_ugly.pdf

https://christophm.github.io/interpretable-ml-book/interpretability-importance.html

