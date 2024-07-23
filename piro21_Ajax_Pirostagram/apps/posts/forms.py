from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('__all__')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class SortForm(forms.Form):
    SORT_CHOICES = [
        ('등록순', '등록순'),
        ('최신순', '최신순'),
        ('이름순', '이름순'),
    ]
    sort_by = forms.ChoiceField(
        label='정렬',
        choices=[('','--정렬기준--')] + SORT_CHOICES,
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'sort-input',
                'id': 'sort-options'
            }
        )
    )