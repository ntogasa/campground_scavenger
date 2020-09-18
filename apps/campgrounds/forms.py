from django import forms
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


class IDSearchForm(forms.Form):
    start_id = forms.CharField(label='Start ID', max_length=10)
    end_id = forms.CharField(label='End ID', max_length=10)
