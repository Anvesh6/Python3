# Dealing with Missing data iin Pandas

import numpy as np
import pandas as pd

population = [[1999,2344,1233,np.nan,np.nan,3455],
              [2344,np.nan,4567,4343,5676,np.nan],
              [3456,7654,9876,8766,4545,2111],
              [6787,np.nan,np.nan,4322,2322],
              [3422,1212,2222,2344,np.nan,np.nan],
              [1002,1234,np.nan,3456,np.nan,3434]]

years = [2000,2001,2002,2003,2004,2005]

countries = ['USA','China','India','Russia','Japan','Pakistan']

data = pd.DataFrame(data= population, index=countries, columns =years)

databck = data[:] #backup data

print(data,'\n')
#Thresh is minimum number of data the is not nan to be present in column/ row to be retained. axis = 0 is for rows , 1 is for columns

#print(data.dropna(axis = 0, thresh=5))

#print(data.fillna(value='Filling data'))
for i in countries:
    data.loc[i]= data.loc[i].fillna(value = data.loc[i].mean())

'''
data.loc['USA']= data.loc['USA'].fillna(value = data.loc['USA'].mean())
data.loc['China']= data.loc['China'].fillna(value = data.loc['China'].mean())
data.loc['Japan']= data.loc['Japan'].fillna(value = data.loc['Japan'].mean())
data.loc['Russia']= data.loc['Russia'].fillna(value = data.loc['Russia'].mean())
data.loc['Pakistan']= data.loc['Pakistan'].fillna(value = data.loc['Pakistan'].mean())
'''
print(data)
