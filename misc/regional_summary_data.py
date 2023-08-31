# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:19:10 2023

@author: Admin
"""


import pandas as pd



monthly = pd.read_csv("monthly.csv",index_col=1)
consumption = pd.read_csv("consumption.csv",index_col=1)


states = monthly.columns[1:]


monthly.index = pd.to_datetime(monthly.index, format='%b-%y')

# Remove commas and convert to numeric
year_2012 = monthly['2012']
year_2012 = year_2012.drop(columns=['Year'])
year_2012 = year_2012.replace(',', '', regex=True)
year_2012 = year_2012.replace({'NA': None, 'inf': None, '-inf': None})
year_2012 = year_2012.apply(pd.to_numeric, errors='coerce')


# Find the maximum peak demand and corresponding date for each state in 2012
max_demand_2012 = year_2012.max()
date_of_max_demand_2012 = year_2012.idxmax().dt.strftime('%b')






result_df = pd.DataFrame({
    'Max Demand 2012': max_demand_2012,
    'Date of Max Demand 2012': date_of_max_demand_2012
})

result_df.to_csv("2012.csv")


# Remove commas and convert to numeric
year_2022 = monthly['2022']
year_2022 = year_2022.drop(columns=['Year'])
year_2022 = year_2022.replace(',', '', regex=True)
year_2022 = year_2022.replace({'NA': None, 'inf': None, '-inf': None})
year_2022 = year_2022.apply(pd.to_numeric, errors='coerce')


# Find the maximum peak demand and corresponding date for each state in 2012
max_demand_2022 = year_2022.max()
date_of_max_demand_2022 = year_2022.idxmax().dt.strftime('%b')



result_df = pd.DataFrame({
    'Max Demand 2022': max_demand_2022,
    'Date of Max Demand 2022': date_of_max_demand_2022
})

result_df.to_csv("2022.csv")



summed_consumption = consumption.groupby('State')[['2012', '2022']].sum()

# Calculate the CAGR formula: (Ending Value / Beginning Value) ^ (1 / Number of Years) - 1
summed_consumption['CAGR'] = ((summed_consumption['2022'] / summed_consumption['2012']) ** (1 / 10) - 1)*100

# Create the result DataFrame with 'Region', summed consumption values, and CAGR
result_df = summed_consumption.join(consumption['Region']).reset_index()

result_df.to_csv("cons.csv")

result_df.index = result_df['State']





#%% Finding sectoral results



import pandas as pd

# Load the consumption DataFrame from a CSV file
consumption = pd.read_csv("consumption.csv")

# Convert the '2022' column to numeric while handling errors
consumption['2022'] = pd.to_numeric(consumption['2022'], errors='coerce')

# Replace NaN values in the '2022' column with 0
consumption['2022'].fillna(0, inplace=True)

major_sector_consumption = consumption.groupby('State')['2022'].max()

# Calculate the total consumption for each state in 2022
total_consumption_2022 = consumption.groupby('State')['2022'].sum()

# Identify the major contributing sector for each state in 2022
major_sector_idx = consumption.groupby('State')['2022'].idxmax()
major_sector = consumption.loc[major_sector_idx, 'Sector']

# Create DataFrames for each result
total_consumption_df = pd.DataFrame({'2022 Total Consumption': total_consumption_2022})

# Create the major_sector_df using the major_sector and major_sector_idx Series
major_sector_df = pd.DataFrame({'Major Sector': major_sector})
major_sector_df['State'] = major_sector_idx.index
major_sector_df.set_index('State', inplace=True)

# Calculate the share of major sector consumption for each state in 2022
share_major_sector = (major_sector_consumption / total_consumption_2022) * 100
share_major_sector_df = pd.DataFrame({'Share of Major Sector (%)': share_major_sector})

# Combine the DataFrames based on the index ('State')
result_df = pd.concat([total_consumption_df, major_sector_df, share_major_sector_df], axis=1)

# Display the combined result DataFrame
print("Combined Result:")
print(result_df)

result_df.to_csv("results.csv")


