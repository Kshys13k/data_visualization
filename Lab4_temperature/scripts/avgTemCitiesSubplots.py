import pandas as pd
import matplotlib.pyplot as plt

#selecting data for plotting
df=pd.read_csv("../data/cities/Auckland_NEW_avg_temp.csv")
xNEW1_values=df.columns.tolist()
yNEW1_values=df.iloc[0].tolist()
df=pd.read_csv("../data/cities/Hamilton_NEW_avg_temp.csv")
xNEW2_values=df.columns.tolist()
yNEW2_values=df.iloc[0].tolist()

df=pd.read_csv("../data/cities/Brasília_BRA_avg_temp.csv")
xBRA1_values=df.columns.tolist()
yBRA1_values=df.iloc[0].tolist()
df=pd.read_csv("../data/cities/Canoas_BRA_avg_temp.csv")
xBRA2_values=df.columns.tolist()
yBRA2_values=df.iloc[0].tolist()


df=pd.read_csv("../data/cities/Johannesburg_SOU_avg_temp.csv")
xSOU1_values=df.columns.tolist()
ySOU1_values=df.iloc[0].tolist()
df=pd.read_csv("../data/cities/Cape Town_SOU_avg_temp.csv")
xSOU2_values=df.columns.tolist()
ySOU2_values=df.iloc[0].tolist()

df=pd.read_csv("../data/cities/Kiev_UKR_avg_temp.csv")
xUKR1_values=df.columns.tolist()
yUKR1_values=df.iloc[0].tolist()
df=pd.read_csv("../data/cities/Lvov_UKR_avg_temp.csv")
xUKR2_values=df.columns.tolist()
yUKR2_values=df.iloc[0].tolist()
df=pd.read_csv("../data/cities/Odesa_UKR_avg_temp.csv")
xUKR3_values=df.columns.tolist()
yUKR3_values=df.iloc[0].tolist()
df=pd.read_csv("../data/cities/Kherson_UKR_avg_temp.csv")
xUKR4_values=df.columns.tolist()
yUKR4_values=df.iloc[0].tolist()


df=pd.read_csv("../data/cities/Paris_FRA_avg_temp.csv")
xFRA1_values=df.columns.tolist()
yFRA1_values=df.iloc[0].tolist()
df=pd.read_csv("../data/cities/Marseille_FRA_avg_temp.csv")
xFRA2_values=df.columns.tolist()
yFRA2_values=df.iloc[0].tolist()

df=pd.read_csv("../data/cities/Uppsala_SWE_avg_temp.csv")
xSWE1_values=df.columns.tolist()
ySWE1_values=df.iloc[0].tolist()
df=pd.read_csv("../data/cities/Stockholm_SWE_avg_temp.csv")
xSWE2_values=df.columns.tolist()
ySWE2_values=df.iloc[0].tolist()

df=pd.read_csv("../data/cities/Tokyo_JAP_avg_temp.csv")
xJAP1_values=df.columns.tolist()
yJAP1_values=df.iloc[0].tolist()
df=pd.read_csv("../data/cities/Tottori_JAP_avg_temp.csv")
xJAP2_values=df.columns.tolist()
yJAP2_values=df.iloc[0].tolist()


df=pd.read_csv("../data/cities/Warsaw_POL_avg_temp.csv")
xPOL1_values=df.columns.tolist()
yPOL1_values=df.iloc[0].tolist()
df=pd.read_csv("../data/cities/Wroclaw_POL_avg_temp.csv")
xPOL2_values=df.columns.tolist()
yPOL2_values=df.iloc[0].tolist()

colors = {
    "BRA": "green",
    "FRA": "purple",
    "JAP": "pink",
    "NEW": "gray",
    "POL": "red",
    "SOU": "orange",
    "SWE": "blue",
    "UKR": "yellow"
}

fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(15, 20))
axes = axes.flatten()

country="NEW"
ax = axes[0]
ax.plot(xNEW1_values, yNEW1_values, color=colors[country], linewidth=1, label="Auckland")
ax.plot(xNEW2_values, yNEW2_values, color=colors[country], linewidth=1, label="Hamilton")
ax.set_title(f'Avg Temp in cities in {country} each year')
ax.set_xlabel('Year')
ax.set_ylabel('Avg Temp Cel')
ax.legend()
ax.grid(True)
ax.set_xticks([x for i, x in enumerate(xNEW1_values) if i % 20 == 0])

