from rest_framework import serializers
from ..campgrounds.models import Campground, Log


class CampgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campground
        fields = ['camp_id', 'name', 'parent']
        lookup_field = 'camp_id'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['pk', 'date', 'start_id', 'end_id', 'count']
        lookup_field = 'log'
