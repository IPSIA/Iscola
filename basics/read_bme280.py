#!/usr/bin/python

# Read the BME280 sensor from the Weather Click board
# Requirements:
# sudo apt-get python i2c-tools, python-smbus
# sudo pip install bme280

# -*- coding: utf-8 -*-
import re
import sys,time

from bme280.bme280 import bme_read
from datetime import datetime


if __name__ == '__main__':
    while True:
        data = bme_read() 
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        to_write = "%s %7.2f KPa %07.2f %% %07.2f C\n" % (now,data.pressure,data.humidity, data.temperature)
	print to_write
        f = open('data.log',"a")
        f.write(to_write)
        f.close()
        time.sleep(1)
    # sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    # sys.exit(main())
