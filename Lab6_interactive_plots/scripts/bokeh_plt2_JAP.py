from bokeh.plotting import figure, show, output_file,save
from bokeh.palettes import Category20
from bokeh.models import ColumnDataSource
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


    #plot
    df = pd.read_csv("../data/JAP_avg_temp.csv")
    x_val = df.columns.tolist()
    y_val = df.iloc[0].tolist()
    x_val = x_val[-14:]
    y_val = y_val[-14:]

    color = Category20[20][:14]

    source = ColumnDataSource(data=dict(year=x_val, temperature=y_val, color=color))

    p = figure(x_range=x_val, y_range=(min(y_val) - 0.5, max(y_val) + 0.5), height=350,
               title="Temperatures in Japan in years 2000-2013",
               toolbar_location=None, tools="")

    p.vbar(x='year', top='temperature', width=0.9, color='color', source=source)

    p.xgrid.grid_line_color = None


    if argument=="0":
        show(p)

    if argument=="1":
        path="../plots/bokeh_plt2_JAP.html"
        output_file(path)
        save(p)
        print("path to plot: ",path)

if __name__ == "__main__":
    main()

