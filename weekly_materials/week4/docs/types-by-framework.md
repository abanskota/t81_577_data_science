### Frameworks for model building 

#### 1 Statistical 


- Statistical models are normally parametric models that make assumptions about the parameters of the population distribution from which the data are drawn. For example, a linear regression between a target variable `y` and an independent variable `x` can be represented in the following equation.


<img src="http://www.sciweavers.org/tex2img.php?eq=y%20%3D%20%20%20%5Cbeta_0%20%20%2B%20%20%5Cbeta_1%20%2A%20%20%5Csum_1%5En%20x_i%20%2B%20%20%20%5Cxi_i&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="y =   \beta  +  \beta_1 *  \sum_1^n x_i +   \xi_i" width="183" height="50" />

In order for the two coefficients to be accurate estimates (best, unbiased, consistent), several assumptions about the data and the relationship need to hold such as:

<ul>
    
- Model is linear in parameter.
    
- Data were generated randomly.

- Errors($\epsilon$) are normally distributed.
</ul>

If such assumptions are held, the estimated model closely resembles the true model that generated data. If not, estimated coefficient could be biased and inconsistent.

- The coefficients of the models are interpretable (only if the assumptions are held)

- Models are useful in correlation based inference

- Models can also be extended to causal reasoning with proper application of causal inference tools.

- Some statistical methods like randomized control trial provides standard tools for causal reasoning based upon experimentation.


#### 2. Machine learning 

Machine learning models make fewer assumptions about data and the estimated parameters.

- Main focus of machine learning is predictive modeling.

- The function (or relationship) estimated by machine learning models are usually non-linear and hard to interpret.

- Can model highly-complex non-linear relationship 

- Requires greater amount of data compared to statistical couterpart

- Three types:
<ul><li>
    `Supervised` 
  <ul><li>
    Typically used in classification and regression problems 
    <li> Learn model structure with labelled data or target variable 
</ul>
<li>
    `Unsupervised` 
    <ul><li>
    Learn model structure without explicit labels
    <li>Mainly used in clustering/segmentation and dimensionality reduction problems
    
 </ul>
 <li> `Reinforcement learning (RL)`
    <ul> <li>Learn model structure based upon interactions of agent with environment
     <li>Every action taken by an agent is associated with reward. Agent learns the best model that maximizes rewards.
     <li>Common applications include problems with sequential decision making such as in robotics or computer games. There are several other interesting applications of RL such as management of traffic lights, massive reduction in energy cost of Google complex.
     </ul>
     
     
 [Next: Model categories by interpretability](types-by-interpretability.md)
