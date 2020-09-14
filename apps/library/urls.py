from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('api/', include('apps.library.api.urls')),
    path('campgrounds/', views.list_view, name='list')
]
