from bs4 import BeautifulSoup
import helper
from datetime import datetime
import click
import time
import calendar

#Example values
#START_DATE = datetime(2014, 05, 15)
#END_DATE = datetime(2015, 05, 15)
#DAY_DELTA = 7
#TIMEOUT_SECONDS = 30

#Example Command
#python Scraper.py 2014/05/25 2015/05/15 4 0 YYZ POS

@click.command()
@click.argument('start_date')
@click.argument('end_date')
@click.argument('day_delta')
@click.argument('time_out')
@click.argument('origin_airport')
@click.argument('destination_airport')
def find_flights(start_date, end_date, day_delta, time_out, origin_airport, destination_airport):

    start_date = datetime.strptime(start_date, "%Y/%m/%d")
    end_date = datetime.strptime(end_date, "%Y/%m/%d")
    day_delta = int(day_delta)
    time_out = int(time_out)

    flight_dates = helper.generate_dates(start_date, end_date, day_delta)

    #There is a new output file for each run.
    #Use something like time.ctime(int("1284101485")) to get back date
    filename = calendar.timegm(datetime.utcnow().utctimetuple())

    file = open('DataOut/output_'+str(filename)+'.txt', "a")

    for flight_date in flight_dates:
        (depart_date, return_date) = flight_date
        response = helper.hit_the_site(depart_date,
                                       return_date,
                                       origin_airport,
                                       destination_airport)
        soup = BeautifulSoup(response)
        data = helper.parse_data(soup)
        if len(data) == 0:
            file.writelines('No data received might have encounter captcha')
            file.close()
            break
        for a in data:
            print a
            file.writelines(a.encode('utf-8'))
        # Trying to avoid captcha here but looks like timeout is over 30 seconds
        # I can go 10 hit then its turned on
        time.sleep(time_out)
    file.close()

if __name__ == '__main__':
    find_flights()