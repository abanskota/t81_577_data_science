### Assignment 5

In this assignment, you will work with the familiar dataset on on-time performace of US domestic flights for the 2015. You can download the data from [Kaggle](https://www.kaggle.com/usdot/flight-delays). Make sure you download all three files i.e. `flights.csv`, `airport.csv`, and `airlines.csv` in the Data section. 

_NOTE_: If you get memory issue in your computer, answer the airport related question ( e.g question 1.1) by selecting records related to American Airlines only, and the airlines related question (question 1.2 and 1.3) by selecting flights that originated from Atlanta airport (ATL) only. If you cannot read the whole csv file into Pandas due to memory issue, read the file in chunks and select data only for the airport and airline.

1. Perform tabular analysis in a **jupyter notebook** to answer the following questions. 

1.1. What are the top three airports (ORIGIN_AIRPORT) in terms of the total number of flights departed in 2015? Print out the total number of flights by ORIGIN_AIRPORT in descending order.  (2 points)

1.2. What are the top three airlines in terms of the total number of flights they served in three months (Jan-March 2015)?. Print out the values in descending order. (2 points)

1.3. Create a column that classifies airlines into three categories ( big, medium, and small) using `cut` method of dataframe based upon the number of flights they had in 2015. Print out the mean number of flights in each category. (2 points)

2. Create a graph that shows the mean number of flights departed from ATL airport from January to March 2015. The X-axis ticks should show the date in `year-month` format not just the month. (2 points)

3. Create a bar diagram that shows mean delay time by the three categories you created in 1.3 for all airlines that departed from ATL airport in 2015. (2 points)

Good luck!

Submit your Notebook to Canvas for grading!
