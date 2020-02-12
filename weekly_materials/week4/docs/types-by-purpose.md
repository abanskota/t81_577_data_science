
Not all models in data science serve the same purpose. Models are built to answer a variety of business questions and can be categorized into the following types based upon their purpose. This is not an exhaustive and hard-and-fast list. The function of a single model can overlap into two or more categories.

### Segmentation model

- Segmentation model partition the data into meaningful homogeneous parts or segments. 

- Segmentation enables business to implement segment-specific actions for effective outcomes such as targeted advertising and product positioning.

- Segmentation can also be used as a precursor to other modelling for better exploration of the data and to create additional features. 


### Trends and anomaly detection model

- Identify trends, patterns, and anomalies in data across time and geographical space 

- Provides additional insight to business that is not readily available from raw data or from other modelling techniques

- Spatial patterns could provide geographical units (e.g., states) specific insight or some localized information such as map of hot and cool spot of sales data, distribution of customers/competitors in the nearby region.

- Temporal models could provide information on how the business is performing across time in terms of seasonality and trends. 

- Anomaly detection model can provide business with real time detection of unexpected events in an automated manner


###  Inferential

Inferential models infer the relationship between two or more variables in data. Inferential models can belong to two families.

**1. Correlation based inference**

- Inference of relationship between variables based upon correlation (how variables covary)

- If X and Y are two variables in data, and if Y is changing by the same magnitude relative to X, two variables are said to be correlated.

- Standard statistical methods are applied to ensure that the observed correlation in data is real

- Correlation based inference is useful in understanding what would likely happen to a target variable of interest Y if X changes. The conclusion, however, could be very wrong if the observed correlation were spurious one. Such analysis also doesn't provide any insight on "why" does Y change with X. Correlation is not causation.

**2. Causal inference**

- Causal inference attempts to answer to the "Why" question in a causal manner

- If X and Y are two events, X is said to be the cause of Y if Y is listening to X and changing its value accordingly.

- The best way to establish causality is through (randomized) experiment, but experimentation is not always possible.

- Traditional statistical tools are not sufficient for causal inference; other extension tools need to be employed to estimate causal effect from observation data

- Relatively less used historically but receiving increased attention lately in research and data science.


### Predictive

Predictive models seek to answer what would happen to Y variable of interest in the future if X variables take certain values. 

- The most common modeling tools in data science

- Some examples: what crop seed (genetics) is best suited for an agricultural field with given topography, soil conditions, weather, and management practices? What movie users would like to see given their past ratings on other movies?

- Less emphasis is put on modelling the exact relationship among variables in exchange of predictive accuracy, i.e., the exact coefficients of the equations can be compromized if the equation predicts the behavior of the future data well.

- Though exact relationship is not emphasized, it is important that the variables going into the model should be selected based upon sound concepts (proponents of casusal inference argue that having all available variables in a model without proper consideration might degrade the predictive performance).

- Models are derived from either machine learning or statistical algorithms.



### Prescriptive
 
Prescriptive models prescribe the best course of action or possible consequences of actions when making decisions under uncertainty through simulation and optimization. 

- Can be an independent model or work in conjunction with other type of models. 

- Optimization models select the best combination of variables that maximize or minimize certain objectives. For example, portfolio optimization in finance attempts to select the best portfolio of asset types (e.g., stocks and bonds) by either maximizing expected return or minimizing financial risk. Transport network optimization models optimize the best route (less travel time) given the current traffic situation.

- Simulation model simulates the likelihood of various potential outcomes under uncertainty. For example, a simulation model like Monte Carlo simulation can take the best portfolio recommended by an optimization model and generate thousands of simulations to determine the likelihood of the portfolio generating profit for users. Simulation models can also perform sensitivity analysis to determine the behaviour of the model under various scenarios.



[Next: Model categories by algorithms](types-by-framework.md)
