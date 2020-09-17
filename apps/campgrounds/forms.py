from django import forms
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from .models import Log


class IDSearchForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['start_id', 'end_id']
        labels = {'start_id': 'Start ID',
                  'end_id': 'End ID'}
