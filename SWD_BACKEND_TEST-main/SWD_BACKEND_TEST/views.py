
from django.http import JsonResponse

def roman_chart(number):
    roman_m ={
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    result = ""
    remain = number

    for i in sorted(roman_m.keys(),reserve = True):
        if remain > 0:
            multiplier  = i
            roman_digit = roman_m[i]

            times = remain // multiplier      # 3
            remain = remain % multiplier      # 4
            result += roman_digit * times     # 4

    return result


# input number to convert

def convert(request):
    number = int(input('Please input number: '))
    JsonResponse(roman_chart(number))