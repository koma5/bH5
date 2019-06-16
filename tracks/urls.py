from django.urls import path

from . import views

app_name = 'tracks'
urlpatterns = [
    path('', views.index, name='index'),
    path('track/<int:track_id>', views.detail, name='detail'),
    path('track', views.new_track, name='new_track'),
    path('user/<username>/', views.index_by_user, name='index_by_user'),
]
