from .views import *
from django.urls import path

urlpatterns=[
    path('rcballname', RCBPALYESRS.as_view()),
]