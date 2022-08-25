# where the user can create albums
from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'artist', 'release_date')

class EditAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'artist', 'release_date')