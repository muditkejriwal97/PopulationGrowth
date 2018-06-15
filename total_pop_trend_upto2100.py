import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

file = 'Data Population - v5 - 1800 to 2100 World Regions and Countries by Gapminder.xlsx'
data = pd.ExcelFile(file)
df1 = data.parse('pivoted_country_data_for_chart')
#df1 = df1.transpose()
df1 = df1.drop(["geo", "indicator", "name"], axis=1)
df2=df1.sum()
df2.plot()
plt.ticklabel_format(useOffset=False, style='plain')

plt.suptitle('Global Population(1800 to 2100)', fontsize=20)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Population(Billions)', fontsize=18)
plt.xticks(range(1800,2120,20))
plt.grid()
plt.margins(0)
print(df2)
plt.show()
