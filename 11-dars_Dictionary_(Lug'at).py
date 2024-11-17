# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:41:28 2024

@author: DavrServis
"""

#11-dars Dictionary (Lug'at).
#23.10.2024.
#Muallif:Abdurashidov Nurulloh.

# Lug'atlar bilan ishlashda biz uni oddiy chet tili lug'atiga o'xshatsak bo'ladi yani bunda 
# kalit so'z va uning tarjimasi yoki tavsifi bo'ladi.
# car_0 = {'model':'damas', 'rang':'oq'} # Lug'at elementlarini yozishda biz gulli qavslardan {}
# # foydalanamiz.
# print(car_0['model']) # Lug'at elementlarini konsilga chiqarishda car['element'] bilan ifodalaymiz
# print(car_0['rang'])

# # Lug'at elementlarini chaqirish yo'llari bilan tanishamiz.
# mevalar = {'olma':10000, 'anor':15000, 'o\'rik':40000, 'banan':27000}
# print(f"Olmaning narxi {mevalar['olma']} so'm") # Lug'atni ro'yxatdan farqi lug'atda elementning
# # o'zi bilan mevalar ['olma'] murojaat qilinadi ro'yxatda esa ineklar mevalar[2] bilan

# # Yanayam tushunishimiz oson bo'lishi uchun buni talaba ma'lumotlari ko'rinishida ko'ramiz.
# talaba_0 = {'ism':'nurulloh abdurshidov', 'yosh':'25', 't_yil':'1999'}
# print(f"{talaba_0['ism'].title()},\
# {talaba_0['t_yil']}-yilda tug'ilgan,\
# yoshi {talaba_0['yosh']} yoshda")

# # Yangi kalit so'z va qiymat qo'shish.
# talaba_0['kurs'] = 5
# talaba_0['fakultet'] = 'KIF'
# print(talaba_0)

# # Qiymatlarni o'zgartirish uchun esa quyidagicha yo'l tutamiz.
# talaba_0['ism'] = 'Abdulloh'
# print(talaba_0)

# Biz bo'sh lug'at yaratib va keyinchalik uni to'ldirishimiz ham mumkin.
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# Qiymatni yangilash.
# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# Lug'at elementlarini o'chirishni ko'rib chiqamiz, bunda bizga (del) operatori yordamga keladi  
# va o'chirib tashlamoqchi bo'lgan elementga kalit so'zi yordamida murojaat qilishimiz
# kifoya qiladi.
# del talaba_1['yosh']
# print(talaba_1)

# Lug'atlarni bir nechta qatorga yozishimiz ham mumkin buning uchun quyidagicha yo'l tutamiz.
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'nokia',
#     'shodi':'samsung',
#     'qodir':'motorolla'
#     } # shu ko'rinishda.

# Lug'at ichida element bor yo'qligiga qarab chiqadigan habarni tahlil qilamiz.
# Lug'atda yoq element kiritilganda xatolik chiqishini oldini olish uchun biz (.get) metodidan
# foydalanamiz.
# phone = telefonlar.get('hasan','Bunday ism mavjud emas!') # Bu yerda biz (.get) metodidan keyin
# ikkita qiymat bedik.
# print(phone)

# Agar yuqoridagidek ikkita qiymat berilmasa ham qo'rqinchili emas, quyida buni ko'rib chiqamiz.
# phone = telefonlar.get('hasan')
# print(phone) # Bu yerda (none) javob qaytaradi, va bu ham qaysidur manoda foydalanuvchiga 
# tushunarli bo'ladi.

# TOPSHIRIQLAR.
#1 otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida
# kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi
# ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand
# viloyatida tug'ilgan.
# otam = {'ism_sh':'Maksimov Yorqinjon', 'yosh':'54','t_yil':'1970','t_joy':'Oltiariq tumani'}
# print(f"Otamning ism shariflari {otam['ism_sh']}, ular {otam['t_yil']}-yilda tug'ilganlar,\
# yoshlari {otam['yosh']}da, tug'ilgan joylari {otam['t_joy']}.")

#2 Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom
# jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring:
#Alining sevimli taomi osh
# s_taomlar = {'otam':'osh', 'onam':'sho\'rva', 'buvam':'somsa', 'bobom':'manti', 'men':'shirguruch'}
# print(f"Otamning sevimli taomi {s_taomlar['otam']}, Onamning sevimli taomi {s_taomlar['onam']}\
#  Mening sevimli taomim {s_taomlar['men']}")

#3 Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani)
# kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha
# tarjimasini yozing.
# python = {'int':'Butun son','float':'O\'nlik son','str':'Matn','bool':'Mantiqiy',\
# 'if':'Agar shart operatori','else':'Yoki shart operatori','elif':'Agar va yokini chachishgani',\
# 'or':'Yoki operatori','and':'Va operatori','in':'Ro\'yxatlarni tekshiruvchi operator'}
    
#4 Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi
# lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas"
# degan xabarni chiqaring.
# python = {'int':'Butun son','float':'O\'nlik son','str':'Matn','bool':'Mantiqiy',\
# 'if':'Agar shart operatori','else':'Yoki shart operatori','elif':'Agar va yokini chachishgani',\
# 'or':'Yoki operatori','and':'Va operatori','in':'Ro\'yxatlarni tekshiruvchi operator'}

# soz = input("Biron bir so'z kiriting: ")
# print(python.get(soz, "Bunday so'z lug'atimizda yo'q"))

#5 Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli
# ko'rinishda chiqaring.
# python = {'int':'Butun son','float':'O\'nlik son','str':'Matn','bool':'Mantiqiy',\
# 'if':'Agar shart operatori','else':'Yoki shart operatori','elif':'Agar va yokini chachishgani',\
# 'or':'Yoki operatori','and':'Va operatori','in':'Ro\'yxatlarni tekshiruvchi operator'}

# soz = input("Birorta kalit so'z kiriting: ").lower()
# tarjima = python.get(soz)
# if tarjima == None:
#     print("Lug'atimizda bunday so'z yoq.")
# else:
#     print(f"{soz.title()} so'zi {tarjima} deb tarjima qilinadi.")
    
