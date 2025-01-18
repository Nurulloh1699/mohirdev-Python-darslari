# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:37:44 2025

@author: DavrServis
"""

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