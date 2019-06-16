from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404

from .models import Track
from .models import Point

def index(request):

    context = {
	'tracks': Track.objects.order_by('-id')[:50],
        'point_count': Track.objects.count(),
        'track_count': Point.objects.count(),
    }

    return render(request, 'tracks/index.html', context)


def detail(request, track_id):

    track =  get_object_or_404(Track, id=track_id)

    context = {
        'track':  track,
        'points': Point.objects.filter(track=track).order_by('-id')[:50],
    }

    return render(request, 'tracks/detail.html', context)

def index_by_user(request, username):

    context = {
            'tracks': get_list_or_404(Track.objects.filter(owner__username=username).order_by('-id')[:5]),
    }

    return render(request, 'tracks/index.html', context)
