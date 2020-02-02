from rest_framework import serializers
from .models import Dreamreal


class AllDreamrealSerializers(serializers.ModelSerializer):
    class Meta:
        model=Dreamreal
        fields=['website','mail','name','phonenumber']

class CnameSerializers(serializers.ModelSerializer):
    class Meta:
        model=Dreamreal
        fields=['name','phonenumber']