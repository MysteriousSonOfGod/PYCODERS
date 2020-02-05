from rest_framework import serializers
from .models import CSKTEAM

class CSKALL(serializers.ModelSerializer):
    class Meta:
        model=CSKTEAM
        fields=['name']