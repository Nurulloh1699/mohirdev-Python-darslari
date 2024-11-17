# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:19:30 2024

@author: DavrServis
"""

#12-dars Lug'at bilan ishlaymiz.
#24.10.2024.
#Muallif:Abdurashidov Nurulloh.

# O'tkan darsni bir eslab o'tamiz.

# talaba_0 = {
#     'ism':'Nurulloh',
#     'familya':'Abdurashidov',
#     'yosh':'25',
#     't_yil':'1999',
#     'fakultet':'KIF',
#     'kurs':'5'
#     }
# print(talaba_0)

# .items() metodi orqali kalitlar va qiymatlarni to'liq holda chiqaramiz va ularni tartiblaymiz.

# for key, value in talaba_0.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value}")
    
# Lug'at elementlarini for tsikli orqali chiroyli qilib konsolga chiqarishni ko'rib chiqamiz.
# telefonlar ={
#     'ali':'iphone x',
#     'vali':'mi not 9 pro',
#     'shodi':'nokia',
#     'polvon':'samsung'
#     }
# for k,q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q.title()}")

# Endi .keys() metodini ko'rib chiqamiz. Bu metod orqali lug'at elementlarini faqat
# kalitlarini chaqirib olishimiz mumkin.
# mahsulotlar = {
#     'olma':10000,
#     'nok':18000,
#     'shaftoli':25000,
#     'uzum':5000,
#     'anjir': 30000  }  
# print(mahsulotlar.keys())    
    
# Endi yuqoridagilarni ham chiroyli qilib konsolga chiqarib olamiz.
# print("Do'konimizdagi mahsulotlar: ")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
    
# Yuqoridagi kodda biz .keys() metodidan foydalanishim bu ixtiyoriy narsa.
# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())
    
# Ro'yxat va lug'at elementlarini solishtirib ko'ramiz va foydali dastur tuzamiz.
# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
# Yuqoridagi kodga qo'shimcha qilib yana kodlar yozishimiz mumkin.
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Vay {buyum} yo'q ekan, Iltimos do'koningizga {buyum} ham olib kelin.")
# Ro'yxat ichidagi elementlar biz qaysi tartibda kiritsak osha tartibda qoladi va buni biz
# .sorted() funksiyasi yordamida alifbo ketma-ketligida chiqarishimiz mumkin.
# print("Do'konimizdagi mahsulotlar ro'yxati:")
# for mahsulot in sorted(mahsulotlar):
        
#     print(mahsulot.title())
    
# Biz o'zimizga kerak bo'lganda faqat kalit so'zlarni emas balki qiymatlarni ham konsolga
# chiqarishimiz mumkin, buning uchun biz .values() metodidan foydalanamiz.
# print(telefonlar.values())

# Buni biroz tushunarliroq qilib yozamiz.
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel.title())

# Deylik bizning lug'atimizda koproq odam bor va ularning bir nechtasi bir hil telefon tutadi
# bu bir hillikni bartaraf qilish uchun esa biz .set() funksiyasidan foydalanamiz.
# telefonlar ={
#     'ali':'iphone x',
#     'vali':'mi not 9 pro',
#     'shodi':'nokia',
#     'polvon':'samsung',
#     'maryam':'samsung',
#     'hoji':'nokia',
#     'asal':'iphone x'
#     }    
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel.title()) 

# print('Foydalanuvchilar quyidagi telefonlardan foydalanishadi:')
# for tel in set(telefonlar.values()):
#     print(tel.title())   
    
# set ham aslida malumot turi va u ham oz ichida elementlarni saqlashi mumkin.
toys = {"ball","car","ball","car"}
print(toys) # Shu o'rinda albatta setning ozini funksiyasi ishlaydi yani bir hil elementlarni
# tashlab yuboradi va bittasinigina olib qoladi.    
    
# AMALIYOT TOPSHIRIQLARI.
#1 - Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida
# chiroyli qilib konsolga chiqaring. 
# python = {
#     'float': 'o\'nlik son',
#     'in': 'ichida',
#     'bool':'mantiqiy ma\'lumot turi',
#     'not in': 'ichida emas',
#     'int': 'butun son',
#     'str': 'matn',
#     'set': 'not copy',
#     'list': 'ro\'yxat',
#     'print': 'chop etish',
#     'for': 'takrorlash operatori'
#     }    
# for kalit, qiymat in sorted(python.items()):
#     print(f"{kalit.title()}: {qiymat}\n")
    
#2 - Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
# keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
davlatlar = {
    'o\'zbekiston':'toshkent',
    'turkiya':'anqara',
    'amerika':'vashington',
    'rossiya':'maskva',
    'italiya':'rim',
    'qirg\'iziston':'bishkek',
    'braziliya': 'rio-de-janeyro'
    }
    
# print("Davlatlar ro'yxati:")
# for davlat in sorted(davlatlar.keys()):
#     print(davlat.title())

# print("\nPoytaxtlar ro'yxati:")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())    
    
# #3 - Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini
# konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,
# "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.    
# country = input("Qaysi davlatning poytaxtini bilmoqchisiz? ").lower() # Davlat nomini kiritishni
# so'ramoqda, va kiritilgan davlat nomini kichik harflarga o'girib olmaqda.
# capital = davlatlar.get(country) # capitalni davlatlar ichidagi elementlarga tenglab olmaqda.
# if capital == None: # Agar kiritilgan davlat ro'yxatda yo'q bo'lsa yoki davlat haqida ma'lumot
# yo'q bo'lsa. Quyidagi kodni konsolga chiqargin.
#     print(f"Kechirasiz bizda {country} haqida ma'lumot yo'q")
# else:# Aks holda quyidagi kodni konsolga chiqargin.
#     print(f"{country.upper()}ning poytaxti {capital.title()}")
    
# 4 - Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni
# menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda
# "bizda bunday taom yo'q" degan xabarni chiqaring.    
# taomlar = {
#     'osh': 25000,
#     'somsa': 20000,
#     'manti': 7000,
#     'non': 3000,
#     'kompot': 4000,
#     'salat': 7000,
#     'assorti': 10000,
#     'choy': 2000,
#     'kabob': 12000,
#     'tuxum': 5000
#     }

# print("Iltimos 3ta ovqat buyurtma bering: ")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom: ").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in taomlar:
#         print(f"{buyurtma.title()} {taomlar[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz bizda {buyurtma} yo'q")
    
 