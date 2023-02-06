# main/serializers.py
from rest_framework import serializers
from .models import Number

class NumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Number
        fields = ('number')