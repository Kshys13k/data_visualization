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

dfForPlot=df3

#animated plot
fig, ax = plt.subplots(figsize=(10,6))
def update(frame):
    plt.cla()

    row = dfForPlot.iloc[frame]
    year = row.name
    colors = ['blue', 'red', 'pink', 'yellow', 'green']

    # creating plot
    row.plot(kind="bar", color=colors)

    # adding labels on top of bars
    for idx, value in enumerate(row):
        plt.text(idx, value, row.index[idx], ha='center', va='bottom')

    # other stuff:
    plt.title('Comparison of the populations of Poland and 4 similar countries')
    plt.xlabel('Country')
    plt.ylabel('Population')
    plt.ylim(0, 1e9 * 0.06)  # fixed y-axis
    plt.text(x=0.95, y=0.95, s=year, fontsize=30, ha='right', va='top', transform=plt.gca().transAxes)  # adding year
    plt.xticks(ticks=[])  # no labels under the plot

ani = animation.FuncAnimation(fig, update, frames=len(dfForPlot),repeat=True)
ani.save('plots/animated/Poland.mp4', writer='ffmpeg')