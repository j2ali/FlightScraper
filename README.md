FlightScraper
=========

FlightScraper is a python app that scrapes and parses flight information from multiple sources

  - Built in python
  - Easy API
  - Documentation and other batteries included


Installation
--------------
Assuming you have virtualenv set up on your machine, simply clone this repository and do:

```sh
pip install -r requirements.txt
```

Usage
--------------
If you know your travel dates and destination, run the following:

```sh
python Scraper.py end_date start_date range timeout start_dest end_dest
```

Where 
  - end_date - your end date in "%Y/%m/%d" format
  - start_date - your start date in "%Y/%m/%d" format
  - range - your timedelta day range
  - timeout - your timeout (in seconds). Differs based on url
  - start_dest - airport symbol of your start point
  - end_dest - airport symbol of your end point



License
----

See custom license


**Free Software, Hell Yeah!**
