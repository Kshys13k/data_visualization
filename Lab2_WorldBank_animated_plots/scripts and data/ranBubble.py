import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


#picking data for plotig
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_85.csv')
sortedDf= df.sort_values(by="2022", ascending=False)
df2=sortedDf.iloc[50:55,-63:-1]
df2=df2.T
newColNames=sortedDf.iloc[50:55,0]
df2.columns=newColNames.values
dfForPlot=df2
df=df2

#neccessary conversion
df.index = df.index.map(int)

#show data in every 10 years
df_decade = df[df.index % 10 == 0]

areas = {
    "Bangladesh": 147570,
    "Russian Federation": 17098242,
    "Mexico": 1964375,
    "Japan": 377975,
    "Ethiopia": 1104300
}
print(df)
#Calculating population density
for country in areas:
    df_decade[country + '_density'] = df_decade[country] / areas[country]

years_decade = df_decade.index

#generate plot:
plt.figure(figsize=(15, 10))
for country in areas:
    plt.scatter(years_decade, df_decade[country], s=df_decade[country + '_density']*10, alpha=0.5, label=country)

plt.title('Population and Population Density Every Decade')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.savefig("plots/bubbleRan.png")