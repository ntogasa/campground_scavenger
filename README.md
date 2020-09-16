# &#x26FA; Campground Checker
Campsite Checker is a web application that scrapes campground
availabilities from recreation.gov, and also saves campground ID 
numbers. 	

## Purposes/Functions
Reserving campgrounds on recreation.gov is not a very 
efficient process, as checking campground availabilities
requires visiting each campground's website individually. Campground
Checker resolves this inefficiency via mas search capabilities. It
also provides an API.

#### Mass Search Campground Availability
This application allows you to mass-search availabilities for
many campgrounds at the click of a button. 

For instance, if you want to find an available campsite in
Yosemite National Park, rather than visiting each individual campground's
webpage you can use Campground Checker to search them all at once. 

#### API - Access Campground IDs, Names, Parents
Included is an API with public read access. Each campground
object includes a campground name, ID number, and parent zone name.

Example campground object: 
{'camp_id': '232123', 'name': 'Whitney Portal', 'parent': 'Inyo National Forest'}

#### Campground ID Scraper
Authenticated users can scrape the recreation.gov API to discover and save
campground ID numbers, names, and parent zone names. These objects are then
displayed via a Vue JS app, which the public can use to mass search 
availability.

## Usage
##### Suggested flow:
STEP 1 - Visit the 'Campgrounds' page, and type in the name of a parent zone

STEP 2 - Copy the campground ID results to your clipboard

STEP 3 - Go to the 'Availability' page, paste your campground IDs, enter your 
reservation dates, and hit submit!

##### Alternate flow:
STEP 1 - Assemble your own list of campground IDs by combining results 
from different zones

STEP 2 - copy, paste, and submit

## Built Using
- [Django](https://www.djangoproject.com/) (open source Python web framework)
- [Django REST Framework](https://www.django-rest-framework.org/) for the API
- [Vue JS](https://www.vuejs.org/) for interactive campground ID list display
- [HTML5](https://www.w3schools.com/html/)
- [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) (CSS Framework) with some custom CSS
- [Whitenoise](http://whitenoise.evans.io/en/stable/) to handle static files

## Contributing
Pull requests are welcome. For major changes, please
open an issue first to discuss what you would like 
to change. 

## Acknowledgements
The campsite availability checker in this app is an adaptation of the work of 
https://github.com/banool/recreation-gov-campsite-checker, which in turn is 
an adaptation of https://github.com/bri-bri/yosemite-camping 's application. 