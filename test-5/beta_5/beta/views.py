from django.shortcuts import render

from django.http import JsonResponse

# Create your views here.
# def thai_chart(number):
#     if not (1 <= number <= 10000000):
#         k = "Sorry your number not in range"
#         print(k)

#     thai_m = {
#                 1:' ',        
#                 2:'ก',
#                 3:'ข',
#                 4:'ฃ',
#                 5:'ค',
#                 6:'ฅ',
#                 7:'ฆ',
#                 8:'ง',
#                 9:'จ',
#                 10:'ฉ',
#                 11:'ช',
#                 12:'ซ',
#                 13:'ฌ',
#                 14:'ญ',
#                 15:'ฎ',
#                 16:'ฏ',
#                 17:'ฐ',
#                 18:'ฑ',
#                 19:'ฒ',
#                 20:'ณ',
#                 21:'ด',
#                 22:'ต',
#                 23:'ถ',
#                 24:'ท',
#                 25:'ธ',
#                 26:'น',
#                 27:'บ',
#                 28:'ป',
#                 29:'ผ',
#                 30:'ฝ',
#                 31:'พ',
#                 32:'ฟ',
#                 33:'ภ',
#                 34:'ม',
#                 35:'ย',
#                 36:'ร',
#                 37:'ฤ',
#                 38:'ล',
#                 39:'ฦ',
#                 40:'ว',
#                 41:'ศ',
#                 42:'ษ',
#                 43:'ส',
#                 44:'ห',
#                 45:'ฬ',
#                 46:'อ',
#                 47:'ฮ',
#                 48:'ฯ',
#                 49:'ะ',
#                 50:'ั',
#                 51:'า',
#                 52:'ำ',
#                 53:'ิ',
#                 54:'ี',
#                 55:'ึ',
#                 56:'ื',
#                 57:'ุ',
#                 58:'ู',
#                 59:'ฺ',
#                 60:'฿',
#                 61:'เ',
#                 62:'แ',
#                 63:'โ',
#                 64:'ใ',
#                 65:'ไ',
#                 66:'ๅ',
#                 67:'ๆ',
#                 68:'็',
#                 69 :'่',
#                 70 :'้',
#                 71 :'๊',
#                 72 :'๋',
#                 73 :'์',
#                 74 :'ํ',
#                 75 :'๎',
#                 76 :'๏',
#             }
#     result = ""
#     remain = number

#     for i in sorted(thai_m.keys(),reserve = True):
#         if remain > 0:
#             multiplier = i
#             thai_digit = thai_m[i]

#             times = remain // multiplier
#             remain = remain % multiplier
#             result += thai_digit * times
#     return result

# # input number to convert

# def main(request):
#     number = int(input('Please input number: '))
#     # JsonResponse(roman_chart(number), safe=False)
#     print(thai_chart(number))

def main(request):
    number = int(input('Please input number: '))
    ch = chr(number)
    JsonResponse(ch, safe=False)