from .views import *
from django.urls import path

urlpatterns=[
    path('miallname', MIPLAYERS.as_view()),
]