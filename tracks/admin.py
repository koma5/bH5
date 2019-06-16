from django.contrib import admin


from .models import Point, Segment, Track

admin.site.register(Point)
admin.site.register(Segment)
admin.site.register(Track)
