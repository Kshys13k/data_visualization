import pandas as pd
import pygal

def main():

    #plot
    df = pd.read_csv("../data/SOU_avg_temp.csv")
    df2 = pd.read_csv("../data/SWE_avg_temp.csv")
    x_val = df2.columns.tolist()
    y_sou_val = df.iloc[0].tolist()
    y_swe_val = df2.iloc[0].tolist()
    x_val = x_val[-146:]
    y_sou_val=y_sou_val[-146:]
    y_swe_val=y_swe_val[-146:]

    line_chart = pygal.Line()
    line_chart.title = 'Comparison of temperatures in Sweden and South Africa'
    line_chart.x_labels = map(str, x_val)
    line_chart.add('SOU', y_sou_val )
    line_chart.add('SWE', y_swe_val)

    path="../plots/pygal_plt1_SWE_SOU.svg"
    line_chart.render_to_file(path)
    print("path to plot: ",path)

if __name__ == "__main__":
    main()
