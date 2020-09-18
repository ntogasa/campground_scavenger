import requests
from fake_useragent import UserAgent
from datetime import datetime, timedelta
from dateutil import rrule
from itertools import count, groupby

# URL strings
BASE_URL = "https://www.recreation.gov"
AVAILABILITY_ENDPOINT = "/api/camps/availability/campground/"
MAIN_PAGE_ENDPOINT = "/api/camps/campgrounds/"

# Date variables
INPUT_DATE_FORMAT = "%Y-%m-%d"
ISO_DATE_FORMAT_REQUEST = "%Y-%m-%dT00:00:00.000Z"
ISO_DATE_FORMAT_RESPONSE = "%Y-%m-%dT00:00:00Z"

# Generates a random User-Agent to prevent getting blacklisted
headers = {"User-Agent": UserAgent().random}

def get_name_of_site(camp_id):
    """Sends a request to retrieve the name of the campground, given its ID number
    :param camp_id: the campground's ID number
    :type camp_id: str
    :return name: the name of the campground
    :rtype name: str
    """
    url = "{}{}{}".format(BASE_URL, MAIN_PAGE_ENDPOINT, camp_id)
    resp = send_request(url, {})
    name = resp["campground"]["facility_name"]
    return name


def get_num_available_sites(campground_information, start_date, end_date, nights=None):
    """Gets the number of available campsites at a campground.
    :param campground_information: All of the API data for a given campground
    :type campground_information: dict
    :param start_date: the start date of the reservation period
    :type start_date: datetime
    :param end_date: the end date of the reservation period
    :type end_date: datetime
    :param nights: None
    :type nights: None
    :return num_available: The number of available campsites
    :rtype num_available: int
    :return maximum: The total number of sites at the campground
    :rtype maximum: int
    """
    maximum = len(campground_information)
    num_available = 0
    num_days = (end_date - start_date).days
    dates = [end_date - timedelta(days=i) for i in range(1, num_days + 1)]
    dates = set(format_date(i, format_string=ISO_DATE_FORMAT_RESPONSE) for i in dates)
    if nights not in range(1, num_days + 1):
        nights = num_days
    for site, availabilities in campground_information.items():
        # List of dates that are in the desired range for this site.
        desired_available = []
        for date in availabilities:
            if date not in dates:
                continue
            desired_available.append(date)
        if desired_available and consecutive_nights(desired_available, nights):
            num_available += 1
    return num_available, maximum


def consecutive_nights(available, nights):
    """
    Returns whether there are `nights` worth of consecutive nights.
    """
    ordinal_dates = [datetime.strptime(dstr, ISO_DATE_FORMAT_RESPONSE).toordinal() for dstr in available]
    c = count()
    longest_consecutive = max((list(g) for _, g in groupby(ordinal_dates, lambda x: x-next(c))), key=len)
    return len(longest_consecutive) >= nights


def format_date(date_object, format_string=ISO_DATE_FORMAT_REQUEST):
    """This function doesn't manipulate the date itself at all, it just
    formats the date in the format that the API wants.
    :param date_object: the datetime object to be formatted
    :type date_object: datetime
    :param format_string: the string that specifies the desired output format
    :type format_string: str
    :return date_formatted: The formatted datetime object
    :rtype date_formatted: datetime
    """
    date_formatted = datetime.strftime(date_object, format_string)
    return date_formatted


def send_request(url, params):
    """Sends the GET request to the API and handles failed requests.
    :param url: the target url
    :type url: str
    :param params: the associated parameters with the request
    :type params: dict
    :return response: a json object
    :rtype response: json
    """
    try:
        resp = requests.get(url, params=params, headers=headers)
        response = resp.json()
        return response
    except:
        return False


def scrape_campground_availability(camp_id, start_date, end_date, campsite_type=None):
    """Scrapes an API response for the availability of permits, given a specific permit ID and
    start_date.
    :param camp_id: the 6 digit permit id number
    :type camp_id: str
    :param start_date: the start date of the reservation period in YYYY-mm-dd format
    :type start_date: datetime
    :param end_date: the end date of the reservation period in YYYY-mm-dd format
    :type end_date: datetime
    :param campsite_type: None
    :type campsite_type: str
    :return data: campsite availability data
    :rtype data: dict
    """
    # Get first day of month of start date
    start_of_month = datetime(start_date.year, start_date.month, 1)
    # Get a list of all months between start and end dates
    months = list(rrule.rrule(rrule.MONTHLY, dtstart=start_of_month, until=end_date))
    # Iterate through relevant months
    api_data = []
    for month in months:
        params = {"start_date": format_date(month)}
        url = f"{BASE_URL}{AVAILABILITY_ENDPOINT}{camp_id}/month?"
        resp = send_request(url, params)
        if resp:
            api_data.append(resp)
    # Collapse the data into the described output format.
    # Filter by campsite_type if necessary.
    data = {}
    for month_data in api_data:
        for campsite_id, campsite_data in month_data["campsites"].items():
            available = []
            for date, availability_value in campsite_data["availabilities"].items():
                if availability_value != "Available":
                    continue
                if campsite_type and campsite_type != campsite_data["campsite_type"]:
                    continue
                available.append(date)
            if available:
                a = data.setdefault(campsite_id, [])
                a += available
    return data


def master_scraping_routine(campgrounds, start_date, end_date, campsite_type=None):
    """Retrieves the availability of the given campgrounds for the given time periods,
    as specified by the given start_date and end_date.
    :param campgrounds: campground ID numbers seperated by spaces
    :type campgrounds: str
    :param start_date: start date in YYYY-mm-dd format
    :type start_date: str
    :param end_date: end date in YYYY-mm-dd format
    :type end_date: str
    :return results_list: a list of all availabilities and urls for each campsite
    :rtype results_list: list
    """
    # Format input dates as datetime objects
    start_date = datetime.strptime(start_date, INPUT_DATE_FORMAT)
    end_date = datetime.strptime(end_date, INPUT_DATE_FORMAT)
    start_string = start_date.strftime('%a %b %d, %Y')
    end_string = end_date.strftime('%a %b %d, %Y')
    results_list = []
    for camp_id in campgrounds:
        try:
            campground_information = scrape_campground_availability(
                camp_id, start_date, end_date, campsite_type
            )
            name_of_site = get_name_of_site(camp_id)
            current, maximum = get_num_available_sites(
                campground_information, start_date, end_date
            )
            if current:
                # emoji = SUCCESS_EMOJI
                success = True
                availabilities = True
            else:
                # emoji = FAILURE_EMOJI
                success = False
                availabilities = False
            availability = f"{name_of_site} {camp_id} : {current} site(s) available out of {maximum} site(s)"
            rec_url = f"{BASE_URL}/camping/campgrounds/{camp_id}"
            result = {
                'success': success,
                'availability': availability,
                'url': rec_url,
            }
            results_list.append(result)
        except KeyError:
            pass
    return results_list, start_string, end_string
