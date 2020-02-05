from django.shortcuts import render
from .serializers import MIALL
from rest_framework.generics import GenericAPIView
from .models import MITEAM
# Create your views here.
from django.http import HttpResponse, JsonResponse

class MIPLAYERS(GenericAPIView):
    serializer_class = MIALL
    queryset = MITEAM.objects.all()

    def get(self, request):
        if request.GET['method']=='miallpayers':
            result=MITEAM.objects.all()
            company_name = MIALL(result, many=True)
            return JsonResponse(company_name, safe=False)

        def post(self, request):
            if request.method == "POST":
                return HttpResponse('Yes')