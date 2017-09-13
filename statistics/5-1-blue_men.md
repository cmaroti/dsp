[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> About 34% of the U.S. male population is within the required height range for Blue Man Group. We used `spicy.stats.norm` to create a normal distribution with mean 178 cm and standard deviation 7.7 cm. Then using `spicy.stats.norm.cdf` we calculated the  cumulative probability of the high end of the range converted to cm minus the cumulative probability of the low end converted to cm. This resulted in 0.34, or 34%. Below is the code excerpt from the jupyter notebook.

**Exercise:** In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use `scipy.stats.norm.cdf`.

`scipy.stats` contains objects that represent analytic distributions


```python
import scipy.stats
```

For example <tt>scipy.stats.norm</tt> represents a normal distribution.


```python
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)
```




    scipy.stats._distn_infrastructure.rv_frozen



A "frozen random variable" can compute its mean and standard deviation.


```python
dist.mean(), dist.std()
```




    (178.0, 7.7000000000000002)



It can also evaluate its CDF.  How many people are more than one standard deviation below the mean?  About 16%


```python
dist.cdf(mu-sigma)
```




    0.15865525393145741



How many people are between 5'10" and 6'1"?


```python
low = 70*2.54
high = 73*2.54
dist.cdf(high)-dist.cdf(low)
```




    0.34274683763147457
