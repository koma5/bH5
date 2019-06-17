from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Track
from .models import Segment
from .models import Point
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods

from django.contrib.gis.geos import Point as gisPoint

from django.db import transaction

import gpxpy
import gpxpy.gpx

def index(request):

    tracks = Track.objects.all()

    if not request.user.is_authenticated:
        tracks = Track.objects.filter(public=True)

    context = {
	'tracks': tracks.order_by('-id')[:50],
    }

    return render(request, 'tracks/index.html', context)

@transaction.atomic
@login_required(login_url='/admin')
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
                new_point.point = gisPoint(point.longitude, point.latitude)
                new_point.date = point.time
                new_point.segment = new_segment
                new_point.save()


    return HttpResponse('got you, ' + request.user.username)

def detail(request, track_id):

    tracks = Track.objects.all()

    if not request.user.is_authenticated:
        tracks = Track.objects.filter(public=True)

    track =  get_object_or_404(tracks, id=track_id)

    context = { 'track': track, 'segments': [] }

    segments = Segment.objects.filter(track=track)

    for segment in segments:
        context['segments'].append({
            'segment': segment,
            'points': Point.objects.filter(segment=segment).order_by('date')
        })

    return render(request, 'tracks/detail.html', context)

def get_gpx(request, track_id):

    tracks = Track.objects.all()

    if not request.user.is_authenticated:
        tracks = Track.objects.filter(public=True)

    track =  get_object_or_404(tracks, id=track_id)

    gpx = gpxpy.gpx.GPX()
    gpx_track = gpxpy.gpx.GPXTrack(name=track.name)
    gpx.tracks.append(gpx_track)

    segments = Segment.objects.filter(track=track)

    for segment in segments:

        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        points = Point.objects.filter(segment=segment).order_by('date')

        for point in points:
            gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(
                point.latitude,
                point.longitude,
                elevation=point.altitude,
                time=point.date
            ))

        gpx_track.segments.append(gpx_segment)

    return HttpResponse(gpx.to_xml(), content_type="application/gpx+xml")
    #return HttpResponse(gpx.to_xml(), content_type="text/plain")


def index_by_user(request, username):

    tracks = Track.objects.all()

    if not request.user.is_authenticated:
        tracks = Track.objects.filter(public=True)

    context = {
            'tracks': get_list_or_404(tracks.filter(owner__username=username).order_by('-id')[:5]),
    }

    return render(request, 'tracks/index.html', context)
