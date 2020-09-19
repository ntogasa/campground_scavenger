import requests
import os
import json
from lxml.html import fromstring
from fake_useragent import UserAgent
from itertools import cycle
from time import sleep
from random import random
from .models import Campground
from celery import shared_task
from celery.result import AsyncResult
from celery_progress.backend import ProgressRecorder


# Define parameter strings
BASE_URL = "https://www.recreation.gov"
CAMP_STRING = "/api/search?fq=id%3A"
END_STRING = "_asset"


@shared_task(bind=True)
def scraping_routine(self, start_id, end_id):
    # Instantiate progress recorder to show users
    progress_recorder = ProgressRecorder(self)
    # Prepare variables
    start_id = int(start_id)
    end_id = int(end_id) + 1
    job_count = end_id - start_id
    DATA = []
    i = 1
    for camp_id in range(start_id, end_id):
        data = AsyncResult(scrape_camp_info.delay(camp_id))
        DATA.append(data)
        progress_recorder.set_progress(i, job_count, description=f"{i} out of {job_count} potential campground IDs checked")
        i += 1
    count = len(DATA)
    return {"count":count, "data": DATA}


@shared_task()
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
        save_function(camp_id, data)
    except:
        return False
    return data


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
