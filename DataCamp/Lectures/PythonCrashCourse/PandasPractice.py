#Pandas Tutorials

import numpy as np
import pandas as pd

lbls = ['a','b','c','d','e']
vals = [1,2,3,4,5]
tups = (1,2,3,4,5)
dics = {'a':1,'b':2,'c':3,'d':4,'e':5}

pseries1 = pd.Series(vals,lbls )
pseries2 = pd.Series(lbls)
pseries3 = pd.Series(dics)
'''
print(pseries1)
print(pseries2)
print(pseries3)
print(pseries1 + pseries3)
'''
#DataFrames
np.random.seed(1) #To keep the randn values same for all the runs
df = pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)