from django.shortcuts import render
from . import forms, scrape
from .models import Campground, Log


# Create your views here.
def list_view(request):
    campgrounds = Campground.objects.all()
    return render(request, 'campgrounds.html')


def scrape_view(request):
    if request.method == 'POST':
        form = forms.IDSearchForm(request.POST)
        DATA = []
        if form.is_valid():
            start_id = form.cleaned_data['start_id']
            end_id = form.cleaned_data['end_id']
            for camp_id in range(int(start_id), int(end_id)):
                data = scrape.scrape_camp_info(camp_id)
                if data:
                    # If campground already exists in database, update
                    if Campground.objects.filter(camp_id=str(camp_id)).exists():
                        # Save to campground model
                        campground = Campground.objects.filter(camp_id=str(camp_id))
                        campground.camp_id = data['camp_id']
                        campground.name = data['name']
                        campground.parent = data['parent']
                        DATA.append(data)
                    # If campground does not exist yet, save new object
                    else:
                        campground = Campground(camp_id=data['camp_id'],
                                                name=data['name'],
                                                parent=data['parent'])
                        campground.save()
                        DATA.append(data)
            count = len(DATA)
            # Save to Log model
            log = form.save(commit=False)
            log.count = count
            log.save()
        LOG = Log.objects.all()
        return render(request, 'scrape_results.html', {"start_id": start_id,
                                                       "end_id": end_id,
                                                       "logs": LOG,
                                                       "data": DATA,
                                                       "count": count})
    else:
        form = forms.IDSearchForm()
        return render(request, 'scrape_ids.html', {'form': form})
