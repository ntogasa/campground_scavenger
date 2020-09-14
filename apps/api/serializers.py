from rest_framework import serializers
from ..library.models import Campground


class CampgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campground
        fields = ['camp_id', 'name', 'parent']
        lookup_field = 'camp_id'