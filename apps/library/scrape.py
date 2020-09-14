import requests
import json
from lxml.html import fromstring
from fake_useragent import UserAgent
from itertools import cycle
from time import sleep
from random import random

BASE_URL = "https://www.recreation.gov"
CAMP_STRING = "/api/search?fq=id%3A"
# CAMP_STRING = "/api/camps/campgrounds/"
END_STRING = "_asset"


def scrape_camp_info(camp_id):
    url = f"{BASE_URL}{CAMP_STRING}{camp_id}{END_STRING}"
    # Wait between 0 to 1 seconds
    sleep(random())
    # Scraping routine
    try:
        resp = requests.get(url=url,
                            headers={"User-Agent": UserAgent().random},)
        response = resp.json()
        name = response['results'][0]['name']
        parent_name = response['results'][0]['parent_name']
        data = {
            "camp_id": str(camp_id),
            "name": name,
            "parent": parent_name
        }
    except:
        return False
    return data
