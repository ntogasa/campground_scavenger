from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Set up the router to handle the url paths for our viewset
router = DefaultRouter()
router.register(r'campgrounds', views.CampgroundViewSet, basename='campground')

urlpatterns = [
    path('', include(router.urls)),
]

