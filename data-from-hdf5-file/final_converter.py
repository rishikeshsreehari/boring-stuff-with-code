
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 23:31:16 2022

@author: Rishikesh Sreehari
"""

import h5py
import numpy as np
import pandas as pd
import time
from pyproj import Proj, transform

#import geopandas as gpd


#%%
start_time = time.time()



f = h5py.File('mer.h5', 'r')

for key in f.keys():
    #print(key) #Names of the root level object names in HDF5 file - can be groups or datasets.
    #print(type(f[key])) # get the object type: usually group or dataset
    ls = list(f.keys())
   



#Get the HDF5 group; key needs to be a group name from above
key ='DHI'
#group = f['OBSERVATION_TIME']

#print("Group")
#print(group)

#for key in ls:
 #data = f.get(key)   
 #dataset1 = np.array(data)

#length=len(dataset1)


masterdf=pd.DataFrame()


data = f.get(key)   
dataset1 = np.array(data)
#masterdf[key]=dataset1


X = f.get('X')
X_1 = pd.DataFrame(X)

Y = f.get('Y')
Y_1 = pd.DataFrame(Y)




#%%

## Copied the values from array to a dataframe

data_df = pd.DataFrame(index=range(len(Y_1)),columns=range(len(X_1)))

for i in data_df.index:
    data_df.iloc[i] = dataset1[0][i]
    
    
#data_df.to_csv("test.csv")


#%%

## Converting 



final = pd.DataFrame(index=range(1616*1616),columns=['X', 'Y','GHI'])


k=0

for y in range(len(Y_1)):
    
    for x in range(len(X_1[:-2])):   #X and Y ranges are not same
        
        final.loc[k,'X'] = X_1[0][x]
        final.loc[k,'Y'] = Y_1[0][y]
        final.loc[k,'GHI'] = data_df.iloc[y,x]
        k=k+1
        print(k)
        
        
print("--- %s seconds ---" % (time.time() - start_time))



