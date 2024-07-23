import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

YEAR=2022 #<1960,2022>

#selecting data for plot
df=pd.read_csv("../data/rwanda.csv")
categories=df["Country Name"].tolist()
values=df[str(YEAR)].tolist()
colors=["red", "blue", "green"]

#making plot
fig, ax = plt.subplots(figsize=(10,6))
bars= ax.bar(categories,values)

#changinf colors
for bar, color in zip(bars,colors):
    bar.set_color(color)

#adding labels on top of bars
for rect, label in zip(bars, categories):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

#other stuff
plt.title("Comparison of the populations of Rwanda and neighbor countries with similar size")
plt.xlabel("Country")
plt.ylabel("Population [100k]")
plt.ylim(0,100 * 5.5) #fixed y-axis
plt.xticks(ticks=[]) #no labels under the plot

#year
plt.text(x=0.05, y=0.95, s=YEAR, fontsize=30, ha='left', va='top', transform=plt.gca().transAxes)

plt.show()
path="../plots/RwandaPlot.png"
#plt.savefig(path)
