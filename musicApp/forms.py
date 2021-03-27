from django import forms
from .models import Artist, SongName, Review


class ArtistForm(forms.ModelForm):
    class Meta:
        model=Artist
        fields='__all__'

class SongForm(forms.ModelForm):
    class Meta:
        model=SongName
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'