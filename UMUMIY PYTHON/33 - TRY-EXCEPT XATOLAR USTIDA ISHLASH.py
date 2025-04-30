# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:48:23 2025

@author: DavrServis
"""

# 33 - DARS.
# TRY-EXCEPT XATOLAR USTIDA ISHLASH.
yosh = input("Yoshingizni kiriting: ")
yosh = int(yosh)
print(f"Siz {2025-yosh}-yilda tug'ilgansiz!")
# Yoshingizni kiriting: 26
#Natija: Siz 1999-yilda tug'ilgansiz.

# Yoshingizni kiriting: 25.5
# ValueError: invalid literal for int() with base 10: '25.5'

# Endi shu holatlarni oldini olishni ko'rib chiqamiz. Buning uchun try-except funksiyasidan
# foydalanamiz: 
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)    
    print(f"Siz {2025 - yosh}-yilda tug'ilgansiz.")
except:
    print("Siz butun son kiritmadingiz!")    
# Yoshingizni kiriting: 26.5
# Natija: Siz butun son kiritmadingiz!

# Yoshingizni kiriting: 26
# Natija: Siz 1999-yilda tug'ilgansiz.

# Agar yanayam to'g'riroq yozmoqchi bo'lsak bunday qilamiz:
yosh = input("Yoshingizni kiritng: ")
try:
    yosh = int(yosh)
except:
    print("Siz butun son kiritmadingiz!")
else:
    print(f"Siz {2025-yosh}-yilda tug'ilgansiz.")
# Aytish kerakki yuqoridagi amallar bilan kod to'htab qolmaydi va agar kod davomiga biz ayrim
# qo'shimchalar yozsak o'shalar ham bajarilib keyin kodlar tugasa shunda dastur to'htaydi
print("Dastur davom etyapti.")
print("Dastur tugadi.")    
# Bunda ham natija o'zgarmaydi.

# except bilan biz turli xil xatolarni ushlashimiz mumkin. Yuqoridagi xolatga o'xshab har turli
# xatoga bir hil habar chiqavermaydi. Buni qanday amalga oshiramiz hozir ko'ramiz:

# ZeroDivisionError
# x, y = 5, 10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
    
# IndexError
# mevalar = ['olma', 'banan', 'gilos', 'shaftoli']
# try:
#     print(mevalar[5])
# except IndexError:
#     print("Xato index kiritdingiz ro'yxatda 4ta element bor xolos!")

# KeyError
# user = {"username" : "Nurulloh",
#         "status" : "Admin",
#         "email" : "nurik9.99@bk.ru",
#         "phone" : "998971234567"
#         }

# key = "tel"
# try:
#     print(f"Foydalanuvchi {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas.")

# Keling endi fayllar bilan ishlab ularda uchrashi mumkin bo'lgan xatolar bilan tanishamiz:
# filename = 'data.txt' # Bunday fayl mavjud emas.
# try: 
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"{filename} fayli mavjud emas.")
    
# Bir nechta fayllar bilan ishlab ko'ramiz:
# import json     
# talaba1 = "Abdurashidov Nurulloh"
# json_talaba1 = json.dumps(talaba1)
# talaba2 = "Abdurashidova Mavludaxon"
# json_talaba2 = json.dumps(talaba2)
# talaba4 = "Olim Olimov"
# json_talaba4 = json.dumps(talaba4)


# Json turidagi ma'lumotlarimizni faylga yuklaymiz:
# with open('json_talaba1', 'w') as f:
#      json.dump(talaba1, f) 
     
# with open('json_talaba2', 'w') as f:
#      json.dump(talaba2, f) 

# with open('json_talaba4', 'w') as f:
#      json.dump(talaba4, f) 
     
# files = ['json_talaba1', 'json_talaba2', 'json_talaba3', 'json_talaba4']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas!")
#     else:
#         print(talaba)      
# Shu tariqa biz fayllar bilan ishlashimiz mumkin.


# Biz faqat bitta EXCEPT emas, balki bir nechta EXCEPTlar yozishimiz ham mumkin:
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20 / n
# except ValueError:
#     print("Butun son kiritmadingiz!")
# except ZeroDivisionError:
#     print("0ga bo'lish mumkin emas.")
# else:
#     print(f"x = {x}")
    
# Aslida bizbunday kodlarni TRY-EXCEPT bilan emas WHILE sikli bilan yozsak ham bo'ladi ya'ni
# TRY-EXCEPT bizda jiddiyroq xatolar uchun desak, keling yuqoridagi kodlarni WHILE sikli orqali
# yozib ko'ramiz:
# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2025 - yosh}-yilda tug'ilgansiz!")

# Endi bu kodni WHILE sikliga tushiramiz:
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit(): # Bu yerda isdigit() metodi orqali kiritilgan qiymat raqamlardan iborat
    # yoki yo'qligini tekshiramiz.
#         yosh = int(yosh)
#         break
# print(f"Siz {2025 - yosh}-yilda tug'ilgansiz!")

# 33 - DARS TUGADI.