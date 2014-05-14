from datetime import timedelta
import mechanize
import locator


def generate_dates(start, end, day_delta):
    delta = timedelta(days=day_delta)
    flight_dates = []
    while start < end:
        depart_date = start.date().strftime("%d/%m/%Y")
        return_date = (start + delta).date().strftime("%d/%m/%Y")
        start += delta
        flight_dates.append((depart_date, return_date))
    if len(flight_dates) == 0:
        print('No flight dates where generated! Check your start/end dates!!')
    return flight_dates


def parse_data(html_response):
    flights = html_response.select(locator.FLIGHT_ROW)
    data = []
    for flight in flights:
        location = flight.select(locator.FLIGHT_LOCATION)[0].get_text().replace("\n", "")
        date = flight.select(locator.FLIGHT_DATE)[0].get_text().replace("\n", "")
        time = flight.select(locator.FLIGHT_TIME)[0].get_text().replace("\n", "")
        cheapest_price = flight.select(locator.FLIGHT_PRICE)
        if len(cheapest_price) > 0:
            cheapest_price = cheapest_price[0].get_text().replace("\n", "") + '\n'
        else:
            cheapest_price = 'DID NOT FIND A PRICE' + '\n'
        row = location + '|' + date + '|' + time + '|' + cheapest_price
        data.append(row)
    return data


def hit_the_site(departure_date, return_date, origin_airport, destination_airport):
    browser = mechanize.Browser()
    #Dont respect Robots.txt
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) '
                                         'Gecko/20100101 Firefox/29.0')]
    url = get_url(departure_date, return_date, origin_airport, destination_airport)
    print 'Hitting URL %s' % url
    response = browser.open(url).read()
    browser.clear_history()
    browser.close()
    return response

def get_url(departure_date, return_date, origin_airport, destination_airport):
    url = 'https://caribbean.sita.aero/itd/itd/DoAirSearch'\
                            '?_originSelected=Airport.' + origin_airport +\
                            '&_destinationSelected=Airport.' + destination_airport +\
                            '&_tripType=Return'\
                            '&_depdateeu=' + departure_date +\
                            '&_retdateeu=' + return_date +\
                            '&_classType=Economy'\
                            '&requestor=AirSimpleReqsPage'\
                            '&_channelLocale=en'\
                            '&_children=0'\
                            '&_adults=1'\
                            '&_infants=0'
    return url