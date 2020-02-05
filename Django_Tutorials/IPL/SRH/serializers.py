from .models import SRHTEAM
from rest_framework import serializers

class SRHALL(serializers.ModelSerializer):
    class Meta:
        model=SRHTEAM
        fields=['name']