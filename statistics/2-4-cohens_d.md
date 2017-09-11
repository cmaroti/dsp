[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> This question asks us to investigate whether first babies are lighter or heavier than others. The mean of the first babies’ weights is 7.20 lbs, while the mean of the other babies’ weights is 7.33 lbs. This might lead us to believe that first babies tend to weigh slightly less than other babies; however, some of this may be due to sample sizes as there are more other babies than first babies. The Cohen’s *d* for the difference in first babies vs. other babies’ weights is -0.089 standard deviations. This is difference is slightly greater in magnitude than the Cohen’s *d* for pregnancy length, 0.029 standard deviations, but is still very small when compared to the Cohen’s *d* for the difference in men and women’s heights, 1.7 standard deviations. Here is the code I used:
```python
import nsfg

def cohens_d(group1, group2):
    '''
    diff in means / combined std dev
    '''
    meandiff = group1.mean() - group2.mean()
    combined = group1.append(group2)
    return meandiff/combined.std()

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
print('Mean of first babies:', firsts.totalwgt_lb.mean())
print('Mean of other babies:', others.totalwgt_lb.mean())
print("Cohen's d:", cohens_d(firsts.totalwgt_lb, others.totalwgt_lb))
```

