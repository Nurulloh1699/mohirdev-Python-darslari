# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:25:01 2024

@author: DavrServis
"""
# UMUMIY TAKRORLASH.





























# 21 - DARS.
# MOSLASHUVCHAN FUNKSIYA (*args, **kwargs).
# Agar funksiyangiz bir nechta argument qabul qilishi kerak bo'lsa-yu, lekin siz argumentlar sonini aniq bilmasangiz, Pythonda
# istalgancha qiymat qabul qiluvchi funksiya yaratish imkoniyati bor.


# *args USULI.
# Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa va parametrlar yagona qiymatlar ko'rinishida uzatilsa, funksiya 
# yaratishda argumentdan avval yulduzcha qo'yiladi (*arguments).

# Quyidagi misolni ko'raylik. summa() nomli funksiyamiz istalgancha sonlarni qabul qilib oladi va ularning yig'indisini hisoblaydi:
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# Bu funksiyani istalgancha parametr bilan chaqirish mumkin:
# print(summa(1,2,3,4,54))
# Natija: 64
# print(summa(4,5,6,7,8,3,1,34,564))
# Natija: 632

# *argsusulida barcha uzatilgan parametrlar (birdona bo'lsa ham) funksiya ichida o'zgarmas ro'yxatga (tuple) joylanadi. Bundan
# kelib chiqib yuqoridagi funksiyamizni yanada soddalashtirib yozishimiz mumkin:
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     return sum(sonlar)
# Funksiyani ishlatib ko'ramiz:
# print(summa(4,5,6,7))
# Natija: 22

# Agar funksiya bir nechta argument qabul qilsa, *args argumenti doim ohirida yoziladi:
# def summa(x, y, *sonlar):
#     """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     return x+y+sum(sonlar)
# Yuqoridagi funksiyamiz 2ta majburiy parametr qabul qiladi (x va y), undan keyingi qiymatlar esa ixtiyoriy bo'ladi:
# print(summa(2))
# Natija: TypeError: summa() missing 1 required positional argument: 'y'
# print(summa(9,10,11))
# Natija: 30
# print(summa(-10,10))
# Natija: 0


# **kwargs USULI.
# Agar funksiyaga kalit-qiymat ko'rinishida argumentlarni uzatish talab qilinsa va bunday oarametrlar soni noma'lum bo'lsa,
# argument oldidan ikkita yulduzcha qo'yiladi (**kwargs).

# **kwrgs - keyword argument (kalit so'zli argumentlar)

# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar

# Yuqoridagi funksiyamiz kompaniya va model degan ikki qiymatni qabul qiladi, undan keyin esa funksiyasiga istalgancha parametr
# uzatish mumkin. Bunday funksiyaga parametrlar KALIT = QIYMAT ko'rinishida uzatiladi.

# Funksiya ichida avval foydalanuvchi kiritgan QO'SHIMCHA qiymatlardan iborat ma'lumotlar deb nomlangan lug'at shakllantiriladi.
# Undan keyin esa majburiy parametrlarni lug'atga qo'shamiz.
# avto1 = avto_info("GM", "malibu", rang = "qora", yil = 2018)
# avto2 = avto_info("KIA", 'K5', rang = "qizil", narx = 35000)
# print(avto2)
# Natija: {'rang': 'qizil', 'narx': 35000, 'kompaniya': 'KIA', 'model': 'K5'}

# AMALIYOT TOPSHIRIQLARI.
#1 - Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing.
# def summa(*sonlar): # Funksiya yaratib olyapmiz (istalgancha parametr qabul qiladigan funksiya)
#     kopaytma = 1 # Boshlang'ich qiymat qilib 1 soni olinadi, mega aynan 1? Ko'paytma operatsiyasi 1 bilan boshlanadi (1 * n = n)
#     for son in sonlar: # Son degan o'zgaruvchi yaratib olinadi va u sonlar ichidagi har bir songa tenglanadi.
#         kopaytma *= son # Bu yerda kopaytma o'zgaruvchisiga har bir son ko'paytiriladi. Bu kopaytma = kopaytma * son deganidir.
#     return kopaytma # Funksiya oxirida kpaytma qiymatini tashqi kodga qaytaradi.
# print(summa(3,5,1,6,4,))
# Natija: 360

#2 - Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy
# argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
# def talaba_info(ism, familiya, **malumotlar):
#     malumotlar["ism"] = ism
#     malumotlar["familiya"] = familiya
#     return malumotlar
# talaba1 = talaba_info("Nurulloh", "Abdurashidov", t_yil = 1999, yoshi = 25)
# print(talaba1)
# Natija: {'t_yil': 1999, 'yoshi': 25, 'ism': 'Nurulloh', 'familiya': 'Abdurashidov'}

# 21 - DARS TUGADI.


# 22 - DARS.
# MODULLAR. 

# Funksiyaning qulayliklaridan biri ko'p takrorlanadigan kodlarni funksiya ichida yashirishimiz va kerak bo'lganda funksiya nomi
# orqali murojaat etishimiz mumkinligida. Maqsadimiz dasturimizni ixcham va tushunarli qilib, kelajakda o'zimiz yoki boshqalar uchun
# ham "toza" kod qoldirishdir.Bu yo'nalishda yana bir qadam qo'yib, dasturimizni modullarga ajratishimiz mumkin.


# MODUL NIMA?
# Modul loyihamiz ichidagi alohida fayl bo'lib, dasturimiz davomida ishlatiladigan funksiyalarni (va o'zgaruvchilarni) mana shu
# faylga joylab, ko'zdan yashirib qo'yishimiz mumkin. Bu bizga asosiy dasturimizdan chalg'imasdan kod yozish imkoniyatini beradi.

# Modul va uning ichidagi funksiyalarni istalgan payt asosiy dasturimizga yuklab olishimiz, modullarni boshqa dasturchilar bilan 
# ulashishimiz yoki kelajakda o'zimizning boshqa loyihalarimizda foydalanishimiz mumkin.

# Umiman olganda, katta dasturlar bir necha o'nlab modullardan iborat bo'lishi tabiiy hol.


# MODUL YARATAMIZ.
# Modul yaratish uchun asosiy dasturimizdagi funksiyalarni yangi faylga ko'chiramiz xolos. Modulga oson murojaat etishimiz uchun
# faylimiz asosiy dasturimiz bilay bitta papkada bo'lgani afzal. Bunda adashib ketmaslik uchun loyihamizning (dasturning) asosiy
# faylini main.py deb nomlash o'rinli.

# Keling, biz ham avto_info_mod.py degan fayl yaratamiz va ichiga quyidagi 3ta funksiyalarni joylaymiz:
# def avto_info(make, model, color, korobka, year, narxi = None):
#     avto = {'kompaniya' : make,
#             'model' : model,
#             'rang' : color,
#             'korobka' : korobka,
#             'yil' : year,
#             'narx' : narxi}
#     return avto

# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini
#     beruvchi funksiya"""
#     avtolar = []
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting: ")
#         kompaniya = input("Ishlab chiqaruvchi: ")
#         model = input("Mashina modeli: ")
#         color = input("Mashinaning rangi: ")
#         korobka = input("Mashinaning korobkasi: ")
#         year = input("Ishlab chiqarilgan yili: ")
#         narxi = input("Mashinaning narxi: ")
#         avtolar.append(avto.info(kompaniya, model, color, korobka, year, narxi))
        
#         javob = input("Yana avtomobil qo'shasizmi: (h/y): ")
#         if javob == "y":
#             break
#         return avtolar
    
# def info_print(avto_info):
#     """Avtomobillar haqida saqlangan ma'lumotlarni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['color'].title()}"
#           f"{avto_info['kompaniya'].upper()}"
#           f"{avto_info['model'].upper()},"
#           f"{avto_info['korobka']} korobka,"
#           f"{avto_info['year']}-yil, {avto_info['narx']}$")
# Yuqoridagi funksiyalarga asosiy dasturdan murojaat qilishning bir nechta usuli bor.


# MODULNI CHAQIRIB OLISH.
# Modul ichidagi istalgan funksiyaga murojaat etish uchun import modul_nomi butrug'idan foydalanamiz. Bunda modul ichidagi istalgan
# funksiyaga modul_nomi.funksiya_nomi() ko'rinishida murojaat etishimiz mumkin. Ya'ni avval modul nomi, keyin esa nuqta qo'yilib,
# modul ichidagi funksiya nomi yoziladi.

# Keling, yuqoridagi modulimizdagi avto_info() va info_print() funksiyalariga murojaat etamiz. Buning uchun asosiy dasturimizni 
# (main.py) quyidagicha yozamiz:
# import avto_info_mod # avto_info_mod modulini chaqiramiz.
# avto1 = avto_info_mod.avto_info("gm", "jentra", "qora", "avtomat", 2022, 15000)
# avto_info_mod.info_print(avto1)   
# Natija: Qora GM JENTRA, avtomat korobka, 2022-yil, 15000$

# ETIBOR BERING! impor modul_nomi komandasi bir marta, dastur boshida yoziladi.

# MODULGA QISQA NOM BERISH.
# Yuqoridagi usul modulni chaqirib olishda fayl nomi uzun bol'sa, bu o'ziga yarasha noqulayliklar tug'dirishi mumkin. Buning oldini 
# olish uchun esa modulni chaqirganda unga as operatori yordamida qisqa nom berish va modulga qisqa nom orqali murojaat etish mumkin.
# Quyidagi misolda avto_info_mod ni qisqa qilib aim deb nomlab oldik va 3-4 qatorlarda modulga murojaat etishda qisqa nomidan 
# foydalandik.

# import avto_info_mod as aim 

# avto_info funksiyasini chaqiramiz
# avto1 = aim.avto_info("gm", "malibu", "qora", "avtomat", 2023, 40000)

# info_print funksiyasi yordamida ma'lumotlarni chiqaramiz
# aim.info_print(avto1)

# Modulga nom berganingizda bunday nomli boshqa o'zgaruvchi yoki funksiya yo'qligiga amin bo'ling, Shuningdek, dastur davomida bu
# nomni boshqa o'zgaruvchilarga yoki funksiyalarga berib yubormang.


# MODUL ICHIDAN MA'LUM FUNKSIYALARNI CHAQIRIB OLISH.
# Agar asosiy dasturimizda modul ichidagi muayyan funksiyalarga murojaat etish kerak bo'lsa, quyidagi ko'rinishdagi koddan
# foydalanamiz: from mudul_nomi import funksiya1, funksiya2.

# Bu usulning qulayligi shundaki, chaqirilgan funksiyalarga to'g'ridan-to'g'ri, modul nomini yozmasdan murojaat etish mumkin.
# Misol uchun, avvalgi kodimizda biz faqatgina avto_info va info_print funksiyalaridan foydalandik. Shu funksiyalarni asosiy
# dasturimizga chaqirib olamiz:
# from avto_info_mod import avto_info, info_print
# avto1 = avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
# info_print(avto1)
# Natija: Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$

# FUNKSIYALARGA QISQA NOM BERISH.
# AS operatori yordamida chaqirib olgan funksiyamizga ha qisqa nom berishimiz mumkin:
# from avto_info_mod import avto_info as ainfo
# from avto_info_mod import info_print as iprint
# avto1 = ainfo ("gm", "malibu", "qora", "avtomat", 2020, 40000)
# iprint(avto1)
# Natija: Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$


# MODUL ICHIDAGI BARCHA FUNKSIYALARNI CHAQIRIB OLISH.
# Modul ichidagi barcha funksiyalarni asosiy dasturga ko'chirib olish uchun from mudul_nomi import * komandasidad foydalanamiz.
# from avto_info_mod import * 
# avto1 = avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
# info_print(avto1)
# Natija: Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$

# ETIBOR BERING! Bir necha sabablarga ko'ra bu usuldan foydalanish tavsiya etilmaydi. Katta modullarda yuzlab funksiyalar bo'lishi
# mumkin va funksiya nomi dasturimizdagi boshqa funksiya yoki o'zgaruvchi bilan bir xil nomga ega bo'lsa, dastur xato ishlashiga
# olib keladi.


# MODULDA O'ZGARUVCHI SAQLASH.
# Modullarning ichida nafaqat funksiyalar, balki turli o'zgaruvchilarni ham saqlash mumkin. Modul ichidagi o'zgaruvchilarga ham
# xuddi yuqoridagi usullar bilan murojaat etamiz.


# PYTHON MODULLARI.
# Python dasturlash tili tayyor modullar bilan keladi, ulardan ba'zilari bilan tanishamiz.

# math MODULI.
# Bu modulda matematik hisob-kitoblarni bajaruvchi funksiyalar va o'zgaruvchilar joylashgan, jumladan:
# sqrt() - qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi:
# import math
# x = 400
# print(math.sqrt(x))
# Natija: 20.0

# pow(x, n) - x ning n-darajasini qaytaruvchi funksiya:
# import math
# print(math.pow(5, 5))
# Natija: 3125.0

# pi - π ning qiymatini saqlovchi o'zgaruvchi:
# from math import pi
# print(pi) 
# Natija: 3.141592653589793

# log2(x) va log10(x) - x ning 2 lik va 10 lik logarifmini aytaruvchi funksiyalar.
# print(math.log2(8)) 
# Natija: 3.0
# print(math.log10(100))
# Natija: 2.0

# math moduliga kelgusida yana qaytamiz.

#  random MODULI.
# RANDOM moduli tasodifiy sonlar bilan ishlash uchun qulay funksiyalarga boy. Ulardan ayrimlari bilan tanishamiz.

# randint(a, b) funksiyasi a va b oralig'idagi tasodifiy butun sonni qaytaradi.
# import random as r  # random modulini r deb chaqiramiz.
# son = r.randint(0, 100)
# print(son) # bu natija endi har safar har hil bo'ladi va 0 dan 100 gacha bo'lgan sonlar ichidan birontasini qaytaradi.
# Natija: 48 # aytkanimizdek har safar har hil natija qaytaradi.

# choice(x) - berilgan x argumentining ichida tasodifiy elementni qaytaruvchi funksiya. Bunda x bir necha elementdan iborat
# o'zgaruvchi (matn, ro'yxat, to'plam, va hokazo) bo'lishi kerak.
# ismlar = ["olim", "anvar", "hasan", "husan"]
# ism = r.choice(ismlar) # Tasodifiy ism tanlaymiz.
# print(ism)
# Natija: hasan # Bu yerda ham har safar har hil natija qaytadi.

# Yana bir misol ko'ramiz:
# x = list(range(0, 51, 5)) # Ro'yxat yaratamiz (0 dan 50 gacha 5ta oraliq bilan).
# print(x)
# print(r.choice(x)) # Tasodifiy elementni tanlaymiz.
# Natija: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50] # 1 - print ni natijasi.
# Natija: 35 # 2 - print ni natijasi (tasodifiy tanlangan son).

# shuffle(x) - x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya. Bunda x bir necha elementlardan iborat o'zgaruvchi
# (mat, ro'yxat) bo'lishi kerak.
# x = list(range(11)) # Ro'yxat yaratamiz (0 dan 11 gacha)
# print(x)
# r.shuffle(x)
# print(x)
# Natija1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Natija2: [6, 1, 8, 9, 5, 3, 7, 2, 0, 4, 10]

# sample(x,k) - x ro'yxat ichidan tasodifiy k ta element ajratib olish:
# from random import sample
# x = list(range(0, 100)) # 0 dan 100 gacha sonlar ro'yxati.
# y = sample(x, k = 10) # x ro'yxatidan tasodifiy 10ta elementni ajratib olamiz.
# print(y)
# Natija: [7, 70, 59, 82, 84, 85, 1, 89, 79, 60]

# math va random modullari ichidagi boshqa funksiyalar haqida Python rasmiy sahifasidagi (docs.python.org) ma'lumot olishingiz
# mumkin.

# 22 - DARS TUGADI.


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


# 24 - DARS.
# OBYEKTGA YO'NALTIRILGAN DASTURLASH.
# Dasturlashni o'rganar ekanmiz, albatta, object oriented programming (OOP), ya'ni obyektga yo'naltirilgan dasturlash tushunchasiga 
# kelamiz. Ko'pchilik uchun bu bosqich biroz tushunarsiz va murakkabdek tuyuladi. Aslida, unday emas. Ushbu bobda object oriented
# programming va unga tegishli tamoyillar haqida gaplashamiz.


# OOP NIMA?

# KLASSIK YOXUD CHIZIQLI DASTURALSH.
# OOPni tushunish uchun avval klassik dasturlashni ko'zdan kechiraylik. Gap shundaki, ilk kompyuterlar va dasturlar matematik muammolarni
# hal etishga qaratilgan. Bunday dasturlar foydalanuvchidan biror ma'lumotni qabul qilib olgan va qat'iy ketma-ketlik, ya'ni tartibga amal
# qilgan holda turli arifmetik amallarni bajarib, Shuning uchun ham bunday dasturlar chiziqli yoki tartibli dasturlar deb ataladi.

# Siz ham dasturlashga ilk qadam qo'yganingizda mana shunday chiziqli dasturlani yozishnio'rganishdan boshlaysiz. Sizning dasturingiz bir
# nechta o'zgarivchilar va funksiyalardan iborat bo'ladi. Bu o'zgaruvchilar va funksiyalar ma'lum ketma-ketlikda bir-biri bilan
# munosabatga kiradi va dastur yakunida esa siz kutkan natijani beradi.


