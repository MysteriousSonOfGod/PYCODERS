from django.shortcuts import render

# Create your views here.
from django import views
from django.http import HttpResponse, JsonResponse
from .models import CSKTEAM
from .serializers import CSKALL
from rest_framework.generics import GenericAPIView


class CSKPALYERS(GenericAPIView):
    serializer_class = CSKALL
    queryset = CSKTEAM.objects.all()

    def get(self, request):
        if request.GET['method']=='cskallpayers':
            result = CSKTEAM.objects.all()
            company_name = CSKALL(result, many=True)
            return JsonResponse(company_name, safe=False)

    def post(self, request):
        if request.method == "POST":
            return HttpResponse("yes")
