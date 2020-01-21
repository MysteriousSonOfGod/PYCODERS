from django import views
from django.http import HttpResponse, JsonResponse
from .models import Dreamreal


class all(views.View):
    def get(self, request):
        if request.GET['method']=="all":
            k = []
            j = Dreamreal.objects.all()
            for each in j:
                a = {"website": each.website}
                k.append(a)
            return HttpResponse({"data": k})


    def post(self, request):
        if request.method == "POST":
            return HttpResponse("yes")
