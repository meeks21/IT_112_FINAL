from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    artistname=models.CharField(max_length=255)
    artistdescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.artistname

    class Meta:
        db_table='songname'

class SongName(models.Model):
    songname=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    songartist=models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.songname

    class Meta:
        db_table='artist'

class Review(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    song=models.ForeignKey(SongName, on_delete=models.CASCADE)
 

    def __str__(self):
        return self.title

    class Meta:
        db_table='review'
