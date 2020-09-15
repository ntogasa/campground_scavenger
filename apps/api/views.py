from rest_framework import viewsets, permissions
from ..library.models import Campground, Log
from .serializers import CampgroundSerializer, LogSerializer


class CampgroundViewSet(viewsets.ModelViewSet):
    queryset = Campground.objects.all()
    serializer_class = CampgroundSerializer
    lookup_field = 'camp_id'


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    # Only authenticated users can access Log data through API
    permission_classes = [permissions.IsAuthenticated]
