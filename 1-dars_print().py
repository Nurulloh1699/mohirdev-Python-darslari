# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:36:48 2024

@author: DavrServis
"""

#1-dars print() funksiyasi.
#13.10.2024
#Muallif:Abdurashidov Nurulloh

# Quyidagi kod "Hello World!" jumlasini konsolga chiqaradi.
print("Hello World!") # Matnlarni yozishda matn ("", '') qo'shtirnoq yoki birtirnoq ichida
# bo'lishini taminlash zarur.

# Matnlarni konsolga chiqarishda davom etamiz.
print("Hayrli tong!")

# ETIBOR BERING! Matnlar ham qo'sh tirnoq ham bir tirnoq ichida bo'lishi mumkin vaziyatga
# qarab ikkisidan ham foydalangan yaxshi chunki matnni o'zida ham bir tirnoq qatnashgan yoki
# qo'sh tirnoq qatnashgan bo'lishi mumkin.
print("Men \"Dell\" markasidagi noutbuk sotib oldim\n") # Bu vaziyatda (\) bu belgi xatolik
# yuz berishini oldini oladi.

# Matnni bir necha qatorda konsolga chiqarish uchun biz (""") uchtali qo'shtirnoqdan
# foydalanamiz.
print(""" Odami ersang odami, demagil odami,
Oniki,yoq xalq g'amidin g'ami \n""")
# Yoki bo'lmasam (\n) belgisidan ham foydalansak bo'ladi bu holatda patski qatordan
# yozilishi kerak bo'lgan matn oldiga (\n) belgisi qo'yiladi.
print("Odami ersang odami, demagil odami,\nOniki,yoq xalq g'amidin g'ami\n")
# (\) Backslesh belgisi qo'llaniladigan joylarga misol.
print('Odami ersang odami, demagil odami,\nOniki,yoq xalq g\'amidin g\'ami\n')

# print() funksiyasi yordamida nafaqat matnlar va balki sonlarni va turli hil idodalarni
# ham konsolga chiqarishimiz mumkin.
print(2+4*2)
# ETIBOR BERING! odatda (/) bittalik bo'lish belgisi bitin sonlarni ham o'nlik
# son ko'rinishida konsolga chiqaradi.
print(19/5)
# Buni bartaraf etish uchun esa (//) ikkitalik bo'lish belgisini ishlatishimiz kifoya 
# qiladi va bunda natijani kasr qismini tashlab yuboradi yani faqat butun qismi qoladi.
print(15//4)
print(15//4)

# Pythonda sonlarni darajasini topish uchun (**) ishlatiladi.
print(2**4) # Bu holatda 2ning 4chi darajasi topiladi va 16 degan javob olamiz.

# Biz print() orqali matn va sonlarni ham birlashtirishimiz mumkin.
print("To'qqizning kvadrati", 9**2, "ga teng")
print('3x3=',3*3)

# TOPSHIRIQLAR.
#1 Quyidagi matnni aynan shunday ko'rinishda konsolga chiqaring:
# "Nexia","Tico",'Damas' ko'rganlar qilar havas.
print('"Nexia","Tico",\'Damas\' k\'rganlar qilar havas.')

#2 Quyidagi misollarga yechimni Pythonda chiqaring. Har bir misoldan avval matnni
#izoh ko'rinishida yozing.
print("Beshning to'rtinchi darajasi = ", 5**4)
print("22ni 4ga bo'lganda",22%4,"qoldiq qoladi.")

#3 Tomonlari 125 bo'lgan kvadratning yuzini va perimetrini toping.
print("Tomonlari 125ga teng bo'lgan kvadratning yuzi", 125*125, 
"ga teng,Perimetri", 4*125, "ga teng")

#4 Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakni gipotenuzasini toping.
print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakni gipotenuzasini",
(6**2+7**2)**(1/2), "ga teng.")



