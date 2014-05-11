from datetime import datetime
from datetime import timedelta

def generate_dates():
    start = datetime(2014, 05, 15)
    end = datetime(2015, 05, 15)
    delta = timedelta(days=7)
    while start < end:
        depart_date = start.date().strftime("%d/%m/%Y")
        return_date = (start + delta).date().strftime("%d/%m/%Y")
        print depart_date, return_date
        start += delta


generate_dates()