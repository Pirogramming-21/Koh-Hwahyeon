from django import forms
from .models import Review

class GenreForm(forms.ModelForm):
    class Meta:
        model=Review
        fields = [
            'title',
            'image',
            'year',
            'genre',
            'star',
            'time',
            'newreview',
            'director',
            'actor'
        ]