# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:22:35 2025

@author: DavrServis
"""

# 4 - DARS.
# SONLAR.

# Pythonda sonlarning bir necha turlari bor,quyida ular bilan birma-bir tanishamiz.

# INTEGER (BUTUN SONLAR).
# a = 20 # Sonlar musbat
# b = -30 # manfiy
# c = 0 # 0ga teng bo'lishi mumkin.
# d = a+b
# print(d)

# KVADRAT YUZINI HISOBLAYMIZ.
# k_tomoni = 20 # Kvadrat tomonlari 20 ga teng ekan.
# k_yuzi = k_tomoni ** 2 # Yani bu yerda 2*2 dek gab k_tomonlarini darajaga oshirib qoyamiz va jvadrat yuzini olamiz.

#O'NLIK SONLAR.FLOATS (SUZUVCHI NUQTALI SONLAR).
# Bu sonlarni misol orqali tushunishga harakat qilamiz.
# pi = 3.14159 # O'nlik son (float).
# radius = 10 # Butun son. 
# diametr = 2 * radius # Aylana diametrini topish uchun radiusni 2ga ko'paytiramiz.
# print("Aylana uzunligu", pi * diametr, "ga teng.") # Bu qadam orqali biz aylana uzunligini toptik (pi * diametr) orqali.

# BUTUN SONDAN O'NLIK SONGA.
# Avval aytkanimizdek ikkita butun sonni bo'lish bizga doim natijada o'nlik son beradi(natija butun bo'lsa ham).
# a = -20 # Butun son.
# b = 10 # Butun son.
# c = a/b # Bo'lamiz.
# print(c) # Natija o'nlik son ko'rinishida chiqadi(-2.0).

# Shuningdek butun va o'nlik son o'rtasidagi har qanday arifmetik amallarning natijasi ham o'nlik son bo'ladi.
# a = 10 
# b = 2.0
# print(a+b) # Natija 12.0.
# print(a-b) # Natija 8.0.
# print(a*b) # Natija 20.0.
# print(a/b) # Natija 5.0. Shu ko'rinishda.

# UZUN SONLARNI KIRITISH. 
# Uzun sonlarni kiritishda (_) pastki chiziqdan foydalanishimiz mumkin. Python pstki chiziqni (_) son tarkibida
# inobatga olmasdan uzun sonligicha qabul qiladi, ammo bu bizga qulaylik yaratadi va sonlarni kiritishda tushunarliroq
# harakat qilishimizga yordam beradi.
# aholi_soni = 33_580_000
# print("O'zbekistonda aholi soni", aholi_soni, "dan ortiqroqni tashkil qiladi.") # Bu yerda son 33580000 ko'rinishida chiqadi.

# KONSTANTA.
# Aksar dasturlash tillarida o'zgarmas qiymat (KONNSTANTA) lar mavjud. Misol uchun (π = 3.14159) doimiy holatda.
# Pythonda konstanta tushunchasi yo'q va bunday o'zgarmas qiymatlar kiritish uchun bosh harflardan foydalanilari(PI).
# PI = 3.14159 # KONSTANTA.
# radius = 21.1   

# BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH.
# Birdaniga bir nechta o'zgaruvchiga qiymat berish uchun o'zgaruvchilar va ularga mos qiymatlar vergul (,) bilan
# ajratiladi: Quyida buni ko'rib chiqamiz.
# x, y, z = 12, 234, 254 # Shu ko'rinishda.
# print(x, y, z)

# Bu usulni istalgan turdagi o'zgaruvchiga qo'llashimiz mumkin.
# yosh, ism = 36, "Nurulloh"
# print("Meni ismim", ism, ", yoshim esa ", yosh, "da")

#O'ZGARUVCHILAR TURINI ALMASHTIRISH.
# ism = "Jobir"
# yosh = 30
# xabar = ism + ' ' + yosh + 'yoshda'
# print(xabar) # Bu yerda xatolik yuz beradi va bu xatolik shundan iboratki int tipidagi ma'lumotni str tipidagi
# ma'lumotga qo'shib bo'lmasligi haqida. Buni to'g'irlash uchun quyidagicha yo'l tutamiz.
# xabar = ism + ' ' + str(yosh) + 'yoshda' # Bu yerda yoshni str ga tenglab oldik.

#O'ZGARUVCHI TURINI TEKSHIRISH.
# O'zgaruvchilarni tekshirish bizga yuqoridagi singari xatolarni oldini olish imkonini beradi va bu dasturda
# o'zgaruvchilar soni ko'payib ketkanda ham ish beradi.
# ism = "Jobir"
# yosh = 36
# print(type(yosh)) # Bu yerda yosh ning tipini.
# print(type(ism)) # Bu yerda esa ism ning tipini aniqladik.

# .INPUT() va SONLAR.
# Avvalgi bo'limda o'rganganimiz .input("") foydalanuvchidan qandaydir ma'lumot so'rash. Kelin foydalanuvchidan 
# tug'ilgan yilini so'ragan holda uni yoshini hisoblab ko'ramiz.
# tyil = input("Itimos tug'ilgan yilingizni kiriting: ") # Foydalanuvchini tug'ilgan yilini so'raymiz.
# yosh = 2024 - tyil # Joriy yildan ayiramiz tug'ilgan yilini yoshi kelib chiqadi bu teskarisiga ham ishlaydi yani 
# tug'ilgan yilini topish uchun ham.
# print(f"Siz {yosh}da ekansiz.") # Natijani chiqaramiz.Va bu yerda xatolik beradi. Uni tarjima qilsak int tipidan
# str tipidagi malumotni ayirib bo'lmaydi degan hulosa hosil bo'ladi. Gap shindaki .input() o'ziga kiritilgan har qanday
# qiymatni str ko'rinishida qabul qiladi.

# Bu kodni to'gri yozish uchun esa quyidagicha yo'l tutamiz.
# tyil = int(input("Iltimos tug'ilgan yilingizni kiriting: ")) # Foydalanuvchini tug'ilgan yilini so'raymiz, va uni int
# butun son korinishida saqlaymiz.
# yosh = 2024 - tyil # Joriy yildan tug'ilgan yilni ayiramiz.
# print(f"Sizning yoshingiz {str(yosh)} da ekan.") # Ntijani chiqarishta yoshni tipini str ga o'tkazamiz va tayyor.

# AMALIYOT TOPSHIRIQLARI.
#1 - Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur.
# son = float(input("Istalgan soningizni kiriting:"))
# print(f"Kiritilgan {son} sonining kvadrati = {son**2}.")
# print(f"Kiritilgan {son} sonining kubi = {son**3}.")

#2 - Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur.
# yosh = int(input("Yoshingiz nechchida? "))
# print(f"Siz {2024 - yosh}-yilda tug'ilgan ekansiz.")

#3 - Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va
# bo'linmasini chiqaruvchi dastur
# print("Istalgan ikki sonni kiriting!")
# bson = float(input("Birinchi sonni kiriting: "))
# ison = float(input("Ikkinchi sonni kiriting: "))
# print(bson + ison)
# print(bson - ison)
# print(bson * ison)
# print(bson / ison)

# 4 - DARS TUGADI.