from datetime import datetime
from lib.svi import SVIModel, SVIPlot


def parse_date(dt_str):
    return datetime.strptime(dt_str, "%d%b%y")


def plot(df):
    # prepare data
    today = datetime.now().strptime("2024-10-10", "%Y-%m-%d")
    df2 = df.rename(columns={"mark_iv": "IV", "underlying_price": "F"}).copy()
    df2["Strike"] = df2.apply(lambda x: float(x["instrument_name"].split("-")[-2]), axis=1)

    df2["Date"] = df2.apply(lambda x: parse_date(x["instrument_name"].split("-")[-3]), axis=1)
    df2["Tau"] = df2.apply(lambda x: (x["Date"] - today).days / 365.25, axis=1)

    # get model ready
    m = SVIModel(df2)
    m.fit()

    # plot
    plt = SVIPlot()
    fig = plt.allsmiles(m)
    return fig
