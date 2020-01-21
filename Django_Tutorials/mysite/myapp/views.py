from django import views
from django.http import HttpResponse, JsonResponse
from .models import Dreamreal


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
