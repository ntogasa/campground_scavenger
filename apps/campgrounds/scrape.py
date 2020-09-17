import requests
import json
from lxml.html import fromstring
from fake_useragent import UserAgent
from itertools import cycle
from time import sleep
from random import random
from .models import Campground, Log

BASE_URL = "https://www.recreation.gov"
CAMP_STRING = "/api/search?fq=id%3A"
# CAMP_STRING = "/api/camps/campgrounds/"
END_STRING = "_asset"


@shared_task
def scraping_routine(start_id, end_id)
    for camp_id in range(int(start_id), int(end_id)):
        data = scrape_camp_info(camp_id)
        # If data for a campground is found, then save/update
        if data:
            save_function(camp_id, data)
            return start_id, end_id, data
    data = None
    return start_id, end_id, data


@shared_task
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


@shared_task
def save_function(camp_id, data):
    # If campground already exists in database, update
    if Campground.objects.filter(camp_id=str(camp_id)).exists():
        # Save to campground model
        campground = Campground.objects.filter(camp_id=str(camp_id))
        campground.camp_id = data['camp_id']
        campground.name = data['name']
        campground.parent = data['parent']
    # If campground does not exist yet, save new object
    else:
        campground = Campground(camp_id=data['camp_id'],
                                name=data['name'],
                                parent=data['parent'])
        campground.save()
    return data