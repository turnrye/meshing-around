# helper functions to use location data for data outside US/north america
# K7MHI Kelly Keeton 2024

import json # pip install json
from geopy.geocoders import Nominatim # pip install geopy
import maidenhead as mh # pip install maidenhead
import requests # pip install requests
import bs4 as bs # pip install beautifulsoup4
import xml.dom.minidom 
from modules.log import *

def get_govUK_alerts():
    # get UK weather alerts
    url = 'https://www.gov.uk/alerts'
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, 'html.parser')
    return "not implemented yet"

def get_wxUKgov():
    # get UK weather warnings
    url = 'https://www.metoffice.gov.uk/weather/guides/rss'
    return "not implemented yet"
    
def get_floodUKgov():
    # get UK flood warnings
    url = 'https://environment.data.gov.uk/flood-widgets/rss-feeds.html'
    return "not implemented yet"