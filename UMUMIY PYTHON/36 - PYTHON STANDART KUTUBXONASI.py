# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:51:47 2025

@author: DavrServis
"""

# 36 - DARS.
# PYTHON STANDART KUTUBXONASI.

# Biz o'zimizni dasturimizda turli hil tayyor kutubxonalardan foydalanishimiz mumkin va bu bizga dasturimizda bir necha qulayliklar
# yaratishimiz mumkin.

# Birinchi tanishadigan kutubxonamiz datetime() kutubxonasi bo'ladi. Bu kutubxona orqali biz aniq vaqtni belgilash imkoniga ega bo'lamiz:
# import datetime as dt
# datetime()
# hozir = dt.datetime.now()
# print(hozir)
# Sanani ajratib olish:
# print(hozir.date())
# Vaqtni o'zini ajratib olish:
# print(hozir.time())
# Soatni o'zini ajratib olish:
# print(hozir.hour)
# Minutni o'zini ajratib olish:
# print(hozir.minute)
# Sekundlarni o'zini ajratib olish:
# print(hozir.second)

# datetime ni ichida yana bitta maxsus obyekt bor date deb ataladi va faqat sanani ko'rsatadi:
# date()
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")

# Endi masalan biz alohida sana yaratmoqchi bo'lsam nima qilaman:
# ertaga = dt.date(2025, 1, 16)
# print(f"Ertangi sana: {ertaga}")

# Endi biz time ni ko'rib chiqamiz yani yaxlit soat:
# time()
# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozirgi soat: {vaqtHozir}")
# vaqtKeyin = dt.time(23, 45, 30)
# print(f"Keyingi vaqt: {vaqtKeyin}")

# Sanalar orasidagi farqni qanday topamiz? Buning uchun oddiy - airuv amalidan foydalanamiz:
# bugun = dt.date.today()
# ramazon = dt.date(2025, 2, 20)
# farq = ramazon - bugun
# print(farq)
# Agar etibor bersak, natija obyekt ko'rinishida hosil bo'ldi va buni yahlitlash uchun biz quyidagicha yo'l tutamiz:
# farq.days # kunni yahlitlab oldik.
# print(f"Ramazonga {farq.days} kun qoldi!")

# Soatlar orasidagi farqni ko'ramiz:
# hozir = dt.datetime.now()
# futbol = dt.datetime(2025, 1, 16, 23, 45, 00)
# farq = futbol - hozir
# print(farq)
# sekundlar = farq.seconds
# print(sekundlar)
# Sekundlardan minutlarni hisoblashimiz mumkin:
# minutlar = int(sekundlar/60)
# print(minutlar)
# Soatlar ham shu tartibda topiladi.
# soatlar = int(minutlar/60)
# print(soatlar)

# Bu date kutubxonasi edi:
    
# Endi math kutubxonasi bilan tanishamiz:
# import math

# PI  = math.pi
# print(f"PI ning qiymati: {PI}")
# E = math.e
# print(f"e ning qiymati: {E}") 

# Trigonometriyaga oid funksiyalar:
# math.sin(math.pi/2)
# math.cos(0)
# math.tan(PI)

# Radianlar va burchaklar o'rtasida konvertatsiya
# print(math.degrees(math.pi/2)) # Radian qiymat berilgan burchak qiymatni qaytaradi.
# print(math.radians(90)) # Burchak qiymat bersak radiandagi qiymatlarni qaytaradi.

# Logorifmik funksiyalar:
# Natural logorifm.
# math.log(5)
# 10 asosli logarifm.
# math.log(100)

# Sonlarni yaxlitlash:
# x = 4.6
# print(math.ceil(x)) # Yuqoriga yaxlitlash.
# print(math.floor(x)) # Pastka tomon yaxlitlash.
# round funksiyasi sonni eng yaqin butun songa yaxlitlaydi.
# print(round(x))

# Kvadrat ildiz:
# x = 81
# math.sqrt(x)

# Darajaga oshirish:
# math.pow(x, 3) # x ning kubi.
# math.pow(x, 5) # x ning 5-darajasi.
# math.pow(x, 1/3) # x dan kub ildiz


# Endigi foydali modul pprint moduli va bu modul bilan biz uzundan-uzun matnlarni chiroyli qilib chiqarish uchun foydalanamiz.
# from pprint import pprint
# import json

# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)
    
# print(bemor) # Oddiy print
# pprint(bemor) # PPrint

# import requests
# r = requests.get('https://api.github.com')

# print(r.json())
# pprint(r.json())

# Navbatdagi modul RegEx (RegularExpressions) bu moduldan odatda andozalar ya'ni matnlarni izlash uchun andoza yaratish uchun ishlatiladi.
# import re 
# from word_list import words
# word1 = "темир"
# word2 = "томир"
# word3 = "тулпор"

# andoza = "^т...p$" # Bu o'rinda biz andoza uchun shartlar berdik desak bo'ladi ya'ni bosh harf т va ohirgi harf р bo'lsin deganday.

# print(re.match(andoza, word1)) 
# print(re.match(andoza, word2))
# print(re.match(andoza, word3)) 

# matches = []

# Bu o'rinda tayyoe andozalar olish uchun iHateRegex saytiga kirilsa bu yerda tayyor andozalar olish mumkin.
# Quyida biz bir nechtasini ko'rib chiqamiz:
    
# Tasavvur qiling biz ma'lum bir matning ichidan bizning andozamizga mos matnni sug'urib olmoqchimiz:
# import re
# matn = "Bugungi kun juda qiziqarli o‘tdi, lekin hali ham koʻp ish qilish kerak. Agar qo‘shimcha ma'lumot kerak boʻlsa, menga yozing:\
#     info.random123@gmail.com. \
# Yana bir muhim voqea haqida xabar berishni unutibman. Biz har kuni bir narsa o‘rganamiz, to‘g‘rimi? Bog‘lanish uchun:\
#     contact_me456@outlook.com."

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza, matn)
# print(email)


# Endi parol uchun andoza tayorlaymiz:
# andoza = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
# msg = "Yangi parol kiriting"
# msg += "(kamida 8ta belgidan iborat, kamida 1ta Lotin bosh harf, 1ta kichik harf, "
# msg += "1ta son va 1ta maxsus belgi bo'lishi kerak): "

# while True:
#     password = input(msg)
#     if re.match(andoza, password):
#         print("Maxfiy so'z qabul qilindi!")
#         break
#     else: 
#         print("Maxfiy so'z talabga javob bermadi!")


# AMALIYOT TOPSHIRIQLARI:
#1 - Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring:
# from datetime import datetime, timedelta # Sana va vaqt bilan ishlash uchun kerakli kutubxonalarni import qilib olamiz.

# # Bugungi sana:
# bugungu_sana = datetime.now() # Hozirgi vaqtni olib, bugungi_sana o'zgaruvchisiga saqlaymiz.
# # 2 haftalik farq bilan 10ta sana:
# for i in range(10): # 10ta iteratsiya uchun siklni ishga tushiramiz.
#     yangi_sana = bugungu_sana + timedelta(weeks = 2 * i)
#     print(yangi_sana.strftime('%Y-%m-%d')) # Yangi sana 'YYYY-MM-DD' formatida konsolga chiqadi.

# Natija: 2025-01-16
        # 2025-01-30
        # 2025-02-13
        # 2025-02-27
        # 2025-03-13
        # 2025-03-27
        # 2025-04-10
        # 2025-04-24
        # 2025-05-08
        # 2025-05-22
    
#2 - Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring:
# from datetime import datetime # Sana va vaqt bilan ishlash uchun 'datatime' kutubxonasini yuklab olamiz.
# # Ramazon va Qurbon hayiti sanalari:
# ramazon_hayiti = datetime(2025, 3, 31) # Ramazon hayitining sanasi: 2025 - yil 31 - mart.
# qurbon_hayiti = datetime(2025, 6, 28) # Qurbon hayitining sanasi: 2025 - yil 28 - iyun.

# # Bugungi sana:
# bugun = datetime.now() # Hozirgi vaqt va sanani 'datetime.now' funksiyasi orqali bugun o'zgaruvchisiga yuklaymiz.

# # Kunning farqini hisoblash:
# ramazon_kunlari_qoldi = (ramazon_hayiti - bugun).days # Ramazon hayitigacha qolgan kunlar.
# qurbon_kunlari_qoldi = (qurbon_hayiti - bugun).days # Qurbon hayitigacha qolgan kunlar.

# # Natijani konsolga chiqarish:
# if ramazon_kunlari_qoldi >= 0: # Agar Ramazon hayitigacha qolgan kunlar 0 yoki undan katta bo'lsa.
#     print(f"Ramazon hayitigacha {ramazon_kunlari_qoldi} kun qoldi!") # Konsolga qolgan kunlar chiqadi.
# else: # Aks holda (hayit o'tib ketkan bo'lsa)
#     print("Ramazon hayiti o'tib ketkan!") # Ramazon hayiti o'tib ketkanligi haqidagi xabar konsolga chiqarilsin.
    
# if qurbon_kunlari_qoldi >= 0:
#     print(f"Qurbon hayitigacha {qurbon_kunlari_qoldi} kun qoldi!")
# else:
#     print("Qurbon hayiti o'tib ketkan!")

# Natija: Ramazon hayitigacha 73 kun qoldi!
        # Qurbon hayitigacha 162 kun qoldi!
        
#3 - Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing
# from datetime import datetime
# def hisobla_tugilgan_kun(tugilgan_sana):
#     """Tug'ilgan kundan boshlab bugungi sanagacha qancha yil, oy va kun o'tganini hisoblaydi.
    
