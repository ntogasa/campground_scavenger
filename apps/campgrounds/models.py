from django.db import models


# Create your models here.
class Campground(models.Model):
    camp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    parent = models.CharField(max_length=10000)

    def __str__(self):
        return self.name