"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', include('apps.campsite_checker.urls')),
    path('about/', views.about_view, name='about'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('apps.api.urls')),
    path('api-gate/', views.api_gateway_view, name='api_gateway'),
    path('campgrounds/', include('apps.campgrounds.urls')),
    path('celery-progress/', include('celery_progress.urls')),
    path('contact/', include('apps.contact.urls')),
]
