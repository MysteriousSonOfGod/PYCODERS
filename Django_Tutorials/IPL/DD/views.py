from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import DDTEAM
from .serializers import DDALL
from rest_framework.generics import GenericAPIView
# Create your views here.


class DDPALYERS(GenericAPIView):
    serializer_class = DDALL
    queryset = DDTEAM.objects.all()

    def get(self, request):
        if request.GET['method']=='cskallpayers':
            result = DDTEAM.objects.all()
            company_name = DDALL(result, many=True)
            return JsonResponse(company_name, safe=False)

    def post(self, request):
        if request.method == "POST":
            return HttpResponse("yes")