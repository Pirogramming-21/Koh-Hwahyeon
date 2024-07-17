from django.urls import path
from .views import *

app_name='devTools'

urlpatterns=[
    path('list/', list, name='list'), 
    path('create/', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('update/<int:pk>/', update, name='update'),
]