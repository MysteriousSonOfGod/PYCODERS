from .models import MITEAM
from rest_framework import serializers

class MIALL(serializers.ModelSerializer):
    class Meta:
        model=MITEAM
        fields=['name']


