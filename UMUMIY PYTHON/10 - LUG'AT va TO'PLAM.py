# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 02:06:25 2025

@author: DavrServis
"""

# 10 - DARS. LUG'AT VA TO'PLAM.

# Lug'at bir obyektga bog'liq ma'lumotlarni kalit so'z va qiymat juftligi ko'rinishida saqalash imkonini beradi.
# Misol uchun, biz biror avtomobilga oid lug'at yaratishimiz va lug'atda shu avtomobilga tegishli barcha
# ma'lumotlarni saqlashimiz mumkin (avtomobilning nomi, rangi, yili, motori, narxi, va hokazo).

# Nima uchun bu ma'lumot turi lug'at deyilishini tushinish uchun oddiy lug'atga qaraylik. Odatda, lug'atdagi
# ma'lumotlar ikki qismdan iborat bo'ladi: KALIT SO'Z va IZOH (yoki TARJIMA). Xuddi oddiy lug'atlardagi kabi Python
# lug'atidagi ma'lumotlar ham ikki qismdan iborat bo'ladi: KALIT SO'Z va QIYMAT (ingliz tilida bu "KEY-VALUE PAIR"), 
# "KALIT-QIYMAT JUFTLIGI deyiladi."

# Dasturlashda ko'p ishlatiladigan atamalarni ingliz tilida yodlab qolish juda muhim! Bu sizga kelajakda yangi
# ma'lumotlar izlashda, xatolar ustida ishlashda, umuman ish faoliyatingizda ko'p asqatadi. Shuning uchun "veriable,
# integer, float, string, list, tuple, dictionary, function, loop, key, key, value" va boshqa atamalarning ma'nosini
# yaxshilab o'zlashtirib oling.

# Pythonda lug'at yaratish uchunkatta {jingalak} qavsdan foydalanamiz. Qavs ichida har bir element uchun kalit so'z
# va qiymat beramiz. Ularning orasi ikki nuqta (:) bilan, har bir element (juftlik) esa vergul (,) bilan ajratiladi.
# car = {'model':'ferrari', 'rang':'qizil'}
# print(car)  

# Yuqorida car degan lug'at yaratdik. Lug'atda 2ta element bor: mashinaning modeli (ferrari) va rangi (qixzil).
# Bu yerda 'model' va 'rang'kalit so'zlar, 'ferrari' va 'qizil' esa mos kelivchi kalit so'zlarning qiymatlaridir.

# Lug'at ichidagi kalitlar takrorlanmasligi kerak. Agar lug'at yaratishda kalit so'zlar takrorlans, ulardan faqat
# oxirgisining qiymati saqlanib qoladi. 
        
# LUG'AT BILAN ISHLASH.
# Lug'atdagi biror elementni ko'rish uchun unga kalit so'z orqali murojaat qilamiz.
# car = {'model':'ferrari', 'rang':'qizil'} # oddiy lug'at yaratib olamiz.
# print(car['model']) # konsolga mashina modeli ni chiqaramiz.
# # ferrari
# print(car['rang']) # konsolga mashina rangi ni chiqaramiz.
# # qizil

# Lug'atdagi qiymatlar son (int, float), matn (string), ro'yxat (list, tuple), hattoboshqa lug'at ham bo'lishi mumkin.
# talaba = {'ism_sh':'murod nazarov', 'yosh': 20, 't_yil': 2000}
# print(f"{talaba['ism_sh'].title()},{talaba['t_yil']}-yilda tug'ilgan,{talaba['yosh']} yoshda.") 
     
# Uzun lug'atlarni bir necha qatorga bo'lib yozishimiz mumkin. Bunda har bir element alohida qatordan yoziladi va
# qator oxirida vergul qo'yilib, yangi qatorga o'tiladi.
# car = {
#      "make":"GM",
#      "model":"Malibu",
#      "color":"Black",
#      "gear":"Automatic",
#      "year":"2020",
#      "price":"40000"
#      }  
# print(car)

# get() METODI.
# Yuqorida biz lug'at elementiga kalit so'z orqali murojaat etishni o'rgandik.
# print(car['model'])
# Malibu

# Bu usulni kamchiligi shundaki, agar lug'atda siz so'ragan kalit topilmasa, dastur KEYERROR xatoligi bilan to'htab
# qoladi.
# print(car['narx'])
# KeyError 'narx'

# Lug'atda 'narx' kalit so'zi bo'lmagani uchun yuqoridagi kod KEYERROR degan xatoni qaytardi.
# Hozir get() metodi yordamida lug'atga murojaat etish va mavjud bo'lmagan kalitning o'rniga biror xabar qaytarishni
# ko'rib chiqaylik.
# narx = car.get('narx', 'Bunday kalit mavjud emas!')

# Yuqoridagi lug'at nomidan so'ng .get() metodini yozdik, argumentlar sifatida kelit so'z ('narx') va kalit mavjud
# bo'lmaganida chiqadigan xabarni yozdik ('Bunday kalit mavjud emas').
# print(narx)

# Agar .get() metodida ikkinchi argumentni tashlab ketsangiz va siz so'ragan kalit mavjud bo'lmasa, .get() metodi
# NONE qiymatini qaytaradi.
# narx = car.get('narx')
# print(narx)
# None

# None, qiymat mavjud emas degan ma'noni beradi.

# YANGI JUFTLIK QO'SHISH.
# Lug'atda yangi element (kalit so'z va qiymatlar =) qo'shishimiz ham mumkin. Keling, yuqoridagi talaba nomli
# lug'atga yana 2ta yangi - kurs va fakultet nomli kalit so'zlar va qiymatlar qo'shamiz:
# talaba['kurs'] = 4
# talaba['fakultet'] = 'informatika'
# Lug'atni konsolga chiqarib ko'ramiz:
# print(talaba)

# BO'SH LUG'AT.
# Bazida dastur boshida bo'sh lug'at yaratib, dastur davomida lug'atga yangi ma'lumotlar kiritib borish talab
# qilinishi mumkin. Bunday holatda bo'sh lug'at quyidagicha yaratiladi:
# car = {}

# Dastur davomida esa lug'atga qiymatlar kiritilib borilishi mumkin:
# car['model'] = 'Mazda 6' # Bu usul orqali yangi bo'sh lug'atga elementlar qo'shamiz.
# car['color'] = 'Red'
# car['price'] = 40000
# print(f"{car['color']} {car['model']}, {car['price']}$")
# Lug'atda kalit so'zlar qanday ketma-ketlikda kiritilsa, shu tartib saqlanib qoladi.

# QIYMATNI O'ZGARTIRISH.
# Biror kalit so'zga tegishli qiymatni o'zgartirish esa quyidagicha amalga oshiriladi:
# car['price'] = 38000
# print(f"{car['color']} {car['model']}, {car['price']}$")

# KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH.
# Lug'atda elementlarning DEL operatori yordamida o'chiramiz:
# car = {'model':'Malibu', 'color':'Red', 'price': 40000} # Oddiy lug'at.
# print(car) # Konsolga chiqaramiz.
# del car['color'] # DEL yordamida 'color' elementini o'chirami bu holatda kalit so'z ham qiymat ham o'chib ketadi.
# print(car) # Natijani konsolga chiqaramiz.

# AMALIYOT TOPSHIRIQLARI.
#1 - otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot
# kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga
# chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# otam = {
#         'ism_sh':'Yorqinjon Maksimov',
#         't_yil': 1970,
#         'yoshi':54,
#         'millati':"o'zbek"
#         }
# onam = {
#         'ism_sh':'Naziraxon Maksimova',
#         't_yil': 1977,
#         'yoshi':47,
#         'millati':"o'zbek"
#         }
# akam = {
#         'ism_sh':'Mamatoji Abdurashidov',
#         't_yil': 1995,
#         'yoshi':29,
#         'millati':"o'zbek"
#         }
# ayolim = {
#         'ism_sh':'Mavludaxon Abdurashidova',
#         't_yil': 2003,
#         'yoshi':21,
#         'millati':"o'zbek"
#         }
# print(f"Mening dadam {otam['ism_sh']}, {otam['t_yil']}-yilda tug'ilgan va yoshi {otam['yoshi']}da millati {otam['millati']}.\n")
# print(f"Mening dadam {onam['ism_sh']}, {onam['t_yil']}-yilda tug'ilgan va yoshi {onam['yoshi']}da millati {onam['millati']}.\n")

#2 - Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# s_taomlar = {
#     'men':'shirguruch',
#     'ayolim':'sho\'rva',
#     'onam':'mastava',
#     'otam':'farqi yo\'q'
#     }
# print(f"Mening sevimli taomim {s_taomlar['men']},\n Ayolimning sevimli taomi {s_taomlar['ayolim']},\n\
#       Onamning sevimli taomlari {s_taomlar['onam']},\n Dadamga bo'lsa {s_taomlar['otam']}.")
      
#3 - Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# python = {
#     'int':'Butun son',
#     'float':'O\'nlik son',
#     'string':'Matn',
#     'list':'Ro\'yxat',
#     'tuple':'O\'zgarmas ro\'yxat',
#     'bool':'Mantiqiy ma\'lumot turi',
#     'dict':'Lug\'at',
#     'for':'Uchun',
#     'in':'Ichida',
#     'not in':'Ichida emas',
#     'if':'Agar'
#     }

#4 - Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
# print("Lug'atimizda quyidagi elementlar bor (int, float, string, list, tuple, bool, dict, for, in, not in, if) \
# sizga qaysinisi haqida ma'lumot kerak?'\n")
# python = {
#     'int':'Butun son',
#     'float':'O\'nlik son',
#     'string':'Matn',
#     'list':'Ro\'yxat',
#     'tuple':'O\'zgarmas ro\'yxat',
#     'bool':'Mantiqiy ma\'lumot turi',
#     'dict':'Lug\'at',
#     'for':'Uchun',
#     'in':'Ichida',
#     'not in':'Ichida emas',
#     'if':'Agar'
#     }            
# soz = input("Yuqoridagi lug'atdan istalgan malumot turini kiriting: ")
# print(python.get(soz, "Bunday ma'lumot turi yo'q!"))

#5 - Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
# print("Lug'atimizda quyidagi elementlar bor (int, float, string, list, tuple, bool, dict, for, in, not in, if) \
# sizga qaysinisi haqida ma'lumot kerak?'\n")
# python = {
#     'int':'Butun son',
#     'float':'O\'nlik son',
#     'string':'Matn',
#     'list':'Ro\'yxat',
#     'tuple':'O\'zgarmas ro\'yxat',
#     'bool':'Mantiqiy ma\'lumot turi',
#     'dict':'Lug\'at',
#     'for':'Uchun',
#     'in':'Ichida',
#     'not in':'Ichida emas',
#     'if':'Agar'
#     }    


# soz = input("Yuqoridagi lug'atdan istalgan ma'lumot turini kiriting: ")
# tarjima = python.get(soz)
# if tarjima == None:
#     print("Lug'atimizda bunday so'z yo'q!")
# else:
#     print(f"Siz so'ragan {soz} soz'ining ma'nosi {tarjima}.")

# 10 - DARS TUGADI.