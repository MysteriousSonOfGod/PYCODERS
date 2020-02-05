from .models import *
from rest_framework import serializers


class KKRALL(serializers.ModelSerializer):
    class Meta:
        model=KKRTEAM
        fields=['name']