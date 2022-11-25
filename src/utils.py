from datetime import datetime, date

import ergast_py


async def is_future(year):
    return datetime.now().year < int(year)


def get_driver_age(yob):
    return datetime.now().year - int(yob)


def get_driver_full_name(driver: ergast_py.Driver):
    return driver.given_name + " " + driver.family_name