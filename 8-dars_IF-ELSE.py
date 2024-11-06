# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:24:29 2024

@author: DavrServis
"""

#8-dars IF-ELSE (agar\yoki)
#15.10.2024.
#Muallif:Abdurashidov Nurulloh.

# TARMOQLANISH (==) tengmi?, (!=) teng emasmi?
  #cars = ['general motors', 'audi', 'mercedes benz', 'bmw', 'tesla']
  #for car in cars: # Bu kodda biz ro'yxat ichidagi hamma elementga bir hi .title() metodini
# qo'lladik.
    #print(car.title())
  #for car in cars:
    #if car == 'bmw': # Endi bu yerda shart qoyyapmiz agar car 'bmw' ga teng bo'lsa.
        #print(car.upper()) # Uni hamma harflarini katta qilib chiqar.
    #else: # aks holda.
        #print(car.title()) # Uni faqat 1 - harfini katta qilgin deb.

# Yani yuqorida biz (==) tengmi degan savolga javob topilgan holda va aks holda bajariladigan
# ish harakatlarni ko'rdi. Aslida bu qanday ishlaydi.

  #a = 10 # a ga 10 degan qiymat berdik.
  #print(a==10) # Bu yerda a ning 10 ga tengligi tekshiriladi.(True) 
  #print(a==4) # Bu yerda a ning 4ga tengligini tekshiriladi.(False)

# ETIBOR BERING! matnlar bilan ishlaganda katta va kichik harflar turlicha talqin qilinadi.
# Matnlar bilan ishlashda ularni tekshirishdan oldin ularni bir hil ko'rinishga keltirib
# olish tavsiya etiladi. Biz endi (!=) teng emas metodini ko'rib chiqamiz.
# Buni tekshirish uchun esa (!=) metodidan foydalanamiz.
  #a = 5 # Bu yerda biz a ni 5 ga tenglab oldik.
  #print(a==5) # (==) metodi yordamida tekshiramiz.
  #print(a==4)
  
  #print(a!=5)# (!=) bu yerda esa aksincha boshqa metod orqali.
  #print(a!=4)

  #ism = input('Ismingiz nima?\n >>> ') # Bu yerda biz foydalanuvhcidan ismini so'rayapmiz
# input() funksiyasi yordamida.
  #if ism.lower() != 'ali': # ism teng emasmi ali ga degan tekshiruv ketyapti.
        #print(f"Uzr, {ism.title()} biz Alini kutyapmiz") # Yoq bo'lsa shu kod.
  #else: # Aks holda
    #print ("Salom,Ali") # Shu kod bajariladi.
        
# Bu yerda biz misolga javob topish tariqasida (!=) teng emasmi metodi ko'rib chiqamiz.
    #javob = float(input("12x6 nechiga teng?>>> "))
  #if javob != 72:
     #print("Javob xato!")
  #else:
     #print("Siz to'g'ri javob berdingiz.")    
     
# Bu yerda biz bazi saytlardek yosh chegarasi yaratishga harakat qilib ko'ramiz.
# (>=) katta yoki teng yordamida.
    #yosh = int(input("Yoshingizni kiriting:>>> "))
  #if yosh >= 18:
    #print("Xush kelibsiz")
  #else:
    #print("Yoshingiz yetarli emas!!!")
    
# Endi bazi saytlardagi login kiritishda qoyiladigan shartlardan biri 5 ta harfdan ko'proq
# degan shartni chiqarishga harakat qilamiz.
  #login = input("Iltimos yangi login tanlang! ")
  #if len(login)<=5:
    #print("Login 5ta harfdan uzun bo'lishi shart")
  #else:
    #print("Login muvoffaqyatli kiritildi.")

# Endi biz foydalanuvchining yoshini hisoblashga harakat qilib ko'ramiz.

  #yil = int(input("Iltimos tug'ilgan yilingizni kiriting: "))
  #if 2024-yil<18: # Foydalanuvchini yoshini hisoblaymiz.
    #print(f"Sizning yoshingiz {2024-yil} da ekan")
    #print("Sizga kirish taqilanadi!")
  #else:
    #print("Xush kelibsiz!")  
    
  #yosh = int(input("Iltimos yoshingizni kiritin: "))
  #if yosh>65: print("Siz COVID-19 risk guruhida ekansiz!")

  #x, y = 12, 25 # Bu yerda x25 ga y12 ga teng bo'ldi.
  #print("x>y")   if x>y else print("x<y") 

# TOPSHIRIRQLAR
#1 Yangi cars  = ['toyota','mazda','hyundai','gm','kia'] degan ro'yxat tuzing,
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chiqaring.GM uchun
# ikkala harfni katta qiling.
  #cars  = ['toyota','mazda','hyundai','gm','kia']
  #for car in cars:
    #if car=='gm':
        #print(car.upper())
    #else:
        #print(car.title())

#2 Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
  #cars  = ['toyota','mazda','hyundai','gm','kia']
  #for car in cars:
    #if car!='gm':
        #print(car.title())
    #else:
        #print(car.upper())        
        
#3 Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz",Admin.
# Foydalanuvchilar ro'yxatini korasizmi?" xabarini konsolga chiqaring. Aks holda,
# "Xush kelibsiz,{foydalanuvchi_ismi}!" matnini konsolga chiqaring.
  #login = (input("Iltimos loginingizni kiriting: "))
  #if login.lower() == 'admin':
    #print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
    #print(f"Xush kelibsiz,{login.title()}")

#4 Foydalanuvchidan 2ta son kiritishini so'rang. Agar ikki son bir-biriga teng bo'lsa,
# "Sonlar teng ekan" degan yozuvni konsolga chiqaring.    
  #x = float(input("Birinchi sonni kiriting: "))
  #y = float(input("Ikkinchi sonni kiriting: "))   
  #if x==y: print("Sonlar teng ekan")
  
#5 Foydalanuvchidan istalgan son kiritishini so'rang. Agar son manfiy bo'lsa konsolga
# "Manfiy son", agar son musbat bo'lsa "Musbat son" degan yozuvni konsolga chiqaring.
  #son = int(input("Istalgan soningizni kiriting: "))
  #if son<0:
        #print("Kiritilgan son manfiy") 
  #else:       
        #print("Kiritilgan son musbat")
    
#5 Foydalanuvchidan istalgan son kiritishini so'rang, agar son musbat bo'lsa uning ildizini
# hisoblan agar son manfiy bo'lsa "Musbat son kiriting" degan yozuvni konsolga chiqaring.

son = int(input("Istalgan sonni kiriting: "))
if son > 0:
    print(f"Kiritilgan son ildizi {son**2}ga teng bo'ladi")
else:
    print("Musbat son kiriting")
    
    