# Dastur kattalashgani sari o'zgaruvchilar va funksiyalar soni ortib boradi. Ular o'rtasidagi munosabatlar ham chigallashib, kodingiz 
# murakkab va tushunishga qiyin bo'lib ketadi. Dasturlash jarayonida bitta funksiyaga o'zgartirish kiritishingiz esa unga bog'liq boshqa
# funksiyalarning ishdan chiqishiga va dasturingiz xato natija berishiga olib kelishi ham mumkin.

# Chiziqli dasturlashning afzalliklari:
    # 1. Dasturlashni o'rganishga qulay.
    # 2. Sodda va tushunarli kod.
    # 3. Dastur algoritmini kuzatish oson.
    # 4. Dastur xotirada kamroq joy egallaydi.
# Chiziqli dasturlashning kamchiliklari:
    # 1. Murakkab dasturlarni chiziqli usulda yozish qiyin (ilojsiz).
    # 2. Bir dastur uchun yozilgan koddan boshqa dasturda qayta foydalanib bo'lmaydi.
    # 3. Dastur ichidagi ma'lumotlar (o'zgaruvchilar) barcha funksiyalar uchun ochiq. 
    # 4. ZAMONAVIY DASTURLAR CHIZIQLI EMAS.
# Vaqt o'tib dasturlarga qo'yilgan talablar murakkablashib borgani sababli chiziqli dasturlash tamoyili zamon talabiga javob bermay qo'ydi
# va 1970-yillarda OOP tamoyili olg'a surila boshlandi.


# OBYEKT NIMA?
# Object oriented dasturlashda o'zaro bog'liq bo'lgan o'zgaruvchilar va funksiyalar bitta konteynerga jamlanadi, bunday konteynerlar 
# obyekt deb ataladi. Bir obyektga tegishli o'zgaruvchilar uning xususiyatlari, unga tegishli funksiyalar esa metodlari deb ataladi.

# Keling misol tariqasida avtomobil degan obyektni ko'rib chiqamiz. Avtomobilning modeli, rangi va narxi uning xususiyatlari. Avtomobilga
# tegishli bo'lgan start(), stop() va tezlashish() kabi amallar esa uning metodlari deyiladi.

# Agar real dasturdam misol keltiradigan bo'lsak, istalgan dastur ichidagi tugma - bu obyekt. Uning shakli, rangi va matni esa
# xususiyatlari bo'ladi. Tugma ustida bajariladigan amallar tugmaning metodlari deyiladi. Misol uchun, tugmani bosish, uzoq bosish,ustiga
# sichqonchani olib borish va hokazo.

# Object oriented dasturlar o'nlab, balki, yuzlab obyektlardan iborat bo'ladi va bunday dasturlar uchun dastur boshiyoki oxiri degan 
# tushunchalar nisbiy.

# Object oriented dasturlar bajarilishida qat'iy ketma-ketlikka amal qilmaydi. Foydalanuvchi istalgan obyektga murojaat etishi, uning
# ustida turli amallar bajarishi mumkin. O'z navbatida, bitta obyektga murojaat ortidan boshqa obyektlar ham faollashishi mumkin.

# Misol uchun, mobil ilovalarda obyektlar dastur ichidagi tugmalar, matnlar, rasmlar va boshqa elementlardir. Foydalanuvchi istalgan
# tugmani bosishi, istalgan matnni ajratib olishi va boshqa amallarni istalgan tartibda bajarishi mumkin. Bunda bitta tugma (ya'ni obyektni)
# bosish bilan boshqa obyekt (masalan, rasm) o'zgarishi mumkin.

# Zamonaviy kompyuter o'yinlari ham minglab obyektlardan iborat. Foydalanuvchi esa virtual o'zyin olamida erkin harakat qilishi, istalgan
# tarafga yurishi, istalgan vaqtda turli obyektlar turli amallar bajarishi mumkin.


# KLASS NIMA?
# Object oriented programming haqida gaplashar ekanmiz, uning fundamental tushunchalaridan biri - klass haqida gapirib o'tmaslikning iloji 
# yo'q. Klass obyekt yaratish uchun shablon yoki qolipdir Bitta klassdan istalgancha nusxa olishimiz va yangi obyektlar yaratishimiz
# mumkin. Demak, obyekt - bu biror klassning xususiy ko'rinishi. Odatda, klasslarning nomi o'zgarmas, undan yaratilgan obyektlar esa 
# istalgancha nomlanishimumkin.

# Dasurimiz yuzlab obyektlardan iborat bo'lishi mumkin. Klasslar esa bizga obyektlarni yaratishni yengillashtiradi. Xoh dastur
# innterfeysidagi o'nlab turli xil tugmalar bo'lsin, xoh komyuter o'yinidagi qahramonlar bo'lsin. Har bir tugma yoki o'yin qahramoni
# va uning harakatlarini qayta-qayta yozmasdan, bir marta yaratilgan klassdan nusxa olib, o'nlab obyektlarni yaratishimiz mumkin.

# 24 - DARS TUGADI.

# 25 - DARS.
# OOP TAMOYILLARI.

# INKAPSULYATSIYA.
# Biz object oriented dasturlash haqida gapira turib ma'lum bir obyektga tegishli bo'lgan xususiyatlar va metodlarni bitta konteynerga
# joylaylmiz dedik. Bu jarayon INKAPSULYATSIYA (ya'ni kapsulaga solish) deb ataladi. Inkapsulyatsiya bizga klasslar yaratish va
# keyinchalik bu klasslardan boshqa obyektlarni yaratishga yordam beradi.

# ABSTRAKSIYA. 
# Abstraksiya yordamida biz kodimizning ichki tuzilishini yashiramiz. Ya'ni tashqaridan obyektimiz 2ta parametr va 2ta metoddan iborat
# bo'lish mumkin, lekin obyekt to'g'ri ishlashi uchun uning ichida o'nlab boshqa o'zgaruvchilar va funksiyalar yashirin bo'ladi. Klassdan
# foydalanishda esa uning ichki tuzilishi va qanday ishlashini bilish talab etilmaydi. Bu o'zimizga ham, boshqa dasturchilarga ham mazkur
# klassdan foydalanishda qulayliklar yaratadi.

# VORISLIK.
# Dasturlash jarayonida biz bir klassdan boshqa klasslar yaratishimiz mumkin. Misol uchun, bizda transport klassi bor, biz bi klassdan
# qo'shimcha avtomobil, avtobus, kema, poyezd kabi klasslarni yaratishimiz mumkin. Bundabizning asl klassimiz ota yoki super-klass deb
# ataladi, undan yaratilgan klasslar esa voris klasslar deyiladi.

# ETIBOR BERING! Voris klasslar ota klassning va'zi yoki barcha xususiyatlari va metodlariga ega bo'ladi.

# POLIMORFIZM.
# Voris klass super-klassdan o'zlashtirgan metodning nomini saqlagan holda uning ishlashini o'zgartirishi POLIMORFIZ deyiladi.

# Keling, bie misol ko'raylik, Biz kompyuter o'yini yaratish jarayonida o'yin qahramoni uchun super-klass yaratamiz. Qahramon bir nechta
# xususiyatlarga va metodlarga ega. Jumladan attack(), ya'ni hujum qilish metodi qahramonni hujum qilishga undaydi. Endi biz bu 
# super-klassdan boshqa voris klasslarni yaratamiz.
    # 1. Birinchi qahramonimiz - Qilichboz, u hujum qilganda qilichdan foyalanadi.
    # 2. Ikkinchi qahramonimiz - Jangchi, u qurolsiz bo'lgani sababli qo'l va oyoqlari bilan hujum qiladi.
    # 3. Uchunchi qahramonimiz - Pistolet bilan qurollangan.
    # 4. To'rtinchi qahramonimiz - kamon va yoylar bilan qurollangan 
# To'rt qahramonimiz ham super-klassdan attack() metodini meros oladi, lekin bu metodni biz har bir qahramonlar va turli hujum turlari
# uchun alohida metodlar yozishdan qutqaradi.

# Manashu yuqorida keltirilgan ma'lumotlar OOPning asosiy tamoyillari ekan.

# OOP AFZALLIKLARI VA KAMCHILIKLARI.
# Keling darsimiz yakunida OOPning afzalliklari va kamchiliklariga to'htalib o'taylik.

# Afzalliklari:
    # 1. Parallel dasturlash - bir loyihaning turli qismlari bir vaqtda yaratilishi mumkin.
    # 2. Vorislik tamoyili klasslardan qayta foydalanish imkonini beradi.
    # 3. Polimorfizm tamoyili klasslarni moslashuvchan qiladi.
    # 4.Klasslardan boshqa dastur va loyihalarda qayta-qayta foydalanish mumkin.
# Kamchiliklari.
    # 1. Dasturlashga yangi qadam qo'yganalr uchun biroz tushunarsiz.
    # 2. Har doim ham samarali emas.
    # 3. Ba'zida dasturimizni haddan tashqari murakkablashtirib yuborishi mumkin.
    
# OOP bilan qisqacha tanishuvimiz shundan iborat edi. Endi esa Python OOP bilan tanishuvni boshlasak ham bo'ladi.

# 25 - DARS TUGADI.


# 26 - DARS.
# KLASSLAR
# Klasslar object oriented dasturlashning poydevorlaridan biridir Klasslar bizga dasturlashga va dastur elementlariga real hayotdagi
# buyumlarga (obyektlarga) yondoshgandek yondoshi9sh imkonini beradi.

# Klasslar, obyektlar va ularning qanday ishlashini tushungan dasyurchi mantiqiy fikrlashda ham kuchli bo'ladi. Mukammal va kompleks
# muammolarga ham yechimni ko'ra biladi.


# PYTHONDA KLASSLAR.
# Klass tushunchasi siz uchun yangi bo'lishi mumkin, lekin biz shu vaqtgacha ulardan doimiy ravishda foydalanib keldik.

# Keling, x o'zgaruvchi yaratamiz, unga biror qiymat yuklaymiz va type() funksiyasi yordamiz uning turini ko'ramiz:
# x = 10
# print(type(x))
# # Natija: <class 'int'>
# matn = "salom"
# print(type(matn))
# Natija: <class 'str'>
# Ko'ryapmizki, x int klassidagi, matn esa str klassidagi obyektlar ekan. Demak, biz o'zgaruvchi yaratganimizda, aslida, Python int
# yoki str klassidan foydalangan holda yangi obyektlar yaratib kelayotgan ekan.

# Xuddi shu kabi, agar yangi funksiya yaratib, uning ham turini tekshirsak, funksiyamiz function klassiga tegishli obyekt bo'lib chiqadi.
# def salom_ber():
#     print("Assalomu Aleykum")
# print(type(salom_ber))
# Ntija: <class 'function'>
# Demak, Pythondagi har qanday o'zgaruvchi, funksiya va boshqa elementlar, aslida, obyektlar ekan.


# METODLAR.
# Har bir obyekt uning ustida bajarish mumkin bo'lgan funksiyalar bilan keladi. Bu funksiyalar obyekt ichida yashirin bo'ladi, Biz ularga
# nuqta va funksiya nomi orqali murojaat etishimiz mumkin. Bunday funksiyalar shu klassga (yoki obyektga) tegishli METODLAR deyiladi.

# Ba'zi metodlar bilan avvalgi darslarimizda tanishdik. bir klassga tegishli metodlar boshqa klassdagi obyektlar uchun mavjud bo'lmasligi
# tabiiy. Masalan, matnlar uchun mavjud metodlarni butun yoki o'nlik sonlarga qo'llab bo'lmaydi.
# matn = "salom"
# print(matn.upper()) 
# Natija: SALOM
# son = 20
# print(son.lower())
# Natija: AttributeError: 'int' object has no attribute 'lower'


# KLASS YARATISH.
# Yangi klass yaratish uchun class operatoridan foydalanamiz va klassimizga tugunarli nom beramiz. Esingizda bo'lsin, klass hali obyekt
# emas, obyekt uchun shablondir. Shuning uchun klass yaratishda mazkur klassdagi obyektlar uchun umumiy bo'lgan xususiyatlar va
# funksiyalarni o'ylashimiz kerak.

# Keling. Talaba degan klass yaratamiz:
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familya, tyil):
#         """Talaba xususiyatlari"""
#         self.ism = ism
#         self.familiya = familya
#         self.tyil = tyil
# Yuqoridagi kodimizni tahlil qilamiz:
# class Talaba  - Talaba nomli klass yaratdik. Klasslarga nom berishda uning birinchi harfini bosh harfdan boshlash tavsiya etiladi. 
# Agar klass nomi 2 va undan ko'p so'zdan iborat bo'lsa, har bir so'zni bosh harf bilan boshlang.

# def __init__(self) - klassga tegishli xususiyatlarni saqlovchi maxsus metod (funksiya). self so'zi ingliz tilidan "o'zi" deb tarjima
# qilinadiva bu klassdan yaratilgan obyektning o'ziga ishora qiladi. Ya'ni keyinchalik biz obyekt ichidagi metodga murojaat etganimizda
# shu obyektning o'zi birinchi bo'lib funksiyaga argument sifatida uzatiladi, obyekt ustida turli amallar bajarish imkonini beradi.

# def __init__(self, ism, familiya, tyil) - yaratayotgan klassimizga xos xususiyatlarni def __init__(self) funksiyasiga argument
# sifatida uzatamiz. Bizning Talaba klassimiz ism, familiya, va tug'ilgan yilga (tyil) ega bo'ladi.

# Keyingi qatorda esa self.xususiyat = argument komandasi yordamida uzatilgan argumentlarni klassning xususiyatlari bilan bog'laymiz. 
# Bu yerda xususiyat nomi uzatilgan argument nomi bilan mos tushishi shart emas, xususiyatga istalgan nom berishimiz mumkin (masalan,
# self.name = ism) 

# ETIBOR BERING! def __init__ metodi yozilishida init so'zidan avval va keyin ikki pastki chiziq yoziladi.


# KLASSDAN OBYEKT YARATISH.
# Klassimiz tayyor, keling, endi klassimizdan yangi obyekt yaratamiz.
# talaba1 = Talaba("Alijon", "Valiyev", 2000)

# Mana talaba obyektimiz tayyor. Obyektni yaratish uchun Talaba klassiga murojaat etdik va talabaning ismi, familiyasi va tug'ilgan
# yilini parametr sidatida uzatdik.

# OBYEKTNING XUSUSIYATLARINI KO'RISH.
# Obyerktning xususiyatlarini ko'rish uuchun nuqta orqali murojaat etishimiz mumkin.
# print(talaba1.ism)
# Natija: Alijon
# print(talaba1.familiya)
# Natija: Valiyev

# KLASSDAN BIR NECHTA OBYEKTLAR YARATISH.
# Yuqoridagi klassdan istalgancha obyektlar yaratishimiz mumkin:
# talaba2 = Talaba("Olim", "Olimov", 1995)
# talaba3 = Talaba("Husan", "Akbarov", 2004)
# talaba4 = Talaba("Hasan", "Akbarov", 2004)

# Bunda har bir obyekt o'zining alohida xususiyatlariga ega bo'ladi.
# print(talaba2.ism)
# Natija: Olim
# print(talaba4.familiya)
# Natija: Akbarov


# KLASSGA METODLAR QO'SHAMIZ.
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
        
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}."
#               f"{self.tyil}-yilda tug'ilganman, yoshim {2024-self.tyil} da."
#               )

# Boshlanishiga klassimizga bitta, tanishtir metodini qo'shdik. Bu metodimiz, ko'rib turganingizdek, bitta self (ya'ni obyektning o'zini)
# argumentini qabul qiladi va talaba haqidagi ma'lumotlarni konsolga chiqaradi.

# OBYEKTING METODLARIGA MUROJAAT ETAMIZ.
# Obyekt ichidagi funksiyaga, ya'ni obyektning metodiga murojaat etamiz:
# talaba4 = Talaba("Husan", "Akbarov", 2004) 
# talaba4.tanishtir()   
# Natija: Ismim Husan Akbarov.2004-yilda tug'ilganman, yoshim 20 da.

# Klassimiz istalgancha metodlarga ega bo'lishi mumkin. Yuqoridagi klassga yana obyektlar qo'shamiz:
# class Talaba :
#     """Tlaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyi = tyil
    
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#     def get_fullname(self):
#         """Talabaning to'liq ismini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
# Metodlarni tekshirib ko'ramiz.
# talaba1 = Talaba("Alijon", "Valiyev", 1999) 
# print(talaba1.get_fullname())
# Natija: Alijon Valiyev
# print(talaba1.get_lastname())
# Natija: Valiyev

# ARGUMENT QABUL QILUVCHI METODLAR.
# Avvalgi misolimizda barcha metodlar faqatgina self parametrini qabul qilyapti. Aslida, boshqa funksiyalar kabi klass ichidagi metodlar
# ham argumentlar qabul qilishi mumkin. Yuqoridagi Talaba klassimizga yangi get_age() metodini qo'shamiz:
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#     def get_lastname(self):
#         """Tlabaning familiyasini qaytaradi"""
#         return self.familiya
#     def get_fullname(self):
#         """Talabaning to'liq ismini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil
# get_age() metodi obyektning o'zidan tashqari qo'shimcha yil argumentini ham qabul qiladi va talabaning yoshini qaytaradi.
# talaba1 = Talaba("Nurulloh", "Abdurashidov", 1999)
# print(talaba1.get_age(2024))
# Natija: 25

