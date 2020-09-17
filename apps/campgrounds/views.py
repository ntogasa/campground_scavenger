from django.shortcuts import render
from . import forms
from .models import Campground
from . import tasks


# Create your views here.
def list_view(request):
    campgrounds = Campground.objects.all()
    return render(request, 'campgrounds.html')


def scrape_view(request):
    if request.method == 'POST':
        form = forms.IDSearchForm(request.POST)
        if form.is_valid():
            start_id = form.cleaned_data['start_id']
            end_id = form.cleaned_data['end_id']
            task = tasks.scraping_routine.delay(start_id, end_id)
        return render(request, 'scrape_results.html', {"task_id": task.task_id})
    else:
        form = forms.IDSearchForm()
        return render(request, 'scrape_ids.html', {'form': form})
