# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:58:18 2025

@author: DavrServis
"""

# 3 - DARS.
# MATN (STRING).

# String matn Pythonda eng muhim ma'lumot turlaridan biri va ular ("") yoki ('') qo'shtirnoq yoki birtirnoq ichida yoziladi.
# ism = "Abdurashidov"
# avto = "Nexia"
# print(ism)
# print(avto)

# Pythonda matnlar Unicode jadvalidagi istalgan belgilardan iborat bo'lishi mumkin.
# matn = ('Men yangi 📱 oldim.')
# print(matn)

# MATNLARNI QO'SHISH. Matnlarni qo'shish uchun (+) dan foydalanamiz.
# ism = "Abdulloh"
# print("Mening ismim " + ism)

# ism = 'Ahad'
# familya = 'Qayum'
# print(ism + familya)

# Yuqoridagi misolda ikki matn bir-biriga yopishib qoldi bini oldini olish uchun o'rtada joy tashlashimiz kerak.
# print(ism + ' ' + familya) # ko'rinishida.

# F-STRING yordamida biz bir necha matnlarni bir biriga qo'shishimiz mumkin bo'ladi.
# mat1 = "Men seni sevaman!"
# mat2 = "Mavluda"
# print(f"{mat1} {mat2}")

# bu usul yordamida uzun matnlarni ham yozsak bo'ladi.
# fname = 'Bond'
# lname = 'James'
# matn = f"Salom mening ismim {fname}. {lname} {fname}!"
# print(matn)

# F-STRING yordamida nafaqat matnlarni balki balki turli ifodalarni ham ham jamlab yozishimiz mumkin bo'ladi. Bunda ifodalar va
# o'zgaruvchilar katta qavs {} ichida yoziladi.
# tyil = 1999
# print(f"Siz {tyil}-yilda tug'ulgansiz")
# print(f"Yoshingiz {2025 - tyil} da")

# MAXSUS BELGILAR. Maxsus belgilar yordamida matnga turli o'zgarishlar kiritish mumkin. Masalan, matnga bo'shliq qo'shish uchun (\t)
# belgisidan, yangi qatordan boshlash uchun (\n) belgisidan foydalanamiz.
# print("Hello World!")
# print("Hello \tWorld!") # matnlar orasida bo'sh joy tashlaydi.
# print("Hello \nWorld") # (\n) belgisidan keyin kelgan matn yangi qatordan boshlanadi.

# MATNLAR BILAN ISHLASH. Pythonda matnlar ustida amalga oshirish mumkin bo'lgan tayyor funksiyalar mavjud. Odatda, biror funksiya
# ma'lum bir obyektga (o'zgaruvchi, ma'lumot turiga) xos bo'lsa, bunday funksiyalar METODLAR deb ataladi.
# Metodlarni qo'llash uchun metod nomi matndan so'ng (.metod_nomi()) ko'rinishida yoziladi.
# Bularga misol: .upper() va lower() metodlari.

# .upper() metodi matndagi har bir harfni bosh harfga o'zgartiradi. 
# ism_sharif = "Abdurashidov Nurulloh"
# print(ism_sharif.upper())

# .lower() metodi matndagi har bir harfni kichik harfga o'zgartiradi.
# ism_sharif = "ABDURASHIDOV NURULLOH"
# print(ism_sharif.lower())

# .title( metodi matndagi har bir so'zni birinchi harfini katta harfga o'zgartiradi.
# ism_sharif = "abdurashidov nurulloh"
# print(ism_sharif.title())

# .capitalize() metodi matndagi birinchi so'zning birinchi harfini katta harfga o'zgartiradi.
# ism_sharif = "ABDURASHIDOV NURULLOH"
# print(ism_sharif.capitalize())

# Bizda navbatdagi metodlar .strip(), .rstrip() va .lstrip() metodlari bularning har biri o'ziga hos.

# .lstrip() metodi matn boshidagi bo'shliqni yani chap tomondagi.
# .rstrip() metodi matn ohiridagi bo'shliqni yani o'ng tomondagi.
# .strip() metodi esa matn boshi va oxiridagi bo'shliqlarni olib tashlaydi. Quyida buni misol asosida ko'ramiz.
# meva = "    meva    "
# print("Men " + meva.lstrip() + " ni yaxshi ko'raman.") # .lstrip()
# print("Men " + meva.rstrip() + " ni yaxshi ko'raman.") # .rstrip()
# print("Men " + meva.strip() + " ni yaxshi ko'raman.") # .strip()

# ESLATMA. Yuqoridagi metodlar o'zgaruvchi ichidagi asl matnni o'zgartirmaydi! O'zgartirilgan matnni saqlab qolish uchun uni
# o'zgaruvchiga qayta yuklash lozim bo'ladi: meva = meva.strip().
# meva = meva.strip()
# print(meva)

# .input() FOYDALANUVCHI BILAN MULOQOT.
# fOYDALANUVCHI BILAN MULOQOTGA KIRISHISH UCHUN BIZ .INPUT() FUNKSIYASINI ISHLATAMIZ.
# ism = input("Ismingiz nima? ") # Bu o'rinda foydalanuvchidan ma'lumot kiritishini so'rayapti.
# print("Assalomu Alekum, " + ism)

# Keling endi shu dasturni chiroyliroq ko'rinishda qilishga harakat qilib ko'ramiz.
# ism = input("Ismingiz nima? \n>>> ")
# print(f"Assalomu Alekum, {ism.title()}")

# AMALIYOT TOPSHIRIQLARI.
#1 - Quyidagi o'zgaruvchilarni yarating: 

# kocha="Bog'bon"

# mahalla="Sog'bon"

# tuman="Bodomzor" 

# viloyat="Samarqand"

#2 - Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring: Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani,
# Samarqand viloyati
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati.")

#3 - Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# print("Qayerda yashaysiz? ")
# kocha = input("Ko'changizni kiriting: ")
# mahalla = input("Mahallangizni kiriting: ")
# tuman = input("Qaysi tumanda yashaysiz: ")
# viloyat = input("Viloyatingizni kiriting: ")
# print(f"Men {kocha.title()} ko'chasi, {mahalla.title()} mahallasi, {tuman.title()} tumani, {viloyat.title()} viloyatida yashayman.")

#4 - Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# print(f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati.")

#5 - Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang.
# manzil = f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati."
# print(manzil)

#6 - manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
# manzil = f"{kocha.title()} ko'chasi, \n{mahalla.upper()} mahallasi, \n{tuman.lower()} tumani, \n{viloyat.capitalize()} viloyati."
# print(manzil)

# 3 - DARS TUGADI.