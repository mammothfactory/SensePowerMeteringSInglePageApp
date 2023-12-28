#!/usr/bin/env python3
"""
__authors__    = ["Blaze Sanders"]
__contact__    = "blazes@mfc.us"
__copyright__  = "Copyright 2023"
__license__    = "MIT License"
__status__     = "Development
__deprecated__ = False
__version__    = "0.1.0"
__doc__        = "CONSTANTS for both LiteHouse and Lustron home configurations"
"""

# SQLite Database CONSTANTS
INSTANT_ENERGY_COLUMN_NUMBER = 1
COST_COLUMN_NUMBER = 2
TIMESTAMP_COLUMN_NUMBER =3
TOTAL_ENERGY_COLUMN_NUMBER = 1
WATT_HOUR_COLUMN_NUMBER = 1
WEEK_NUMBER_COLUMN_NUMBER = 2
MONTH_NUMBER_COLUMN_NUMBER = 2
LOG_MESSAGE_COLUMN_NUMBER = 1

# Default file location for code
MAC_CODE_DIRECTORY   = '/Users/venus/GitRepos/SensePowerMeteringSinglePageApp'
LINUX_CODE_DIRECTORY = '/SensePowerMeteringSinglePageApp'
WINDOWS_CODE_DIRECTORY = 'C:/Users/???/SensePowerMeteringSinglePageApp'


# GUI Display CONSTANTS
DEBUG_STATEMENTS_ON = True
RUN_ON_NATIVE_OS = False
LOCAL_HOST_PORT_FOR_GUI = 8282
DOLLAR_STORE_LOGO_BLUE = '#001B36'
DOLLAR_STORE_LOGO_GRREN = '#8EE511'

# Input Number Box CONSTANTS
VALID_EMPLOYEE_ID_LENGTH = 4

# NiceGUI ui.timer() CONSTANTS
UI_UPDATE_TIME = 0.5
ONE_SECOND = 1
ONE_HOUR = ONE_SECOND * 60 * 60
CLOCK_UPDATE_TIME = 60 * ONE_SECOND
LABEL_UPDATE_TIME = 4 * ONE_SECOND
DATABASE_DAILY_REPORT_UPDATE_TIME  = 12 * ONE_HOUR
DATABASE_WEEKLY_REPORT_UPDATE_TIME =  4 * ONE_HOUR

# DateTime Object CONSTANTS
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

# NiceGUI ui.button() CONSTANTS
CLOCK_IN = 0
CLOCK_OUT = 1
CLOCK_IN_MISSED  = -99
CLOCK_OUT_MISSED = -88