# pass OPERATORI.
# Pythonda hech qanday vazifani bajarmaydigan pass operatori mavjud. Bu operatordan bo'sh metodlar yaratishda foydalanish mumkin. Misol
# uchun, siz klassingiz uchun muhim metodlarni bilasiz, lekin metod badani hali tayyor emas. Agar metod badanini bo'sh qoldirsangiz,
# Python IndentationError xatosini qaytaradi. Shunday holatlarda funksiya badaniga pass operatorini qo'yib ketishimiz mumkin:
# class User:
#     def __init__(self, name, username, email):
#         self.name = name
#         self.uname = username
#         self.mail = email
#     def describe():
#         pass
#     def get_email():
#         pass
# Yuqoridagi klassimizda describe() va get_mail() funksiyalar badani hali tayyor emas, bo'shliqni to'ldirish uchun esa pass operatorodan
# foydalanamiz.

# ETIBOR BERING! pass operatori bilan if-else, for, while bloklarini ham vaqtinchalik to'ldirib turish mumkin.

# AMALIYOT TOPSHIRIQLARI:
#1 - Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab
# qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo).
# class User:
#     def __init__(self, username, login, password, email):
#         self.username = username
#         self.login = login
#         self.password = password
#         self.email = email
        
#2 - Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib
# chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).        

    # def get_info(self):
    #     return f"Foydalanuvchi {self.username}ning logini:{self.login}, paroli:{self.password} va emaili: {self.email}."
# user1 = User("Nurulloh", "nur", "n1282754N", "nurik9.99@bk.ru")
# print(user1.get_info())

#3 - Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
#     def get_username(self):
#         return f"Foydalanuvchining username mi:{self.username}."
    
#     def get_login(self):
#         return f"{self.username} userining logini: {self.login}"

# user1 = User("Nurulloh", "nur", "n1282754N", "nurik9.99@bk.ru")
# user2 = User("Mavluda", "mav", "m2730209N", "mav9.99@bk.ru")
# user3 = User("Abdurahmon", "abu", "a1276464A", "abu9.99@bk.ru")
    
# print(user1.get_info())
# print(user2.get_username())
# print(user3.get_login())

# 26 - DARS TUGADI.


# 27 - DARS.
# OBYEKTLAR USTIDA ISHLASH.

# XUSUSIYATLARGA STANDART QIYMAT BERISH.
# Avvalgi bo'limda biz klass yaratish, unga xususiyatlar ca metodlar qo'shishni ko'rib chiqdik. Klassdan obyekt yaratganimizda esa uning
# xususiyatlarini parametr sifatida uzatishni o'rgandik.

# Pythonda obyektning ba'zi xususiyatlarini parametr yordamida uzatmasdan, klass yaratishda unga standart qiymat berib ketishimiz mumkin.
# Keling, Talaba klassimizga qaytamiz. Bu klassimiz 3ta xususiyatga ega edi: ism, familiya, tyil. Biz yana bitta qo'shimcha bosqich nomli
# xususiyat qo'shamiz, va unga standart qiymat sifatida 1 beramiz, e'tibor qiling, bu xususiyat obyekt yaratilishida parametr sifatida
# uzatilmaydi:
# class Talaba:
#     """Talab nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
# Endi Talaba klassidan yangi obyekt yaratganimizda har bir yangi talabaning kursi 1ga teng bo'ladi.

# talaba1 = Talaba ("Nurulloh", "Abdurashidov", 1999)
# print(talaba1.get_info())
# Natija: Nurulloh Abdurashidov. 1-bosqich talabasi.

# STANDART QIYMATNI O'ZGARTIRISH.
# Obyektning standart qiymatiga ham boshqa xususiyatlar kabi nuqta orqali murojaat etishimiz va uningqiymatini almashtirishimniz mumkin:
# talaba1.bosqich = 2
# print(talaba1.bosqich)
# Natija: 2

# Yana boshqa usuli - obyekt xususiyatini yangilovchi metod yozish.
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
    
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
# Metodga murojaat etamiz:
# talaba1 = Talaba("Nurulloh", "Abdurashidov", 1999)
# talaba1.set_bosqich(3)
# print(talaba1.get_info())
# Natija: Nurulloh Abdurashidov. 3-bosqich talabasi.

# Umuman olganda, xususiyatlarni yangilashda turli usullardan foydalanish mumkin. Misol uchun,talabaning bosqichi, odatda, 1 tadan
# ko'payib boradi, shuning uchun quyidagicha metod ham yozishimiz mumkin:
# class Talaba:
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.tyil}-yilda tug'ilgan, {2024 - self.tyil} yoshda. {self.bosqich}-bosqich talabasi."
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod."""
#         self.bosqich = bosqich
#     def update_bosqich(self):
#         """Talabaning bosqichini bittaga ko'tarish."""
#         self.bosqich += 1
# update_bosqich() metodiga murojaat etganimizda talabaning bosqichi oshib boradi:
# talaba1 = Talaba("Olim", "Olimov", 1995)
# talaba2 = Talaba("Husan", "Akbarov", 2004)
# talaba3 = Talaba("Hasan", "Akbarov", 2004)
# print(talaba1.get_info())
# Natija: Olim Olimov. 1995-yilda tug'ilgan, 29 yoshda. 1-bosqich talabasi.

# talaba1.update_bosqich()
# print(talaba1.get_info())
# Natija: Olim Olimov. 1995-yilda tug'ilgan, 29 yoshda. 2-bosqich talabasi. 

# talaba1.update_bosqich()
# print(talaba1.get_info())
# Natija: Olim Olimov. 1995-yilda tug'ilgan, 29 yoshda. 3-bosqich talabasi.


# OBYEKTLAR O'RTASIDAGI MUSOSABAT.
# Obyektga yo'nlatirilgan dasturlashning afzalligi turli obyektlar o'rtasida o'zaro munosabatlarni oson yo'lga qo'yish mumkinligidadir.
# Kleing,yangi Fan degan klass yaratamiz va fanimizga talabalar qo'shish uchun add_student() metodini yozamiz:
# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
        
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
        
# ETIBOR BERING! Fan klassi faqatgina yagona nomi degan parametrga ega. Qolgan xususiyatlariga esa standart qiymat berilgan:
# talabalar_soni = 0, talabalar ro'yxati bo'sh.

# Fanimizga talaba qo'shish uchun add_student() metodini chaqiramiz. Bu metod parametr sifatida Talaba klassiga oid obyektni qabul qiladi
# va unitalabalar ro'yxatiga qo'shadi. Shuningdek, bu metod yangi talaba qo'shilganda talabalar_soni ni bittaga oshirib qo'yadi.

# Keling, boshlanishiga yangi fan obyektini va bir nechta talabalarni yaratamiz:
# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Olim", "Olimov", 1995)
# talaba2 = Talaba("Husan", "Akbarov", 2004)
# talaba3 = Talaba("Hasan", "Akbarov", 2004)

# # Talabalarni yangi fanimizga qo'shamiz:
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# Mana fanimiz tayyor, talabalar qo'shildi. Keling, endi fan haqida ma'lumotlarni olamiz:
# print(matematika.talabalar_soni)
# Natija: 3

# Fanimizga 3ta talaba qo'shilibti. Talabalar haqida ma'lumot olsak bo'ladimi?
# print(matematika.talabalar)
# Natija: [<__main__.Talaba object at 0x0000025598EDB3E0>,
          # <__main__.Talaba object at 0x0000025598B47BF0>,
          # <__main__.Talaba object at 0x0000025598D76060>]     
    
# Talabalarning ism-familiyasi o'rniga qandaydir tushunarsiz ma'lumorlar. Aslida, hammasi to'g'ri, yuqorida fanimizga yangi talabalarni
# obyekt sifatida qo'shgan edik, yuqoridagi natija esa matemarika.talabalar ro'yxatida Talaba klassiga oid 3ta obyekt borligini
# ko'rsatmoqda.

# Fanimizga yozilgan talabalar haqida tushunarli ma'lumot olish uchun Fan klassiga yangi get_students() metodini qo'shamiz. Bu metod
# talabalar ichidagi har bir talaba obyektiga murojaat etib, get_info() metodi yordamida talabaning ma'lumotlarini oladi, ro'yxatga
# qo'shadi va shu ro'yxatni qaytaradi:
# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
        
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
    
# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Olim", "Olimov", 1995)
# talaba2 = Talaba("Husan", "Akbarov", 2004)
# talaba3 = Talaba("Hasan", "Akbarov", 2004)

# Talabalarni yangi fanimizga qo'shamiz:
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
# Shu o'rinda Pythonda ro'yxatlar bilan ishlashning qulayliklaridan birini ham ko'rsatib o'tsak. get_students() metodiga e'tibor
# bersangiz, biz yangi ro'yxat shakllantirishda 1 qator koddan foydalandik:
# [talaba.get_info() for talaba in self.talabalar]

# Kodimizni tahlil qilsak, self.talabalar ichidagi har bir talaba uchun get_info() metodini bajar degan ma'no kelib chiqadi. Kodni 
# kvadrat qavslar ichiga olganimiz uchun har bir sikl natijasi avtomatik ravishda ro'yxatga qo'shib boriladi.

# Mana, endi metodga murojaat etib, talabalar haqida ma'lumot olishimiz mumkin:
# mat_talabalar = matematika.get_students()
# print(mat_talabalar)
# Natija: ["Olim Olimov. 1995-yilda tug'ilgan, 29 yoshda. 1-bosqich talabasi.",
          # "Husan Akbarov. 2004-yilda tug'ilgan, 20 yoshda. 1-bosqich talabasi.",
          # "Hasan Akbarov. 2004-yilda tug'ilgan, 20 yoshda. 1-bosqich talabasi."]

# Shunday qilib, ikki bir-biriga bog'liq bo'lmagan obyektlar ustida turli munosabatlar o'rnatishimiz mumkin


# NUQTA YOKI METOD ?
# Pythondagi obyektlarning o'ziga xos xususiyatlarridan biri - obyektning xususiyatiga nuqta orqali to'g'ridan to'g'ri murojaat etish
# mumkin. Misol uchun, avval yaratilgan talaba1 obyektining ismini bilish uchun talaba1.ism deb yozish kifoya.

# Bu ancha qulay bo'lsa-da, mazkur usuldan foydalanishtavsiya etilmaydi. Sababi, vaqt o'tib klassingiz takomillashishi, uning ba'zi
# xususiyatlari o'zgarishi, o'chirilishi yoki almashishi mumkin. Shunday holatlarda nuqta orqali murojaat etish siz kutkan natijani
# bermasligi va dastur xato ishlashiga olib kelishi tabiiy. Bunday holatlarning oldini olish uchun esa obyektning xususiyatlariga
# murojaat etish yoki ularni o'zgartirishni metod orqali  yo'lga qo'yishni odat qilish kerak.

# ETIBOR BERING! Umuman olganda, obyektning xususiyatlariga to'g'ridan to'g'ri murojaat etishni taqiqlash uchun inkapsulyatsiyadan 
# foydalanamiz. Bu haqida kelgusi bo'limda batafsil to'xtalamiz. Bu haqida kelgusi bo'limda batafsil to'xtalamiz.

# Dasturchilar orasida obyektning xususiyatlarini o'zgartiradigan metodlarni set(o'zgartirish) so'zi bilan, xususiyatlarni qaytaradigan
# metodlarni esa get (olish) so'zi bilan boshlash qoida qilib olingan. Masalan: set_name() va get_name() kabi.

# Agar yuqoridagi qoidalarga amal qilgan holda Talaba klassimizni yangilaydigan bo'lsak, u shunday ko'rinishga ega bo'ladi:
# class Talaba:
#     """Talaba nomli klass yaratamiz""" 
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil 
#         self.bosqich = 1
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
#     def update_bosqich(self):
#         """Talabaning bosqichini 1 taga ko'paytirish"""
#         self.bosqich += 1
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
#     def get_name(self):
#         """Talabaning ismini qaytaradi."""
#         return self.ism
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi."""
#         return self.familiya
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi."""
#         return f"{self.ism} {self.familiya}."
#     def get_age(self, jyil):
#         """Talabaning yoshini qaytaruvchi dastur."""
#         return jyil - self.tyil
    
# Xuddi shu kabi, Fan klassimizning yakuniy ko'rinishi quyidagicha bo'ladi:
# class Fan():
#     """Fan nomli klass"""
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabar = []
#     def add_students(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi 
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot."""
#         return [x.get_info() for x in self.talabar]
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni
    
# OBYEKTNING XUSUSIYATLARI VA METODLARINI KO'RISH.
# Obyektlar bilan ishlaganda, o'z-o'zidan, shu obyektga tegishli xususiyatlar va metodlarni bilish talab qilinadi. Agar obyekt tegishli
# bo'lgan klassni o'zimiz yaratgan bo'lsak, istalgan payt klass ichini ko'rib olishimiz mumkin. Lekin klass juda ham uzun bo'lsa yoki
# boshqalar yaratgan klass haqida ma'lumot olish talab qilinsa, buning bir nechta yo'li bor.

# dir() FUNKSIYASI.
# dir() funksiyasi yordamida istalgan obyekt yoki klassning metodlarini ko'rib olishimiz mumkin:
# print(dir(Talaba))
# Natija: ['__class__',
          # '__delattr__',
          # '__dict__',
          # '__dir__',
          # '__doc__',
          # '__eq__',
          # '__format__',
          # '__ge__',
          # '__getattribute__',
          # '__getstate__',
          # '__gt__',
          # '__hash__',
          # '__init__',
          # '__init_subclass__',
          # '__le__',
          # '__lt__',
          # '__module__',
          # '__ne__',
          # '__new__',
          # '__reduce__',
          # '__reduce_ex__',
          # '__repr__',
          # '__setattr__',
          # '__sizeof__',
          # '__str__',
          # '__subclasshook__',
          # '__weakref__',
          # 'get_age',
          # 'get_fullname',
          # 'get_info',
          # 'get_lastname',
          # 'get_name',
          # 'set_bosqich',
          # 'update_bosqich']
          
# Lekin bunda har bir klass bilan keluvchi maxsus DUNDER METODLAR ham chiqib keldi. Dunder metodlar ikki pastki chiziq (__) bilan 
# boshlanadi va maxsus holatlar uchun sqlab qo'yilgan. Biz hozircha faqat __init__ metodi bilan tanishdik, qolganlari bilan keyingi
# darslarimizda yana ko'rishamiz. Dunder metodlardan keyin esa biz murojaat etishimiz mumkin bo'lgan metodlar ro'yxati kelgan.

# Kelin, dunder metodlarni tashlab, bizga kerak metodlarni qaytaruvchi sodda funksiya yozamiz:
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]
# # Funksiya yordamida Talaba klassining metodlarini ko'ramiz:
# print(see_methods(Talaba))
# Natija: ['get_age',
          # 'get_fullname',
          # 'get_info',
          # 'get_lastname',
          # 'get_name',
          # 'set_bosqich',
          # 'update_bosqich']
# Agar dir() funksiyasiga klass emas, obyekt uzatsak, metodlardan tashqari xususiyatlar ham chiqib keladi:
# print(see_methods(talaba1))
# Natija: ['get_age',
          # 'get_fullname',
          # 'get_info',
          # 'get_lastname',
          # 'get_name',
          # 'set_bosqich',
          # 'update_bosqich']

     #    ['bosqich',
     # 'familiya',
     # 'get_info',
     # 'ism',
     # 'set_bosqich',
     # 'tyil',
     # 'update_bosqich']
     
     
# __dict__ METODI.
# Yuqorida zikr qilingan dunder metodlardan biri __dict__ metodi bo'lib, bu metod OBYEKTNING xususiyatlarini lug'at ko'rinishida
# qaytaradi:
# print(talaba1.__dict__)
# Natija: {'ism': 'Olim', 'familiya': 'Olimov', 'tyil': 1995, 'bosqich': 1}

# Natijadan faqatgina kalitlarni ajratib olsak, obyektning xususiyatlari chiqadi:
# print(talaba1.__dict__.keys())
# Natija: dict_keys(['ism', 'familiya', 'tyil', 'bosqich'])

# AMALIYOT TOPSHIRIQLARI.
#1 - Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo)
# qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0).
# class Avto:
#     def __init__(self, model, rang, korobka, narx):
#         self.model = model
#         self.rang = rang
#         self.korobka = korobka
#         self.narx = narx
#         self.km = 0
#     def set_km(self, km):
#         """Avtomobilni km sini yangilaydigan metod"""
#         self.km = km
#     def update_km(self):
#         """Avtomobilni yurgan km sini yangilaydigan metod"""
#         self.km += 10

#2 -  Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing get_info() metodi avti haqida to'liq ma'lumotni matn
# ko'rinishida qaytarsin.       
#     def get_info(self):
#         """Avtomo9billar haqida to'liq ma'lumotni qaytaradi"""
#         return f"{self.model} modelidagi mashina, {self.rang} rangda, korobkasi {self.korobka}, narx {self.narx} va yurgan km si {self.km} km."        
# avto1 = Avto("Jentra", "qora", "avtomat", 15000)
# print(avto1.get_info())
# Natija: Jentra modelidagi mashina, qora rangda, korobkasi avromat, narx 15000 va yurgan km si 0 km.

#3 - Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing. update_km() metodi son qabul qilib olib, avtomobilning
# yurgan kilometrajini yangilab borsin.
# avto1 = Avto("Jentra", "qora", "avtomat", 15000)
# print(avto1.get_info())
# avto1.km = 100
# print(avto1.get_info())
# avto1.update_km()
# print(avto1.get_info())

#4 - Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar
# va hokazo).
# class Avtosalon:
#     def __init__(self, nomi, manzili):
#         self.nomi = nomi
#         self.manzili = manzili
#         self.avtolar_soni = 0
#         self.s_avtomobillar = []
        
#5 - Avtosalonga yangi avtomobillar qo'shish uchun metod yozing.
    # def add_avto(self, avto):
    #     """Salonga avtolar qo'shish uchun metod"""
    #     self.s_avtomobillar.append(avto)
    #     self.avtolar_soni += 1

