from django.urls import path
from . import views

urlpatterns = [
    path('', views.campground_checker_view, name='search'),
]