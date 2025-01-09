from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'release_date', 'price', 'stock', 'cover_image']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
