from django.urls import path
from .views import *

urlpatterns=[
    path("ddallname/",DDPALYERS.as_view()),
]