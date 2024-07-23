from bokeh.plotting import figure, show, output_file,save
import pandas as pd
import sys


def main():
    if len(sys.argv) > 2:
        print("Usage: python script.py <argument>")
        print("0 - show plot")
        print("1 - save plot")
        sys.exit(1)
    if len(sys.argv) < 2:
        argument = '0'
    if len(sys.argv) == 2:
        argument = sys.argv[1]
    if argument != '1' and argument != '0':
        argument = '0'

    df = pd.read_csv("../data/BRA_avg_temp.csv")
    x_val = df.columns.tolist()
    y_val = df.iloc[0].tolist()

    p = figure(title="Temperatures in Brasil", x_axis_label="Year", y_axis_label="Temperature in Celsius", )
    p.line(x_val, y_val, legend_label="Temperature", line_width=2, line_color="green")
    p.legend.location = "top_left"

    if argument=="0":
        show(p)

    if argument=="1":
        path="../plots/bokeh_plt1_BRA.html"
        output_file(path)
        save(p)
        print("path to plot: ",path)

if __name__ == "__main__":
    main()

