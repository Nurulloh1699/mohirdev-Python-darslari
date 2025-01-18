# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:38:22 2025

@author: DavrServis
"""

# 23 - DARS.
# lambda - NOMSIZ FUNKSIKYA.
# Pythonnig o'ziga xos xususiyatlaridan biri nomsiz, vaqtinchalik funksiyalar yaratish imkoniyatidir. Bunday funksiyalarni
# yaratishda DEF operatori o'rniga LAMBDA operatori ishlatilgani uvhun ham LAMBDA funksiyalar deb ataladi.

# Nomsiz funksiyalar quyidagicha yaratiladi:
# lambda argument: ifoda

# LAMBDA funksiyalari istalgan miqdordagi argumentlarga ega bo'lishi mumkin, ammo funksiya badanida faqat bitta ifoda mavjud
# bo'ladi. Ifoda bajariladi va qaytariladi (return operatori yozilmaydi).

# Nomsiz funksiyalar biror ifodani tezda hisoblab olishda juda qulay. Misol uchun, quyidagi lambda funksiya ikkita argument qabul
# qiladi (pi, r) va aylana uzunligini qaytaradi:
# import math
# uzunlik = lambda pi, r : 2 * pi * r
# print(uzunlik(math.pi, 10))
# Kodni tahlil qilamiz:
# 1 - qatorda math modulini chiqarib oldik.
# 2 - qatorda lambda funksiyani yaratdik.
# Funksiyamiz pi va r argumentlarini qabul qilib 2 * pi * r qiymatni qaytaradi. Funksiyaga nom beramdik, ;ekin unga uzunlik
# identifikatori orqali murojaat etishimiz mumkin. U uzunlik qayoqdan keldi deyilsa (uzunlik = lambda pi, r : 2 * pi * r).

# 3 - qatorda funksiyamizga murojaat etdik va natijani konsolga chiqardik.

# Yana bir misol, toping_chi, quyidagi funksiyaning vazifasi nima?
# product = lambda x, y : x**y # Bu lambda funksiyasini daraja topish deb atasak bo'ladi (x sonining y darajasi desak bo'ladi)
# print(product(3, 2)) # 3 ning 2 - darajasi so'ralyapti.
# Natija: 9

# Shu yerda so'rashingiz mumkin, nima uchun lambda nomsiz deb ataladi, axir, unga hozirgina product nomi bilan murojaat etdik-ku.

# Gap shundaki, lambda funksiyalarning asl mohiyati boshqa funksiyalar bilan birga ishlaganda ko'rinadi. Keling, tushunarli
# bo'lishi uchun soddaroq misolni ko'rib chiqamiz.

# Quyidagi dasturda biz avval daraja degan funksiya yasadik, bu funksiyamiz n degan o'zgaruvchi qabul qilib oladi va funksiya
# ichidagi noma'lum x ning n - darajasini qaytaradi.

# Ya'ni daraja funksiya yasaydigan funksiya hosil bo'ldi. Xo'sh undan qanday foydalanamiz? 4 - 5-qatorlarga e'tibor bering, biz
# daraja funksiyasidan yana 2ta funksiya yasadik: kvadrat kiritlgan sonning kavadratini hisoblaydi, kub kiritilgan sonning
# kvadratini hisoblaydi, kub kiritilgan sonning kubini hisoblaydi.
# def daraja(n):
#     return lambda x : x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3 ning kvadrati {kvadrat(3)} ga teng.")
# print(f"3 ning kubi {kub(3)} ga teng.")
# Natija: 3 ning kvadrati 9 ga teng.
#         3 ning kubi 27 ga teng.

# Lambda funksiyalaridan argument sifatida boshqa funksiyani qabul qiluvchi funksiyalar bilan ishlashda ham keng foydalaniladi
# Misol uchun, map() va filter() funksiyalari.

# Quyida ularni ko'rib o'tamiz:
    
# map() FUNKSIYASI.
# Bu funksiya argument sifatida ro'yxat (yoki lug'at) va boshqa bir funksiyani qabul qilib, ro'yxat elementlariga qabul qilingan
# funksiya yordamida ishlov beradi. Tushunarli bo'lishi uchun quyidagi misolni ko'rib chiqamiz:
# from math import sqrt
# sonlar = list(range(11)) # 0 dan 10 gacah sonla ro'yxati.
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)
# Natija: [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907,
#         2.8284271247461903, 3.0, 3.1622776601683795]

# Yuqoridagi misolda avval 0 dan 10 gacha sonlar ro'yxatini tuzib oldik, keyin esa MAP funksiyasiga ro'yxat va sqrt funksiyasini
# uzatib, ro'yxatdagi barcha sonlarning ildizini hisoblab oldik. map() funksiyasi obyekt qaytargani sababli qaytgan obyektni
# ro'yxatga o'tkazib olish uchun list() funksiyasidan foydalandik (obyektlar haqida kelgusi bobda batafsil gaplashamiz).

# Yana bir misol:
# sonlar = list(range(11)) # 0 dan 10 gacah sonla ro'yxati.
# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
# print(sonlar)
# print(list(map(daraja2, sonlar)))
# Natija: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Yuqoridagi misolda biz avval berilgan sonning kvadratini hisoblovchi funksiya yaratdik, undan keyin esa map yordamida sonlar
# ro'yxatidagi elementlarining kvadratini ham hisoblab oldik.

# Endi, keling, xuddi shu misolni lambda yordamida yozamiz:
# kvadratlar = list(map(lambda x:x*x, sonlar))
# print(kvadratlar)
# Natija: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Bu safar daraja degan funksiyani yaratib o'tirmasdan, map funksiyasiga to'g'ridan to'gri darajani hisoblovchi lambda funksiyasini
# uzatdik.

# map() funksiyasi bo'lmaganida, biz bunday dasturlarni for yordamida yozishimiz kerak bo'lar edi:
# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)
# Natija: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# map() funksiyasiga bir nechta ro'yxatlar ham uzatish mumkin:
# a = [4,5,6]
# b = [7,8,9]
# a_plus_b  = list(map(lambda x,y:x+y, a, b))
# print(a_plus_b)     
# # Natija: [11, 13, 15]
# # map() istalgan ko'rinishdagi ma'lumot turlari bilan ishlaydi.
# ismlar = ['hasan', 'olim', 'husan', 'umid']
# print(list(map(lambda matn:matn.upper(), ismlar)))
# Natija: ['HASAN', 'OLIM', 'HUSAN', 'UMID']

# filter() FUNKSIYASI.
# Bu funksiya ham argument sifatida ro'yxat va boshqa funksiyani qabul qilib oladi va berilgan ro'yxat elementlarini berilgan
# funksiya yordamida saralaydi (filter). Bunda argument sifatida uzatiladigan funksiya mantiqiy qiymat qaytarishi kerak
# (True/False).

# Keling bunga bir misol keltiramiz: tasodifiy sonlar ro'yxatidan juft sonlarni ajratib oluvchi dastur yozamiz. Dastur 3 qismdan
# iborat:

# 1. Avvalo, random modulidagi sample() funksiyasi yordamida 0 - 99 oralig'idagi 10ta tasodifiy sonlar ro'yxatini tuzamiz. 

# 2. Berilgan son juft (True) yoki juft emas (False) ekanligini qaytaruvchi funksiya yozamiz.

# 3. filter() funksiyasiga yangi yaratgan juftmi funksiyasi va tasodifiy sonlar ro'yxatini uzatib, yangi juft_sonlar ro'yxatini 
# shakllantiramiz.
# import random as r 
# sonlar = r.sample(range(100),10)
# def juftmi(x):
#     """x juft bo'lsa, True, aks hold, False qaytaramiz"""
#     return x%2 == 0

