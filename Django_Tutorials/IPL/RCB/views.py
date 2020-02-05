from django.shortcuts import render
from .serializers import RCBALL
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse, JsonResponse
from .models import RCBTEAM
# Create your views here.


class RCBPALYESRS(GenericAPIView):
    serializer_class = RCBALL
    queryset = RCBTEAM.objects.all()

    def get(self, request):
        if request.GET['method'] == 'rcballpayers':
            result = RCBTEAM.objects.all()
            company_name = RCBALL(result, many=True)
            return JsonResponse(company_name, safe=False)

        def post(self, request):
            if request.method == "POST":
                return HttpResponse('Yes')