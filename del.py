from scipy import stats
import numpy as np
n=10
p=0.5
kk = np.arange(0, 11+1)
bin=stats.binom.cdf(kk,n,p)
b=bin[9]
print(b)





