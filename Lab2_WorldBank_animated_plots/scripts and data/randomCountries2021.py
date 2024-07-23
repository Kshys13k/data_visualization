import pandas as pd
import matplotlib.pyplot as plt

#picking data for plotig
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_85.csv')
sortedDf= df.sort_values(by="2022", ascending=False)
df2=sortedDf.iloc[50:55,-63:-1]
df2=df2.T
newColNames=sortedDf.iloc[50:55,0]
df2.columns=newColNames.values
dfForPlot=df2

#Generating one, color plot
row = dfForPlot.iloc[61]
year=row.name
colors=['orange', 'red', 'yellow', 'blue', 'green']

#creating plot
plt.figure(figsize=(10,6))
row.plot(kind="bar", color=colors)

#adding labels on top of bars
for idx, value in enumerate(row):
    plt.text(idx, value, row.index[idx], ha='center', va='bottom')

#other stuff:
plt.title('Comparison of the populations of 5 randomly chosen countries')
plt.xlabel('Country')
plt.ylabel('Population')
plt.ylim(0, 1e9 * 0.2) #fixed y-axis
plt.text(x=0.95, y=0.95, s=year, fontsize=30, ha='right', va='top', transform=plt.gca().transAxes) #adding year
plt.xticks(ticks=[]) #no labels under the plot

#plt.show()

filename="plots/plotRan.png"
plt.savefig(filename)