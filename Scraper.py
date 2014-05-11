from bs4 import BeautifulSoup
import helper
from datetime import datetime
import time

START_DATE = datetime(2014, 05, 15)
END_DATE = datetime(2015, 05, 15)
DAY_DELTA = 7


flight_dates = helper.generate_dates(START_DATE, END_DATE, DAY_DELTA)

flight_groups = []

file = open('output.txt', "a")

for flight_date in flight_dates:
    response = helper.hit_the_site(flight_date)
    soup = BeautifulSoup(response)
    data = helper.parse_data(soup)
    for a in data:
        print a
        file.writelines(a.encode('utf-8'))
    # Trying to avoid captcha here but looks like timeout is over 30 seconds
    # I can go 10 hit then its turned on
    time.sleep(10)
    flight_groups.append(data)

file.close()

for flight_group in flight_groups:
    print flight_group


