# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:26:17 2025

@author: DavrServis
"""

# 8 - DARS.
# SHARTLAR VA TARMOQLANISH.

# TAQQOSLASH OPERATORLARI.
# Dastur tarmoqlanishi uchun, avvalo, biror shart bajarilishi kerak. Shart bajarilishini tekshirish uchun esa maxsus 
# taqqoslash operatorlari mavjud. Bu operatorlar yordamida biz o'zgaruvchilarning ma'lum qiymatga tengligini yoki,
# aksincha, teng emasligini yoxud ifodalarning natijasini berilgan qiymatdan katta yoki kichikligini va hokazo
# shartlarni tekshirib ko'rishimiz mumkin.
# Quyida Pythondagi taqqoslash operatorlarini ko'rib chiqamiz.

# == (Tenglik) a == b.
# != (Tengsizlik) a != b.
# < (Kichik) a < b.
# <= (Kichik yoki teng) a <= b.
# > (Katta) a > b.
# >= (Katta yoki teng) a >= b.

# Taqqoslash operatorlari mantiqiy qiymat qaytaradi (bool). Mantiqiy qiymatlar True (Shart bajarildi) yoki
# False (Shart bajarilmadi) bo'lishi mumkin.
# True ingliz tiladan (To'g'ri), False esa (Yolg'on) deb tarjima qilinadi. Quyida bir misol bilan buni mustaxkamlaymiz.
# a = 5
# b = 6
# print(a == b) # a teng(mi)? b ga. Natija False bo'ladi chunki teng emas.

# Yana bitta boshqacharoq misol ko'ramiz.
# a = 5
# b = 6
# print(a == (b - 1))

# Matnlarni va sonlarni taqqoslash usullari.
# print('anvar' == 'Anvar ') # Matnlarni taqqoslash.
# print(10**2<2**10) # Sonlarni taqqoslash.

# Taqqoslash qanday bajarilishini tushunish uchun quyidagi mashqlarni bajarib ko'ramiz.
# ism = 'anvar' # O'zgaruvchiga yuklandi.
# print(ism != 'Ahad') # ism da bosh harfli 'Ahad' teng emas kichik harfli 'ahad' ga (True) javob qaytadi.
# print(ism.title() == 'Ahad') # Bu yerda endi title() metodidan foydalandik va endi mantiqiy qiymat (False) ga teng bo'ladi.

# num1 = [1,2,3] # <- 1 - ro'yxat.
# num2 = [1,2,4] # <- 2 - ro'yxat.

# print(num1 != num2) # Ikkita ikki ro'yxatni teng emasligini so'rayapmi va bu (True) javob qaytaradi.
# print(9**2 >= 7*9+18) # 9 ning kvadrati (81) katta yoki teng ifodadan, hisoblasak ifoda ham (81) ga teng bo'ladi.
# Kelib chiqadiki (True) qiymat qaytaradi.

#x = 10 # <- x ni 10ga tengalab olamiz va uni turli ifodalar oraqali turli ifodalarga tenglashga urunib ko'ramiz.
# print(x*x < x**2) # 10 ko'paytirilgan 10ga va bu ifoda kichikmi 10 ning kvadratidan. (False) degan javob qaytaradi.
# print(x*x >= float(f"{x**2}")) # Bu yerda ham huddi shunday ifoda boshqacharoq talqinda. (True) qiymat qaytaradi.

# IF-ELSE OPERATORI.
# Avvalgi bo'limda biz turli ifodalarni  taqqoslashni o'rgandik, keling, endi taqqoslashning natijasiga ko'ra
# tarmoqlanishini ham ko'zdan kechiraylik. Buning uchun dasturlash tillarida maxsus "if" operatori mavjud. "if" so'zi 
# ingliz tilidan "agar" deb tarjima qilinadi va ma'lum bir shart qanoatlantirilishiga qarab shu shartga bog'langan
# kod ham bajariladi.
# son = int(input("Istalgan son kiriting: ")) # Foydalanuvchidan istalgan son kiriting deb so'raymiz.
# if son > 0: # "if" operatori orqali kiritilgan sonnig 0dan katta ekanini tekshiramiz. Bu qatorni "agar son 0 dan katta
# bo'lsa" deb o'qish mumkin.
    # print(son, "musbat son") # Bu qator "if" operatorining badani hisoblanadi va faqatgina yuqoridagi shart to'g'ri
# (True) bo'lsa, bajariladi.

# Agar yuqorida biz misol uchun: -10 sonini kiritganimizda kod bajarilmasdi va hech narsa konsolga chiqmasdi.
# Keling endi buni tekshirishimiz uchun yangi "else" operatori bilan tanishamiz."else" so'zi ingliz tiladan "aks holda"
# debn tarjima qilinadi va "if" operatorida bajarilgan shart qanoatlantirilmasa, "else" operatoridan keyingi kod
# bajariladi.

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 7: # Agar yosh 7dan kichik yoki 7ga teng bo'lsa.
#     print("Sizga aftobus bepul!")
# else: # Aks holda.
    # print("Sizga chipta 7000")
    
# Shart "badani" shartdan biroz o'nggasurib yozilgan har bir qator if/else shartining badani hisoblanadi.

# BIR QATOR IF-ELSE
# Qisqa kodlar uchun shart va uning badanini 1 qatorga jamlab yozishimiz ham mumkin. Agar shartimiz faqat "if" dan
# iborat bo'lsa, uning badanini keyingi qatordan emas, ikki nuqtadan keyin yozish kifoya.
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh > 65: print("Siz COVID-19 havf guruhida ekansiz.")

# Deylik kodimizda "if-else" birgalikda qatnashsa, "if" ning badani undan oldin, "else" ning badani esa keyin yoziladi:
# x, y = 50, 29 # x = 50, y = 29
# print("x < y") if x < y else print("x > y") # Shu ko'rinishta.

# MATNLARNI SOLISHTIRISH.
# Matnlarni solishtirish bu yana bir muhim jihatlardan biri, buni biz birorbir satda yangi akkaunt ochyotgan odam
# misolida ko'rishimiz mumkin.
# Matnlarni solishtirishdan avval ularni lower metodidan foydalangan holda bir hil ko'rinishga olib kelib olish
# maqsadga muvofiq bo'ladi.
#ism = 'Ali' # O'zgaruvchi misolida ko'ramiz.
#ism.lower() == 'ali' # Bu yerda biz bor o'zgaruvchini oldin bir ko'rinishga keltirib olyapmiz va endi natija (True).

# AMALIYOT TOPSHIRIQLARI.
#1 - Quyidagi dasturlarni Pythonda bajarib ko'ring.
#1
# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

#2        
# javob = float(input("12x6 nechiga teng? "))
# if javob != 72:
#     print("Javobingiz xato!")        
# else:
#     print("Siz to'g'ri javob berdingiz.")

#3
# yosh = int(input("Yoshingiz nechida? "))
# if yosh >= 18:
#     print("Xush kelibsiz!")
# else:
#     print("Sizga kirish mumkin emas!")

#4
# yil = int(input("Tug'ilgan yilingizni kiriting: ")) # Foydalanuvchidan tug'ilgan yilini so'raymiz.
# if 2024 - yil < 18: # Agar joriy yoldan foydalanuvchi tug'ilgan yilini ayirilganda hosil bo'qlgan qiymat 18dan kichik
# # bo'lsa.
#     print(f"Yoshingiz {2021-yil}da ekan.") # Bu yerda foydalanuvchi kiritkan yilga qarab uning yoshi aniqlanadi.
#     print("Kirishingiz mumkin emas.") # Shart bajarilsa shu habar chiqadi.
# else: # Aks holda.
#     print(f"Yoshingiz {2024-yil}da, Xus kelibsiz!") # Bu habar chiqariladi.

#5
# login = input("Yangi login kiriting: ")
# if len(login) <= 5: # login uzunligini tekshiramiz.
#     print("Login 5ta harfdan ko'proq bo'lishi shart!")
# else:
#     print("Login qabul qilindi.")


#2 - Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi
# harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling. 
# cars =  ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())
        
#3 - Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.   
# cars =  ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())
        
#4 - Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini
# ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga
# chiqaring.
# login = input("Yangi login kiriting: ")
# if login.lower() == 'admin':
#     print(f"Xush kelibsiz, {login.title()}. \nFoydalanuvhcilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Salom {login}, Xush kelibsiz!")

#5 - Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan
# yozuvni konsolga chiqaring.
# print("Iltimos ikkita son kiriting!") 
# son1 = int(input("Birinchi sonni kiriting: ")) 
# son2 = int(input("Ikkinchi sonni kiriting: ")) 
# if son1 == son2: 
#     print(f"{son1} va {son2} sonlari bir-biriga teng.") 
# else: 
#     print(f"{son1} va {son2} sonlari bir-biriga teng emas.")
     
#6 - Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat
# bo'lsa "Musbat son" degan xabarni chiqaring. 
# son = int(input("Istalgan son kiriting: "))
# if son < 0:
#     print(f"{son} soni manfiy")
# else:
#     print(f"{son} soni musbat")
    
#7 - Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
# son = float(input("Istalgan musbat son kiriting: "))
# if son < 0:
#     print("Musbat son kiriting!")
# else:
#     print(f"{son} ning ildizi {son**0.5}")

# 8 - DARS TUGADI.