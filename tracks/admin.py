from django.contrib import admin


from .models import Point, Segment, Track

class SegmentInLine(admin.StackedInline):
    model = Segment
    extra = 0

class TrackAdmin(admin.ModelAdmin):
    inlines = [SegmentInLine]


admin.site.register(Point)
admin.site.register(Segment)
admin.site.register(Track, TrackAdmin)

