import pandas as pd
import matplotlib.pyplot as plt

#selecting data for plotting
df=pd.read_csv("../data/FRA_avg_temp.csv")
x_values=df.columns.tolist()
y_values=df.iloc[0].tolist()


#making plot
plt.figure(figsize=(10, 5))
plt.scatter(x_values,y_values, edgecolor= "none", facecolor="darkblue")
plt.title('Avg temperature in France each year')
plt.xlabel('Year')
plt.ylabel('Avg Temp Cel')


plt.xticks([x for i, x in enumerate(x_values) if i % 20 == 0])

plt.grid(True)





#making plot


#plt.show()
plt.savefig("../plots/scatter_fra.png")
