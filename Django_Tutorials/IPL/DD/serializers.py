from rest_framework import serializers
from .models import DDTEAM

class DDALL(serializers.ModelSerializer):
    class Meta:
        model=DDTEAM
        fielda=['name']
