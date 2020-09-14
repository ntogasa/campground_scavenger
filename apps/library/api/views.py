from rest_framework import viewsets
from ..models import Campground
from .serializers import CampgroundSerializer


class CampgroundViewSet(viewsets.ModelViewSet):
    queryset = Campground.objects.all()
    serializer_class = CampgroundSerializer
    lookup_field = 'camp_id'