#6 - Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
    # def get_avtolar(self):
    #    """Salondagi avtomobillar haqida ma'lumot qaytaruvchi metod"""
    #    return [avto.get_info() for avto in self.s_avtomobillar]

#7 - Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring.
# avto1 = Avto("Jenta", "qora", "avtomat", 15000) 
# avto2 = Avto("Malibu", "qora", "mexanika", 33000) 
# avto3 = Avto("Gelenwagen", "oq", "korobka", 400000) 

# avtosalon = Avtosalon("LUX Avtosalon", " Tahskent")
# avtosalon.add_avto(avto1)
# avtosalon.add_avto(avto2)
# avtosalon.add_avto(avto3)
# for avto_info in avtosalon.get_avtolar():
#     print(avto_info)

#7 - dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini
# toping (dir(str), dir(int) va hokazo)
# print("Avtosalon sinfining atributlari va metodlari")
# print(dir(Avtosalon))
# print("\nAvtosalon obyektining holati: (__dict__):")
# print(avtosalon.__dict__)


# 27 - DARS TUGADI.


# 28 - DARS.
# VORISLIK VA POLIMORFIZM.

# Shaxs degan klass yaratamiz.
# class Shaxs:
#     """Shaxslar haqida ma'lumot""" # nomidan ham ko'rinib turibdiki klassimizning vazifasai shaxslar haqidagi ma'lumotlarni shakllantirish
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
        
#     def get_info(self):
#         """Shaxs haqida ma'lumot""" # Shaxs haqidagi jamlangan ma'lumotlarni chiroyli shaklda konsolga chiqaradi.
#         info = f"{self.ism} {self.familiya}."
#         info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan."
#         return info
#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
# inson = Shaxs("Nurulloh", "Abdurashidov", "FB112233", 1999)
# print(inson.get_info())   
# Natija: Nurulloh Abdurashidov.Passport: FB112233, 1999-yilda tug'ilgan.
# print(inson.get_age(2024))
# Natija: 25
# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         """Talabaning xusussiyatlari"""
#         super().__init__(ism, familiya, passport, tyil) # Yuqoridagi super klassdan shu voris klassga yuqoridagi elementlarni olamiz.
#         self.idraqam = idraqam
#         self.bosqich = 1
        
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    
# talaba1 = Talaba("Nurulloh", "Abdurashidov", "FB112233", 1999, "N000001")
# print(talaba1.get_id()) # Talabaning ID raqamini chaqiramiz.
# Natija: Nurulloh Abdurashidov.Passport: FB112233, 1999-yilda tug'ilgan.
# print(talaba1.get_age(2024)) # Bu metod aslida Talaba metodida yo'q lekin yuqoridagi super klassda bor shunchun bemalol bubga murojaat
# qilsak bo'ladi.
# Natija: 25
# print(talaba1.get_info()) # Bu metod ham xuddi shunday aslida Talabada yo'q lekin super-klassdan meros qilib olgan.
# Natija: Nurulloh Abdurashidov.Passport: FB112233, 1999-yilda tug'ilgan.

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
# talaba1 = Talaba("Nurulloh", "Abdurashidov", "AB112233", 1999, "N00001")
# print(talaba1.get_info())
# Natija: Nurulloh Abdurashidov. 1-bosqich. ID raqami: N00001

# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talabaning xusussiyatlari"""
#         super().__init__(ism, familiya, passport, tyil) # Yuqoridagi super klassdan shu voris klassga yuqoridagi elementlarni olamiz.
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
        
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
# class Manzil:
#     """Manzil saqlash uchun klass"""
#     def  __init__(self, uy, kocha, tuman, viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
        
#     def get_manzil(self):
#         """Manzil ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy."
#         return manzil
# talaba1_manzil = Manzil("1/71", "Navroz", "Oltiariq", "Farg'ona")
# talaba1 = Talaba("Nurulloh", "Abdurashidov", "AB112233", 1999, "N00001", talaba1_manzil)
# print(talaba1.manzil.get_manzil())

# AMALIYOT TOPSHIRIQLARI.
#1 - Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh
# ro'yxatdan iborat bo'lsin (self.fanlar=[])
# class Talaba:
#     """Talaba degan klass yaratamiz"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil, fanlar):
#         """Talaba xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#         self.idraqam = idraqam
#         self.manzil = manzil
#         self.fanlar = []
    
#2 - Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
# class Fan:
#     """Fan degan klass yaratamiz"""
#     def __init__(self, nomi, soat, oqituvchi):
#         """Fan xususiyatlari"""
#         self.nomi = nomi
#         self.soat = soat
#         self.oqituvchi = oqituvchi
        
#     def get_fan_info(self):
#         """Fan haqida ma'lumot"""
#         return f"Fan: {self.nomi}, Soatlar: {self.soat}. O'qituvchi: {self.oqituvchi}."
# Turli fanlar uchun obyektlar yaratish.
# matematika = Fan("Oliy Matematika", 48, "Ibrohimov Anvar")
# fizika = Fan("Fizika", 60, "Abdurashidova Mavludaxon")
# informatika = Fan("Informatika", 80, "Abdurashidov Nurulloh")

# Fanlar haqidagi ma'lumotlarni chiqaramiz.
# print(matematika.get_fan_info())
# print(fizika.get_fan_info())
# print(informatika.get_fan_info())

#3 - Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib
# olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
# class Talaba:
#     """Talaba degan klass yaratamiz"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talaba xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#         self.idraqam = idraqam
#         self.manzil = manzil
#         self.fanlar = []  # Bo'sh ro'yxat
    
#     def fanga_yozil(self, fan):
#         """Talabani fanga yozish"""
#         self.fanlar.append(fan)  # Tekshiruvsizlik qo'shish

#     def get_fanlar(self):
#         """Talabaning fanlari haqida ma'lumot"""
#         return [fan.get_fan_info() for fan in self.fanlar]


# class Fan:
#     """Fan degan klass yaratamiz"""
#     def __init__(self, nomi, soat, oqituvchi):
#         """Fan xususiyatlari"""
#         self.nomi = nomi
#         self.soat = soat
#         self.oqituvchi = oqituvchi
        
#     def get_fan_info(self):
#         """Fan haqida ma'lumot"""
#         return f"Fan: {self.nomi}, Soatlar: {self.soat}. O'qituvchi: {self.oqituvchi}."


# Misol
# Fan obyektlari
# fan1 = Fan("Matematika", 60, "Olimov Anvar")
# fan2 = Fan("Fizika", 40, "Karimova Dilnoza")

# Talaba obyekti
# talaba1 = Talaba("Ali", "Valiyev", "AA123456", 2000, 1, "Toshkent")

# Talabani fanga yozamiz
# talaba1.fanga_yozil(fan1)
# talaba1.fanga_yozil(fan2)

# Talabaning fanlari haqida ma'lumot
# print(talaba1.get_fanlar())

#4 - Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan
# uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.
# class Talaba:
#     """Talaba degan klass yaratamiz"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talaba xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#         self.idraqam = idraqam
#         self.manzil = manzil
#         self.fanlar = []  # Bo'sh ro'yxat
    
#     def fanga_yozil(self, fan):
#         """Talabani fanga yozish"""
#         self.fanlar.append(fan)

#     def remove_fan(self, fan):
#         """Talabaning fanlari ro'yxatidan fanni o'chirish"""
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#             return f"{fan.nomi} fani ro'yxatdan o'chirildi."
#         return "Siz bu fanga yozilmagansiz."

#     def get_fanlar(self):
#         """Talabaning fanlari haqida ma'lumot"""
#         return [fan.get_fan_info() for fan in self.fanlar]


# class Fan:
#     """Fan degan klass yaratamiz"""
#     def __init__(self, nomi, soat, oqituvchi):
#         """Fan xususiyatlari"""
#         self.nomi = nomi
#         self.soat = soat
#         self.oqituvchi = oqituvchi
        
#     def get_fan_info(self):
#         """Fan haqida ma'lumot"""
#         return f"Fan: {self.nomi}, Soatlar: {self.soat}. O'qituvchi: {self.oqituvchi}."


# Misol
# Fan obyektlari
# fan1 = Fan("Matematika", 60, "Olimov Anvar")
# fan2 = Fan("Fizika", 40, "Karimova Dilnoza")
# fan3 = Fan("Kimyo", 50, "Rahmonov Shavkat")

# Talaba obyekti
# talaba1 = Talaba("Ali", "Valiyev", "AA123456", 2000, 1, "Toshkent")

# Talabani fanga yozamiz
# talaba1.fanga_yozil(fan1)
# talaba1.fanga_yozil(fan2)

# Talabaning fanlari haqida ma'lumot
# print("Talabaning fanlari:")
# print(talaba1.get_fanlar())

# Fanni ro'yxatdan o'chirish
# print(talaba1.remove_fan(fan2))  # Fizika fani o'chiriladi
# print(talaba1.remove_fan(fan3))  # Kimyo fani mavjud emas

# Yangilangan fanlar ro'yxati
# print("Yangilangan fanlar ro'yxati:")
# print(talaba1.get_fanlar())

#5 - Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)        
# class Shaxs:
#     """Shaxs degan umumiy klass"""
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}, Passport: {self.passport}, Tug'ilgan yil: {self.tyil}"

#     def get_age(self, yil):
#         """Shaxsning yoshini hisoblash"""
#         return yil - self.tyil


# Professor klassi
# class Professor(Shaxs):
#     """Professor klassi"""
#     def __init__(self, ism, familiya, passport, tyil, kafedra):
#         super().__init__(ism, familiya, passport, tyil)
#         self.kafedra = kafedra

#     def get_info(self):
#         """Professor haqida ma'lumot"""
#         return f"{super().get_info()}, Kafedra: {self.kafedra}"


# Foydalanuvchi klassi
# class Foydalanuvchi(Shaxs):
#     """Foydalanuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, username, email):
#         super().__init__(ism, familiya, passport, tyil)
#         self.username = username
#         self.email = email

#     def get_info(self):
#         """Foydalanuvchi haqida ma'lumot"""
#         return f"{super().get_info()}, Username: {self.username}, Email: {self.email}"


# Sotuvchi klassi
# class Sotuvchi(Shaxs):
#     """Sotuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, dokon):
#         super().__init__(ism, familiya, passport, tyil)
#         self.dokon = dokon

#     def get_info(self):
#         """Sotuvchi haqida ma'lumot"""
#         return f"{super().get_info()}, Do'kon: {self.dokon}"


# Mijoz klassi
# class Mijoz(Shaxs):
#     """Mijoz klassi"""
#     def __init__(self, ism, familiya, passport, tyil, manzil, xaridlar_soni):
#         super().__init__(ism, familiya, passport, tyil)
#         self.manzil = manzil
#         self.xaridlar_soni = xaridlar_soni

#     def get_info(self):
#         """Mijoz haqida ma'lumot"""
#         return f"{super().get_info()}, Manzil: {self.manzil}, Xaridlar soni: {self.xaridlar_soni}"


# Misollar
# professor = Professor("Anvar", "Olimov", "AA123456", 1975, "Fizika")
# foydalanuvchi = Foydalanuvchi("Ali", "Valiyev", "BB654321", 1995, "ali123", "ali@mail.com")
# sotuvchi = Sotuvchi("Dilnoza", "Karimova", "CC789101", 1988, "Bozor do'koni")
# mijoz = Mijoz("Murod", "Bekmurodov", "DD543210", 1990, "Toshkent, Chilonzor", 12)

# Ma'lumotlarni chiqarish
# print(professor.get_info())
# print(foydalanuvchi.get_info())
# print(sotuvchi.get_info())
# print(mijoz.get_info())

#6 - Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
# class Shaxs:
#     """Shaxs degan umumiy klass"""
#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"
    
#     def get_age(self, yil):
#         """Shaxsning yoshini hisoblash"""
#         return yil - self.tyil


# Professor klassi
# class Professor(Shaxs):
#     """Professor klassi"""
#     def __init__(self, ism, familiya, passport, tyil, fanlar, daraja):
#         super().__init__(ism, familiya, passport, tyil)
#         self.fanlar = fanlar  # Professor o'qitadigan fanlar ro'yxati
#         self.daraja = daraja  # Professorlik darajasi (PhD, Doktor, va h.k.)
    
#     def get_professor_info(self):
#         """Professor haqida ma'lumot"""
#         fanlar = ", ".join(self.fanlar)
#         return f"{self.get_info()}, Fanlari: {fanlar}, Ilmiy daraja: {self.daraja}"


# Mijoz klassi
# class Mijoz(Shaxs):
#     """Mijoz klassi"""
#     def __init__(self, ism, familiya, passport, tyil, mijoz_id, buyurtmalar):
#         super().__init__(ism, familiya, passport, tyil)
#         self.mijoz_id = mijoz_id  # Mijoz identifikatori
#         self.buyurtmalar = buyurtmalar  # Buyurtmalar ro'yxati
    
#     def add_order(self, buyurtma):
#         """Mijozga yangi buyurtma qo'shish"""
#         self.buyurtmalar.append(buyurtma)
    
#     def get_mijoz_info(self):
#         """Mijoz haqida ma'lumot"""
#         orders = ", ".join(self.buyurtmalar)
#         return f"{self.get_info()}, Mijoz ID: {self.mijoz_id}, Buyurtmalari: {orders}"


# Foydalanuvchi klassi
# class Foydalanuvchi(Shaxs):
#     """Foydalanuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, login, email):
#         super().__init__(ism, familiya, passport, tyil)
#         self.login = login  # Foydalanuvchi login
#         self.email = email  # Foydalanuvchi elektron pochta
    
#     def change_email(self, new_email):
#         """Emailni o'zgartirish"""
#         self.email = new_email
    
#     def get_foydalanuvchi_info(self):
#         """Foydalanuvchi haqida ma'lumot"""
#         return f"{self.get_info()}, Login: {self.login}, Email: {self.email}"


# Sotuvchi klassi
# class Sotuvchi(Shaxs):
#     """Sotuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, dokon_nomi, savdo_hisoboti):
#         super().__init__(ism, familiya, passport, tyil)
#         self.dokon_nomi = dokon_nomi  # Sotuvchining do'koni nomi
#         self.savdo_hisoboti = savdo_hisoboti  # Sotuv hisobotlari ro'yxati
    
#     def add_sale(self, savdo):
#         """Yangi savdo qo'shish"""
#         self.savdo_hisoboti.append(savdo)
    
#     def get_sotuvchi_info(self):
#         """Sotuvchi haqida ma'lumot"""
#         sales = ", ".join(self.savdo_hisoboti)
#         return f"{self.get_info()}, Dokon nomi: {self.dokon_nomi}, Savdo hisobotlari: {sales}"
#7 - Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
# class Shaxs:
#     """Shaxs degan umumiy klass"""
#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida umumiy ma'lumot"""
#         return f"{self.ism} {self.familiya}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Professor klassi
# class Professor(Shaxs):
#     """Professor klassi"""
#     def __init__(self, ism, familiya, passport, tyil, fanlar, daraja):
#         super().__init__(ism, familiya, passport, tyil)
#         self.fanlar = fanlar  # Professor o'qitadigan fanlar ro'yxati
#         self.daraja = daraja  # Professorlik darajasi (PhD, Doktor, va h.k.)
    
#     def get_info(self):
#         """Professor haqida ma'lumot"""
#         fanlar = ", ".join(self.fanlar)
#         return f"Professor: {self.ism} {self.familiya}, Daraja: {self.daraja}, Fanlari: {fanlar}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Mijoz klassi
# class Mijoz(Shaxs):
#     """Mijoz klassi"""
#     def __init__(self, ism, familiya, passport, tyil, mijoz_id, buyurtmalar):
#         super().__init__(ism, familiya, passport, tyil)
#         self.mijoz_id = mijoz_id  # Mijoz identifikatori
#         self.buyurtmalar = buyurtmalar  # Buyurtmalar ro'yxati
    
#     def get_info(self):
#         """Mijoz haqida ma'lumot"""
#         orders = ", ".join(self.buyurtmalar)
#         return f"Mijoz: {self.ism} {self.familiya}, ID: {self.mijoz_id}, Buyurtmalar: {orders}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Foydalanuvchi klassi
# class Foydalanuvchi(Shaxs):
#     """Foydalanuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, login, email):
#         super().__init__(ism, familiya, passport, tyil)
#         self.login = login  # Foydalanuvchi login
#         self.email = email  # Foydalanuvchi elektron pochta
    
#     def get_info(self):
#         """Foydalanuvchi haqida ma'lumot"""
#         return f"Foydalanuvchi: {self.ism} {self.familiya}, Login: {self.login}, Email: {self.email}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Sotuvchi klassi
# class Sotuvchi(Shaxs):
#     """Sotuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, dokon_nomi, savdo_hisoboti):
#         super().__init__(ism, familiya, passport, tyil)
#         self.dokon_nomi = dokon_nomi  # Sotuvchining do'koni nomi
#         self.savdo_hisoboti = savdo_hisoboti  # Sotuv hisobotlari ro'yxati
    
