import pandas as pd
import pygal

def main():

    #plot
    df = pd.read_csv("../data/UKR_avg_temp.csv")
    x_val = df.columns.tolist()
    y_val = df.iloc[0].tolist()
    x_val = x_val[-12:]
    y_val = y_val[-12:]

    bar_chart = pygal.Bar()
    bar_chart.x_labels = map(str, x_val)
    bar_chart.y_labels = range(8, 12)
    bar_chart.add('Temperatures in Ukraine', y_val )
    path="../plots/pygal_plt2_UKR.svg"
    bar_chart.render_to_file(path)
    print("path to plot: ",path)

if __name__ == "__main__":
    main()
