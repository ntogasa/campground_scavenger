from rest_framework import viewsets, permissions
from ..campgrounds.models import Campground
from .serializers import CampgroundSerializer


class CampgroundViewSet(viewsets.ModelViewSet):
    """Viewset to handle CRUD operations on campground objects."""
    queryset = Campground.objects.all()
    serializer_class = CampgroundSerializer
    lookup_field = 'camp_id'

