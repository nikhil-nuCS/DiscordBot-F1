from datetime import datetime, date

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
