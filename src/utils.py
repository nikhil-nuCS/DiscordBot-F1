from datetime import datetime, date
import matplotlib.pyplot as plt

import load
from load import DRIVERS, save_figure
import ergast_py


async def is_future(year):
    return datetime.now().year < int(year)


def get_driver_age(yob):
    return datetime.now().year - int(yob)


def get_driver_full_name(driver: ergast_py.Driver):
    return driver.given_name + " " + driver.family_name


def get_formatted_date(from_date: datetime):
    return from_date.date().strftime("%Y-%m-%d") + " " + from_date.time().strftime("%H:%M:%S") + " GMT"


def get_formatted_pit_stop_time(from_date):
    return str(from_date.second) + "." + str(from_date.microsecond)[:4]


def get_formatted_quali_time(from_time):
    if not from_time:
        return "--"
    return str(from_time.minute) + ":" + str(from_time.second) + "." + str(from_time.microsecond)[:4]


def get_lap_timings_plot(season, round_no, drivers):
    api = ergast_py.Ergast()
    fig = plt.figure(figsize=(12, 6))
    for driver in drivers:
        laps = api.season(season).round(round_no).driver(driver).limit(1000).get_laps()[0]
        x_values = []
        y_values = []
        for lap in laps.laps:
            x_values.append(lap.number)
            lt = lap.timings[0].time
            tt = (lt.minute * 60) + lt.second + lt.microsecond / 1000000
            y_values.append(tt)
        plt.plot(x_values, y_values, marker="o", linestyle='--', label=driver)

    plt.title(f"{season} - Round {round_no} - Lap Times")
    plt.xlabel("Lap")
    plt.ylabel("Time (s)")
    # plt.grid(axis='y')
    plt.legend(loc="upper left")
    load.save_figure(fig, name='plot_laps.png')


def find_driver(driver_inp):
    """Find the driver entry and return as a dict.
    Parameters
    ----------
    `id` : str
        Can be either a valid Ergast API ID e.g. 'alonso', 'max_verstappen' or the
        driver code e.g. 'HAM' or the driver number e.g. '44'.
    `drivers` : list[dict]
        The drivers dataset to search.
    Returns
    -------
    `driver` : dict
    Raises
    ------
    `DriverNotFoundError`
    """
    for d in DRIVERS:
        if d.get('driverId', '').lower() == str(driver_inp).lower():
            return d
        elif d.get('code', '').lower() == str(driver_inp).lower():
            return d
        elif d.get('permanentNumber', '') == str(driver_inp):
            return d
        else:
            continue
