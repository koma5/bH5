from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels
from django.template.defaultfilters import pluralize
import uuid

class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    def display_name(self):
        if self.name:
            return self.name
        else:
            return self.id

    def segment_count(self):
        return self.segments.count()

    def point_count(self):
        return sum([segment.point_count() for segment in self.segments.all()])

    def __str__(self):
        return "Track({} | {} point{})".format(self.name if self.name else self.id, self.point_count(), pluralize(self.point_count()))

class Segment(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='segments')

    def point_count(self):
        return self.points.count()

    def __str__(self):
        return 'Segment({} | {} point{})'.format(self.id, self.point_count(), pluralize(self.point_count()))


class Point(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='points')
    latitude = models.DecimalField(max_digits=23, decimal_places=17)
    longitude = models.DecimalField(max_digits=23, decimal_places=17)
    point = geomodels.PointField()
    altitude = models.FloatField(null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return 'Point({}|{}|{})'.format(self.id, self.latitude, self.longitude)

