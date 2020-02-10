from django.shortcuts import render
from django.template import loader
# Create your views here.
from django import views
from django.http import HttpResponse, JsonResponse
from .models import CSKTEAM
from .serializers import CSKALL
from rest_framework.generics import GenericAPIView
import json
from django.shortcuts import render
from .form import EmpForm


class CSKPALYERS(GenericAPIView):
    serializer_class = CSKALL
    queryset = CSKTEAM.objects.all()

    def get(self, request, method=None):
    # if request.GET['method']=="cskallplayerslist":
        result = CSKTEAM.objects.all()
        company_name = CSKALL(result, many=True)
        return JsonResponse(company_name.data, safe=False)

    def post(self, request):
        if request.method == "POST":
            return HttpResponse("yes")


# def index(request):
#    template = loader.get_template('index.html') # getting our template
#    data=CSKTEAM.objects.all()
#    for i in data:
#        d={'tname':i.name}
#    return HttpResponse(template.render(d))





# def index(request):
#     stu = EmpForm()
#     return render(request, "index.html", {'form': stu})