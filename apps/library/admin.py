from django.contrib import admin
from .models import Campground, Log


# Register your models here.
class CampgroundAdmin(admin.ModelAdmin):
    list_display = ['camp_id', 'name', 'parent']
    ordering = ['parent', 'camp_id']


# Register your models here.
class LogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'date', 'start_id', 'end_id', 'count']
    ordering = ['date',]


admin.site.register(Campground, CampgroundAdmin)
admin.site.register(Log, LogAdmin)
