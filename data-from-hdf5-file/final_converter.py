# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:28:16 2022

@author: Rishikesh Sreehari
"""

import pandas as pd
import h5py
import time
from pyproj import Proj, transform


input_epsg=24378
output_epsg=4326

start_time = time.time()


with h5py.File("mer.h5", "r") as file:
    df_X = pd.DataFrame(file.get("X")[:-2], columns=["X"])
    df_Y = pd.DataFrame(file.get("Y"), columns=["Y"])
    DHI = file.get("DHI")[0][:, :-2].reshape(-1)

final = df_Y.merge(df_X, how="cross").assign(DHI=DHI)[["X", "Y", "DHI"]]



final['X2'],final['Y2']=transform(input_epsg,output_epsg,final[["X"]].to_numpy(),final[["Y"]].to_numpy(),always_xy=True)


#final.to_csv("final_converted1.csv", index=False)

print("--- %s seconds ---" % (time.time() - start_time))
