import pandas as pd
import matplotlib.pyplot as plt

#selecting data for plotting
df=pd.read_csv("../data/BRA_avg_temp.csv")
x_values=df.columns.tolist()
y_values=df.iloc[0].tolist()
df=pd.read_csv("../data/FRA_avg_temp.csv")
x1_values=df.columns.tolist()
y1_values=df.iloc[0].tolist()
df=pd.read_csv("../data/JAP_avg_temp.csv")
x2_values=df.columns.tolist()
y2_values=df.iloc[0].tolist()
df=pd.read_csv("../data/NEW_avg_temp.csv")
x3_values=df.columns.tolist()
y3_values=df.iloc[0].tolist()
df=pd.read_csv("../data/POL_avg_temp.csv")
x4_values=df.columns.tolist()
y4_values=df.iloc[0].tolist()
df=pd.read_csv("../data/SOU_avg_temp.csv")
x5_values=df.columns.tolist()
y5_values=df.iloc[0].tolist()
df=pd.read_csv("../data/SWE_avg_temp.csv")
x6_values=df.columns.tolist()
y6_values=df.iloc[0].tolist()
df=pd.read_csv("../data/UKR_avg_temp.csv")
x7_values=df.columns.tolist()
y7_values=df.iloc[0].tolist()

#making plot
plt.figure(figsize=(10, 5))
plt.plot(x4_values, y4_values, color="black", linewidth=1, label="POL")
plt.plot(x_values, y_values, color="black", linewidth=1, label="BRA")
plt.plot(x1_values, y1_values, color="black",  linewidth=1, label="FRA")
plt.plot(x2_values, y2_values, color="black",  linewidth=1, label="JAP")
plt.plot(x3_values, y3_values, color="black", linewidth=1, label="NEW")
plt.plot(x5_values, y5_values, color="black",  linewidth=1, label="SOU")
plt.plot(x6_values, y6_values, color="black",  linewidth=1, label="SWE")
plt.plot(x7_values, y7_values, color="black",  linewidth=1, label="UKR")
plt.title('Avg temperatures in 8 countries each year')
plt.xlabel('Year')
plt.ylabel('Avg Temp Cel')

plt.legend()

plt.xticks([x for i, x in enumerate(x4_values) if i % 20 == 0])

plt.grid(True)

#plt.show()
plt.savefig("../plots/lab5/avgTemAllBW.png")