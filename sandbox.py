from datetime import datetime
import requests
import json
import pandas as pd
from fake_useragent import UserAgent

my_start_date = '2020-10-10'
my_end_date = '2020-10-12'
my_camp_id = '232871'

start_date = datetime.strptime(my_start_date, '%Y-%m-%d')
print(start_date.date())