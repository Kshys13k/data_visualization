import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#selecting data for plotting
df=pd.read_csv("../data/cleaned_temperature.csv")
dfNew=df[df["country_id"]=="NEW"]
dfBra=df[df["country_id"]=="BRA"]
dfSou=df[df["country_id"]=="SOU"]
dfUkr=df[df["country_id"]=="UKR"]
dfFra=df[df["country_id"]=="FRA"]
dfSwe=df[df["country_id"]=="SWE"]
dfJap=df[df["country_id"]=="JAP"]
dfPol=df[df["country_id"]=="POL"]

new=dfNew["AverageTemperatureCel"].tolist()
bra=dfBra["AverageTemperatureCel"].tolist()
sou=dfSou["AverageTemperatureCel"].tolist()
ukr=dfUkr["AverageTemperatureCel"].tolist()
fra=dfFra["AverageTemperatureCel"].tolist()
swe=dfSwe["AverageTemperatureCel"].tolist()
jap=dfJap["AverageTemperatureCel"].tolist()
pol=dfPol["AverageTemperatureCel"].tolist()

forPlot=[new,bra,sou,ukr,fra,swe,jap,pol]

#making plot
plt.boxplot(forPlot)
plt.xlabel("Country")
plt.ylabel("AverageTemperatureCelsius")
plt.title("Average temperatures in different countries")
plt.grid(True)
plt.xticks([1,2,3,4,5,6,7,8],["NEW","BRA","SOU","UKR","FRA","SWE","JAP","POL"])

#jitter
for i, countryData in enumerate(forPlot, start=1):
    # Adding random jitter on x line
    jittered_x = np.random.normal(i, 0.1, size=len(countryData))
    # Adding plot with jitter
    plt.scatter(jittered_x, countryData, color='orange', alpha=0.2, s=1)




plt.savefig("../plots/finalVersionsOfPlots/boxPlot.png")
# plt.show()