# juft_sonlar = list(filter(juftmi, sonlar))
# print(sonlar)
# print(juft_sonlar)
# Natija: [62, 29, 61, 35, 81, 48, 37, 59, 54, 57]
#         [62, 48, 54]

# Keling, endi shu daturni lambda yordamida yozamiz:
# import random as r # random funksiyasini import qilib uni as orqali r ga tenglab oldik.

# sonlar = r.sample(range(100), 10) # sonlar degan o'zgaruvchiga range(100) orqali 100 gacha sonlarni oldil, r.sample orqali esa
# # shu 100ta son ichidan tasodifiy 10tasini ajratamiz va sonlar degan o'zgaruvchiga qo'shamiz.
# juft_sonlar = list(filter(lambda son: son%2 == 0, sonlar)) # juft_sonlar degan yangi o'zgaruvchiga list bilan ro'yxat yaratamiz
# # filter orqali saralaymiz lambda orqali esa aynan qanday sonlarni saralashni aytamiz vu holatda faqat juft sonlarni.

# print(sonlar)
# print(juft_sonlar)
# Natija: [28, 64, 27, 89, 93, 39, 65, 11, 79, 98]
#         [28, 64, 98]

# Ko'rib turganingizdek, lambda funksiya yordamida dastur birmuncha qisqaroq chiqadi. Agar juftmi funksiyasi kelajakda shart
# bo'lmasa, alohida funksiya yaratib o'tirmasdan, bir martalik lambda funksiyasidan foydalangan afzal.

