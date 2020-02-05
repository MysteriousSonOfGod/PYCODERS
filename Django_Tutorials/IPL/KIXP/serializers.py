from rest_framework import serializers
from .models import KIXPTEAM

class KIXPALL(serializers.ModelSerializer):
    class Meta:
        model=KIXPTEAM
        fields=['name']