from django.contrib import admin
from .models import Campground


# Register your models here.
class CampgroundAdmin(admin.ModelAdmin):
    list_display = ['camp_id', 'name', 'parent']
    ordering = ['parent', 'camp_id']


admin.site.register(Campground, CampgroundAdmin)
