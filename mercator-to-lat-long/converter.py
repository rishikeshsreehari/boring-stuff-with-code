# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:48:29 2022

@author: Rishikesh
"""

from pyproj import Proj, transform
import pandas as pd


cordinates = pd.read_csv('Y.csv')
cordinates['X2'] = ''
cordinates['Y2'] = ''


def convert(x1,y1,i):
    inProj = Proj(init='epsg:3857')
    outProj = Proj(init='epsg:4326')
    x2,y2 = transform(inProj,outProj,x1,y1)
    cordinates.loc[i,'X2'] = x2
    cordinates.loc[i,'Y2'] = y2
    return(x2,y2)


for i in range(len(cordinates)):
    x1=cordinates.loc[i,'X'] 
    y1=cordinates.loc[i,'Y'] 
    convert(x1, y1, i)
    

cordinates.to_csv("converted.csv", index=False)




