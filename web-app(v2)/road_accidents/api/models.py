from django.db import models

# Create your models here.

class Accident(models.Model):
    accident_index = models.CharField(max_length=20, unique=True)
    location_easting = models.FloatField(null=True, blank=True)
    # location_northing = models.FloatField(null=True, blank=True)
    location_northing = models.CharField(max_length=20)
    # longitude = models.FloatField(null=True, blank=True)
    longitude = models.CharField(max_length=20)
    # latitude = models.FloatField(null=True, blank=True)
    latitude = models.CharField(max_length=20)
    # accident_severity = models.IntegerField()
    accident_severity = models.CharField(max_length=5)
    # number_of_vehicles = models.IntegerField()
    number_of_vehicles = models.CharField(max_length=5)
    # number_of_casualties = models.IntegerField()
    number_of_casualties = models.CharField(max_length=5)
    # date = models.DateField()
    date = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.accident_index} - Severity: {self.accident_severity}"