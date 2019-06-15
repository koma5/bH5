from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Track
from .models import Point

def index(request):

    context = {
	'tracks': Track.objects.order_by('-id')[:50],
        'point_count': Track.objects.count(),
        'track_count': Point.objects.count(),
    }

    template = loader.get_template('tracks/index.html')

    return HttpResponse(template.render(context, request))


def detail(request, track_id):

    track =  Track.objects.get(id=track_id)

    context = {
        'track':  track,
        #'points2': mytrack.points,
        'points': Point.objects.filter(track=track).order_by('-id')[:50],
    }

    return HttpResponse(render(request, 'tracks/detail.html', context))

def index_by_user(request, username):

    context = {
        'tracks': Track.objects.filter(owner__username=username).order_by('-id')[:50],
    }

    return HttpResponse(render(request, 'tracks/index.html', context))
