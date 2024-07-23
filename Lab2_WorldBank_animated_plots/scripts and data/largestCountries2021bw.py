import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#picking data for ploting
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_85.csv')
sortedDf= df.sort_values(by="2022", ascending=False)
dfIndia=df.iloc[109,-63:-1]
dfChina=df.iloc[40,-63:-1]
dfIndonesia=df.iloc[106,-63:-1]
dfPakistan=df.iloc[184,-63:-1]
dfNigeria=df.iloc[174,-63:-1]
dfForPlot=pd.concat([dfIndia, dfChina, dfIndonesia, dfPakistan, dfNigeria], axis=1)
dfForPlot.columns=["IND","CHN","IDN","PAK","NGA"]

#One black and white plot

#translation from pandas df to lists for x and y axis (this time i won't use df.plot):
row = dfForPlot.iloc[61]
year=row.name
colNames = row.index.tolist()
values = row.values

labels = ["India", "China", "Indonesia", "Pakistan", "Nigeria"] #for legend
hatches = ["/", "\\", "x", 'o', '-']

#creating plot:
fig, ax = plt.subplots()
bars = ax.bar(colNames, values, color="white", edgecolor="black")

#adding hatches to bars:
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

#adding legend under the plot:
legend_patches = [mpatches.Patch(facecolor="white", edgecolor="black", hatch=hatch) for hatch in hatches]
plt.legend(handles=legend_patches, labels=labels, loc='upper center', bbox_to_anchor=(0.5, -0.02), ncol=3, frameon=False)

#adding labels on top of bars
for rect, label in zip(bars, colNames):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

#other stuff:
plt.title('Comparison of the populations of the largest countries')
plt.xlabel('Country')
plt.ylabel('Population')
plt.ylim(0, 1e9 * 1.5) #fixed y-axis
plt.text(x=0.95, y=0.95, s=year, fontsize=30, ha='right', va='top', transform=ax.transAxes) #year
plt.xticks(ticks=[]) #no labels under the plot

#saving plot
filename="plots/plot1bw.png"
plt.savefig(filename)