from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.

def roman_chart(number):

    if (1 <= number <= 100):
        rem = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
      
        while number:
            div = number // rem[i]
            number %= rem[i]
    
            while div:
                # print(sym[i], end = "")
                div -= 1
                return JsonResponse(sym[i], safe=False)
            i -= 1
    else:
        k = "Sorry your number not in range"
        return JsonResponse(k, safe=False)
    # roman_m ={
    #     1: "I",
    #     4: "IV",
    #     5: "V",
    #     9: "IX",
    #     10: "X",
    #     40: "XL",
    #     50: "L",
    #     90: "XC",
    #     100: "C",
    #     400: "CD",
    #     500: "D",
    #     900: "CM",
    #     1000: "M",
    # }

    # result = ""
    # remain = number
 

    # for i in sorted(roman_m.keys(),reserve = False):
    #     if remain > 0:
    #         multiplier  = i
    #         roman_digit = roman_m[i]

    #         times = remain // multiplier      # 3
    #         remain = remain % multiplier      # 4
    #         result += roman_digit * times     # 4
    # return result


# input number to convert

def main(request):
    number = int(input('Please input number: '))
    roman_chart(number)
    # print(roman_chart(number))