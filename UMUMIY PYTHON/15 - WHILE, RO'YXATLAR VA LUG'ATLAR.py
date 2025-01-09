# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 02:14:15 2025

@author: DavrServis
"""

# 15 - DARS.
# WHILE, RO'YXATLAR VA LUG'ATLAR.

# Ro'yxatlar (lug'atlar) bilan ishlashda while siklining foydalari juda ko'p. Misol uchun, foydalanuvchidan bir nechta
# ma'lumotlarni qabul qilib olish, ro'yxatdan takrorlanuvchi qiymatlarni o'chirib tashslash yoki bir ro'yxatni ikkinchi
# ro'yxatga ko'chirishda while siklidan foydalanish mumkin.


# WHILE YORDAMIDA RO'YXATNI TO'LDIRISH.
# Quyidagi dasturga e'tibor bering, avval ismlar degan bo'sh ro'yxat yaratib oldik. Keyin esa while sikli yordamida
# foydalanuvchidan ro'yxatga ism qo'shishni so'rayapmiz. So'ngra foydalanuvchidan yana ism qo'shmoqchi yoki yo'q ekanini so'raymiz 
# va foydalanuvchining javobiga ko'ra yo sikl boshiga qaytamiz, yo siklni to'xtatamiz.
# ismlar = []
# print("Do'stlaringizni ro'yxatini tuzamiz!")
# n = 1
# while True:
#     savol = f"{n} - do'stingizni ismini kiriting: "
#     ism = input(savol).lower()
#     ismlar.append(ism)
#     javob = input("Yana is qo'shasizmi? (ha/yoq): ").lower()
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         break
# print("Ro'yxat tuzildi quyidagi ismlar bor!")
# for i in ismlar:
#     print(i.title())

# WHILE YORDAMIDA LUG'ATNI TO'LDIRISH.
# Yuqoridagi usul bilan while sikli yordamida lug'atlarni ham shakllantirishimiz ham mimkin. Quyidagi kodda ism bu kalit, yosh esa
# kalitga mos kelivchi qiyma. WHILE siklining davomiyligi esa ishira qiymatiga bog'liq.
# print("Do'stlaringizni yoshini saqlaymiz!") # Foydalanuvchiga ma'lumot.
# dostlar = {} # Bo'sh lug'at yaratib olamiz.
# n = 1 # n ga 1 qiymat beramiz. 
# ishora = True # Ishora ham qo'shib olamiz va True qiymat beramiz.
# while ishora: # WHILE sikli ishoraning qiymatiga qarab davom etadi. Yani u True bo'lsa ishlaydi va aksincha False bo'lsa to'htaydi.
#     ism = input("Do'stingizni ismini kiriting: ") # ism degan o'zgaruvchi. Keyinchalik undan kalit so'z sifatida foydalanamiz.
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ") # yosh degan o'zgaruvchi ism degan o'zgaruvchining qiymati bo'ladi.
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat. Lug'at elementlarini shakllantirib oldik.
    
#     javob = input("Yana ma'lumot qo'shasizmi: (ha/yo'q) ") # Foydalanuvchidan so'raymiz, yangi elementlar qo'shamizmi ha/yo'q
#     if javob == "yo'q": # Agar javob yo'q bo'lsa.
#         ishora = False # Ishora qiymati False ga o'zgaradi. Natijada dastur tugaydi.
    
# print("Do'stlaringiz haqidagi ma'lumotlar tayyor:")
# for ism, yosh in dostlar.items(): # for orqali lug'at elementlariga murojaat qilamiz.     
#     print(f"{ism.title()} {yosh} yoshda.") # Ularni chiroyli shaklda konsolga chiqaramiz.

# RO'YXAT ELEMENTLARINI O'CHIRISH.
# Avvalgi darslarimizning birida ro'yxat elementlarini o'chirish uchun .remove(qiymat) metodi bilan tanishgan edik.
# Esingizda bo'lsa, bu metod ro'yxatdan eng birinchi uchragan qiymatni o'chiradi. Agar ro'yxatimizda ma'lum bir qiymat
# bir necha bor takrorlangan bo'lsa, ularning barchasini o'chirish uchun WHILE siklidan foydalanishimiz mumkin:
# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'malibu', 'nexia'] # Oddiy ro'yxat faqat ichida bir xil elementlari bor.
# print(cars) # Konsolda ko'rishimiz mumkin.
# while 'nexia' in cars: # WHILE sikli orqali 'nexia' nomli elementlar ro'yxatda bor ekan degan manodagi sikl yozdik. 
#     cars.remove('nexia') # 'nexia' degan elementni o'chirgin.
# print(cars) # Natijani chiqaramiz.

# RO'TXATDAN RO'YXATGA ELEMENT KO'CHIRISH.
# Tassavur qiling, bizda ma'lum bir ro'yxat bor, biz ro'yxat bor, biz ro'yxatdagi har bir element ustida biror amalni bajarib, 
# uni birinchi ro'yxatdan ikkinchi ro'yxatga ko'chirib olmoqchimiz. Shunday halotlarda WHILE sukli juda qo'l keladi.

# Quyidagi misolni ko'raylik. Bizda talabalar ro'yxati bor. WHILE sikli, toki ro'yxatda talabalar bor ekan, aylanaveradi,
# Sikl ichida biz .pop() metodi yordamida talabaning ismini ro'yxatdan sug'urib oldik va foydalanuvchidan talabani baholashni
# so'radik. Talabaning ismi va bahosini lug'at elementi ko'rinishida saqlab qo'ydik (talaba - kalit, baho - qiymat).
# talabalar = ['hasan', 'husan', 'olim', 'botir'] # Oddiy talabar ro'yxatini yaratib oldik.
# for t in talabalar: # talabalar ro'yxatidagi har bir talaba uchun.
#     print(f"{t.title()}.", end=' ') # Uni konsolga chiqar.
# baholangan_talabalar = {} # Yangi bo'sh lug'at.
# while talabalar: # Toki talabalar ro'yxatida element borakan.
#     talaba = talabalar.pop() # Har bir talabani talabalar ichidan sug'urib olyapmiz.
#     baho = input(f"\n{talaba.title()}ning bahosini kiriting: ") # Foydalanuvchidan talabaga baho qo'yishini so'rayapmiz.
#     print(f"{talaba.title()} baholandi!") # Foydalanuvchi talabani baholasa shu talab baholandi degan habarni chiqaryapmiz.
#     baholangan_talabalar[talaba] = baho # Hosil bo'lgan ikkita o'zgaruvchini (talab va baho) baholangan_talabalar degan
# # o'zgaruvchiga lug'at ko'rinishida joylayapmiz.
# for talaba, baho in baholangan_talabalar.items(): # Hosil bo'lgan lug'atimizni elementlariga murojaat qilgan holda.
#     print(f"\n{talaba.title()}ning bahosi: {baho}!") # Ularni konsolga chiqaryapmiz.
    
# AMALIYOT TOPSHIRIQLARI.
#1 - Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# print("Foydalanuvchidan buyurtmalarni qabul qilib oluvchi dastur.")
# buyurtmalar = []
# n = 1
# while True:
#     buyurtma = input(f"{n} - buyurtmani kiriting: ")
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana biror nima buyurtma berasizmi? (ha/yo'q): ")
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         break
# print(f"Buyurtmalar qabul qilindi ular bilan tanishing:")
# for buyurtma in buyurtmalar:
#     print(f"{buyurtma.title()}")

#2 - e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir
# nechta elementlar (mahsulot va uning narhi) kiritishni so'rang. 
# print("e-bozor mahsulotlarini ro'yxatini tuzamiz!")
# mahsulotlar = {}
# n = 1
# while True:
#     mahsulot = input(f"{n} - mahsulotni kiritng: ")
#     narh = input(f"{mahsulot.title()}ni narhini kiriting: ")
#     print(f"{mahsulot} ro'yxatga qo'shildi!")
#     mahsulotlar[mahsulot] = narh
#     javob = input("Yana mahsulot kiritasizmi? (h/y): ")
#     if javob == 'h':
#         n += 1
#         continue
#     else:
#         break
    
# print("e-bozor mahsulotlari ro'yxati tuzildi:")
# for mahsulot, narh in mahsulotlar.items():
#     print(f"{mahsulot.title()}ning narhi - {narh} so'm!")
    
#3 - Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar
# bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring,
# aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# buyurtmalar = ["o'rik", "shaftoli", "olma"] # Foydalanuvchi kerakli mahsulotlar ro'yxati.
# mahsulotlar = { # Mahsulotlar ro'yxati (LUG'AT KO'RINISHIDA).
#     'olma': 20000,
#     'anjir': 40000,
#     'shaftoli': 37000,
#     'uzum': 50000,
#     'qovun': 12000,
#     'tarvuz': 7000,
#     }

# while buyurtmalar: # Toki buyurtmalar ichida element bor ekan 
#     buyurtma = buyurtmalar.pop() # Buyurtmalar ichidagi har bir buyurtmani sug'urib ol.
#     if buyurtma in mahsulotlar.keys(): # Sug'urib olingan buyurtma mahsulotlar lug'atining kalitlari ichida bo'lsa 
#         narh = mahsulotlar[buyurtma] # Xuddi shu mahsulotni qiymatini, yani narhini yangi NARH degan o'zgaruvchiga yuklagin.
#         print(f"{buyurtma.title} - {narh} so'm") # Natijani chiroyli va tushunarli ko'rinishda chiqaramiz.
#     else: # Aks holda.
#         print(f"Bizda {buyurtma} yo'q!") # Foydalanuvchiga bizda bunday mahsulot yo'qligi haqida ma'lumot beramiz.

# 15 - DARS TUGADI.