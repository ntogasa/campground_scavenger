from django import forms
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


class CampgroundForm(forms.Form):
    """Allows users to search for campground availability"""
    day1 = (dt.now() + relativedelta(days=14)).strftime('%Y-%m-%d')
    day2 = (dt.now() + relativedelta(days=16)).strftime('%Y-%m-%d')
    start_date = forms.CharField(label="Start date (yyyy-mm-dd)",
                                 max_length=20,
                                 widget=forms.TextInput(attrs={'placeholder': day1}))
    end_date = forms.CharField(label="End date (yyyy-mm-dd)",
                               max_length=20,
                               widget=forms.TextInput(attrs={'placeholder': day2}))
    camp_ids = forms.CharField(label='Campground ID(s) - separate each ID number with a space',
                               max_length=10000,
                               widget=forms.Textarea(attrs={'rows': 10, 'placeholder': '232305 232123 233807'}))
