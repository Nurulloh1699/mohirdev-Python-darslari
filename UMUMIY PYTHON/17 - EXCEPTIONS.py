# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:25:41 2025

@author: DavrServis
"""

# 17 - DARS.
# EXCEPTIONS.

# Avvalgi bo'limda "Run time error" xatoliklari bilan tanishdik. Bunday xatolar dastur bajarish jarayonida kelib chiqadi va
# dasturning ishlashini to'xtatadi. Sintaksis xatolikdan farqli ravishda, Python bunday xatolarni dasturni bajarishdan avval
# aniqlay olmaydi. Ushbu darsimizda mana shunday xatoliklarni jilovlashni o'rganamiz. Maqsadimiz - xatolik yuz berganda dastur
# to'xtab qolishining oldini olish. Gap shundaki, dastur davomida xato yuz berganda Python maxsus EXCEPTION (istisno) obyektini 
# yaratadi. Agar bu obyekt "tutib" olinmasa, dastur bajarilishdan to'xtaydi.

# TRY-EXCEPT.
# Istisno obyektlarni tutib olish uchun Pythonda maxsus TRY-EXCEPT operatorlari bor. Bu operatorlar quyidagicha ishlaydi.
# TRY operatori badanida bajarish kerak bo'lgan kod yoziladi, EXCEPT operatori badanida esa xatolik sodir bo'lganda bajarilishi
# kerak bo'lgan kod yoziladi. Ya'ni dasturimiz to'xtab qolmasdan bajarilaveradi.

# Tushunarli bo'lishi uchun quyidagi misolni ko'ramiz:
# yosh = input("Iltimos yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2024-yosh} yilda tug'ilgansiz!")

# Yuqoridagi dasturning 1-qatorida biz foydalanuvchidan yoshini kiritishni so'radik. Navbatdagi qatorda esa foydalanuvchi kiritgan
# qiymatni int() funksiyasi yordamida butun songa o'tkazyapmiz. Agar foydalanuvchi kiritganda butun emas, o'nlik son kiritsa bu
# ValueError xatoligiga olib keladi va dastur bajarilishdan to'xtaydi:

# Yoshingizni kiriting: 32.5
# ValueError: invalid literal for int() with base 10: '32.5'

# Mana shunday xatoliklarning oldini olish uchun xato yuz berishi mumkin bo'lgan qatorlarni TRY-EXCEPT bloki yordamida yozamiz.
# Bunda Try bloki ichida bevosita xato keltirib chiqarishi mumkin bo'lgan kodni, EXCEPT bloki ichida esa xatolik yuz berganda 
# bajarilishi kerak bo'lgan buyruqni yozamiz.

# Tushunarli bo'lishi uchun yuqoridagi dasturni yangidan yoxamiz:
# yosh = input("Iltimos yoshingini kiriting: ")
# try: # Kod to'g'ri ishlaganda bajariladigan soha.
#     yosh = int(yosh) 
#     print(f"Siz {2024-yosh} yilda tug'ilgansiz!")
# except: # Kodda xatolik bo'lganda bajariladigan soha.
#     print("Butun son kiritmadingiz!")
# print("Dastur tugadi!")

# Bu yerda ham dastavval foydalanuvchi yoshini so'radik. int() funksiyasini esa TRY badani ichida yozdik, agar foydalanuvchi
# to'g'ri qiymat kiritgan bo'lsa, kodimiz foydalanuvchining tug'ilgan yilini hisoblab ko'rsatadi, EXCEPT (istisno) yuz berganda 
# esa "Butun son kiritmadingiz" xabarini konsolga chiqaradi. Lekin dastur bajarilishdan to'xtamaydi va TRY-EXCEPT blokidan keyingi 
# qatorlar ham bakarilaveradi (print(Dastur tugadi!)).

# Dasturni tekshiramiz. Boshlanishiga to'g'ri qiymat kiritaylik:
# Iltimos yoshingini kiriting: 25
# Siz 1999 yilda tug'ilgansiz!
# Dastur tugadi!

# Yana bir bor, lekin bu safar o'nlik son kiritamiz:
# Iltimos yoshingini kiriting: 32.5
# Butun son kiritmadingiz!
# Dastur tugadi!   

# TRY-EXCEPT operatorining afzalliklaridan biri - foydalanuvchiga Python ko'rsatadigan tushunarsiz xatolar o'rniga o'zimiz istagan,
# tushunarliroq matnni ko'rsatish imkonini beradi. Shuningdek, kompleks tizimlarda arzimagan xatoni deb dasturimiz to'xtab
# qolishining oldini oladi.

# TRY-EXCEPT-ELSE.
# Yuqoridagi kodimizda vi TRY moduli ichida xato qaytarishi mumkin bo'lgan ifodani ham (yosh = int(yosh)), xato qaytarmaganda
# bajarilishi kerak bo'lgan ifodani ham (print(f"Siz {2024-yosh} yilda tug'ilgansiz!")) deb birdan yozib ketyapmiz. Aslida bunday
# qilishimiz to'g'ri emas. 

# To'g'ri usuli - avval xatoga tekshirish va xato yuz bermaganda bajariladigan ifodani alohida, ELSE blokida yozish:
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except:
#     print("Butun son kiritmadingiz!")
# else:
    # print(f"Siz {2024-yosh} yilda tug'ilgansiz!")
    
# Yoshingizni kiriting: 21
# Siz 2003 yilda tug'ilgansiz!

# MA'LUM TURDAGI XATOLARNI USHLASH.
# Xatolarning turlari ko'p, EXCEPT operatori yordamida biz aynan qaysi xatolarni ushlamoqchi ekanimizni ham ko'rsatishimiz mumkin.
# Misol uchun, yuqoridagi misolda int() funksiyasi ValueError xatosini qaytardi. Agar biz faqatgina shu turdagi xatolarni
# ushlamoqchi bo'lsak, EXCEPT operatoridan so'ng xatolik nomini ham ko'rsatamiz:
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2024 - yosh} yilda tug'ilgansiz!")
# Natija: Butun son kiritmadingiz
# Shu yo'sinda boshqa xatolarni ham tutib olish mumkin.

# ZeroDivisionError.
# x, y = 5, 10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0ga bo'lib bo'lmaydi!")
# Natija: 0ga bo'lib bo'lmaydi!

# IndexError.
# mevalar = ['olma', 'anor', 'anjir', 'uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva  bor xolos!")
# Natija: Ro'yxatda 4 ta meva  bor xolos!

# KeyError.
# Bu xatolik lug'atda mavjud bo'lmagan kalitga murojaat etishda kelib chiqadi:
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"998971234567"}
# key = "tel"
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas!")
# Natija: Bunday kalit mavjud emas!   

# FileNotFoundError.
# Bu xatolik Pythonda fayllar bilan ishlashda mavjud bo'lmagan faylga murojaat etish ortidan kelib chiqadi. Biz fayllar bilan 
# ishlash haqida kelgusi boblarda to'xtalamiz, bu bo'limda esa shunday xatolikni ushlashni ko'ramiz, xolos:
# fayl = "data.txt" # Bunday fayl aslida mavjud emas.
# try: # Faylni ochishga harakat qilamiz.
#     f = open(fayl)
# except FileNotFoundError:
#     print(f"{fayl} fayli mavjud emas!")
# Natija: data.txt fayli mavjud emas!

# BIR NECHTA XATOLARNI USHLASH.
# TRY-EXCEPT ketma-ketligida bir nechta EXCEPT operatorlari ham bo'lishi mumkin. Ularning har biri ma'lum turdagi xatolik uchun
# javobgar bo'ladi:
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20 / n
# except ValueError: # Foydalanuvchi butun son kiritmasa.
#     print("Butun son kiritmadingiz!")
# except ZeroDivisionError: # Foydalanuvchi 0 sonini kiritsa.
#     print("0ga bo'lib bo'lmaydi!")
# else:
#     print(f"x = {x}")
# Natija: Butun son kiriting: 2.4
# Butun son kiritmadingiz!    

# Natija: Butun son kiriting: 0
# 0ga bo'lib bo'lmaydi!

# Natija: Butun son kiriting: 10
# x = 2.0 

# XATOLARNI KO'RSATMAY O'TISH.
# Yuqoridagi misollarda kodimiz xato qaytarganida dasturimiz foydalanuvchiga xatolik haqida ma'lumot ko'rsatyapti. Agar dastur 
# hech qanday ma'lumot ko'rsatmay, dasturni davom etishi talab qilinsa except badanida pass operatorini yozamiz.
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"998971234567"}
# key = "tel"
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     pass

# Umuman olganda, pass hech narsa bajarmasa-da, juda foydali operator. Bu operator yordamida biz funksiyalar, sikllar yoki IF-ELSE
# shartlarining badanini vaqtincha to'ldirib turishimiz mumkin. Misol uchun, siz dasturning skeletini o'ylab qo'ydingiz, qanday 
# sikllar yoki shartlar bo'lishini reja qildingiz, lekin bevosita sikl yoki funksiya badanini yozishga yetib kelmagan bo'lsangiz,
# IndentationError xatoligining oldini olish uchun pass operatoridan foydalanasiz.
# if yosh < 20:
#     pass
# else:
#     pass

# if yosh < 20:

# else:

# XATOLARNING OLDINI OLISH.
# Yuqoridagi xatolar yuz berganda ularni ushlash va dastur to'xtashining oldini olishni ko'rib chiqtik. Lekin TRY-EXCEPT
# ketma-ketligi xatolarning oldini olishga yordam bera olmaydi. Xatolarning oldini olish uchun IF-ELSE va WHILE sikllaridan
# foydalanganimiz afzal. 

# Avvalgi bo'limdagi misolimizga qaytsak:
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh) # Xato qaytargan kod.
#     print(f"Siz {2024 - yosh} - yilda tug'ilgansiz!")
# except: # Xato yuz berganda bajariluvchi kod.
#     print("Butun son kiritmadingiz.")
    
# Biz foydalanuvchi yoshini so'radik va foydalanuvchi butun son kiritmagani sababli dasturni to'xtatdik. Aslida, bunday holatda
# WHILE sikli yordamida foydalanuvchi to'g'ri qiymat kiritgunga qadar uning yoshini qayta qayta so'rash to'g'riroq yechim bo'ladi:
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2024 - yosh} - yilda tug'ilgansiz!")
# Natija: Yoshingizni kiriting: 32.5
# Natija: Yoshingizni kiriting: 12.4
# Natija: Yoshingizni kiriting: 24.9
# Natija: Yoshingizni kiriting: 25
# Siz 1999 - yilda tug'ilgansiz!

# .isdigit() metodi = foydalanuvchi kiritgan matn yoki oldindan o'zgaruvchiga yuklangan matn faqatgina sonlardan iborat ekanini
# tekshiradi.

# ETIBOR BERING, foydalanuvchi kiritgan matn faqatgina sonlardan iborat ekanligini tekshirish uchun .isdigit() metodidan
# foydalandik.
        
# Ko'rib turganingizdek, biz dastavval 32.5 qiymatini kiritdik va matn tarkibida nuqta belgisi bo'lgani uchun .isdigit("32.5")
# metodi False qaytardi va siklimiz bishiga qaytdi. Biz yana 2 marta xato qiymat kiritdik va har gal sikl boshidan takrorlandi.
# 4 - urunishda 25 qiymatini kiritganimiz sababli .isdigit("25") metodi True qaytardi, siklimiz to'xtadi va "Siz 1999 - yilda 
# tug'ilgansiz!" degan natija konsolga chiqdi.

# Albatta yuqoridagi usul barcha xatolar ushlamaydi. Shunday xatolar bo'lishi mumkinki, biz ularni oldindan to'g'irlay olmasligimiz 
# mumkin yoki xato foydlanuvchiga bog'liq bo'lmasligi mumkin. Shunday holatlarda TRY-EXCEPT operatorlari bizning xaloskorimizga 
# aylanadi.

# AMALIYOT TOPSHIRIQLARI.
#1 - Quyidagi kod bajarilishida yuzaga kelishi mumkin bo'lgan xatolarni ushlab, xatoga mos matnni konsolga chiqaring:
# x = int(input("Son kiriting: "))
# y = int(input("Yana bir son kiriting: "))
# print(x, '/', y, '=', x/y)

# x = input("Son kiriting: ")
# y = input("Yana son kiriting: ")
# try: # Kod to'g'ri ishlaganda bajariladigan soha.
#     x = int(x)
#     y = int(y)
#     result = x/y # Bo'linish shu yerda amalga oshadi va RESULT ga yuklanadi.
# except ValueError: # Agar butun son kiritilmasa.
#     print("Butun son kiritmadingiz!")
# except ZeroDivisionError: # Agar 0 soni kiritilsa.
#     print("0ga bo'lib bo'lmaydi")
# else:
#     print(x, '/', y, '=', 'result')
    
# Yuqoridagi kodni while sikli yordamida xato qiymat qaytarilganda takrorlanadigan qiling:
# while True: # Doimiy ishlovchi sikl
#     x = input("Son kiriting: ")
#     y = input("Yana son kiriting: ")
#     try:
#         x = int(x)
#         y = int(y)
#         result = x/y # Bo'linish natijasi
#     except ValueError: 
#         print("Butun son kiritmadingiz qaytadan urunib ko'ring!")
#         continue# Siklni qayta boshlash
#     except ZeroDivisionError: 
#         print("0ga bo'lib bo'lmaydi!")
#         continue # Siklni qayta boshlash
#     else:
#         print(f"x / y = {result}")
#         break # Muvaffaqiyatli hisoblashdan so'ng siklni tugatish

# 17 - DARS TUGADI.