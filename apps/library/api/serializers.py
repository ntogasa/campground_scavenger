from rest_framework import serializers
from ..models import Campground


class CampgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campground
        fields = ['camp_id', 'name', 'parent_name']
        lookup_field = 'camp_id'

