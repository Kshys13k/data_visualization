import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_85.csv')
sortedDf= df.sort_values(by="2022", ascending=False)
dfIndia=df.iloc[109,-63:-1]
dfChina=df.iloc[40,-63:-1]
dfIndonesia=df.iloc[106,-63:-1]
dfPakistan=df.iloc[184,-63:-1]
dfNigeria=df.iloc[174,-63:-1]
dfForPlot=pd.concat([dfIndia, dfChina, dfIndonesia, dfPakistan, dfNigeria], axis=1)
dfForPlot.columns=["IND","CHN","IDN","PAK","NGA"]

#Animated plot
fig, ax = plt.subplots(figsize=(10,6))
def update(frame):
    plt.cla()

    row = dfForPlot.iloc[frame]

    year = row.name
    labels = ["India", "China", "Indonesia", "Pakistan", "Nigeria"]
    colors = ['orange', 'red', 'pink', 'blue', 'green']

    row.plot(kind="bar", color=colors)

    for idx, value in enumerate(row):
        plt.text(idx, value, row.index[idx], ha='center', va='bottom')

    plt.title('Comparison of the populations of the largest countries')
    plt.xlabel('Country')
    plt.ylabel('Population')
    plt.ylim(0, 1e9 * 1.5)
    plt.text(x=0.95, y=0.95, s=year, fontsize=30, ha='right', va='top', transform=plt.gca().transAxes)
    plt.xticks(ticks=[])

    # Legend
    custom_lines = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
    plt.legend(custom_lines, labels, loc='upper center', bbox_to_anchor=(0.5, -0.04), ncol=3)

ani = animation.FuncAnimation(fig, update, frames=len(dfForPlot),repeat=True)
ani.save('plots/animated/largest.mp4', writer='ffmpeg')
