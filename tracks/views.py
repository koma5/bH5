from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Track
from .models import Segment
from .models import Point
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods

import gpxpy
import gpxpy.gpx

def index(request):

    context = {
	'tracks': Track.objects.order_by('-id')[:50],
        'point_count': Track.objects.count(),
        'track_count': Point.objects.count(),
    }

    return render(request, 'tracks/index.html', context)

@require_http_methods(["POST"])
def new_track(request):

    if not request.user.is_authenticated:
        raise PermissionDenied


    parsed_gpx = gpxpy.parse(request.POST['raw_gpx'])

    for track in parsed_gpx.tracks:

        new_track = Track(name=track.name, owner=request.user)
        new_track.save()

        for segment in track.segments:

            new_segment = Segment(track=new_track)
            new_segment.save()

            for point in segment.points:
                new_point = Point()
                new_point.latitude = point.latitude
                new_point.longitude = point.longitude
                new_point.date = point.time
                new_point.segment = new_segment
                new_point.save()


    return HttpResponse('got you, ' + request.user.username)

def detail(request, track_id):

    track =  get_object_or_404(Track, id=track_id)

    context = { 'track': track, 'segments': [] }

    segments = Segment.objects.filter(track=track)

    for segment in segments:
        context['segments'].append({
            'segment': segment,
            'points': Point.objects.filter(segment=segment).order_by('date')
        })

    return render(request, 'tracks/detail.html', context)

def index_by_user(request, username):

    context = {
            'tracks': get_list_or_404(Track.objects.filter(owner__username=username).order_by('-id')[:5]),
    }

    return render(request, 'tracks/index.html', context)
