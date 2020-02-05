from .views import *
from django.urls import path

urlpatterns=[
    path('kixpall',KIXPPALYERS.as_view()),
]