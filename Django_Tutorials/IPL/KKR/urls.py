from .views import *
from django.urls import path

urlpatterns=[
    path('kkrallname',KKRPALYERS.as_view()),
]