#     def get_info(self):
#         """Sotuvchi haqida ma'lumot"""
#         sales = ", ".join(self.savdo_hisoboti)
#         return f"Sotuvchi: {self.ism} {self.familiya}, Dokon: {self.dokon_nomi}, Savdo hisobotlari: {sales}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"

#8 - Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating. 
# class Admin(Foydalanuvchi):
#     """Admin klassi - Foydalanuvchi klassidan voris"""
#     def __init__(self, ism, familiya, passport, tyil, login, email, admin_huquqlari):
#         """Admin xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil, login, email)
#         self.admin_huquqlari = admin_huquqlari  # Adminning huquqlari ro'yxati
    
#     def add_permission(self, huquq):
#         """Yangi huquq qo'shish"""
#         if huquq not in self.admin_huquqlari:
#             self.admin_huquqlari.append(huquq)
    
#     def remove_permission(self, huquq):
#         """Huquqni olib tashlash"""
#         if huquq in self.admin_huquqlari:
#             self.admin_huquqlari.remove(huquq)
#         else:
#             return "Bunday huquq yo'q."
    
#     def get_permissions(self):
#         """Admin huquqlari ro'yxatini qaytarish"""
#         return f"{self.ism} {self.familiya}ning admin huquqlari: {', '.join(self.admin_huquqlari)}"
    
#     def get_info(self):
#         """Admin haqida ma'lumot"""
#         permissions = ", ".join(self.admin_huquqlari)
#         return f"Admin: {self.ism} {self.familiya}, Login: {self.login}, Email: {self.email}, Huquqlari: {permissions}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Sinov dasturi
# admin = Admin("Anvar", "Valiyev", "EE1234567", 1987, "admin_user", "admin@gmail.com", ["Foydalanuvchilarni boshqarish", "Sahifalarni o'chirish"])
# print(admin.get_info())  # Admin haqida to'liq ma'lumot

# Yangi huquq qo'shish
# admin.add_permission("Hisobotlarni ko'rish")
# print(admin.get_permissions())  # Yangi huquqlar ro'yxati

# Mavjud huquqni olib tashlash
# admin.remove_permission("Sahifalarni o'chirish")
# print(admin.get_permissions())  # Yangilangan huquqlar ro'yxati

# Sinov dasturi
# professor = Professor("Olim", "Qodirov", "AA1234567", 1980, ["Matematika", "Fizika"], "PhD")
# mijoz = Mijoz("Dilnoza", "Karimova", "BB7654321", 1990, "M12345", ["Telefon", "Noutbuk"])
# foydalanuvchi = Foydalanuvchi("Jasur", "Akmalov", "CC4567890", 1995, "jasur_ak", "jasur@gmail.com")
# sotuvchi = Sotuvchi("Salim", "Sobirov", "DD0987654", 1985, "TechStore", ["Telefon: 5 ta", "Kompyuter: 3 ta"])

# Har bir obyekt haqida yangi get_info() metodi orqali ma'lumot
# print(professor.get_info())
# print(mijoz.get_info())
# print(foydalanuvchi.get_info())
# print(sotuvchi.get_info())


# Dastur sinovi
# professor = Professor("Olim", "Qodirov", "AA1234567", 1980, ["Matematika", "Fizika"], "PhD")
# mijoz = Mijoz("Dilnoza", "Karimova", "BB7654321", 1990, "M12345", ["Telefon", "Noutbuk"])
# foydalanuvchi = Foydalanuvchi("Jasur", "Akmalov", "CC4567890", 1995, "jasur_ak", "jasur@gmail.com")
# sotuvchi = Sotuvchi("Salim", "Sobirov", "DD0987654", 1985, "TechStore", ["Telefon: 5 ta", "Kompyuter: 3 ta"])

# Har bir obyekt haqida ma'lumot
# print(professor.get_professor_info())
# print(mijoz.get_mijoz_info())
# print(foydalanuvchi.get_foydalanuvchi_info())
# print(sotuvchi.get_sotuvchi_info())

# Dastur sinovi davomida yangilash
# mijoz.add_order("Televizor")
# foydalanuvchi.change_email("jasur_akmalov@gmail.com")
# sotuvchi.add_sale("Monitor: 2 ta")

# Yangilangan ma'lumotlar
# print(mijoz.get_mijoz_info())
# print(foydalanuvchi.get_foydalanuvchi_info())
# print(sotuvchi.get_sotuvchi_info())

#9 - Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn
# chiqarsin.
# class Admin(Foydalanuvchi):
#     """Admin klassi - Foydalanuvchi klassidan voris"""
#     def __init__(self, ism, familiya, passport, tyil, login, email, admin_huquqlari):
#         """Admin xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil, login, email)
#         self.admin_huquqlari = admin_huquqlari  # Adminning huquqlari ro'yxati
    
#     def add_permission(self, huquq):
#         """Yangi huquq qo'shish"""
#         if huquq not in self.admin_huquqlari:
#             self.admin_huquqlari.append(huquq)
    
#     def remove_permission(self, huquq):
#         """Huquqni olib tashlash"""
#         if huquq in self.admin_huquqlari:
#             self.admin_huquqlari.remove(huquq)
#         else:
#             return "Bunday huquq yo'q."
    
#     def get_permissions(self):
#         """Admin huquqlari ro'yxatini qaytarish"""
#         return f"{self.ism} {self.familiya}ning admin huquqlari: {', '.join(self.admin_huquqlari)}"
    
#     def ban_user(self, foydalanuvchi):
#         """Foydalanuvchini bloklash"""
#         print(f"Foydalanuvchi {foydalanuvchi} bloklandi.")
    
#     def unban_user(self, foydalanuvchi):
#         """Foydalanuvchining blokini yechish"""
#         print(f"Foydalanuvchi {foydalanuvchi} blokdan chiqarildi.")
    
#     def reset_password(self, foydalanuvchi):
#         """Foydalanuvchi parolini qayta o'rnatish"""
#         print(f"Foydalanuvchi {foydalanuvchi} paroli qayta o'rnatildi.")
    
#     def get_info(self):
#         """Admin haqida ma'lumot"""
#         permissions = ", ".join(self.admin_huquqlari)
#         return f"Admin: {self.ism} {self.familiya}, Login: {self.login}, Email: {self.email}, Huquqlari: {permissions}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Sinov dasturi
# admin = Admin("Anvar", "Valiyev", "EE1234567", 1987, "admin_user", "admin@gmail.com", ["Foydalanuvchilarni boshqarish", "Sahifalarni o'chirish"])
# print(admin.get_info())  # Admin haqida to'liq ma'lumot

# Foydalanuvchini bloklash va blokdan chiqarish
# admin.ban_user("Aliyev Zokir")
# admin.unban_user("Aliyev Zokir")

# Foydalanuvchi parolini qayta o'rnatish
# admin.reset_password("Karimov Aziz")
# Natija: Farg'ona viloyati, Oltiariq tumani, Navroz ko'chasi, 1/71-uy.
# 28 - DARS TUGADI.


# 29 - DARS.
# INKAPSULYATSIYA VA KLASSGA OID XUSUSIYAT VA METODLAR.
# from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     def __init__(self, make, model, rang, yil, narx, km=0):
#         """Avtomobillarni xusuiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()

# avto1 = Avto("GM", "Malibu", "qora", 2024, 40000, 1000)
# print(avto1.narx)
# Natija: 40000
# print(avto1.km)
# Natija: AttributeError: 'Avto' object has no attribute 'km'
    # def get_km(self):
    #     return self.__km
    
    # def get_id(self):
    #     return self.__id
# avto1 = Avto("GM", "Malibu", "qora", 2024, 40000, 1000)
# print(avto1.get_km())
# Natija: 1000
# print(avto1.get_id())
# Natija: 7d5053c3-0955-4453-b81a-8081ba52435f
    # def add_km(self, km):
    #     """Mashinaga km qo'shish"""
    #     if km >= 0:
    #         self.__km += km
    #     else:
    #         print("""Mashinanig km sini o'zgartirib bo'lmaydi""")
# avto1 = Avto("GM", "Malibu", "qora", 2024, 40000, 1000)
# print(avto1.get_id())
# print(avto1.get_km())
# Natija: 3275fdfb-8776-471d-8d0f-5ce967e4111e
          #1000
# avto1.add_km(2000) # Km qo'shamiz.
# print(avto1.get_km())
# Natija: 3000
# avto1.add_km(-2000) # Manfiy son yozib ko'ramiz.
# print(avto1.get_km())
# Natija: Mashinanig km sini o'zgartirib bo'lmaydi
          # 3000
          
# from uuid import uuid4
# class Avto:
    # __num_avto = 0 # Bu o'rinda biz num_avto ni inkapsulyatsiya qilib qo'ydik.
    # PI = 14159 # Bu o'rinda konstanta qiymat yaratdik va bu qiymatdan ushbu klassni obyektalari foydalanishi
    # mumkin
    # """Avtomobil klassi"""
#     def __init__(self, make, model, rang, yil, narx, km=0):
#         """Avtomobillarni xusuiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1          
    
#     # Quyidagi metod num_avto inkapsulyatsiya qilingandan keyin uni ko'rish imkonini beradi.
#     @classmethod # Dekarator
#     def get_num_avto(cls): # Obyektni emas klass ni uzatkanimiz uchun cls yozildi qavs ichiga. 
#         return cls.__num_avto 
    
#     def get_km(self):
#          return self.__km
     
#     def get_id(self):
#          return self.__id     
    
#     def add_km(self, km):
#          """Mashinaga km qo'shish"""
#          if km >= 0:
#              self.__km += km
#          else:
#              print("""Mashinanig km sini o'zgartirib bo'lmaydi""")
# avto1 = Avto("Chevrolet", "Subaru", "Sariq", 2024, 70000)
# avto2 = Avto("Dodge", "Chalenger", "Qora", 2022, 55000)
# avto3 = Avto("GM", "Malibu", "Qora", 2023, 35000)
# Endi istalgan obyekt orqali yuqoridagi num_avtoga murojaat qilishimiz mumkin.
# print(avto1.num_avto)
# Natija: 3 # Yani Avto degan klassimizdan 3ta obyekt yaratildi degan ma'noda. Bu metod dastur ishga tushgandan 
# beri nechta foydalanuvchi yokida mashina ro'yxatdan o'tdi shuni nazorat qilib borish mumkin.

# num_avto inkapsulyatsiya bo'lgandan keyingi (__num_avto) holat.
# print(avto1.__num_avto)
# Natija: AttributeError: type object 'Avto' has no attribute 'num_avto'

# Endi yuqorida inkapsulyatsiya amallari bajarilgani uchun, num_avto ko'rish uchun quyidagicha yo'l tutamiz:
# print(Avto.get_num_avto())
# Natija: 3 # Bu o'rinda 3 klassdan foydalanishlar sonini ko'rsatadi.

# Bu o'rinda biz num_avto metodiga obyekt orqali murojaat qilsak ham bo'ladi.
# print(avto1.get_num_avto())
# Natija: 3

# Endi biz bu klasslarni modullarga ajratishni ko'rib chiqamiz. Yuqorida yozilgan klasslarni endi alohida 
# faylga joylaymiz va dasturimizni bemalol yangi va bo'sh muhitda yozib boramiz. 

# Biz endi yangi muhitda ishlay turib bu muhitga yaratilgan faylni import qilib olishimiz kerak bo'ladi.
# import avto
# avto1 = Avto("Chevrolet", "Subaru", "Sariq", 2024, 70000)
# avto2 = Avto("Dodge", "Chalenger", "Qora", 2022, 55000)
# avto3 = Avto("GM", "Malibu", "Qora", 2023, 35000)

# AMALIYOT TOPSHIRIQLARI.
#1 - Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing va ularning
# qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
# class Shaxs:
    
#     """Shaxslar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif
    
#     def __init__(self, ism, familiya, passport, tyil):
#         # Shaxsni yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         self.ism = ism  # Shaxsning ismi (ochiq xususiyat)
#         self.familiya = familiya  # Shaxsning familiyasi (ochiq xususiyat)
#         self.__passport = passport  # Shaxsning pasport raqami (yopiq xususiyat)
#         self.tyil = tyil  # Shaxsning tug'ilgan yili (ochiq xususiyat)
        
#     def get_info(self):
#         """Shaxs haqida umumiy ma'lumot qaytaruvchi metod"""
#         info = f"{self.ism} {self.familiya}."  # Ism va familiya
#         info += f" Passport: {self.__passport}, {self.tyil}-yilda tug'ilgan."  # Pasport va tug'ilgan yil haqida ma'lumot
#         return info  # To'plangan ma'lumotni qaytaradi

#     def get_age(self, yil):
#         """Shaxsning yoshini hisoblab qaytaruvchi metod"""
#         return yil - self.tyil  # Joriy yil va tug'ilgan yil farqini qaytaradi

#     # Passport uchun getter va setter metodlar
#     def get_passport(self):
#         """Yopiq pasport qiymatini qaytaruvchi metod"""
#         return self.__passport
    
#     def set_passport(self, yangi_passport):
#         """Pasport qiymatini yangilovchi metod"""
#         self.__passport = yangi_passport


# class Talaba(Shaxs):
    
#     """Talabalar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif

#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         # Talabani yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         super().__init__(ism, familiya, passport, tyil)  # Superklassning atributlarini chaqirish
#         self.__idraqam = idraqam  # Talabaning ID raqami (yopiq xususiyat)
#         self.bosqich = 1  # Talabaning o'qish bosqichi (ochiq xususiyat)
        
    
#     def get_id_raqam(self):
#         """"""

#     def set_id(self, yangi_idraqam):
#         """ID raqam qiymatini yangilovchi metod"""
#         self.__idraqam = yangi_idraqam

#     def get_bosqich(self):
#         """O'qish bosqichini qaytaruvchi metod"""
#         return self.bosqich

#2 - Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
# class Shaxs:
#     odamlar_soni = 0
#     """Shaxslar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif
    
#     def __init__(self, ism, familiya, passport, tyil):
#         # Shaxsni yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         self.ism = ism  # Shaxsning ismi (ochiq xususiyat)
#         self.familiya = familiya  # Shaxsning familiyasi (ochiq xususiyat)
#         self.__passport = passport  # Shaxsning pasport raqami (yopiq xususiyat)
#         self.tyil = tyil  # Shaxsning tug'ilgan yili (ochiq xususiyat)
#         Shaxs.odamlar_soni += 1
#     def get_info(self):
#         """Shaxs haqida umumiy ma'lumot qaytaruvchi metod"""
#         info = f"{self.ism} {self.familiya}."  # Ism va familiya
#         info += f" Passport: {self.__passport}, {self.tyil}-yilda tug'ilgan."  # Pasport va tug'ilgan yil haqida ma'lumot
#         return info  # To'plangan ma'lumotni qaytaradi

#     def get_age(self, yil):
#         """Shaxsning yoshini hisoblab qaytaruvchi metod"""
#         return yil - self.tyil  # Joriy yil va tug'ilgan yil farqini qaytaradi

#     # Passport uchun getter va setter metodlar
#     def get_passport(self):
#         """Yopiq pasport qiymatini qaytaruvchi metod"""
#         return self.__passport
    
#     def set_passport(self, yangi_passport):
#         """Pasport qiymatini yangilovchi metod"""
#         self.__passport = yangi_passport
        
    
    
        
# class Talaba(Shaxs):
#     talabalar_soni = 0
#     """Talabalar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif

#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         # Talabani yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         super().__init__(ism, familiya, passport, tyil)  # Superklassning atributlarini chaqirish
#         self.__idraqam = idraqam  # Talabaning ID raqami (yopiq xususiyat)
#         self.bosqich = 1  # Talabaning o'qish bosqichi (ochiq xususiyat)
#         Talaba.talabalar_soni += 1
    
#     def get_id_raqam(self):
#         """"""

#     def set_id(self, yangi_idraqam):
#         """ID raqam qiymatini yangilovchi metod"""
#         self.__idraqam = yangi_idraqam

#     def get_bosqich(self):
#         """O'qish bosqichini qaytaruvchi metod"""
#         return self.bosqich
    
    
#3 - Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing 
# class Shaxs:
#     odamlar_soni = 0
#     """Shaxslar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif
    
#     def __init__(self, ism, familiya, passport, tyil):
#         # Shaxsni yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         self.ism = ism  # Shaxsning ismi (ochiq xususiyat)
#         self.familiya = familiya  # Shaxsning familiyasi (ochiq xususiyat)
#         self.__passport = passport  # Shaxsning pasport raqami (yopiq xususiyat)
#         self.tyil = tyil  # Shaxsning tug'ilgan yili (ochiq xususiyat)
#         Shaxs.odamlar_soni += 1
#     def get_info(self):
#         """Shaxs haqida umumiy ma'lumot qaytaruvchi metod"""
#         info = f"{self.ism} {self.familiya}."  # Ism va familiya
#         info += f" Passport: {self.__passport}, {self.tyil}-yilda tug'ilgan."  # Pasport va tug'ilgan yil haqida ma'lumot
#         return info  # To'plangan ma'lumotni qaytaradi

#     def get_age(self, yil):
#         """Shaxsning yoshini hisoblab qaytaruvchi metod"""
#         return yil - self.tyil  # Joriy yil va tug'ilgan yil farqini qaytaradi

