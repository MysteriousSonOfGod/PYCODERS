from django.shortcuts import render
from .serializers import SRHALL
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import GenericAPIView
from .models import SRHTEAM
# Create your views here.


class SRHPALYERS(GenericAPIView):
    serializer_class = SRHALL
    queryset = SRHTEAM
    def get(self, request):
    # if request.GET['method'] == 'rrallplayers':
        result = SRHTEAM.objects.all()
        company_name = SRHALL(result, many=True)
        return JsonResponse(company_name.data, safe=False)

    def post(self, request):
        if request.method == "POST":
            return HttpResponse('Yes')
