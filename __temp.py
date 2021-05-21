import numpy
import joblib

from __Parameters import *
from sklearn.cluster import KMeans


a = {1:[1,2,3], 2:[1,2,3], 3:[1,2,3]}
f = [1,2,3,45,6]
for key, val in a.items():
    val[1] = 0
for i in f:
    i = 0
print(f)