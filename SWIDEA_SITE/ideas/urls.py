from django.urls import path
from .views import *

app_name='ideas'

urlpatterns=[
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('detail/<int:pk>', detail, name='detail'),
    path('delete/<int:pk>', delete, name='delete'),
    path('update/<int:pk>', update, name='update'),
    path('toggle_star/<int:idea_id>/', toggle_star, name='toggle_star'),
    path('update_interest/<int:idea_id>/<str:action>/', update_interest, name='update_interest'),
]
