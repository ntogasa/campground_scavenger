from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from . import views


urlpatterns = [
    path('', views.list_view, name='campgrounds'),
    path('find_camp_ids/', views.scrape_view, name='scrape_ids'),
]
