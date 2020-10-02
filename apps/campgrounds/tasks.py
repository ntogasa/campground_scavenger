import requests
from fake_useragent import UserAgent
from time import sleep
from random import random
from .models import Campground
from celery import shared_task
from celery_progress.backend import ProgressRecorder


# Define parameter strings
BASE_URL = "https://www.recreation.gov"
CAMP_STRING = "/api/search?fq=id%3A"
END_STRING = "_asset"


@shared_task(bind=True)
def scraping_routine(self, start_id, end_id):
    """Iterates through a given range of numbers and checks the recreation.gov API to see if there
    are any matching campground ID numbers. If a campground ID has already been saved, then it is
    updated. If not then a new campground object is created.
    :param start_id:    lower bound of the search range
    :type start_id:     str
    :param end_id:      high bound of the search range
    :type end_id:       str
    """
    # Instantiate progress recorder to show users
    progress_recorder = ProgressRecorder(self)
    # Check what is already saved in database
    status_quo = Campground.objects.values_list('camp_id', flat=True)
    # Prepare variables
    start_id = int(start_id)
    end_id = int(end_id) + 1
    job_count = end_id - start_id
    DATA = []
    i = 1
    for camp_id in range(start_id, end_id):
        data = scrape_camp_info(camp_id, status_quo)
        DATA.append(data)
        progress_recorder.set_progress(i, job_count, description=f"{i} out of {job_count} potential campground IDs checked")
        i += 1
    count = len(DATA)
    return {"count":count, "data": DATA}


def scrape_camp_info(camp_id, status_quo):
    """Checks recreation.gov to see if a campground ID number has any associated data, and either
    updates an existing campground in the database or creates a new campground object.
    :param camp_id:     the target number to check/scrape
    :type camp_id:      int
    :param status_quo:  the currently 'known' campground IDs
    :type status_quo:   list
    """
    url = f"{BASE_URL}{CAMP_STRING}{camp_id}{END_STRING}"
    # Wait between 0 to 1 seconds
    sleep(random())
    # Scraping routine
    # try:
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
    store_data(camp_id, data, status_quo)
    # except:
    #     return False
    return data


def store_data(camp_id, data, status_quo):
    """Checks if a campground object already exists or not"""
    if camp_id in status_quo:
        update(camp_id, data)
    # If campground does not exist yet, save new object
    else:
        save(data)


def update(camp_id, data):
    """Updates the attributes of an existing campground object"""
    campground = Campground.objects.filter(camp_id=str(camp_id))
    campground.camp_id = data['camp_id']
    campground.name = data['name']
    campground.parent = data['parent']


def save(data):
    """Creates and saves a new campground object"""
    campground = Campground(camp_id=data['camp_id'],
                            name=data['name'],
                            parent=data['parent'])
    campground.save()