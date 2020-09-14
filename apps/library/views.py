from django.shortcuts import render
from . import models


# Create your views here.
def list_view(request):
    campgrounds = models.Campground.objects.all()
    return render(request, 'list.html', {'campgrounds': campgrounds})
