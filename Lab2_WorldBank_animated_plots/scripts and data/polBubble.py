import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


#picking data for plotig
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_85.csv')
sortedDf= df.sort_values(by="2022", ascending=False)
df3=sortedDf.loc[df.iloc[:,0]=="Poland"]
indexOfPoland = int(np.where(sortedDf.iloc[:,0] == 'Poland')[0])
df3=sortedDf.iloc[(indexOfPoland-2):(indexOfPoland+3),-63:-1]
df3=df3.T
newColNames=sortedDf.iloc[(indexOfPoland-2):(indexOfPoland+3),0]
df3.columns=newColNames.values
df=df3

#neccessary conversion
df.index = df.index.map(int)

#show data in every 10 years
df_decade = df[df.index % 10 == 0]

areas = {
    "Ukraine": 603628,
    "Morocco": 710850,
    "Poland": 322575,
    "Saudi Arabia": 2150000,
    "Uzbekistan": 448900
}

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
plt.savefig("plots/bubblePl.png")