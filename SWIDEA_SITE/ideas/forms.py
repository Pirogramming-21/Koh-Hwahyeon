from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta():
        model=Idea
        fields=('__all__')

class SortForm(forms.Form):
    SORT_CHOICES = [
        ('등록순', '등록순'),
        ('최신순', '최신순'),
        ('이름순', '이름순'),
        ('찜하기순', '찜하기순'),
    ]
    sort_by = forms.ChoiceField(
        label='정렬',
        choices=[('','--정렬기준--')] + SORT_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'sort-input',
                'id': 'sort-options'
            }
        )
    )