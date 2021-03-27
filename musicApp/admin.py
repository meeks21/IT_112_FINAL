from django.contrib import admin
from . models import Artist, SongName, Review
# Register your models here.

admin.site.register(Artist)
admin.site.register(SongName)
admin.site.register(Review)