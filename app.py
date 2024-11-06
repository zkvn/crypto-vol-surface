"""
TODO
2. Save plot
3. Automate
"""

from lib.data_deribit import get_option_data
from lib.plot import plot
from datetime import datetime
import pandas as pd
from loguru import logger
import click
import glob
import os


def get_data():
    # print data and time for log
    # print("Date and time: " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " , format: dd/mm/yyyy hh:mm:ss")
    logger.info("Downloading bitcoin options data from Deribit")
    # download data -- BTC
    btc_data = get_option_data("BTC")

    logger.info("Saving getting data")
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    btc_data.to_pickle(f"./data/{dt}.pickle")
    logger.info(f"Result saved to data folder as {dt}.pickle")
    return btc_data


def generate_plot(df):
    logger.info("Generating plots in your browser")
    fig = plot(df)
    logger.info("Saving plot to output folder")
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    # BUG: https://github.com/plotly/Kaleido/issues/78
    fig.write_image(f"output/{dt}.pdf")


def find_last_pickle():

    list_of_files = glob.glob("./data/*.pickle")  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


@click.command()
@click.option("--download", is_flag=True, default=False, help="To download bitcoin options data from Deribit")
def main(download):
    if download is True:
        get_data()

    file_name = find_last_pickle()
    logger.info(f"Loading latest data from ./data/{file_name} folder")
    df1 = pd.read_pickle(file_name)
    generate_plot(df1)


if __name__ == "__main__":
    main()