# Keling, endi filter() funksiyasi yordamida matnlarni saralashga ha misollar keltiraylik:

# Quyidagi dastur mevalar ro'yxatidan b harfi bilan boshlanuvchi mevalarni ajratib oladi. Bu yerda biz matnlarga tegishli bo'lgan
# .startswith() metodidan foydalandik. Bu metod berilgan matn shu harfdan boshlanadimi yoki yo'qligini teksgiradi va True yoki
# False qiymat qaytaradi.
# mevalar = ['olma', 'anor', 'anjir', "o'rik", 'qovun', 'banan']
# mevb = list(filter(lambda meva:meva.startswith('b'), mevalar))
# print(mevb)
# Natija: ['banan']

# Quyidagi dastur esa mevlar ro'yxatidan nomi yoki undan kam harfdan iborat mevalarni saralab oladi.
# mevalar2 = list(filter(lambda meva:len(meva) <= 4, mevalar))
# print(mevalar2)
# Natija: ['olma', 'anor']

# Toping-chi quyidagi kod qanday vazifani bajaradi?
# mevalar3 = list(filter(lambda meva:meva.startswith('a') and meva.endswith('r'), mevalar)) # Bu kod mevalar ichidan bosh harfi 'a'
# va ohirgi harfi 'r' bo'lgan mevalarni saralab oladi.
# print(mevalar3)
# Natija: ['anor', 'anjir']


# AMALIY TOPSHIRIQLAR.
#1 - Berilgan sonno 10ga ko'paytiruvchi lambda funksiyasi yozing.
# numbers = [1,2,3,4,5]
# result = list(map(lambda x: x * 10, numbers))
# print("Asl ro'yxat:", numbers)
# print("10ga ko'paytirilgan:", result)
# Natija: Asl ro'yxat: [1, 2, 3, 4, 5]
#         10ga ko'paytirilgan: [10, 20, 30, 40, 50]

#2 - Ikki son qabul qilib, ularning yig'indisini qaytaruvchi lambda funksiya yozing.
# son1 = float(input("Birinchi sonni kiriting: ")) # Kiritilgan sonni o'nlik son qilib olamiz.
# son2 = float(input("Ikkinchi sonni kiriting: ")) # Kiritilgan sonni o'nlik son qilib olamiz.
# result = lambda x, y: x + y # Lambda ikki sonni qo'shadi
# print("Natija:", result(son1, son2)) # Lambda funktsiyasini argumentlar bilan chaqiramiz

#3 - random moduli ichidagi sample funksiyasi yordamida 0 dan 1000 gacha sonlar oralig'idagi
# tasodifiy 10ta sonlar ro'yxatini tuzing.
# import random 
# tasodifiy_sonlar = random.sample(range(1001), 10)
# print(tasodifiy_sonlar)

# map() va lambda funksiya yordamida sonlarning kvadratini hisoblang.
# sonlar_kvadrati = list(map(lambda x: x*x , tasodifiy_sonlar))
# print(sonlar_kvadrati)

# filter() va lambda funksiya yordamida ro'yxatdan toq sonlarni ajratib oling.
# toq_sonlar = list(filter(lambda x: x%2!=0 , tasodifiy_sonlar))
# print(toq_sonlar)

#4 - Berilgan son tub bo'lsa, True, aks holda False qaytaruvchi funksiya yozing.
# def tub_sonmi(son):
#     if son < 2:
#         return False
#     for i in range(2, int(son**0.5) + 1):
#         if son % i == 0:
#             return False
#     return True

# son = int(input("Istalgan son kiriting: "))
# if tub_sonmi(son):
#     print(f"{son} tub son.")
# else:
#     print(f"{son} tub emas.")

# # filter() va yuqoridagi funksiya yordamida 1 dan 10000 gacha oraliqdagi bo'lgan
# # tub sonlar ro'yxatini tuzing.
# tub_sonlar = list(filter(tub_sonmi, range(10001)))
# print(tub_sonlar)

# 23 - DARS TUGADI.