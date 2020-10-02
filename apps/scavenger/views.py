from django.shortcuts import render
from . import models, forms, check


# Create your views here.
def campground_checker_view(request):
    """Handles availability requests and loads the form for users to submit requests."""
    # If POST request, retrieve data from API
    if request.method == 'POST':
        form = forms.CampgroundForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            camp_ids = form.cleaned_data['camp_ids']
            camp_id_list = camp_ids.split()
            try:
                results, start_string, end_string = check.master_scraping_routine(camp_id_list, start_date, end_date)
                return render(request, 'availability_results.html', {'start_date': start_string,
                                                                     'end_date': end_string,
                                                                     'results': results})
            except:
                return render(request, 'no_results_found.html')
        else:
            return 'No success'
    # If GET or other type of request, load empty form
    else:
        form = forms.CampgroundForm()
        return render(request, 'availability.html', {'form': form})