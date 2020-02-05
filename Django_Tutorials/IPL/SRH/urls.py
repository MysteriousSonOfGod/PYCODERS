from .views import *
from django.urls import path

urlpatterns=[
    path('srhallname', SRHPALYERS.as_view()),
]