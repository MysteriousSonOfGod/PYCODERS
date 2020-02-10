from django.shortcuts import render
from .models import RRTEAM
from rest_framework.generics import GenericAPIView
from .serializers import RRALL
from django.http import HttpResponse, JsonResponse
# Create your views here.


class RRPLAYERS(GenericAPIView):
    serializer_class = RRALL
    queryset = RRTEAM.objects.all()

    def get(self, request):
    # if request.GET['method']=='rrallplayers':
        result = RRTEAM.objects.all()
        company_name = RRALL(result, many=True)
        return JsonResponse(company_name.data, safe=False)

        def post(self, request):
            if request.method == "POST":
                return HttpResponse('Yes')