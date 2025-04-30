from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'cover', 'audio_file']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 rounded bg-gray-100 text-black',
                'placeholder': 'Song Title'
            }),
            'artist': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 rounded bg-gray-100 text-black',
                'placeholder': 'Artist Name'
            }),
            'cover': forms.ClearableFileInput(attrs={
                'class': 'w-full text-black'
            }),
            'audio_file': forms.ClearableFileInput(attrs={
                'class': 'w-full text-black'
            }),
        }
