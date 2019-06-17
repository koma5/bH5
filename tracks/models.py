from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels

class Track(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    def __str__(self):
        return "Track({})".format(self.name if self.name else self.id)

class Segment(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self):
        return 'Segment({})'.format(self.id)


class Point(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return 'Point({})'.format(self.id)

