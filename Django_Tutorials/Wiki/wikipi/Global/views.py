from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import CountryNames
from django import views
# Create your views here.

class all(views.View):
    def get(self, request):
        if request.GET['method']=="all":
            return HttpResponse("Yes")