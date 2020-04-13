## Splitting data into validation and test sets

**_Note_:** This lecture is based upon Andrew Ng's book: Machine Learning Yearning, which you can download from [here](https://www.deeplearning.ai/machine-learning-yearning/). 

![](../files/train-test.jpeg)

**Recap:**

• Training set — Which you run your learning algorithm on.

• Dev (development) set — Which you use to tune parameters, select features, and
make other decisions regarding the learning algorithm. Sometimes also called the
hold-out cross validation set.

• Test set — which you use to evaluate the performance of the algorithm, but not to make
any decisions regarding what learning algorithm or parameters to use.

### How to select dev and test data

Choose dev and test sets from a distribution that reflects your future data. This may not be the same as your training data’s distribution.


- The dev set should be large enough to detect differences between algorithms that you are
trying out. For example, a dev set of 10000 examples would probably be required to detect the performance difference of 0.1% among learning algorithms.



- Your dev set should be large enough to detect meaningful changes in the accuracy of your
algorithm, but not necessarily much larger. Your test set should be big enough to give you
a confident estimate of the final performance of your system.

- The test data should be large enough to give high confidence in the overall performance of your system. The old heuristic of a 70%/30% train/test split does not apply for problems where you have a lot of data; the dev and test sets can be much less than 30% of the data.


- Choose dev and test sets from the same distribution if possible.
 

- Don’t assume your training distribution is the same as your test distribution. However, the dev and test sets should come from the same distribution. If the dev and test sets come from different distributions,it might not be possible to pipoint why your model is performing well on dev set but not your test set. It could be because of one or more of the following reasons.

- You had overfit to the dev set.
- The test set is harder than the dev set. So your algorithm might be doing as well as could
be expected, and no further significant improvement is possible.
- The test set is not necessarily harder, but just different, from the dev set. So what works
well on the dev set just does not work well on the test set. In this case, a lot of your work
to improve dev set performance might be wasted effort.

Having mismatched dev and test sets introduces additional uncertainty about whether improving on the dev set distribution also improves test set performance. Having mismatched dev and test sets makes it harder to figure out what is and isn’t working, and thus makes it harder to prioritize what to work on.


- If your dev set and metric are no longer pointing your team in the right direction, quickly
change them: (i) If you had overfit the dev set, get more dev set data. (ii) If the actual
distribution you care about is different from the dev/test set distribution, get new
dev/test set data

