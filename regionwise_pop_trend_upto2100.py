import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

#Reading File and Parsing
file = 'Data Population - v5 - 1800 to 2100 World Regions and Countries by Gapminder.xlsx'
data = pd.ExcelFile(file)
df1 = data.parse('pivoted_region_data_for_chart')

#Transpose of a dataframe and dropping 
df1 = df1.transpose()
df1 = df1.drop('geo')
df1 = df1.drop('indicator')
df1 = df1.drop('name')

#Renaming columns
df1.columns = ['America', 'Europe', 'Africa', 'Asia']

#Plotting Graph
df1.plot.line()

plt.suptitle('Region Wise Population (1800 to 2100)', fontsize=20)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Population(Billions)', fontsize=18)

#Optimizing ticks on x and y axis
plt.ticklabel_format(useOffset=False, style='plain')
plt.xticks(range(1800,2120,20))
plt.grid()

plt.show()

