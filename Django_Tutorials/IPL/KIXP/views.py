from django.shortcuts import render
from .models import *
from .serializers import KIXPALL
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse, JsonResponse
# Create your views here.

class KIXPPALYERS(GenericAPIView):
    serializer_class = KIXPALL
    queryset = KIXPTEAM.objects.all()

    def get(self, request):
    # if request.GET['method'] == 'cskallpayers':
        result = KIXPTEAM.objects.all()
        company_name = KIXPALL(result, many=True)
        return JsonResponse(company_name.data, safe=False)

    def post(self, request):
        if request.method == "POST":
            return HttpResponse("yes")