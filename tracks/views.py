from django.shortcuts import render, get_list_or_404
from django.http import Http404
from django.template import loader

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

    try:
        track =  Track.objects.get(id=track_id)
    except Track.DoesNotExist:
        raise Http404('Track does not exist.')

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
