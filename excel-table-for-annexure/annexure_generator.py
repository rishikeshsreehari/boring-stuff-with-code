# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 21:20:46 2022

@author: Admin
"""

import pandas as pd
import numpy as np
import xlsxwriter as xl






res_data=pd.read_excel(r'C:\Users\Admin\Desktop\Demand_consolidated.xlsx','res_consolidated',index_col=0)
ser_data=pd.read_excel(r'C:\Users\Admin\Desktop\Demand_consolidated.xlsx','ser_consolidated',index_col=0)                       
ag_data=pd.read_excel(r'C:\Users\Admin\Desktop\Demand_consolidated.xlsx','ag_consolidated',index_col=0)   
ind_data=pd.read_excel(r'C:\Users\Admin\Desktop\Demand_consolidated.xlsx','ind_consolidated',index_col=0)                      
                       

state_reg_dict = {'Telangana':'SR', 'Andaman & Nicobar Island':'SR', 'Andhra Pradesh':'SR',

           'Arunanchal Pradesh':'NER', 'Assam':'NER', 'Bihar':'ER', 'Chhattisgarh':'WR',

           'Daman & Diu':'WR', 'Goa':'WR', 'Gujarat':'WR', 'Haryana':'NR', 'Himachal Pradesh':'NR',

           'Jammu & Kashmir':'NR', 'Jharkhand':'ER', 'Karnataka':'SR', 'Kerala':'SR',

           'Lakshadweep':'SR', 'Madhya Pradesh':'WR', 'Maharashtra':'WR', 'Manipur':'NER',

           'Chandigarh':'NR', 'Puducherry':'SR', 'Punjab':'NR', 'Rajasthan':'NR', 'Sikkim':'ER',

           'Tamil Nadu':'SR', 'Tripura':'NER', 'Uttar Pradesh':'NR', 'Uttarakhand':'NR',

           'West Bengal':'ER', 'Odisha':'ER', 'Dadara & Nagar Havelli':'WR', 'Meghalaya':'NER',

           'Mizoram':'NER', 'Nagaland':'NER', 'NCT of Delhi':'NR'}



regions = set(state_reg_dict.values())


# for column in ag_data  :
    
#     print(column)

#%%
states = ind_data.columns[:-1]
years = ['2024-25', '2026-27', '2029-30']

#%%

list_bau_all_states = {}





for state in states:
    
    df_format = pd.DataFrame(index=['Agriculture','Services','industry','Residential'],columns=['2024-25','2026-27','2029-30'])
   
    for y in years:
    
    

        df_format.loc['industry',y] = ind_data[state].loc[y]
        df_format.loc['Agriculture',y] = ag_data[state].loc[y]
        df_format.loc['Services',y] = ser_data[state].loc[y]
        df_format.loc['Residential',y] = res_data[state].loc[y]
        
    list_bau_all_states[state]=df_format
    
writer = pd.ExcelWriter("rishi.xlsx")



#for states in list_bau_all_states:
#  print(states)
#  temp=pd.DataFrame()
#  temp= list_bau_all_states[states]
#  temp.to_excel(writer, sheet_name=states)
  


workbook = xl.Workbook(writer)
workbook  = writer.book
format = workbook.add_format({'border': 1})


merge_format = workbook.add_format({
    'bold':     True,
    'border':   1,
    'align':    'center',
    'valign':   'vcenter',
    #'fg_color': '#D7E4BC',
})

merge_format1 = workbook.add_format({
    'bold':     True,
    'border':   1,
    'align':    'center',
    'valign':   'vcenter',
    'fg_color': '#D7E4BC',
})


row_value=3

for states in list_bau_all_states:
  temp=pd.DataFrame()
  temp= list_bau_all_states[states]
  temp.to_excel(writer, sheet_name='Sheet1',startrow=row_value) 
  worksheet = writer.sheets['Sheet1']
  worksheet.merge_range(row_value-1, 0, row_value, 0,states,merge_format1)
  worksheet.conditional_format(row_value,1, row_value+4, 4,  {'type': 'no_blanks','format': format})
  worksheet.merge_range(row_value-1, 1, row_value-1, 3, 'BAU',merge_format)
  row_value = row_value + 10

row_value=3
  
for states in list_bau_all_states:
  temp=pd.DataFrame()
  temp= list_bau_all_states[states]
  temp.to_excel(writer, sheet_name='Sheet1',startrow=row_value,startcol=4,index=False) 
  worksheet = writer.sheets['Sheet1']
  worksheet.conditional_format(row_value,4, row_value+4, 7,  {'type': 'no_blanks','format': format})
  worksheet.merge_range(row_value-1, 4, row_value-1, 6, 'High Growth Rate',merge_format)
  row_value = row_value + 10
  
  
row_value=3
  
for states in list_bau_all_states:
  temp=pd.DataFrame()
  temp= list_bau_all_states[states]
  temp.to_excel(writer, sheet_name='Sheet1',startrow=row_value,startcol=7,index=False)
  worksheet = writer.sheets['Sheet1']
  worksheet.conditional_format(row_value,7, row_value+4, 10,  {'type': 'no_blanks','format': format})
  worksheet.merge_range(row_value-1, 7, row_value-1, 9, 'Historical Growth Rate',merge_format)
  row_value = row_value + 10


writer.save()








        
        
    