country="BRA"
ax = axes[1]
ax.plot(xBRA1_values, yBRA1_values, color=colors[country], linewidth=1, label="Brasilia")
ax.plot(xBRA2_values, yBRA2_values, color=colors[country], linewidth=1, label="Canoas")
ax.set_title(f'Avg Temp in cities in {country} each year')
ax.set_xlabel('Year')
ax.set_ylabel('Avg Temp Cel')
ax.legend()
ax.grid(True)
ax.set_xticks([x for i, x in enumerate(xBRA1_values) if i % 20 == 0])

country="SOU"
ax = axes[2]
ax.plot(xSOU1_values, ySOU1_values, color=colors[country], linewidth=1, label="Johannesburg")
ax.plot(xSOU2_values, ySOU2_values, color=colors[country], linewidth=1, label="Cape Town")
ax.set_title(f'Avg Temp in cities in {country} each year')
ax.set_xlabel('Year')
ax.set_ylabel('Avg Temp Cel')
ax.legend()
ax.grid(True)
ax.set_xticks([x for i, x in enumerate(xSOU1_values) if i % 20 == 0])

country="UKR"
ax = axes[3]
ax.plot(xUKR1_values, yUKR1_values, color=colors[country], linewidth=1, label="Kiev")
ax.plot(xUKR2_values, yUKR2_values, color=colors[country], linewidth=1, label="Lwow")
ax.plot(xUKR3_values, yUKR3_values, color=colors[country], linewidth=1, label="Odessa")
ax.plot(xUKR4_values, yUKR4_values, color=colors[country], linewidth=1, label="Kherson")
ax.set_title(f'Avg Temp in cities in {country} each year')
ax.set_xlabel('Year')
ax.set_ylabel('Avg Temp Cel')
ax.legend()
ax.grid(True)
ax.set_xticks([x for i, x in enumerate(xUKR1_values) if i % 20 == 0])

country="FRA"
ax = axes[4]
ax.plot(xFRA1_values, yFRA1_values, color=colors[country], linewidth=1, label="Paris")
ax.plot(xFRA2_values, yFRA2_values, color=colors[country], linewidth=1, label="Marseille")
ax.set_title(f'Avg Temp in cities in {country} each year')
ax.set_xlabel('Year')
ax.set_ylabel('Avg Temp Cel')
ax.legend()
ax.grid(True)
ax.set_xticks([x for i, x in enumerate(xFRA1_values) if i % 20 == 0])

country="SWE"
ax = axes[5]
ax.plot(xSWE1_values, ySWE1_values, color=colors[country], linewidth=1, label="Uppsala")
ax.plot(xSWE2_values, ySWE2_values, color=colors[country], linewidth=1, label="Stockholm")
ax.set_title(f'Avg Temp in cities in {country} each year')
ax.set_xlabel('Year')
ax.set_ylabel('Avg Temp Cel')
ax.legend()
ax.grid(True)
ax.set_xticks([x for i, x in enumerate(xSWE1_values) if i % 20 == 0])

country="JAP"
ax = axes[6]
ax.plot(xJAP2_values, yJAP2_values, color=colors[country], linewidth=1, label="Tottori")
ax.plot(xJAP1_values, yJAP1_values, color=colors[country], linewidth=1, label="Tokyo")
ax.set_title(f'Avg Temp in cities in {country} each year')
ax.set_xlabel('Year')
ax.set_ylabel('Avg Temp Cel')
ax.legend()
ax.grid(True)
ax.set_xticks([x for i, x in enumerate(xJAP2_values) if i % 20 == 0])

country="POL"
ax = axes[7]
ax.plot(xPOL1_values, yPOL1_values, color=colors[country], linewidth=1, label="Warsaw")
ax.plot(xPOL2_values, yPOL2_values, color=colors[country], linewidth=1, label="Wroclaw")
ax.set_title(f'Avg Temp in cities in {country} each year')
ax.set_xlabel('Year')
ax.set_ylabel('Avg Temp Cel')
ax.legend()
ax.grid(True)
ax.set_xticks([x for i, x in enumerate(xPOL1_values) if i % 20 == 0])

# Ajusting sublots to prevent overlapping
plt.subplots_adjust(hspace=0.5)

# plt.show()
plt.savefig("../plots/lab5/avgTemCitiesSubplots.png")