#     # Passport uchun getter va setter metodlar
#     def get_passport(self):
#         """Yopiq pasport qiymatini qaytaruvchi metod"""
#         return self.__passport
    
#     def set_passport(self, yangi_passport):
#         """Pasport qiymatini yangilovchi metod"""
#         self.__passport = yangi_passport
        
#     @classmethod
#     def get_odamlar_soni(cls):
#         """Hozirgi vaqtda yaratilgan shaxslar sonini qaytaradi"""
#         return cls.odamlar_soni

#     # Klassga oid xususiyatni o'zgartiruvchi metod
#     @classmethod
#     def reset_odamlar_soni(cls):
#         """Shaxslar sonini noldan boshlash"""
#         cls.odamlar_soni = 0
        
# class Talaba(Shaxs):
#     talabalar_soni = 0
#     """Talabalar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif

#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         # Talabani yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         super().__init__(ism, familiya, passport, tyil)  # Superklassning atributlarini chaqirish
#         self.__idraqam = idraqam  # Talabaning ID raqami (yopiq xususiyat)
#         self.bosqich = 1  # Talabaning o'qish bosqichi (ochiq xususiyat)
#         Talaba.talabalar_soni += 1
    
#     def get_id_raqam(self):
#         """"""

#     def set_id(self, yangi_idraqam):
#         """ID raqam qiymatini yangilovchi metod"""
#         self.__idraqam = yangi_idraqam

#     def get_bosqich(self):
#         """O'qish bosqichini qaytaruvchi metod"""
#         return self.bosqich
    
#     @classmethod
#     def get_talabalar_soni(cls):
#         """Hozirgi vaqtda yaratilgan talabalar sonini qaytaradi"""
#         return cls.talabalar_soni

#     # Klassga oid xususiyatni o'zgartiruvchi metod
#     @classmethod
#     def reset_talabalar_soni(cls):
#         """Talabalar sonini noldan boshlash"""
#         cls.talabalar_soni = 0

# 29 - DARS TUGADI.


# 30 - DARS.
# DUNDER METODLAR.

# Bu metodlarni muisollar orqali ko'rib chiqamiz.
# class Avto:
#     __num_avto = 0
#     """Avto nomli klass"""
#     def __init__(self, make, model, rang, yil, narx, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model 
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         Avto.__num_avto += 1
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 40000, 1000)
# print(avto1)
# # Natija: <__main__.Avto object at 0x0000013267839430>

    # def __str__(self):
    #     return f"Avto: {self.make} {self.model}"

    # def __repr__(self):
    #     return f"Avto: {self.make} {self.model}"
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 40000, 1000)
# print(avto1)    
# Natija: Avto: GM Malibu.

# repr(avto1)
# Natija: Avto: GM Malibu

# Asosiy matn bilan ishlaydigan Dunder metodlar bilan tanishdik.

# Endi taqqoslash metodlari bilan tanishamiz.
# x.__lt__(self, y) = (x < y)
# x.__le__(self, y) = (x <= y)
# x.__gt__(self, y) = (x > y)
# x.__ge__(self, y) = (x >= y)
# x.__eq__(self, y) = (x == y)
# x.__ne__(self, y) = (x != y)

    # def __eq__(self, y):
    #     return self.narx == y.narx
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# print(avto1 == avto2)
# print(avto1 < avto2)
# Natija: False # Yuqorida funksiya yozganimiz uchun osongina ikki avto narxlari teng ekanini tekshirib olyabmz.
# Natija: TypeError: '<' not supported between instances of 'Avto' and 'Avto'

# Endi ikki avtolarning narxlari kicik yoki katta ekanini tekshiramiz.
    # def __lt__(self, y):
    #     return self.narx < y.narx
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# print(avto1 > avto2)
# print(avto1 < avto2)
# print(avto1 <= avto2)
# Natija: False
# Natija: True
# Natija: TypeError: '<=' not supported between instances of 'Avto' and 'Avto'
    # def __le__(self, y):
    #     return self.narx <= y.narx
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# print(avto1 <= avto2)
# print(avto1 <= avto2)
# Natija: True
# Natija: False

# Endi biz metodlarni uzunligini ko'rishni uchun nima qilishimizni ko'rib chiqamiz.
# class Avtosalon:
#     """Avtosalon klassi"""
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []
   
#     def __repr__(self):
#         return f"{self.name} avtosalon"

# salon1 = Avtosalon("MaxAvto")

# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)

# print(salon1)
# Natija: MaxAvto avtosalon\
    
# Shu o'rinda isinstance funksiyasi bilan tanishamiz. Bu funksiya ma'lum bir obyekt u yoki bu klassga tegishlimi yoki yo'q shuni aniqlab
# beradi.
# print(isinstance(4, int))
# Natija: True
    # def add_avto(self, * qiymat):
    #     for avto in qiymat:
    #         if isinstance(avto, Avto):
    #             self.avtolar.append(avto)
    #         else:
    #             print("Avto klassiga oid avto kiriting")
# Bu funksiya bilan tanishishimizdan maqsad yuqoridagi avtolar = [] ro'yxatimizga faqat Avto (va o'rniga boshqa klasslarni ham yozishimiz
# mumkin) klassiga tegishli avtolarni qo'shishga ruxsat beramiz holos.
# salon1 = Avtosalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.append(avto1, avto2, avto3)
    # def __getitem__(self, index):
    #     return self.avtolar[index]
    
# salon1 = Avtosalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)
# print(salon1[1])
# print(salon1[:])
# Natija: Avto: BMW M5
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]
# salon1[0] = Avto("Mercedes Benz", "S-klass", "Qora", 2024, 200000)
# Natija: TypeError: 'Avtosalon' object does not support item assignment

    # def __setitem__(self, index, qiymat):
    #    self.avtolar[index] = qiymat

# salon1 = Avtosalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)
# salon1[0] = Avto("Mercedes Benz", "S-klass", "Qora", 2024, 200000)
# print(salon1[0])
# Natija: Avto: Mercedes Benz S-klass

# salon1()
# Natija: TypeError: 'Avtosalon' object is not callable

# Endi shu xatoni bartaraf etishni ko'rib chiqamiz. Buning uchun:
    # def __call__(self):
    #     return [avto for avto in self.avtolar]
# Kerakli metodni yozib oldik va endi salon1 chaqirsak bo'ladi.
# salon1 = Avtosalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)    

# print(salon1())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]

# Bu __call__ metodiga biz istalgancha shart berishimiz mumkin va hozir bu metodga murojaat qilganimizda berilgan qiymatlarimiz
# chaqirilgan metodga qo'shilsin deb shart yozamiz: 
    # def __call__(self, * qiymat): # Biz call metodi orqali istalgancha metod chaqirsa bo'ladigan qilib qo'ydik. 
    #     if qiymat:
    #         for avto in qiymat:
    #             self.add_avto(avto)
    #     else:
    #         return [avto for avto in self.avtolar]

# salon1 = Avtosalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)  

# avto4 = Avto("Mazda", "6", "Qizil", 2016, 25000)
# avto5 = Avto("Volkswagen", "Polo", "Oq", 2020, 18000)
# avto6 = Avto("Honda", "Accord", "Qora", 2018, 22000)
# print(salon1[:])
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]

# salon1(avto4, avto5)
# print(salon1[:])
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra, Avto: Mazda 6, Avto: Volkswagen Polo] # Mana yana 2ta mashina qo'shdik.
# salon1(avto6)
# print(salon1[:])
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra, Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord] # + yana 1ta mashina.
# salon1() # Klassimizni chaqirish uchun shu usulni qo'llash to'g'riroq bo'ladi.
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra, Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord]

# OPERATOR OVERLOADING.
# x, y = 5, 10

# print(x + y)
# Natija: 15
# print(x * 5)
# Natija: 25
# Yoki matnlar bilan har hil amallar.
# s1 = "Assalomu "
# s2 = "Aleykum"

# print(s1 + s2)
# Natija: Assalomu Aleykum
# print(s1 * 5)
# Natija: Assalomu Assalomu Assalomu Assalomu Assalomu 

# Shunga o'xshash. Va endi shu amallar aslida qanday ishlaydi shularni ko'rib chiqamiz.
# salon1 = Avtosalon("MaxAvto")
# salon2 = Avtosalon("LuxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)  

# avto4 = Avto("Mazda", "6", "Qizil", 2016, 25000)
# avto5 = Avto("Volkswagen", "Polo", "Oq", 2020, 18000)
# avto6 = Avto("Honda", "Accord", "Qora", 2018, 22000)
# salon2(avto4, avto5, avto6)
# print(salon1)
# Natija: MaxAvto avtosalon
# print(salon1())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]
# print(salon2)
# Natija: LuxAvto avtosalon
# print(salon2())
# Natija: [Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord]

# Endi biz bu ikki avtosalonni bir biriga qo'shib beradigan metod yozamiz (nomini, ichidagi avtomobillarni). Buning uchun maxsus
# metodlar bor avval ular bilan tanishamiz so'ngra metod yozamiz:
# __add__ - Qo'shish uchun 
# __sub__ - Ayirish uchun
# __mul__ - Ko'paytirish uchun
# __pow__ - Darajaga oshirish uchun
# __div__ - Bo'lish uchun

# Deamak endi biz metod yozishni boshlaymiz.
# class Avto:
#     __num_avto = 0
#     def __init__(self, make, model, rang, yil, narx, km=0):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         Avto.__num_avto += 1

#     def __str__(self):
#         return f"Avto: {self.make} {self.model}"

#     def __repr__(self):
#         return f"Avto: {self.make} {self.model}"

#     def __eq__(self, y):
#         return self.narx == y.narx

#     def __lt__(self, y):
#         return self.narx < y.narx

#     def __le__(self, y):
#         return self.narx <= y.narx


# class Avtosalon:
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosalon"

#     def add_avto(self, *qiymat):
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto klassiga oid avto kiriting")

#     def __getitem__(self, index):
#         return self.avtolar[index]

#     def __setitem__(self, index, qiymat):
#         self.avtolar[index] = qiymat

#     def __call__(self, *qiymat):
#         if qiymat:
#             for avto in qiymat:
#                 self.add_avto(avto)
#         else:
#             return [avto for avto in self.avtolar]

    # def __add__(self, boshqa_salon):
    #     if isinstance(boshqa_salon, Avtosalon):
    #         yangi_salon = Avtosalon(f"{self.name} {boshqa_salon.name}")
    #         yangi_salon.avtolar = self.avtolar + boshqa_salon.avtolar
    #         return yangi_salon


# salon1 = Avtosalon("MaxAvto")
# salon2 = Avtosalon("LuxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)

# avto4 = Avto("Mazda", "6", "Qizil", 2016, 25000)
# avto5 = Avto("Volkswagen", "Polo", "Oq", 2020, 18000)
# avto6 = Avto("Honda", "Accord", "Qora", 2018, 22000)
# salon2(avto4, avto5, avto6)

# Endi biz bu ikki salonni bir-biriga qo'shamiz:
# print(salon1())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]
# print(salon2())
# Natija: [Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord]

# salon3 = salon1 + salon2
# print(salon3())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra, Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord]    
# print(salon3.name)
# Natija: MaxAvto LuxAvto

# Endi keling biz yana shart qo'shaylik.
#     def __add__(self, y):
#         if isinstance(y, Avtosalon):
#            yangi_salon = Avtosalon(f"{self.name} {y.name}")
#            yangi_salon.avtolar = self.avtolar + y.avtolar
#            return yangi_salon
#         elif isinstance(y, Avto):
#            self.add_avto(y)

# salon1 = Avtosalon("MaxAvto")
# salon2 = Avtosalon("LuxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)

# avto4 = Avto("Mazda", "6", "Qizil", 2016, 25000)
# avto5 = Avto("Volkswagen", "Polo", "Oq", 2020, 18000)
# avto6 = Avto("Honda", "Accord", "Qora", 2018, 22000)
# salon2(avto4, avto5, avto6)

# print(salon1)
# Natija: MaxAvto avtosalon
# print(salon1())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]
# print(avto4)
# Natija: Avto: Mazda 6
# salon1 + avto4
# print(salon1())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra, Avto: Mazda 6]

# Demak shunday usullar orqali o'zingizni obyektingizga qo'shimcha imkoniyatlar qo'shsangiz bo'ladi.

# AMALIYOT TOPSHIRIQLARI:
#1 - Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling. 

# Obyekt haqida ma'lumot (__rerp__)

# Talabalarni bosqichi bo'yicha solishtirish (__lt__,__eg__ va hokazo)
# class Shaxs:
#     """Shaxs degan klass yaratamiz"""
#     def __init__(self, ism, familiya, passport, email):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.email = email
#     def __repr__(self):
#         return f"{self.ism} {self.familiya}, {self.passport} {self.email}"
        
# shaxs1 = Shaxs("Nurulloh", "Abdurashidov", "AA002211", "nur2012@mail.ru")
# print(shaxs1)

# class Talaba:
#     def __init__(self, ism, familiya,idraqam):
#         self.ism = ism 
#         self.familiya = familiya
#         self.idraqam = idraqam
#     def __lt__(self, y):
#         return self.idraqam < y.idraqam

        
# talaba1 = Talaba("Nurulloh", "Abdurashidov", 123336)
# talaba2 = Talaba("Mavluda", "Abdurashidova", 15685)
# print(talaba1 > talaba2)
# print(talaba1 < talaba2)



#2 - Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga
# add_student(), __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.
# class Talaba:
#     def __init__(self, ism, familiya, idraqam):
#         self.ism = ism  # Talabaning ismini saqlash.
#         self.familiya = familiya  # Talabaning familiyasini saqlash.
#         self.idraqam = idraqam  # Talabaning ID raqamini saqlash.

#     def __repr__(self):
#         return f"{self.ism} {self.familiya} ({self.idraqam})"  # Talabaning matnli ko'rinishini qaytaradi.


# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi  # Fanning nomini saqlash.
#         self.talabalar = []  # Talabalar ro'yxatini bo'sh holda yaratish.

#     def add_student(self, talaba):
#         """Yangi talaba qo'shish."""
#         if isinstance(talaba, Talaba):  # Talaba obyektini tekshirish.
#             self.talabalar.append(talaba)  # Talabalar ro'yxatiga qo'shish.
#         else:
#             raise ValueError("Faqat Talaba obyekti qo'shilishi mumkin!")  # Noto'g'ri obyekt bo'lsa, xato chiqarish.

#     def __getitem__(self, index):
#         """Index orqali talabani olish."""
#         return self.talabalar[index]  # Berilgan indeksdagi talabani qaytaradi.

#     def __setitem__(self, index, talaba):
#         """Index orqali talabani o'zgartirish."""
#         if isinstance(talaba, Talaba):  # Talaba obyektini tekshirish.
#             self.talabalar[index] = talaba  # Berilgan indeksdagi talabani almashtirish.
#         else:
#             raise ValueError("Faqat Talaba obyekti qo'shilishi mumkin!")  # Noto'g'ri obyekt bo'lsa, xato chiqarish.

#     def __len__(self):
#         """Talabalar ro'yxatining uzunligini aniqlash."""
#         return len(self.talabalar)  # Talabalar ro'yxatidagi talabalar sonini qaytarish.

#     def __add__(self, talaba):
#         """+ operatori orqali talaba qo'shish."""
#         if isinstance(talaba, Talaba):  # Talaba obyektini tekshirish.
#             yangi_fan = Fan(self.nomi)  # Yangi fan obyektini yaratish.
#             yangi_fan.talabalar = self.talabalar + [talaba]  # Talabalar ro'yxatiga yangi talabani qo'shish.
#             return yangi_fan  # Yangi fan obyektini qaytarish.
#         else:
#             raise ValueError("Faqat Talaba obyekti qo'shilishi mumkin!")  # Noto'g'ri obyekt bo'lsa, xato chiqarish.

#     def __sub__(self, talaba_id):
#         """- operatori orqali talaba olib tashlash."""
#         yangi_fan = Fan(self.nomi)  # Yangi fan obyektini yaratish.
#         yangi_fan.talabalar = [talaba for talaba in self.talabalar if talaba.idraqam != talaba_id]  
#         # Talabalar ro'yxatidan berilgan IDga ega talabani olib tashlash.
#         return yangi_fan  # Yangi fan obyektini qaytarish.

#     def __call__(self, talaba=None):
#         """Fanni chaqiriladigan qilish."""
#         if talaba:  # Agar talaba berilgan bo'lsa.
#             self.add_student(talaba)  # Talabani qo'shadi.
#         else:
#             return self.talabalar  # Aks holda talabalar ro'yxatini qaytaradi.

#     def __repr__(self):
#         """Fanni va ro'yxatdagi talabalarni ko'rsatish."""
#         talabalar_ro_yxati = ", ".join([str(t) for t in self.talabalar])  # Talabalar ro'yxatini matnli formatda tuzish.
#         return f"{self.nomi} fani: [{talabalar_ro_yxati}]"  # Fanning nomi va talabalar ro'yxatini qaytarish.


# Misol uchun ishlatish
# fan = Fan("Matematika")  # "Matematika" nomli fan obyektini yaratish.

# talaba1 = Talaba("Nurulloh", "Abdurashidov", 123336)  # 1-talaba obyekti.
# talaba2 = Talaba("Mavluda", "Abdurashidova", 15685)  # 2-talaba obyekti.
# talaba3 = Talaba("Jasur", "To'raev", 987654)  # 3-talaba obyekti.

