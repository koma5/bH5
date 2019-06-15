from django.shortcuts import render
from django.http import HttpResponse

from .models import Track
from .models import Point

def index(request):
    track_count = Track.objects.count()
    point_count = Point.objects.count()
    return HttpResponse("bH5 is tracking you. There {1} currently {0} point{2} in the database.".format(point_count, 'is' if point_count == 1 else 'are', '' if point_count == 1 else 's'))

