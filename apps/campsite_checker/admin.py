from django.contrib import admin
from .models import Campground, Zone


# Register your models here.
class CampgroundAdmin(admin.ModelAdmin):
    list_display = ['name', 'camp_id', 'zone']
    ordering = ['zone', 'camp_id']


class ZoneAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


admin.site.register(Campground, CampgroundAdmin)
admin.site.register(Zone, ZoneAdmin)
