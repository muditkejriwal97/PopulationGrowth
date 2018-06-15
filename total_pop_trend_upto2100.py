import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

#Reading File and Parsing
file = 'Data Population - v5 - 1800 to 2100 World Regions and Countries by Gapminder.xlsx'
data = pd.ExcelFile(file)
df1 = data.parse('pivoted_country_data_for_chart')

#Dropping
df1 = df1.drop(["geo", "indicator", "name"], axis=1)

#Finding total population for each year
df2=df1.sum()
df2.plot()

#Fromatting axis ticks
plt.ticklabel_format(useOffset=False, style='plain')

plt.suptitle('Global Population(1800 to 2100)', fontsize=20)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Population(Billions)', fontsize=18)
plt.xticks(range(1800,2120,20))

plt.grid()
plt.margins(0)

plt.show()