# Talabalarni qo'shish
# fan.add_student(talaba1)  # "Nurulloh Abdurashidov"ni ro'yxatga qo'shish.
# fan.add_student(talaba2)  # "Mavluda Abdurashidova"ni ro'yxatga qo'shish.
# fan.add_student(talaba3)  # "Jasur To'raev"ni ro'yxatga qo'shish.

# + operatori orqali talaba qo'shish
# talaba4 = Talaba("Shaxzod", "Nazarov", 54321)  # Yangi talaba.
# fan = fan + talaba4  # "Shaxzod Nazarov"ni ro'yxatga qo'shish.

# - operatori orqali talaba olib tashlash
# fan = fan - 15685  # ID raqami 15685 bo'lgan talabani olib tashlash.

# __call__ orqali fanni chaqirish va talaba qo'shish
# talaba5 = Talaba("Aziz", "Karimov", 112233)  # Yangi talaba.
# fan(talaba5)  # "Aziz Karimov"ni ro'yxatga qo'shish.

# Talabalarni ko'rish
# print(fan())  # Fanga qo'shilgan barcha talabalar ro'yxatini chiqaradi.
# print(fan)  # Fanning nomi va talabalar ro'yxatini chiqaradi.

# 30 - DARS TUGADI.


# 31 - DARS.
# FAYLLAR.
# Faylni ochish va o'qish
# with open(r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\test.txt') as file:
#     pi = file.read()  # Fayl ichidagi barcha matnni o'qib, `pi` o'zgaruvchisiga saqlash

# Fayldan o'qilgan matnni konsolga chiqarish
# print(pi)

# Matn oxiridagi bo'sh joylar va yangi qator belgilarini olib tashlash
# pi = pi.rstrip()

# Matndagi barcha yangi qator (`\n`) belgilarini olib tashlash
# pi = pi.replace('\n', '')

# Matnni float turiga o'zgartirish
# pi = float(pi)

# Float qiymatni konsolga chiqarish
# print(pi)

# Endi boshqa fayl misolida ko'ramiz:
# filename = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\talabalar.txt'
# with open(filename) as file:  # `filename` o'zgaruvchisida ko'rsatilgan faylni ochadi
#     for line in file:  # Fayldagi har bir qatorni ketma-ket ko'rib chiqadi
#         print(line)  # Har bir qatorni ekranga chiqaradi

# Endi bu talabalarni ismlarini har birini bittadan obyekt sifatida saqlashni ko'rib chiqamiz:
# with open(filename) as file:  # `filename` o'zgaruvchisida ko'rsatilgan faylni ochadi
#     talabalar = file.readlines()  # Fayldagi barcha qatorlarni ro'yxat (list) sifatida o'qiydi

# O'qilgan qatorlar ro'yxatini konsolga chiqarish
# print(talabalar)  # `talabalar` ro'yxatini ekranga chiqaradi

# Keling endi talaba ma'lumotlari ohiridagi \n belgisini olib tashlashni ko'rib chiqamiz:
# talabalar = [talaba.rstrip() for talaba in talabalar]

# print(talabalar)

# Biz yuqorida faqat fayllarni o'qishni ko'rdik, endi ularga yozishni ko'rib chiqamiz.
# faylnomi = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\new_file.txt'
# ism = "Nurulloh"
# tyil = 1999
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism + '\n')
#     fayl.write(str(tyil) + '\n')
# print(faylnomi)
# Yuqoridagi usul orqali fayldagi eski ma'lumotlar o'chirilib ustidan yangi ma'lumotlar yoziladi, buni oldini olish uchun quyidagicha yo'l
# tutamiz:
# faylnomi = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\new_file.txt'

# with open(faylnomi, 'a') as fayl:
#     fayl.write("Anvarov" + "\n")
#     fayl.write("2004" + "\n")
    
# Biz matnlarni fayllarga saqladik, endi fayllarga lug'atlar va o'zgaruvchilar saqlashni ko'rib o'tamiz.
# import pickle # Bu usulda yaratilgan fayllar faqatgina Pythonning o'zida ochish mumkin bo'ladi boshqa hech qanday usul bilan ochib
# bo'lmaydi.

# talaba1 = {"ism":"Hasan", "familiya":"Husanov", "tyil":2003, "kurs":2}
# talaba2 = {"ism":"Alijon", "familiya":"Valiyev", "tyil":2004, "kurs":1}

# with open('info', 'wb') as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)
    
# Faylimizni tayorlab oldik keling endi uni o'qishga harakat qilamiz:
# import pickle

# with open('info', 'rb') as file:
#     talaba1 = pickle.load(file)
#     talaba1 = pickle.load(file)

# print(talaba1)
# print(talaba2)

# AMALIYOT TOPSHIRIQLARI:
#1 - Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching.
# import pickle  # pickle moduli import qilinmoqda, lekin hozircha bu kodda ishlatilmayapti

# Fayl manzilini belgilash
# filename = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\topshiriq1.txt'

# Faylni ochish va uning ichidagi qatorlarni o'qish
# with open(filename) as file:  # Faylni ochadi. "with" konstruktsiyasi faylni ishlatib bo'lgandan keyin yopishni ta'minlaydi.
#     for line in file:  # Fayldagi har bir qatorni ketma-ket ko'rib chiqadi
#         print(line)  # O'qilgan qatorni ekranga chiqaradi

#2 - Quyidagi pi_million_digits.txt faylini yuklab oling (faylda π  soni nuqtadan so'ng million xona aniqlik bilan yozilgan). 
# Sizning tug'ilgan kuningiz π soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz
# 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.
# import pickle
# pitop = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\pi_million_digits.txt'
# with open(pitop) as file:
#     pi = file.read()
# pi = pi.rstrip()
# pi = pi.replace('\n', '')
# pi = pi.replace(' ', '')

# bdate = '16031999' or '03161999' or '19991603'
# # print(pi)
# print(bdate in pi)

# #4 - Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.
# pi = float(pi)
# print(pi)

# with open('pi','wb') as file:
#     pickle.dump(pi,file)

# 31 - DARS TUGADI.


# 32 - DARS.
# JSON.

# Boshlamishiga google maps bilan ishlab ko'ramiz.
# import json
# import googlemaps
# from apikey import APIKEY

# ## GoogleMaps
# gmaps = googlemaps.Client(key = APIKEY)

# data = gmaps.geocode('Oltiariq, Farg\'ona, Uzbekistan')

# # print(geocode_result)

# g = json.dumps(data[0], indent = 4, sort_keys = True)
# print(g)  

# import json
# x = 10
# x_json = json.dumps(x)
# print(x)
# print(x_json)

# y = 5.5
# y_json = json.dumps(y)
# print(y)
# print(y_json)

# JSON ni ishlatkanimizda yani ma'lumotlarni JSON ga olib o'tkanimizda, ma'lumotlar avval
# JavaScript so'ngra sting ga o'tkaziladi:
# m = True
# print(m)
# Natija: True
# m_json = json.dumps(m)
# print(m_json)
# Natija: true

# Yana bir misol ko'ramiz:
# sonlar = (1,2,3,4,5)
# print(sonlar)
# Natija: (1, 2, 3, 4, 5)
# sonlar_json = json.dumps(sonlar)
# print(sonlar_json)
# Natija: [1, 2, 3, 4, 5]

# Ko'rib turganingizdek bizdagi tuple ro'yxati to'rtburchak qavsli [] oddiy ro'yxatga o'zgarib
# qoldi. Buning sababi shundaki JavaScript da Pythondagi tuple ro'yxatlar maxsus ARRAY degan 
# ma'lumot turiga o'tkaziladi.

# Keling Pythondagi ma'lumot turlari JavaScript da qanday ma'lumot turiga o'zgarishini ko'ramiz:
    # dict -> Object
    # list -> Array 
    # tuple -> Array
    # str -> String
    # int -> Number
    # float -> Number
    # True -> true
    # False -> false
    # None -> null
# Demak ma'lumot turlari shu ko'rinishda o'zgarar ekan.

# Keling endi bu ma'lumot turlarini yana qaytadan Pythonga o'tkazamiz:
# print(json.loads(m_json))
# Yuqorida mantiqiy qiymat o'z holatiga qaytdi keling endi ro'yxatimizni ham o'z holiga
# qaytaramiz:
# print(json.loads(sonlar_json))

# Endi bu yerda ro'yxatimiz oddiy ro'yxatligicha qoldi buning sababi ro'yxatimiz JavaScriptga
# o'tkanidan keyin Array ma'lumot turiga o'tkazilgan edi. Python bu ma'lumot turini aniq turini 
# bilmagani uchun uni oddiy ro'yxat ko'rinishida qabul qildi.

# Bu holatda albatta sonlar_json string ko'rinishida saqlandi va biz uni elamentlarini
# ko'ramiz desak bunday qila olmaymiz:
# print(sonlar_json[0])
# Natija: [ 
# Yani bu str turiga mansub bo'lgani uchun ro'yxatning har bir elamentini alohida db yuritadi.

# Keling endi json ekranga chiqaradigan ma'lumotlarni chiroyliroq qilib chiqarsin shuni tashkil
# qilamiz:
# bemor = {
#     "ism" : "Alijon Valiyev",
#     "yoshi" : 30,
#     "oila" : True,
#     "farzandlar" : ("Axmad", "Bonu"),
#     "allergiya" : None,
#     "dorilar" : [
#         {"nomi": "Analgin", "miqdori" : 0.5},
#         {"nomi": "Panadol", "miqdori" : 1.2}
#         ]
#     }
# print(type(bemor))
# Natija: dict
#bemor_json = json.dumps(bemor)
#print(type(bemor_json))
# Natija: str
#print(bemor_json)

# bemor_json = json.dumps(bemor, indent = 4)
# print(bemor_json)

# Aytaylik biz bemor ichadigan dorilarini ko'rmoqchimiz:
# print(bemor.keys())
# print(bemor["dorilar"])

# Biz bu jsonlarni fayllarga saqlashimiz mumkin:
# with open('bemor.json', 'w') as f:
#     json.dump(bemor, f) 

# Endi biz bemor_json degan o'zgaruvchini toyorlaymiz va uni qayta oddiy o'zgaruvchi holatiga
# o'tkazamiz:
# bemor_json = json.dumps(bemor)
# print(type(bemor_json))

# Demak xulosa: json.dumps orqali biz o'zgaruvchini json ga o'tkazamiz json.loads orqali esa uni
# yana oddiy o'zgaruvchi holatiga qaytaramiz.

# Endi fayllarni qanday ochamiz shuni ko'rib chiqaylik:
# import json

# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)
# print(type(bemor))
# Endi uni qaytadan yana oddiy o'zgaruvchiga o'tkazamiz.
# bemor2 = json.loads(bemor_json)
# print(type(bemor2))

# AMALIYOT TOPSHIRIQLARI:
#1 - Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring:
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# import json
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_json = json.dumps(data)
# print(data_json)

#2 - Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring:
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)
# print(type(talaba))
# print(talaba["ism"])
# print(talaba["familiya"])

#3 - Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.
# with open('data.json', 'w') as d:
#     json.dump(data, d)
    
# with open('talaba.json', 'w') as t:
#     json.dump(talaba, t)
    
#4 - Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan.
# Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida
# konsolga chiqaring.
# import json  # JSON formatdagi fayllar bilan ishlash uchun json kutubxonasini yuklaymiz

# try:  
    # Xatolarni ushlash va ishlov berish uchun try-except blokidan foydalanamiz
    # with open('students.json', 'r') as s:  
        # 'students.json' faylini o'qish uchun ochamiz ('r' - read mode, faqat o'qish rejimi)
        # talabalar = json.load(s)  
        # JSON fayldan ma'lumotlarni yuklaymiz va Python ro'yxati yoki lug'atiga aylantiramiz

        # print(talabalar)  
        # Yuklangan ma'lumotlarni konsolga chiqaramiz
# except json.JSONDecodeError as e:  
    # Agar JSON fayl noto'g'ri formatda bo'lsa, bu xatoni ushlaydi
    # print("JSON formatida xatolik:", e)  
    # Xato haqida batafsil ma'lumotni konsolga chiqaramiz
# except FileNotFoundError:  
    # Agar fayl topilmasa (masalan, noto'g'ri nom berilgan bo'lsa), bu xatoni ushlaydi
    # print("Fayl topilmadi.")  
    # Fayl yo'qligi haqida xabar beramiz

# JSON ma'lumotlarini dictionary formatida saqlaymiz
# data = {
#     'student': [
#         {'id': '01', 'name': 'Tom', 'lastname': 'Price', 'year': 4, 'faculty': 'Engineering'},
#         {'id': '02', 'name': 'Nick', 'lastname': 'Thameson', 'year': 3, 'faculty': 'Computer Science'},
#         {'id': '03', 'name': 'John', 'lastname': 'Doe', 'year': 2, 'faculty': 'ICT'}
#     ]
# }

# Talabalar ro'yxatidan 'name' va 'lastname' ma'lumotlarini chiqaramiz
# for talaba in data['student']:  
    # Har bir talaba uchun data['student'] ro'yxatini takrorlaymiz
    # name = talaba['name']  
    # Talabaning ismini olish
    # lastname = talaba['lastname']  
    # Talabaning familiyasini olish
    
    # print(f"{name} {lastname}")  
    # Ism va familiyani formatlangan holda chiqarish.
    
#5 - Quyidagi bog'lamaga kirsangiz, Wikipediadagi Python dasturlash tili haqidagi maqolani JSON ko'rinishida ko'rishingiz mumkin. Brauzerda chiqqan ma'lumotni JSON ko'rinishida saqlang (brauzerda Ctrl+S tugmasini bosib). Faylni Pythonda oching va konsolga maqolaning sarlavhasi (title) va qisqa matnini (extract) chiqaring: https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python

# import json

# JSON faylni ochish va o'qish
# with open('python_wikipedia.json', 'r', encoding='utf-8') as f:
    # data = json.load(f)

# JSON ma'lumotlarini to'liq ko'rish
# print(json.dumps(data, indent=4, ensure_ascii=False))

# Identifikatorni JSON tarkibidan toping va shunga qarab kodni o'zgartiring
# page_id = list(data['query']['pages'].keys())[0]  # Birinchi identifikatorni avtomatik olish

# Sarlavha va qisqa matnni olish
# title = data['query']['pages'][page_id]['title']
# extract = data['query']['pages'][page_id]['extract']

# Natijani konsolga chiqarish
# print("Sarlavha:", title)
# print("Qisqa matn:", extract)
 

# 32 - DARS TUGADI.

# 33 - DARS.
# TRY-EXCEPT XATOLAR USTIDA ISHLASH.
# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2025-yosh}-yilda tug'ilgansiz!")
# Yoshingizni kiriting: 26
# Natija: Siz 1999-yilda tug'ilgansiz.

# Yoshingizni kiriting: 25.5
# ValueError: invalid literal for int() with base 10: '25.5'

# Endi shu holatlarni oldini olishni ko'rib chiqamiz. Buning uchun try-except funksiyasidan
# foydalanamiz: 
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)    
#     print(f"Siz {2025 - yosh}-yilda tug'ilgansiz.")
# except:
#     print("Siz butun son kiritmadingiz!")    
# Yoshingizni kiriting: 26.5
# Natija: Siz butun son kiritmadingiz!

# Yoshingizni kiriting: 26
# Natija: Siz 1999-yilda tug'ilgansiz.

# Agar yanayam to'g'riroq yozmoqchi bo'lsak bunday qilamiz:
# yosh = input("Yoshingizni kiritng: ")
# try:
#     yosh = int(yosh)
# except:
#     print("Siz butun son kiritmadingiz!")
# else:
#     print(f"Siz {2025-yosh}-yilda tug'ilgansiz.")
# Aytish kerakki yuqoridagi amallar bilan kod to'htab qolmaydi va agar kod davomiga biz ayrim
# qo'shimchalar yozsak o'shalar ham bajarilib keyin kodlar tugasa shunda dastur to'htaydi
# print("Dastur davom etyapti.")
# print("Dastur tugadi.")    
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

# 34 - DARS.
# FUNKSIYALARNI TEKSHIRISH.

# Bu dars orqali biz dasturimizni tekshirishni o'rganishni davom etamiz. Biz dasturimiz davomida
# turli hil finksiyalar va obyektlar yaratishimiz tabiiy va albatta o'z-o'zidan yozgan ko'dimizni 
# joyidayoq tekshirib ketishimiz kerak bo'ladi.

# Bu darsda biz qanday qilib bu tekshirishlarni avtomatlashtirishni o'rganamiz.

# Oddiy funksiyani tekshirishdan boshlaymiz:
# def get_full_name(ism, familiya):
#     return f"{ism} {familiya}".title()

# print(get_full_name('alijon', 'valiyev'))
# Natija: Alijon Valiyev
# Yuqoridagi kod ishladi va xatolarsiz

# Biz endi funksiyalarni UNITTEST orqali test qilishni boshlaymiz.
# Aslida quyida keltirilgan misollar alohida modullarda bajariladi lekin misol sifatida
# darsimizda yozib qo'yamiz.

# Deylik bu yerda xatolik bo'ldi va biz kutgan natija chiqmadi. Etibor bersangiz biz funksiyani 
# qo'lda tekshiryapmiz, lekin odatda Pythonda buni avtomatlashtirish mumkin va dastur o'zini-o'zi
# tekshiradigan qilib dastur yozishimiz mumkin.

