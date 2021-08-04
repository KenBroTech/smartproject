from django.db import models
import geocoder
from django.utils import timezone
import datetime

# Create your models here.
REGIONS = (
    ('Ashanti', 'Ashanti'),
    ('Bono', 'Bono'),
    ('Bono East', 'Bono East'),
    ('Ahafo', 'Ahafo'),
    ('Central', 'Central'),
    ('Eastern', 'Eastern'),
    ('Greater Accra', 'Greater Accra'),
    ('Northern', 'Northern'),
    ('Savannah', 'Savannah'),
    ('North East', 'North East'),
    ('Upper East', 'Upper East'),
    ('Upper West', 'Upper West'),
    ('Volta', 'Volta'),
    ('Oti', 'Oti'),
    ('Western', 'Western'),
    ('Western North', 'Western North'),
)


class Smart_Meter_Data(models.Model):
    meter_id = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=20, choices=REGIONS, null=True)
    latitude = models.FloatField(default=0, null=True)
    longitude = models.FloatField(default=0, null=True)

    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.location).lat
        self.longitude = geocoder.osm(self.location).lng
        if self.latitude or self.longitude == None:
            self.location, self.latitude, self.longitude = 'Invalid Location', 0, 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = 'Meter Data'
