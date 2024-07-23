import plotly.express as px
import pandas as pd
import plotly.express as px
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

    fig = px.line(x=x_val, y=y_val)

    fig.update_layout(
        title="Temperatures in Japan",
        xaxis_title="Year",
        yaxis_title="Temp [Celc]"

    )

    if argument=="0":
        fig.show()

    if argument=="1":
        path="../plots/plotly_plt1_JAP.html"
        fig.write_html(path, auto_open=False)
        print("path to plot: ",path)

if __name__ == "__main__":
    main()
