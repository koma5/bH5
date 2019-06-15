from django.db import models
from django.contrib.auth.models import User

class Track(models.Model):
    name = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField('date_published', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False, blank=True)

    def __str__(self):
        if self.name is '':
            return "Track(" + str(self.id) + ')'
        else:
            return "Track(" + self.name + ')'

class Point(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return "Point(" + str(self.id) + ')'

