import pandas as pd
import matplotlib.pyplot as plt

#selecting data for plotting
df=pd.read_csv("../data/POL_without_outliers.csv")
x_values=df.columns.tolist()
y_values=df.iloc[0].tolist()


#making plot
plt.figure(figsize=(10, 5))
plt.scatter(x_values,y_values, edgecolor= "none", facecolor="crimson")
plt.title('Avg temperature in Poland each year')
plt.xlabel('Year')
plt.ylabel('Avg Temp Cel')


plt.xticks([x for i, x in enumerate(x_values) if i % 20 == 0])

plt.grid(True)





#making plot


#plt.show()
plt.savefig("../plots/pol_without_outliers.png")
