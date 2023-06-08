# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:38:48 2023

@author: Admin
"""

import pandas as pd
import numpy as np


ind_file = r"path\ind.xlsx"
agr_file = r"path\agr.xlsx"
ban_file = r"path\ban.xlsx"
ser_file = r"path\ser.xlsx"
man_file = r"path\man.xlsx"
con_file = r"path\cons.xlsx"




ind = pd.ExcelFile(ind_file)
agr = pd.ExcelFile(agr_file)
ban = pd.ExcelFile(ban_file)
ser = pd.ExcelFile(ser_file)
man = pd.ExcelFile(man_file)
con = pd.ExcelFile(con_file)


ind_sheet_names = ind.sheet_names
agr_sheet_names = agr.sheet_names
ban_sheet_names = ban.sheet_names
ser_sheet_names = ser.sheet_names
man_sheet_names = man.sheet_names
con_sheet_names = con.sheet_names



#Industry data loading
ind1 = pd.read_excel(ind_file, sheet_name=ind_sheet_names[2],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
ind2 = pd.read_excel(ind_file, sheet_name=ind_sheet_names[3],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
ind2 = ind2.iloc[:-2]  #Dropping last 2 rows for cleaning
ind_df = pd.concat([ind1, ind2], axis=1)


#Agriculture data loading
agr1 = pd.read_excel(agr_file, sheet_name=agr_sheet_names[2],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
agr2 = pd.read_excel(agr_file, sheet_name=agr_sheet_names[3],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
agr2 = agr2.iloc[:-2]  #Dropping last 2 rows for cleaning
agr_df = pd.concat([agr1, agr2], axis=1)

#Services data loading
ser1 = pd.read_excel(ser_file, sheet_name=ser_sheet_names[2],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
ser2 = pd.read_excel(ser_file, sheet_name=ser_sheet_names[3],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
ser2 = ser2.iloc[:-2]  #Dropping last 2 rows for cleaning
ser_df = pd.concat([ser1, ser2], axis=1)


#Banking data loading
ban1 = pd.read_excel(ban_file, sheet_name=ban_sheet_names[2],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
ban2 = pd.read_excel(ban_file, sheet_name=ban_sheet_names[3],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
ban2 = ban2.iloc[:-2]  #Dropping last 2 rows for cleaning
ban_df = pd.concat([ban1, ban2], axis=1)



#Manufacturing data loading
man1 = pd.read_excel(man_file, sheet_name=man_sheet_names[2],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
man2 = pd.read_excel(man_file, sheet_name=man_sheet_names[3],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
man2 = man2.iloc[:-2]  #Dropping last 2 rows for cleaning
man_df = pd.concat([man1, man2], axis=1)


#Construction data loading
con1 = pd.read_excel(con_file, sheet_name=con_sheet_names[2],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
con2 = pd.read_excel(con_file, sheet_name=con_sheet_names[3],skiprows=3, header=2,usecols="B:ZZ",index_col=0)
con2 = con2.iloc[:-2]  #Dropping last 2 rows for cleaning
con_df = pd.concat([con1, con2], axis=1)





output_path="path\ouput.xlsx"
excel_file = pd.ExcelWriter(output_path, engine='xlsxwriter')

# Iterate over each state
for state in agr_df.index:
    # Create a new sheet for the state
    sheet_name = state

    # Get the 'ind' and 'agr' sectors data for the state
    ind_data = ind_df.loc[state]
    agr_data = agr_df.loc[state]
    ser_data = ser_df.loc[state]
    ban_data = ban_df.loc[state]
    man_data = man_df.loc[state]
    con_data = con_df.loc[state]

    # Create a new DataFrame for the state sheet
    state_df = pd.DataFrame({'Sector': ['Industry', 'Agriculture','Services','Banking','Manufacturing','Construction'],
                             **{year: [ind_val, agr_val, ser_val, ban_val,man_val, con_val]
                                for year, ind_val, agr_val, ser_val, ban_val,man_val, con_val in zip(ind_data.index, ind_data.values, agr_data.values, ser_data.values, ban_data.values, man_data.values, con_data.values)}})

    # Write the state DataFrame to the Excel file
    state_df.to_excel(excel_file, sheet_name=sheet_name, index=False)

# Save and close the Excel file
excel_file.save()
excel_file.close()



