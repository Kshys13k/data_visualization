import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#picking data for ploting
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_85.csv')
sortedDf= df.sort_values(by="2022", ascending=False)
df2=sortedDf.iloc[50:55,-63:-1]
df2=df2.T
newColNames=sortedDf.iloc[50:55,0]
df2.columns=newColNames.values
dfForPlot=df2

#One black and white plot

#translation from pandas df to lists for x and y axis (this time i won't use df.plot):
row = dfForPlot.iloc[61]
year=row.name
colNames = row.index.tolist()
colNames[1]="Russia"
values = row.values

hatches = ["/", "\\", "x", 'o', '-']

#creating plot:
fig, ax = plt.subplots()
bars = ax.bar(colNames, values, color="white", edgecolor="black")

#adding hatches to bars:
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

#adding labels on top of bars
for rect, label in zip(bars, colNames):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

#other stuff:
plt.title('Comparison of the populations of the largest countries')
plt.xlabel('Country')
plt.ylabel('Population')
plt.ylim(0, 1e9 * 0.2) #fixed y-axis
plt.text(x=0.95, y=0.95, s=year, fontsize=30, ha='right', va='top', transform=ax.transAxes) #year
plt.xticks(ticks=[]) #no labels under the plot

#saving plot
# plt.show()
filename="plots/plotRanbBw.png"
plt.savefig(filename)