# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:45:49 2024

@author: DavrServis
"""

#2-dars O'zgaruvchilar
#13.10.2024
#Muallif:Abdurashidov Nurulloh

# O'zgaruvhi yaratish uchun birinchi bo'lib u o'zgaruvchiga nom beramiz va
# keyin unga qiymat beramiz.
ism = 'Nurulloh'
print(ism)
# Agar ikkinchi marta yana shu o'zgaruvchiga qiymat bersak
# ikkinchi bo'lib berilgan qiymatni o'zida saqlab qoladi. 
ism = 'Abdurahmon'
print(ism)

# O'zgaruvchilarga faqat nom emas balki ifodalarni qiymat qilib kiritishimiz mumkin.
a = 6
b = 7
c = (a+b)**2
print(a, b, c)

# O'zgaruvchilarga nom berishta ularga chiroyla va tog'ri nom tanlay bilishimiz kerak.
# Bazi qoidalar o'zgaruvchilar lotin harfi yoki pastki chiziqdan (_) boshlanishi kerak.
# O'zgaruvchilar agar ikkita so'zdan iborat bo'lsa ularnin orasiga ham yoki chiziqcha (-),
# yoki pastki chiziq (_) qo'yish talab etiladi.
ism_sharif = ("Abdurashidov Nurulloh")
print(ism_sharif)

# O'zgaruvchilarda katta va kichik harflar har hil deb tushuniladi yani (ism), (ISM)
# va (Ism) 3ta har hil o'zgaruvchi db tushuniladi.
Ism = 'Nurulloh'
ism = 'Abdurahmon'
ISM = 'Hojiakbar'
print(Ism, ism, ISM)

# TOPSHIRIQLAR
#1 "Hello Woeld!" matnini yangi o'zgaruvchiga yuklang va
# print() yordamida uni konsolga chiqaring.
matn = ("Hello World!")
print(matn)

#2 Xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring,
# keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
xabar = 'Salom'
print(xabar)
xabar = "Qales"
print(xabar)

#3 Class deb nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga 
# chiqaring (siz kutgan natija chiqdimi?).
#class = (6+7)
#print(class) # Bu kod ishlamaydi chinki class bu Pythondi ozini komandasi hisoblanadi.

#4 Quyidagi kodni yozing.
radius = 5
pi = 3.14159
aylana_yuzi = pi * radius ** 2
print("Radiusi", radius, "ga teng aylananingyuzi", aylana_yuzi)    
