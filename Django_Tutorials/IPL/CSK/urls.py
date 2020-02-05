from django.urls import path
from .views import *

urlpatterns=[
    path("cskallnames/",CSKPALYERS.as_view()),
]