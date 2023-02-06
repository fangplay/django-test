from django.shortcuts import render
from array import *
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def main(request):
    # k = array('I',[22,55,34,84,33,12,7])
    k = [22,55,34,33,84,12,7]
    m = 0 
    spot = 0
    # l = len(k)
    for index in range(len(k)):
        if k[index] > m:
            m = k[index]
            spot = index
    return JsonResponse(spot, safe=False)