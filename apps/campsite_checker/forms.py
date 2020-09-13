from django import forms


class CampgroundForm(forms.Form):
    start_date = forms.CharField(label="Start date (yyyy-mm-dd)", max_length=20)
    end_date = forms.CharField(label="End date (yyyy-mm-dd)", max_length=20)
    camp_ids = forms.CharField(label='Campground ID(s) - separate each ID number with a space',
                               max_length=10000,
                               widget=forms.Textarea(attrs={'rows': 10}))
