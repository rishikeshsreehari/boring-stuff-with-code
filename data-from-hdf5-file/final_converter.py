# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:28:16 2022

@author: Rishikesh Sreehari
"""

import pandas as pd
import h5py
import time
from pyproj import Proj, transform, transformer
from pyproj import CRS
from pyproj import Transformer
import numpy as np


start_time = time.time()


with h5py.File("mer.h5", "r") as file:
    df_X = pd.DataFrame(file.get("X")[:-2], columns=["X"])
    df_Y = pd.DataFrame(file.get("Y"), columns=["Y"])
    DHI = file.get("DHI")[0][:, :-2].reshape(-1)
    projection= file['Projection_Information']
    lat_0= float(projection.attrs['standard_parallel'])
    lon_0= float(projection.attrs['longitude_of_projection_origin'])
    

final = df_Y.merge(df_X, how="cross").assign(DHI=DHI)[["X", "Y", "DHI"]]


projString='+proj=merc +lat_ts='+str(lat_0)+' +lon_0='+str(lon_0)
inProj=Proj(projString)
outProj=Proj(init='epsg:4326')


final['X2'],final['Y2']=transform(inProj,outProj,final[["X"]].to_numpy(),final[["Y"]].to_numpy())
final.to_csv("plotted.csv", index=False)


print("--- %s seconds ---" % (time.time() - start_time))