#     Args:
#         tug'ilgan_sana (datetime): Tug'ilgan sana (datetime formatida).
        
#     Returns:
#         tuple: (yillar, oylar, kunlar)
#     """
#     bugun = datetime.now() # Hozirgi vaqt va sanani olamiz.
#     yil_farq = bugun.year - tugilgan_sana.year # Yillar farqini hisoblaymiz.
#     oy_farq = bugun.month - tugilgan_sana.month # Oylardagi farqni hisoblaymiz.
#     kun_farq = bugun.day - tugilgan_sana.day # Kunlar farqini hisoblaymiz.
    
#     # Agar oylarda yoki kunlarda manfiy qiymat bo'lsa, tegishli tuzatish kiritamiz:
#     if kun_farq < 0:
#         oy_farq -= 1
#         oldingi_oy_kunlari = (bugun.replace(day = 1) - timedelta(days = 1)).day
#         kun_farq += oldingi_oy_kunlari
        
#     if oy_farq < 0:
#         yil_farq -= 1
#         oy_farq += 12
        
#     return yil_farq, oy_farq, kun_farq

# # Tug'ilgan sana:
# tugilgan_sana = datetime(1999, 3, 16)

# # Hisoblash:
# yil, oy, kun = hisobla_tugilgan_kun(tugilgan_sana)

