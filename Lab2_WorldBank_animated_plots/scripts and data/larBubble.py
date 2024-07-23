import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


#picking data for plotig
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_85.csv')
sortedDf= df.sort_values(by="2022", ascending=False)
dfIndia=df.iloc[109,-63:-1]
dfChina=df.iloc[40,-63:-1]
dfIndonesia=df.iloc[106,-63:-1]
dfPakistan=df.iloc[184,-63:-1]
dfNigeria=df.iloc[174,-63:-1]
dfForPlot=pd.concat([dfIndia, dfChina, dfIndonesia, dfPakistan, dfNigeria], axis=1)
dfForPlot.columns=["IND","CHN","IDN","PAK","NGA"]
df=dfForPlot

print(df)
#neccessary conversion
df.index = df.index.map(int)

#show data in every 10 years
df_decade = df[df.index % 10 == 0]

areas = {
    "IND": 3287263,
    "CHN": 9596961,
    "IDN": 1904569,
    "PAK": 881913,
    "NGA": 923768
}

#Calculating population density
for country in areas:
    print(df_decade[country] )
    print(areas[country])
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
plt.show()
plt.savefig("plots/bubbleLar.png")