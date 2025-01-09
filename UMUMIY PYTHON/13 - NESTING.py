# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 02:11:43 2025

@author: DavrServis
"""

# 13 - DARS.
# NESTING.

# Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yo boshqa lug'atni yoki, aksincha, ro'yxat ichida
# lug'atni saqlash ham qo'l kelishi mumkin. Bu ingliz tilida NESTING deyiladi. Nesting Pythondagi foydali
# xususiyatlardan biridir. Kelin, bunga bir nechta misollarni ko'rib chiqamiz.

# LUG'ATLAR RO'YXATI.
# Biz avvalgi darsimizda talabarning ma'lumotlarni lug'at shaklida saqlashni ko'rgan edik. Shunday talabalardan yuzlab bo'lganda
# ularning har biriga alohida lug'at qilishimiz tabiiy, lekin bu lug'atlar bilan ishlash qiyinchilik tug'dirishi mumkin.
# Shunday holatda barcha lug'atlarni (talabalarni) bitta ro'yxatga joylab, ular ustida turli amallar bajarish mumkin.

# Quyidagi misolda 3ta alohida lug'atda 3ta avtomobil haqida ma'lumotlar saqlangan:
# car0 = {
#         'model':'jentra', 'rang':'qora',
#         'yil':2018, 'narx':13000,
#         'km':50000, 'korobka':'avtomat'
#         }
# car1 = {
#         'model':'cobalt', 'rang':'oq',
#         'yil':2020, 'narx':15000,
#         'km':62000, 'korobka':'avtomat'
#         }
# car2 = {
#         'model':'nexia3', 'rang':'qizil',
#         'yil':2021, 'narx':12500,
#         'km':5760, 'korobka':'mexanika'
#         }
# Agar biz har bir avtomobil haqida ma'lumot olmoqchi bo'lsak, har bir lug'atga alohida murojaat etishimiz talab qilinadi:
# car = car0
# print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narx']}$")
# car = car1
# print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narx']}$")
# car = car2
# print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narx']}$")

# Yuqoridagi natijani chiqarishning osonroq usuli barcha avtolarni bitta ro'yxarga joylab, for siklidan foydalanishdir:
# cars = [car0,car1,car2] # Lug'atlar ro'yxati.
# for car in cars:
#     print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}-yil, {car['narx']}$")
# Ishimiz birmuncha yengillashdi, kodimiz ham qisqardi.
# Natija esa bir xil.

# Ro'yxat ichidagi istalgan lug'atga indeks bo'yicha murojaat etishimiz ham mumkin (lug'at nomini yodlab qolish ham shart emas).
# print(cars[0])

# Biror lug'atdagi elementga murojaat qilish uchun esa quyidagi usuldan foydalanishimiz mumkin:
# print(cars[0] ['model'])

# print(f"{cars[2]['rang'].title()}"
#       f" {cars[2]['model'].title()}")

# for sikli orqali biz bo'sh lug'atlar ro'yxatini ham yaratib olishimiz mumkin:
# malibus = [] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik.
# for n in range(10): # Range orqali 10 element yaratib olamiz va n ni ularning har biriga tenglaymiz.
#     n = { # Har bir n ni lug'at shakliga keltirib olamiz.
#         'model':'malibu',
#         'rang':None,
#         'yil':2024,
#         'narx':None,
#         'km':0,
#         'korobka':'avto'
#                 } 
#     malibus.append(n) # Yuqoridagi lug'atni ro'yxatga qo'shamiz.
# # Yuqoridagi misolda biz 10ta Malibu mashinasidan iborat ro'yxat tuzdik. ETIBOR QILING, 'rang' kalitiga qiymat bermadik va None 
# # deb qoldirdik.
# # Endi ishlab chiqarish jarayonida mashinalarga turli ranglarni berishimiz mumkin. Misol uchun, birinchi 3ta mashinaga qizil rang
# # beramiz:
# for malibu in malibus[:3]: # Malibus ro'yxatidagi birinchi 3ta Malibu uchun:
#     malibu['rang'] = 'qizil' # Rngini qizil qilgin.
# # Keyingi 3tasiga qora:
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'

# # Oxirgi 4ta Malibuni rangini qora, korobkasini esa mexanika qilamiz:
# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['korobka'] = 'mexanika'
    
# # Kelin endi mashinalarni korobkasidan kelib chiqqan holda narx belgilaymiz:
# for malibu in malibus: # Malibus ro'yxatidagi har bir Malibu uchun:
#     if malibu['korobka'] == 'avto': # Agar korobkasi avtomat bo'lsa.
#         malibu['narx'] = 40000 # Narxi 40000$ bo'lsin.
#     else:
#         malibu['narx'] = 35000
# # Mashinalar ro'yxatini konsolga chiqaramiz.
# for malibu in malibus:# Malibus ro'yxatidagi har bir Malibu uchun:
#     print(malibu.values()) # Har bir Malibuni qiymatlarini konsolga chiqargin. Va biz shuncha yozgan kodlarimiz natijasini ko'ramiz.
    
# LUG'AT ICHIDA RO'YXAT.
# Bir kalitga bir nechta qiymatlar berish talab qilinganda qiymatlarni ro'yxat ko'rinishida yozish o'rinlidir. Misol uchun,
# bir tashkilotda bir nechta tashkilotda bir nechta dasturchilar ishlaydi va har bir dasturchi turli dasturlash tillarini biladi.
# Keling, dasturchilar lug'atini tuzamiz va har bir dasturchi haqidagi ma'lumotni konsolga chiqaramiz:
# dasturchilar = {
#     'ali':['python', 'c++'],
#     'vali':['html', 'css'],
#     'hasan':['php', 'sql'],
#     'husan':['python', 'php'],
#     'maryam':['c++', 'c#']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()}: ", end='')
#     for til in tillar:
#         print(f"{til.upper()} ", end='')

# print() funksiyasi har bir matndan so'ng yangi qator tashlaydi. Buning oldini olish uchun quyidagi usuldan foydalanish mumkin:
# print(string, end='') 

# LUG'AT ICHIDA LUG'AT.
# Bunday qilish tavsiya qilinmaydi, istisno holatlarda lug'at ichidagi qiymatlarni lug'at ko'rinishida ham saqlash mumkin.
# Misol uchun, ish joyingizdagi hamkasblaringiz haqidagi ma'lumotlarni saqlashda hamkasblaringizning ismi kalit, u haqidagi
# ma'lumotlar esa lug'at ko'rinishida berilishi mumkin.

# hamkasblar = {
#     'ali':{
#         'familya':'valiyev',
#         'tyil':1995,
#         'malumot':'oliy',
#         'tillar':['python','c++']
#         },
#     'vali':{
#         'familya':'aliyev',
#         'tyil':2000,
#         'malumot':'orta',
#         'tillar':['html','css']
#         },
#     'hasan':{
#         'familya':'husanov',
#         'tyil':1998,
#         'malumot':'oliy',
#         'tillar':['python','php']
#         }
#     }
# print(hamkasblar)

# # Hamkasblar to'g'risidagi ma'lumotlarni esa quyidagicha ko'rish mumkin:
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan.\n"
#           f"Malumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi: ")
#     for til in info['tillar']:
#         print(til.upper())
        
# Lug'at ichidagi lug'atlar bir xil tuzilishga ega bo'lgani ishingizni ancha yengillashtiradi, aks hold, kodingiz murakkablashib
# ketishi mumkin.

# AMALIYOT TOPSHIRIQLARI:
#1 - Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
# buxoriy = {
#         'ism':'Abu Abduloloh Muhammad ibn Ismoil',
#         'tyil':810,
#         'tjoy':'buxoro',
#         'vyil':870
#         }
# qodiriy = {
#         'ism':'Abdulla Qodiriy',
#         'tyil':1894,
#         'tjoy':'toshkent',
#         'vyil':1938
#         }
# vohidov = {
#         'ism':'Erkin Vohidov',
#         'tyil':1936,
#         'tjoy':'fargona',
#         'vyil':2016
#         }
# navoiy = {
#         'ism':'Alisher Navoiy',
#         'tyil':1441,
#         'tjoy':'xirot',
#         'vyil':1501
#         }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"\n{ism} {tyil}-yilda {tjoy.title()}da tug'ilgan, "
#           f"{vyil - tyil} yil umr ko'rgan."
#           )
#2 - Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va
# uning asarlarini konsolga chiqaring.
# buxoriy = {
#         'ism':'Abu Abduloloh Muhammad ibn Ismoil',
#         'tyil':810,
#         'tjoy':'buxoro',
#         'vyil':870,
#         'asarlari':['al-jome as-sahih', 'al-adab al-mufrad', 'at-tarix al-kabir', 'at-tarix as-sag\'ir']
#         }
# qodiriy = {
#         'ism':'Abdulla Qodiriy',
#         'tyil':1894,
#         'tjoy':'toshkent',
#         'vyil':1938,
#         'asarlari':['o\'tkan kunlar', 'mehrobdan chayon', 'obid ketmon']
#         }
# vohidov = {
#         'ism':'Erkin Vohidov',
#         'tyil':1936,
#         'tjoy':'fargona',
#         'vyil':2016,
#         'asarlari':['tong nafasi', 'qo\'shiqlarim sizga', 'o\'zbegim', 'qiziquvchan matmusa']
#         }
# navoiy = {
#         'ism':'Alisher Navoiy',
#         'tyil':1441,
#         'tjoy':'xirot',
#         'vyil':1501,
#         'asarlari':['xamsa', 'lison ut-tayr', 'mahbub al-qulub', 'munojot']
#         }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"\n{ism}ning sevimli asarlari quyidagilar:")
#     for asar in shaxs['asarlari']:
#         print(f"{asar.title()}")
        
#3 - Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli
# kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
# kinolar = {
#     'abdurahmon':['shapka', 'oltin devor', 'sevgi'],
#     'nurulloh':['king kong', 'omar va xanna', 'qasoskorlar'],
#     'mavluda':['shabnam', 'om shanti om', 'baxt']
#     }
# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino.title())
#4 - Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
# Har bir davlat haqida ma'lumotni konsolga chiqaring.
# davlatlar = {
#     'aqsh':{
#         'poytaxti':'vashington',
#         'axolisi': 327000000,
#         'maydoni': '9631418 kv.km',
#         'pul birligi':"dollar"
#         },
#     'rossiya':{
#         'poytaxti':'moskva',
#         'axolisi': 144000000,
#         'maydoni': '17098246 kv.km',
#         'pul birligi':"rubl"
#         },
#     "o'zbekiston":{
#         'poytaxti':'toshkent',
#         'axolisi': 33000000,
#         'maydoni': '448978 kv.km',
#         'pul birligi':"so'm"
#         }
#     }
# for davlat, info in davlatlar.items():
#     print(f"\n{davlat.title()}ning poytaxti {info['poytaxti'].title()}")
#     print(f"Axolisi: {info['axolisi']}")
#     print(f"Maydoni: {info['maydoni']}")
#     print(f"Pul birligi: {info['pul birligi']}")
    
#5 - Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot
# bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
# davlatlar = {
#     'aqsh':{
#         'poytaxti':'vashington',
#         'axolisi': 327000000,
#         'maydoni': '9631418 kv.km',
#         'pul birligi':"dollar"
#         },
#     'rossiya':{
#         'poytaxti':'moskva',
#         'axolisi': 144000000,
#         'maydoni': '17098246 kv.km',
#         'pul birligi':"rubl"
#         },
#     "o'zbekiston":{
#         'poytaxti':'toshkent',
#         'axolisi': 33000000,
#         'maydoni': '448978 kv.km',
#         'pul birligi':"so'm"
#         }
#     }
# print("Biz 3ta davlat haqidagi ma'lumotlarni jamlaganmiz: AQSH, ROSSIYA, O'ZBEKISTON")
# davlat = input("Iltimos davlat nomini kiriting: ").lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.upper()}ning poytaxti {info['poytaxti'].title()}")
#     print(f"Axolisi: {info['axolisi']}")
#     print(f"Maydoni: {info['maydoni']}")
#     print(f"Pul birligi: {info['pul birligi']}")
# else:
#     print(f"Bizda {davlat} haqida ma'lumot yo'q!")

# 13 - DARS TUGADI.