# # Natijani chiqarish:
# print(f"Siz tug'ilganingizdan boshlab {yil} yil, {oy} oy, {kun} kun o'tdi!")

# Natija: Siz tug'ilganingizdan boshlab 25 yil, 10 oy, 2 kun o'tdi!

#4 - Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring:
# import re  # Regular expression kutubxonasini import qilamiz.

# def telefon_raqamini_tekshirish(raqam):
#     """
#     Telefon raqamini O'zbekiston andozasi bo'yicha tekshiradi.
    
#     Args:
#         raqam (str): Telefon raqami.
    
#     Returns:
#         bool: True, agar raqam andozaga mos bo'lsa, aks holda False.
#     """
#     # O'zbekiston telefon raqamlari andozasi:
#     # +998 XX XXX XX XX yoki 998XX XXX XX XX
#     andoza = r"^\+998\s\d{2}\s\d{3}\s\d{2}\s\d{2}$|^998\d{2}\s\d{3}\s\d{2}\s\d{2}$"
#     # Yuqoridagi andoza:
#     # - ^ bilan boshlanadi: satr boshidan boshlanishini bildiradi.
#     # - \+998: Raqam "+998" bilan boshlanishi kerak.
#     # - \s: Bo'sh joy (masalan, ' ').
#     # - \d{2}, \d{3}, \d{2}, \d{2}: raqamlar ketma-ketligi (masalan, XX, XXX, XX, XX).
#     # - |: "yoki" (OR) operatori, boshqa formatni qabul qilish imkonini beradi.
#     return bool(re.match(andoza, raqam))  # Raqamni andoza bilan tekshiramiz. True yoki False qaytaradi.

# # Foydalanuvchidan raqam kiritishni so'rash
# raqam = input("Telefon raqamingizni kiriting (+998 XX XXX XX XX): ").strip()
# # .strip() qo'shilgan bo'lib, kiritilgan raqamni bosh va oxiridagi bo'sh joylardan tozalaydi.

# # Tekshirish va natijani chiqarish
# if telefon_raqamini_tekshirish(raqam):  # Agar raqam andozaga mos bo'lsa:
#     print("Telefon raqami to'g'ri kiritilgan.")  # To'g'ri kiritilgan raqam.
# else:  # Agar raqam noto'g'ri formatda bo'lsa:
#     print("Telefon raqami noto'g'ri! Iltimos, andozaga mos ravishda kiriting.")  
#     # Noto'g'ri formatda raqam bo'lsa, xabar chiqariladi.
    
#5 - Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna sifatida foydalanishingiz mumkin:
# Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI

# Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz.
# Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test

import re  # Pythonning regex (regular expressions) moduli matndan mos qatorlarni topish uchun ishlatiladi

def extract_urls(text):
    # URL topish uchun regex ifodasi
    url_pattern = r'https?://\S+'  # "https" yoki "http" bilan boshlanadigan, keyin "//" va probel bo'lmagan har qanday belgilarni qamrab oluvchi moslashuvchan naqsh
    urls = re.findall(url_pattern, text)  # Matndagi barcha mos URLlarni qidirib, ro'yxat sifatida qaytaradi
    return urls  # Ajratilgan URLlarni natija sifatida qaytaradi

# Namuna matn
def text():
    """Misol matn. Ushbu qismda URL-larni o'z ichiga olgan test matni berilgan."""
    return (
        "Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI\n"
        "\nUshbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. "
        "Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"
    )

# Funksiyani chaqirish
urls = extract_urls(text())  # "extract_urls" funksiyasini chaqirib, natijada matndan URLlar ro'yxatini oladi
print("Ajratib olingan URLlar:", urls)  # Ajratib olingan URLlar ro'yxatini konsolga chiqaradi

# Natija: Ajratib olingan URLlar: ['https://youtu.be/vsxJPRLXpgI', 'https://python.sariq.dev/testing/37-klass-test']


# 36 - DARS TUGADI.