# Bunday amalni amalga oshirish uchun Pythonda UNITTEST degan modul mavjud. Bu modul orqali biz 
# dasturimiz ustida bir nechta testlarni amalga oshirishimiz mumkin, agar bitta test amalga
# oshirsak, bu TEST CASE dev ataladi.

# Endi biz o'zimizga kerakli bo'lgan funksiyalarni alohida modulda saqlaymiz.

# name_test.py modulida yozilgan kodlar.
# import unittest # Bu qism ham standart shablon desak bo'ladi.
# from name import get_full_name # Bu qism test qilinayotkan obyektga qarab o'zgaradi.

# class NameTest(unittest.TestCase): # Test qilish uchun qo'llaniladigan standart shablon.
# Endi biz bu yerda etiboe beradigan narsamiz oddiy class ning ichida yozilgan metodlar funksiyani
# test qilish uchun yozilgani uchun ularni nomini boshiga test so'zini qo'shib ketamiz. Bu bizga 
# test dasturimizni bajarganimizda qo'l keladi va Python ham avval test so'zi bilan yozilgan 
# dasturlarni qidiradi va birma-bir bajarib chiqadi.
#     def test_toliq_ism(self): # To'liq ismni test qiluvchi metod.
#         name = get_full_name('nurulloh', 'abdurashidov') # Funksiyadan qiymat olyapmiz.
#         self.assertEqual(name, 'Nurulloh Abdurashidov') # Qiymat biz kiritgan qiymatga mos bo'lsa.
        
# unittest.main() # Tekshirish uchun yozilgan kod.
# Natija: Ran 1 test in 0.001s

        # OK
        
# Endi vaqt o'toshi bilan bizning funksiyamiz o'zgardi.
# def get_full_name(ism, otasi, familiya):  # Tartib: ism, otasi, familiya
#     return f"{ism} {otasi} {familiya}".title()

# print(get_full_name('alijon', 'olimovich', 'valiyev'))

# Test funksiyamizni o'zgartirganimiz yo'q. Agar endi tekshirsak quyidagicha javob olamiz:
# Natija: Ran 1 test in 0.002s

        # FAILED (errors=1)
# Ko'rib turganingizdek xato kelib chiqti.

# Nima qilishimiz mumkin? Bu xatoni to'g'irlash uchun biz full_name funksiyamizga o'zgartirish
# kiritamiz:
# def get_full_name(ism, familiya, otasi = ''):
#     if otasi:
#         return f"{ism} {otasi} {familiya}".title()
#     else:
#         return f"{ism} {otasi} {familiya}".title()
    
# Natija: Ran 1 test in 0.001s

        # OK

# Endi kodimiz yana testdan o'tdi.

# Bu holatda funksiyamiz qo'shimcha qiymat qo'shib qo'qganimiz uchun, testimizga ham qo'shimcha 
# qilishimiz kerak.
# def test_otasining_ismi(self):
#     name = get_full_name('nurulloh', 'abdurashidov', "yorqinjon o'g'li")
#     self.assertEqual(name, 'Nurulloh', 'Abdurashidov', "Yorqinjon o'g'li")
    
# Endi tekshirib ko'rsak.
# Natija: Ran 2 tests in 0.002s

        # FAILED (errors=1)
        
# Ikki marta test qilindi va bittasi xato deyapti.

# Xatoni to'g'irladik.
# Natija: Ran 2 tests in 0.003s

        # OK
# Endi hammasi joyida.

# Biz yuqorida matnlar bilan ishladik endi sonlar va raqamlar bilan ishlab ko'ramiz.
# def getArea(r, pi = 3.14159):
#     """Doiraning yuzini qaytaruvchi funksiya"""
#     return pi*(r**2)

# def getPerimeter(r, pi = 3.14159):
#     """Doiraning perometrini qaytaruvchi dastur"""
#     return 2 * pi * r
# Endi bu funksiyalarni test qilib ko'ramiz va buni yangi test moduli orqali qilamiz:
# import unittest
# from circle import getArea, getPerimeter

# class CircleTest(unittest.TestCase):
#     def test_area(self):
#         self.assertEqual(getArea(5), 78.53975)
#         self.assertEqual(getArea(10), 314.159)
        
# unittest.main()

# Aslida yuqorida matematik yechimlar uchun assertEqual tengligini ishlatishimiz noto'g'ri,
# chunki, nuqta verguligacha aniq natijalar olishimiz kam uchraydi va aynan shuning uchun 
# assertAlmostEquel tengligini ishlatganimiz maqsadga muvofiq bo'ladi Almost so'zining tarjimasi
# deyarli degan manoni beradi. Bu tenglik orqali butun son va undan keyin nuqta va nuqtadan 
# keyingi 7ta songacha tekshiradi agar hohlasak uzunlikni o'zimiz berishimiz ham mumkin.

# Shu tarzda endi biz Perimetrni ham tekshiramiz:

# Agar funksiya mantiqiy qiymat qaytarsa, bunday funksiyalarni assertTrue() va assertFalse() metodlari yordamida tekshirishimiz mumkin. 

# Quyidagi funksiyamiz kiritilgan son tub yoki yo'q ekanini tekshiradi:

# def tubSonmi(n):
#     if n==2 or n==3: return True
#     if n%2==0 or n<2: return False
#     for i in range(3, int(n**0.5)+1, 2):   # faqat toq sonlarni tekshiramiz
#         if n%i==0:
#             return False   
#     return True
# Funksiyani alohida tubSonmi.py fayliga saqlaymiz. Funksiyani tekshirish uchun tubSon_test.py dasturini yozamiz:

# import unittest
# from tubSonmi import tubSonmi

# class tubSonTest(unittest.TestCase):
#     def test_true(self):
#         self.assertTrue(tubSonmi(7))
#         self.assertTrue(tubSonmi(193))
#         self.assertTrue(tubSonmi(547))
#     def test_false(self):
#         self.assertFalse(tubSonmi(6))
#         self.assertFalse(tubSonmi(265))
#         self.assertFalse(tubSonmi(489))
        
# unittest.main()
# Test davomida tubSonmi() funksiyasini bir nechta tub (7, 193, 547) va tub bo'lmagan (6, 265, 489) sonlar bilan chaqirdik. Bunda assertTrue() metodi funksiyamiz haqiqatdan ham True qiymatini qaytarishini, assertFalse() metodi esa funksiyamiz False qiymat qaytarishini tekshiradi.

# TAQQOSLASH METODLARI
# TestCase klassi tarkibidagi boshqa taqqoslash metodlari ham mavjud:

# Metod
# Nimani taqqoslaydi?

# assertEqual(a, b) -> a == b

# assertNotEqual(a, b) -> a != b

# assertTrue(x) -> x ning qiymati True

# assertFalse(x) -> x ning qiymati False

# assertIs(a, b) -> a bu b

# assertIsNot(a, b) -> a bu b emas

# assertIsNone(x) -> x ning qiymati None

# assertIsNotNone(x) -> x ning qiymati None emas

# assertIn(a, b) -> a b ning ichida

# assertNotIn(a, b) -> a b ning ichida emas

# assertIsInstance(a, b) -> a b ning vorisi

# assertNotIsInstance(a, b) -> a b ning vorisi emas

# AMALIYOT TOPSHIRIQLARI:
#1 - Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya.
# def find_max(a, b, c):
#     return max(a, b, c)

# print(find_max(10, 20, 21))
# # Natija: 21

# # Test dasturi:
# class TestFindMax(unittest.TestCase):
#     def test_find_max(self):
#         self.assertEqual(find_max(10, 20, 15), 20)
#         self.assertEqual(find_max(5, 3, 8), 8)
#         self.assertEqual(find_max(-10, -5, -7), -5)


# unittest.main()

# #2 - Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta
# # harfga o'zgatiruvchi funksiya
# def capitalize_first_letters(strings):
#     capitalized_list = []
#     for string in strings:
#         capitalized_list.append(string.capitalize())
#     return capitalized_list
# texts = ['olma', 'shaftoli', 'banan']
# result = capitalize_first_letters(texts)
# print(result)
# # Natija: ['Olma', 'Shaftoli', 'Banan']

# # Test dasturi:
# class TestCapitalizeFirstLetters(unittest.TestCase):
#     def test_capitalize_first_letters(self):
#         self.assertEqual(capitalize_first_letters(['salom', 'dunyo']), ['Salom', 'Dunyo'])
#         self.assertEqual(capitalize_first_letters(['python', 'dasturlash']), ['Python', 'Dasturlash'])
#         self.assertEqual(capitalize_first_letters([]), [])


# unittest.main()

# #3 - Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya.
# def filter_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]   

# nums = [1,2,3,4,5,6,7,8,9]
# result = filter_even_numbers(nums)
# print(result)
# # Natija: [2, 4, 6, 8]

# # Test dasturi:
# class TestFilterEvenNumbers(unittest.TestCase):
#     def test_filter_even_numbers(self):
#         self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
#         self.assertEqual(filter_even_numbers([10, 11, 12, 13]), [10, 12])
#         self.assertEqual(filter_even_numbers([1, 3, 5]), [])
    
# unittest.main()

# #4 - Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) qaytaruvchi
# # funksiya yozing.
# import math
# def is_fibonachi(n):
#     def is_perfect_square(x):
#         s = int(math.sqrt(x))
#         return s * s == x
    
#     return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# print(is_fibonachi(21))
# # Natija: True

# # Test dasturi:
# import unittest

# class TestFibonachi(unittes.TestCase):
#     def test_is_fibonachi(self):
#         self.assertTrue(is_fibonachi(8))
#         self.assertTrue(is_fibonachi(13))
#         self.assertTrue(is_fibonachi(15))
    
# unittest.main()

# 34 - DARS TUGADI.

# 35 - DARS.
# KLASSLARNI TEKSHIRISH.
class Car:
    """(self, make, model, year, km = 0, price = None)"""
    def __init__(self, make, model, year, km = 0, price = None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
        
    def set_price(self, price):
        self.price = price
        
    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas")
            
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}"
        info += f"{self.year}-yil, {self.__km} km yurgan"
        if self.price:
            info += f" Narhi: {self.price}"
        return info
    
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}"
        info += f"{self.year}-yil, {self.__km}km yurgan"
        if self.price:
            info += f" Narhi: {self.price}"
        return info
    
    def get_km(self):
        return self.__km
    
     
#  - DARS.
# LOYIHALAR. 
# "SON TOPISH" VA "SO'Z TOPISH" O'YINLARI.

# Ushbu bobda biz ikkita yangi o'yin ustida ishlaymiz. Dasturni yaratish jarayonida avval o'rgangan bilimlarimizni amalda qo'llaymiz.
# Shuningdek, yangi loyiha boshlashda muhim bo'lgan algoritm tushunchasi bilan tanishamiz.

# "SON TOPISH" O'YINI.
# Birinchi dasturimiz sodda "SON TOPISH" o'yini bo'ladi. Bu o'yin quyidagicha o'ynaladi.
#     1. Kompyuter biror berilgan oraliqda (masalan, 1dan 10gacha) son o'ylaydi.
#     2. Foydalanuvchi kompyuter o'ylagan sonni topishga urinadi va biror qiymat taxmin qilib kiritadi.
#     3. Agar taxmin to'g'ri bo'lsa, o'yin tugaydi, agar xato bo'lsa kompyuter foydalanuvchi taxmin qilgan son o'ylangan sondan katta yoki
# kichkligini aytadi va yangi son taxmin qilishni so'raydi.
#     4. Dastur shu zaylda foydalanuvchi to'g'ri sonni topguniga qadar davom etadi.


# ALGORITM.
# Dasturlashning muhim qismi to'g'ri reja qilish va dasturni mayda qadamlarga bo'lib olishdir. Bu Algoritm deyiladi. Xuddi ovqat
# pishirishda retsepdan foydalangandek, dastur yozishda ham Algoritmdan foydalanamiz.

# Yuqoridagi o'yin qoidasini ham bir nechta sodda qadamlarga bo'lib olamiz:
#     1. Kompyuter ma'lum oraliqda son "o'ylaydi": Albatta, kompyuter o'ylashga qodir emas, shuning uchun biz berilgan oraliqda biror 
# tasodifiy sonni qaytarishimiz kifoya (random funksiyasi orqali).
#     2. Foydalanuvchi taxmin qilgan sonni qabul qilib olish (input() orqali bo'ladi).
#     3. Taxmin va tasodifiy sonlarni taqqoslash ("==" sonlarni teng ekanini tekshiramiz).
#     4. Taqqoslash natijasiga ko'ra ("if-else" juftligidan foydalanamiz va natijaga qarab ikki hil yo'l tutamiz (a - b)).
#     a. O'yinni to'xtatish;
#     b. Foydalanuvchiga ishora berish va qayta taxmin qilishni so'rash va yuqoridagi 3 - 4 qadamlarni takrorlash ("while" sikli).
    
# Sodda algoritm tayyor, endi bevosita dastur yozishga kirishsak ham bo'ladi.

# DASTUR.
# Boshlanishiga dastur uchun kompyuterimizda alohida papka yaratamiz va dasturga oid fayllarni (modullarni) shu papkada saqlab boramiz.
# Dastur yozishda asosiy dasturimiz main.py qo'shimcha modullarni esa shu modul ichidagi funksiyaga oid so'zlar bilan nomlash to'g'ri
# bo'ladi.

# Biz ham boshlanishiga sonTop.py faylini yaratamiz va fayl ichiga yuqoridagi algoritm asosida sontop(x) funksiyasini yozamiz.
# Bu funksiyamiz argument sifatida kompyuter o'ylashi kerak bo'lgan sonlar oralig'inining yuqori chegarasini qabul qiladi (0dan x gacha)
# va biz bu parametrga standart 10 qiymatini berib qo'yamiz (ya'ni foydalanuvchi aniq oraliqni ko'rtsatmasa, kompyuter 0 dan 10 gacha
# son "o'ylaydi").

# Funksiyaichida birinchi qiladigan ishimiz - tasodifiy son "o'ylash". Buning uchun random modulidagi randint funksiyasidan foydalanamiz.
# Demak, dastur boshida random modulini import qilishni ham esdan chiqarmaslik kerak: 
# import random 
# def son_top(x = 10):
#     tasodifiy_son = random.randint(1, x) 

# Navbat foydalanuvchidan qiymatlar qabul qilishga. Keling, bundan kompyuter aynan qaysi oraliqda sono'ylaganini ham aytaylik.
    # print(f"Men 1dan {x} gacha son o'yladim. Topa olasizmi?")

# Ana endi bevosita input() funksiyasi yordamida foydalanuvchi kiritgan sonni qabul qilamiz va bu sonni tasodifiy son bilan solishtiramiz.

# Algoritmga ko'ra, biz foydalanuvchining taxminiga qarab turli amallarni bajarishimiz kerak:
    # 1. Agar taxmin tasodifiy sondan kichik bo'lsa, "Kattaroq son ayting";
    # 2. Agar taxmin tasodifiy sondan katta bo'lsa, "Kichikroq son ayting";
    # 3. Agar taxmin to'g'ri bo'lsa, "Yutdingiz!" deb aytishimiz kerak.
    
# O'yin foydalanuvchi yutguniga qadar davom etishi uchun kodimizni while sikli ichiga olamiz.

# Marhamat funksiya tayyor.
# import random 

# def son_top(x=10):
#     tasodifiy_son = random.randint(1, x) 
#     print(f"Men 1dan {x} gacha son o'yladim. Topa olasizmi?")
    
#     while True:
#         taxmin = int(input(">>> "))
#         if taxmin < tasodifiy_son:
#             print("O'ylagan sonim bundan kattaroq!")
#         elif taxmin > tasodifiy_son:
#             print("O'ylagan sonim bundan kichikroq!")
#         else: 
#             print("Topdingiz!")
#             break

# Biz funksiyani alohida modulda saqladik, keling main.py faylini yaratamiz-da, yuqoridagi modul va funksiyani import qilamiz:
# from son_top import son_top
# son_top()

# Faylimiz tarkibi qisqagina bo'ldi. main.py faylini bajaramiz
# Natija: Men 1dan 10 gacha son o'yladim. Topa olasizmi?
# 5
# O'ylagan sonim bundan kattaroq!
# 6
# O'ylagan sonim bundan kattaroq!
# 10
# Topdingiz!
        

# pyWebiO
# Avvalgi bobda pywebiomoduli bilan tanishgan edik, keling, ushbu modul yordamida dasturimizni brauzerda ishlaydigan qilamiz.

# Boshlanishiga modul ichidan input va put_text funksiyalarini chaqirib olamiz. input() funksiyasi bevosita qiymat qabul qilish uchun,
# put_text() esa foydalanuvchiga matn ko'rsatish uchun ishlatiladi.

# Avvalgi dasturda "Men 1 dan 10 gacha son o'yladim. Topa olasizmi?>>>" matnini ikkiga bo'lgan edik, bu safar ikkalasini ham input()
# funksiyasiga joylaymiz. Konsolga chiqarilayotgan matnlarni esa brauzerga chiqarish uchun kodimizdagi print funksiyasini put_text() bilan
# almashtiramiz:
# from pywebio.input import input
# from pywebio.output import put_text
# import random
# def sontop(x = 10):
#     tasodifiy_son = random.randint(1, x)
#     while True:
#     taxmin = int(input(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi? >>> "))
#     if taxmin < tasodifiy_son:
#         put_text("Kattaroq son ayting!")
#     elif taxmin > tasodifiy_son:
#         put_text("Kichikroq son ayting!")
#     else:
#         put_text("Yutdingiz!")
#         break
