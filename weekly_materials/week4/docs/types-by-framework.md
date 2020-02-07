### Frameworks for model building 

#### 1 Statistical or parametric


- Parametric models make assumptions about the parameters of the population distribution from which the data are drawn. For example, a linear regression between a target variable `y` and an independent variable `x` can be represented in the following equation.


$$ y = \beta_0  + \beta_1 \sum_{i=1}^n x_i +  \epsilon $$


In order for the two coefficients to be accurate estimates (best, unbiased, consistent), several assumptions about the data and the relationship need to hold such as:

<ul>
    
- Model is linear in parameter.
    
- Data were generated randomly.

- Errors($\epsilon$) are normally distributed.
</ul>

If such assumptions are held, the estimated model closely resembles the true model that generated data. If not, estimated coefficient could be biased and inconsistent.

- The coefficients of the parametric models are interpretable (only if the assumptions are held)

- Parametric models are useful in correlation based inference

- Parametric models can also be extended to causal reasoning with proper application of causal inference tools.

- Some parametric techniques like randomized control trial provides standard tools for causal reasoning based upon experimentation.


#### 2. Machine learning 

Machine learning models are non-parametric and make fewer assumptions about data and the estimated parameters.

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
