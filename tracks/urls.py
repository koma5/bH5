from django.urls import path

from . import views

app_name = 'tracks'
urlpatterns = [
    path('', views.index, name='index'),
    path('track/<track_id>.gpx', views.get_gpx, name='get_gpx'),
    path('track/<track_id>.json', views.get_geojson, name='get_geojson'),
    path('track/<track_id>.svg', views.get_svg, name='get_svg'),
    path('track/<track_id>', views.detail, name='detail'),
    path('track', views.new_track, name='new_track'),
    path('user/<username>/', views.index_by_user, name='index_by_user'),
]
