from django import forms
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


class IDSearchForm(forms.Form):
    """Form that takes in campground ID range to check and scrape."""
    start_id = forms.CharField(label='Start ID', max_length=10)
    end_id = forms.CharField(label='End ID', max_length=10)
