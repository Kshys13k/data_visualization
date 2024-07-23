import pandas as pd
import matplotlib.pyplot as plt

#selecting data for plotting
df=pd.read_csv("../data/cleaned_temperature.csv")
x_values=df["year"].tolist()
y_values=df["AverageTemperatureCel"].tolist()


#making plot
plt.scatter(x_values,y_values, edgecolor= "none", facecolor="blue", marker=".", alpha=0.25)
plt.xlabel("Year")
plt.ylabel("AverageTemperatureCel")
plt.title("Average temperatures in different years")
plt.grid(True)


#plt.show()
plt.savefig("../plots/finalVersionsOfPlots/scatterPlot.png")
