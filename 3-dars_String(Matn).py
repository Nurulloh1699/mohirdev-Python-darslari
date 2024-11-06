# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:23:26 2024

@author: DavrServis
"""

#3-dars String(Matn)
#13.10.2024
#Muallif:Abdurashidov Nurulloh

# O'zgaruvchilarning ozi lotin alifbosida bo'lishi kerak lekin ularning qiymatlari 
# kiril alifbosida bo'lsa ham bolaveradi.
viloyat = 'Фаргона'
shahar = 'Кокон'
print(viloyat, shahar)

# O'zgaruvchilarga qiymat berishta biz maxsus belgilardan ham foydalansak bo'ladi (📱)
# kabilar shular jumlasidan.
matn = "Men kecha yangi 📱 oldim"
print(matn)
smayl = "🙄"
print(smayl)

# String tipli o'zgaruvchilarni biz bemalol bir biriga qo'shsak ham bo'ladi.
ism = "Nurullo"
print("Meninig ismim " + ism)

# 2ta string tipli o'zgaruvchilarni biz (+) shunchaki qo'shib qo'ysak ham bo'ladi.
ism = "Nurulloh"
familya = "Abdurashidov"
print(ism + familya) # Bu yerda etibor bergan bo'lsangiz sozlar orasida 
# ochiq joy qolmayapti,
# Buni bartaraf qilish uchun biz (' ') bo'sh joydan foydalanamiz.
print(ism + ' ' + familya)

# Shuningdek biz matnlarni f-string bilan ham jamlasak bo'ladi va
# bu usul ko'proq qollaniladi
ism_sharif = f"{ism} {familya}"
print(ism_sharif)

# f-strin yordamida biz ikkita uchta va hohlagancha matnlarni birlashtirishimiz mumkin.
ism = "James"
familya = "Bond"
print(f"Mening ismim {familya}. {ism} {familya}!")

# MAHSUS BELGILAR (\t) uzun bo'shliqva (\n) qatorni pastga tushirish.
print('Hello World!') # Oddiy string.
print('Hello \tWorld!') # (\t) yani uzun bo'shliq qo'yib beradigan mahsus belgi.
print('Hello \nWorld!') # (\n) qator ko'chirish mahsus belgisi.

# String metodlari bilan tanishamiz.
# ETIBOR BERING! bu metodlarni qo'llaganimizda o'zgaruvchining as qiymati o'zgarmaydi.
# Qiymatni o'zgartirish uchun esa  qiymatni shu metodlardan biriga tenglashimiz kerak bo'ladi.
# ism_sharif = ism_sharif.upper() ko'rinishida.
ism = "James"
familya = "Bond"
ism_sharif = f"{ism} {familya}"
print(ism_sharif.upper()) # Matnning hamma harfini katta qiladi (JAMES).
print(ism_sharif.lower()) # Matnning hamma harfini kichkina qiladi (james). 
print(ism_sharif.title()) # Matnning har bir so'zini birinchi harfini katta qiladi(Tim Kuk).
print(ism_sharif.capitalize()) # Matnning faqatgina eng birinchi so'zini birinchi harfini 
# katta qiladi(Tim kuk).

# Navbatdagi metodlar .lstrip(), .rstrip() va .strip() lar bilan tanishamiz.
meva = "   olma   "
print("Men" + meva.lstrip() + "ni yaxshi ko'raman.") # chap tomondan boshliqni olib tashlaydi.
print("Men" + meva.rstrip() + "ni yaxshi ko'raman.") # o'ng tomondan boshliqni olib tashlaydi.
print("Men" + meva.strip() + "ni yaxshi ko'raman.") # ikkala tomondan boshliqni olib tashlaydi.
print("Men" + meva + "ni yaxshi ko'raman.") # asl holati.

# INPUT bu foydalanuvchidan qiymat kiritishini so'raydigan funksiya.
#ism = input("Ismingiz nima? ") # Ism asnosida foydalanuvchidan qiymat kiritishini so'rayapti.
#print("Assalomu Alekum," + ism) # Foydalanuvchi kiritgan qiymat va matn birlashtirilyapti.

#ism = input("Ismingiz nima?\n>>> ")
#print("Assalomu Alekum, " + ism.title()) 

# TOPSHIRIQLAR
#1 Quyidagi o'zgaruvchilarni yarating:
kocha = "Navro'z"
mahalla = "Navoiy"
tuman = "Oltiariq"
viloyat = "Farg'ona"

#2 Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Farg'ona viloyati, Oltiariq tumani, Navoiy mahallasi, Navroz kochasi
#print(f"{viloyat} viloyati, {tuman} tumani, {mahalla} mahallasi, {kocha} ko'chasi")

#3 Yuqoridagi o'zgaruvchilarni (viloyat, tuman, mahalla, ko'cha) qiymatini foydalanuvchidan
# so'rang. Va avvalgi mashqni takrorlang.
#viloyat = input("Qaysi viloyatta yashaysiz? ")
#tuman = input("Qaysi tuman yashaysiz? ")
#mahalla = input("Qaysi mahalla yashaysiz? ")
#kocha = input("Qaysi kocha yashaysiz? ")
#print(f"Men {viloyat} viloyati {tuman} tumani {mahalla} MFYsi {kocha} kochasida yashayman.")

#4 Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing.
#viloyat = input("Qaysi viloyatta yashaysiz? ")
#tuman = input("Qaysi tuman yashaysiz? ")
#mahalla = input("Qaysi mahalla yashaysiz? ")
#kocha = input("Qaysi kocha yashaysiz? ")
#print(f"Men {viloyat} viloyati,\n{tuman} tumani,\n{mahalla} MFYsi,\n{kocha} kochasida yashayman.")

#5 Yuqoridagi matnni f-string yordamida yangi, manzil deb nomlanga o'zgaruvchiga yuklang.
manzil = (f"{viloyat} viloyati, {tuman} tumani, {mahalla} mahallasi, {kocha} ko'chasi.")
#print(manzil)

#6 Manzilga biz yuqorida o'rgangan .title(), .upper(), .lawer() va .capitalize() 
# metodlarini qollab ko'ring
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
