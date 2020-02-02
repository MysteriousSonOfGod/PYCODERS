from django.urls import path
from .views import *

urlpatterns = [
    path("", all.as_view()),
    path("alldis/", AllDisplay.as_view()),
    path("company/", Cname.as_view()),
]
