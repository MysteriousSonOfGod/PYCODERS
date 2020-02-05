from .models import RRTEAM
from rest_framework import serializers

class RRALL(serializers.ModelSerializer):
    class Meta:
        model=RRTEAM
        fields=['name']
