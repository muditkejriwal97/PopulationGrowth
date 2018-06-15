import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

file = 'Data Population - v5 - 1800 to 2100 World Regions and Countries by Gapminder.xlsx'
data = pd.ExcelFile(file)
df1 = data.parse('pivoted_region_data_for_chart')
df1 = df1.transpose()
df1 = df1.drop('geo')
df1 = df1.drop('indicator')
df1 = df1.drop('name')
df1.columns = ['America', 'Europe', 'Africa', 'Asia']
df1.plot.line()
li= list(df1.index.values)

plt.suptitle('Region Wise Population (1800 to 2100)', fontsize=20)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Population(Billions)', fontsize=18)
plt.ticklabel_format(useOffset=False, style='plain')
plt.xticks(range(1800,2120,20))

plt.grid()
plt.show()

