from django.urls import path
from .views import *

urlpatterns=[
    path('', reviews_list),
    path('create/', reviews_create),
    path('<int:pk>/', reviews_detail),
    path('<int:pk>/update/', reviews_update),
    path('<int:pk>/delete/', reviews_delete),
]