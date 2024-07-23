from django.urls import path
from .views import *

app_name='users'

urlpatterns = [
    path('list/', list, name='list'),
    path('create', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
    path('search_user/', search_user, name='search_user'),
]

