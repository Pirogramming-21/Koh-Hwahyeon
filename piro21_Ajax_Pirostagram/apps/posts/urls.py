from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
    path('like_ajax/', like_ajax, name='like_ajax'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('search/', search, name='search'),
    path('comment_ajax/', comment_ajax, name="comment_ajax"),
    path('delete_comment_ajax/', delete_comment_ajax, name="delete_comment_ajax"),
]
