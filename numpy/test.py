import numpy as np

A = [45,37,42,35,39]
B = [38,31,26,28,33]

data = np.array([A,B])

covMatrix = np.cov(data,bias=False)
print (covMatrix)