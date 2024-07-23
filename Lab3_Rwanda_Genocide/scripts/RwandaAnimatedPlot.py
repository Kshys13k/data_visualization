import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

YEAR=2022 #<1960,2022>

#selecting data neccessary for all frames
df=pd.read_csv("../data/rwanda.csv")
categories=df["Country Name"].tolist()
df=df.iloc[:,1:]
colors=["red", "blue", "green"]

fig, ax = plt.subplots(figsize=(10,6))

fr=[] #list of frames to slow down animation in years close to genocide in rwanda

for i in range(60):
    fr.append(i)
    if 32<i and i <37:
        for _ in range(4):
            fr.append(i)

def update(frame):
    plt.cla()

    #selecting data for specyfic frame and making bars
    frame+=1960
    values = df[str(frame)].tolist()
    bars= ax.bar(categories,values)

    #changing colors
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

    #captions
    plt.text(x=0.05, y=0.95, s=frame, fontsize=30, ha='left', va='top', transform=plt.gca().transAxes) #current year
    if 1992 < frame and frame < 1999: #caption about genocide
        plt.text(x=0.05, y=0.75, s="1993- year of genocide in Rwanda", fontsize=12, ha='left', va='top', transform=plt.gca().transAxes, color="red")


ani = animation.FuncAnimation(fig, update, frames=fr,repeat=True)

# plt.show()
path="../plots/RwandaAnimatedPlot.mp4"
ani.save(path, writer='ffmpeg')

