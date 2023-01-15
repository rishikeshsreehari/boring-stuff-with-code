# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:28:16 2022

@author: Rishikesh Sreehari
"""

import pandas as pd
import h5py
import time
from pyproj import Proj, transform
#import numpy as np
import geopandas 
#from shapely.geometry import Point 
import shapely.speedups

shapely.speedups.enable()

start_time = time.time()


with h5py.File("mer.h5", "r") as file:
    df_X = pd.DataFrame(file.get("X")[:-2], columns=["X"])
    df_Y = pd.DataFrame(file.get("Y"), columns=["Y"])
    DHI = file.get("DHI")[0][:, :-2].reshape(-1)
    DNI = file.get("GHI")[0][:, :-2].reshape(-1)
    GHI = file.get("DNI")[0][:, :-2].reshape(-1)
    projection= file['Projection_Information']
    lat_0= float(projection.attrs['standard_parallel'])
    lon_0= float(projection.attrs['longitude_of_projection_origin'])
    

final = df_Y.merge(df_X, how="cross").assign(DHI=DHI, GHI=GHI,DNI=DNI )[["X", "Y", "DHI","GHI","DNI"]]

projString='+proj=merc +lat_ts='+str(lat_0)+' +lon_0='+str(lon_0)
inProj=Proj(projString)
outProj=Proj(init='epsg:4326')


final['X2'],final['Y2']=transform(inProj,outProj,final[["X"]].to_numpy(),final[["Y"]].to_numpy())



filepath =r'D:\Work\MOSDAC\india_shape\india_st.shp'  #Reading polygon
map_df = geopandas.read_file(filepath)



map_df['geometry'] = map_df.geometry.simplify(tolerance=0.1)

map_df = map_df.geometry.unary_union  #Joining all polygons into a single multipolygon


#Convert both dataframe into Geodataframes
final = geopandas.GeoDataFrame(final, geometry=geopandas.points_from_xy(final['X2'], final['Y2']))
map_df = geopandas.GeoDataFrame(geometry=[map_df])



result_df = geopandas.sjoin(final, map_df, op='within') #Using spatial join to find points inside



result_df.to_csv("plot999.csv")


print("--- %s seconds ---" % (time.time() - start_time))










