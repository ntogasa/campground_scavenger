from django.shortcuts import render
from . import models, forms, check


# Create your views here.
def campground_checker_view(request):
    # If POST request, retrieve data from API
    if request.method == 'POST':
        form = forms.CampgroundForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            camp_ids = form.cleaned_data['camp_ids']
            camp_id_list = camp_ids.split()
            results, start_string, end_string = check.master_scraping_routine(camp_id_list, start_date, end_date)
            return render(request, 'results.html', {'start_date': start_string,
                                                    'end_date': end_string,
                                                    'results': results})
        else:
            return 'No success'
    # If GET or other type of request, load empty form
    else:
        form = forms.CampgroundForm()
        return render(request, 'search.html', {'form': form})