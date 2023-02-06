from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def main(request):
    n = int(input("Enter a number: "))
    d = {}
    l = 1
    fac = 1

    if n < 0: #Check if the number is negative
        return JsonResponse('Sorry that number is exits!')
    elif n == 0: #Check if the number is zero
        fac = 1
        z = 0
        return JsonResponse(z, safe=False)
    else:
        for i in range(1,n + 1):
            fac = fac*i
        k = str(fac)
        q = len(k)
        
        for l in q:
            if k[l] not in d and k[l] == "0":
                d[0] += 1
            d[0] += 0          
        return JsonResponse(d, safe=False)