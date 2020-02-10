from django.shortcuts import render
from .models import *
from .serializers import KKRALL
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse, JsonResponse
from django import views
# Create your views here.


class KKRPALYERS(GenericAPIView):
    serializer_class = KKRALL
    queryset = KKRTEAM.objects.all()

    def get(self, request):
    # if request.GET['method'] == 'kkrallpayers':
        result = KKRTEAM.objects.all()
        company_name = KKRALL(result, many=True)
        return JsonResponse(company_name.data, safe=False)

    def post(self, request):
        if request.method == "POST":
            return HttpResponse('Yes')