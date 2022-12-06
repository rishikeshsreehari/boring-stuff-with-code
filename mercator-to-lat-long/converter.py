# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:48:29 2022

@author: Rishikesh Sreehari
"""

from pyproj import Proj, transform
import pandas as pd
import numpy as np
import h5py


# read coordinates in a dataframe
df_y = pd.DataFrame(np.array(h5py.File("mer.h5")['Y']))
df_x = pd.DataFrame(np.array(h5py.File("mer.h5")['X']))

# combine dataframes
df_comb = pd.concat([df_x,df_y], ignore_index=True, sort=False, axis=1)
# name columns
df_comb.set_axis(['X1','Y1'], axis=1, inplace=True)
# convert coordinates to degree



#cordinates = pd.read_csv('Y.csv')
df_comb['X2'] = ''
df_comb['Y2'] = ''


def convert(x1,y1,i):
    inProj = Proj(init='epsg:3857')
    outProj = Proj(init='epsg:4326')
    x2,y2 = transform(inProj,outProj,x1,y1)
    df_comb.loc[i,'X2'] = x2
    df_comb.loc[i,'Y2'] = y2
    return(x2,y2)


for i in range(len(df_comb))[:2]:
    x1=df_comb.loc[i,'X1'] 
    y1=df_comb.loc[i,'Y1'] 
    convert(x1, y1, i)
    

#cordinates.to_csv("converted.csv", index=False)




