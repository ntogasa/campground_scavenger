# &#x26FA; Campground Checker
Campsite Checker is a Django application that scrapes campground
availabilities from recreation.gov, and also saves campground ID 
numbers. 	

## Why Use This?
Reserving campgrounds on reservation.gov is not a very 
efficient process, because checking campground availabilities
requires visiting each campground's website individually.

#### Mass Search Campground Availability
This application allows you to mass-search availabilities for
many campgrounds at the click of a button. 

For instance, if you want to find an available campground in
Yosemite National Park, rather than visiting each campground's
webpage you can use Campground Checker to search them all at once. 

#### API - Access Campground IDs, Names, Parents
Included is an API with public read access. Each campground
in the database includes a campground name, ID number, and parent zone name.

For example: 
{'camp_id': '232123', 'name': 'Whitney Portal', 'parent': 'Inyo National Forest'}

## Usage
STEP 1 - Visit the 'Campgrounds' page, and type in the name of a parent zone

STEP 2 - Copy and paste the campground ID results

STEP 3 - Go to the 'Availability' page, paste your campground IDs, enter your 
reservation dates, and hit submit!

## Contributing
Pull requests are welcome. For major changes, please
open an issue first to discuss what you would like 
to change. 

## Acknowledgements
The campsite availability checker in this app is an adaptation of the work of 
https://github.com/banool/recreation-gov-campsite-checker, which in turn is 
an adaptation of https://github.com/bri-bri/yosemite-camping 's application. 
I couldn't have done it without them!