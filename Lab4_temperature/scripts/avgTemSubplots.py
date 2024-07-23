import pandas as pd
import matplotlib.pyplot as plt


data_files = {
    "BRA": "../data/BRA_avg_temp.csv",
    "FRA": "../data/FRA_avg_temp.csv",
    "JAP": "../data/JAP_avg_temp.csv",
    "NEW": "../data/NEW_avg_temp.csv",
    "POL": "../data/POL_avg_temp.csv",
    "SOU": "../data/SOU_avg_temp.csv",
    "SWE": "../data/SWE_avg_temp.csv",
    "UKR": "../data/UKR_avg_temp.csv"
}

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

for idx, (country, filepath) in enumerate(data_files.items()):
    df = pd.read_csv(filepath)
    x_values = df.columns.tolist()
    y_values = df.iloc[0].tolist()
    ax = axes[idx]
    ax.plot(x_values, y_values, color=colors[country], linewidth=1, label=country)
    ax.set_title(f'Avg Temp in {country} each year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Avg Temp Cel')
    ax.legend()
    ax.grid(True)
    ax.set_xticks([x for i, x in enumerate(x_values) if i % 20 == 0])

# Ajusting sublots to prevent overlapping
plt.subplots_adjust(hspace=0.5)

# plt.show()
plt.savefig("../plots/lab5/avgTemSubplots.png")

