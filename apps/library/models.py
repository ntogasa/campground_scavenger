from django.db import models


# Create your models here.
class Campground(models.Model):
    camp_id = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Zone(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
