from django import views
from django.http import HttpResponse, JsonResponse
from .models import Dreamreal
from .serializers import AllDreamrealSerializers, CnameSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class all(views.View):
    def get(self, request):
        if request.GET['method']=="all":
            k = []
            j = Dreamreal.objects.all()
            for each in j:
                a = {"id":each.id, "website": each.website, "mail": each.mail, "name": each.name,"phonenumber":each.phonenumber}
                k.append(a)
            return JsonResponse({"data": k})


    def post(self, request):
        if request.method == "POST":
            return HttpResponse("yes")


class AllDisplay(GenericAPIView):
    serializer_class = AllDreamrealSerializers
    queryset = Dreamreal.objects.all()
    def get(self, request):
        j=Dreamreal.objects.all()
        all_data=AllDreamrealSerializers(j, many=True)
        return JsonResponse(all_data.data, safe=False)


class Cname(GenericAPIView):
    serializer_class = CnameSerializers
    queryset = Dreamreal.objects.all()
    def get(self, request):
        if request.GET.get("filter", None)=="category":
            d=[]
            result=Dreamreal.objects.all()
            company_name=CnameSerializers(result, many=True)
            y = request.GET.get("names", None).split(',')
            if y is not None:
                for each in y:
                    for key in company_name.data:
                        if each in key['name']:
                            d.append(key)

            return JsonResponse(d, safe=False)