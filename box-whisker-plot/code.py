
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import seaborn as sns
from matplotlib.patches import Patch




data = pd.read_csv('final_name.csv', index_col=0)
data.sort_index(inplace=True)
data.dropna(inplace=True)
data.index = pd.to_datetime(data.index, format='%d-%m-%Y %H:%M')
data['Month'] = data.index.month_name()
data['Abbreviated Month'] = data.index.strftime('%b')



## Single Plot

region = 'Northern'


# Set the plot style
sns.set(style='ticks')  

# Create the box plot using Seaborn
plt.figure(figsize=(12, 6))
sns.boxplot(x='Abbreviated Month', y=region, data=data, color='orange')

# Customize the plot
plt.title(region+ ' Region Electricity Demand - 2022 ')
plt.xlabel('Months')
plt.ylabel('Electricity Demand(MW)')

# Show the plot
plt.show()


#Overlapping plots

# Set the plot style
sns.set(style='ticks')

# Create the box plot using Seaborn for Eastern region
plt.figure(figsize=(12, 6))
ax1 = sns.boxplot(x='Abbreviated Month', y='Eastern', data=data, color='lightgreen')

# Create a secondary axis for North Eastern region
ax2 = plt.twinx()
sns.boxplot(x='Abbreviated Month', y='North Eastern', data=data, ax=ax2, color='violet')

# Customize the plot
plt.title('Eastern and North Eastern Region Electricity Demand - 2022')
ax1.set_xlabel('Months')
ax1.set_ylabel('Eastern Demand (MW)')
ax2.set_ylabel('North Eastern Demand (MW)')

ax1.set_ylim(0, 30000)
ax2.set_ylim(0, 8000)

# Create custom legend labels
legend_labels = [Patch(facecolor='lightgreen', label='Eastern'),
                 Patch(facecolor='violet', label='North Eastern')]

# Add the legend to the plot
plt.legend(handles=legend_labels)

# Show the plot
plt.show()

