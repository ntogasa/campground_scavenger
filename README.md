# Campsite Checker
Campsite Checker is a Django application that scrapes campground
availabilities from recreation.gov, and also saves campground ID 
numbers.

## Why use this?
Reserving campgrounds on reservation.gov is not a very 
efficient process, because checking campground availabilities
requires visiting each campground's website individually.

This application allows you to mass-search availabilities for
many campgrounds at the click of a button. 

For instance, if you want to find an available campground in
Yosemite National Park, rather than visiting each campground's
webpage you can use Campground Checker to search them all at once. 

## Usage
To perform a scrape, you need to provide three parameters:
1) your desired reservation start-date
2) your desired reservation end-date
3) the ID number of your target campground(s)


## Contributing
Pull requests are welcome. For major changes, please
open an issue first to discuss what you would like 
to change. 

## Acknowledgements
The campsite availability checker in this app is an adaptation of the work of 
https://github.com/banool/recreation-gov-campsite-checker, which in turn is 
an adaptation of https://github.com/bri-bri/yosemite-camping 's application. 
I couldn't have done it without them!