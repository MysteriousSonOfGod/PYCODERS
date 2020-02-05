from .models import RCBTEAM
from rest_framework import serializers

class RCBALL(serializers.ModelSerializer):
    class Meta:
        model=RCBTEAM
        fields=['name']