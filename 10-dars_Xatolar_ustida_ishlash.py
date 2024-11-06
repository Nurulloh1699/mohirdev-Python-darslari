# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:48:39 2024

@author: DavrServis
"""

#10-dars Xatolar ustida ishlash.
#15.10.2024.
#Muallif:Abdurashidov Nurulloh.

#1
# son = float(input("Juft son kiriting: ") # Bu yerda xato ikkinchi qavs yopilmagan edi.
# if son%2 == 0:
#     print("Bu son juft emas.) # Bu yerda xato qo'shtirnoq qo'yishda bo'lgan.
# else:
#     print("Rahmat!")) # Bu yerda ham xato bor ikkita qavs yopilgan belgi.
        
#2
# yosh = (input("Yoshingiz nechida?")) # Bu ikkala qatorda ham type (int) o'tkazilmagan.
# yosh = (input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18 # Bu yerda elif ni yopish uchun (:) qolib ketkan 
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")

#3
# x = float(input("Birinchi sonni kiriting: ") # Bu yerda bitta qavs qolib ketgan.
# y = float(input("Ikkinchi sonni kiriting: ") # Bu yerda bitta qavs qolib ketgan.
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}") # Bu yerda ikki hil qo'shtirnoqdan foydalanilgan.
# else # else dan keyin (:) qo'yilmagan.
#     print(f"{x}>{y}")
    
#4
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun'] # Bu yerda qavs yopilmagan. 

#          # Bu yerda savat degan bo'sh ro'yxat yaratib olish kerak edi.

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat # for ni (:) ikki nuqtasi qo'yilmagan.
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")   

#5
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: ')) # Bu yerda bir tirnoq qo'yishda xato qilingan

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahslot) # Bu yerda mahsulot so'zi to'g'ri yozilmagan.
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")         

#6
# users = ['alisher1983','aziza','yasina' 'umar']

# login = input("Yangi login tanlang:' ) # Bu yerda qo'sh tirnoqqa olishda xato qilingan.

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")