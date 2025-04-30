# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:29:51 2025

@author: DavrServis
"""

# 20 - DARS.
# FUNKSIYA VA RO'YXAT.
# Biz avvalgi darsimizda funksiyaga parametr sifatida yagona qiymat berayotgan edik. Aslida, bu bilan cheklanmasdan, funksiyaga
# ro'yxat (list) ham berishimiz mumkin. Bunda funksiya ro'yxat qiymatlariga to'g'ridan to'g'ri murojaat eta oladi. 

# Keling talabalarni baholaydigan funksiya yozmaiz. Funksiyamiz talabalar ro'yxatini qabul qilib oladi, ro'yxatdan har bir talabani
# sug'urib olib, bahosini kiritishni so'raydi. Talab ismi va bahosinilug'atga joylab, yakuniy lug'atni foydalanuvchiga qaytaradi.
# def bahola(ismlar): # Funksiya yaratib olyapmiz.
#     baholar = {} # Baholar degan bo'sh lug'at yaratib olyapmiz. Quyida return orqali baholar lug'atini qaytaramiz.
#     while ismlar: # Ismlarning ichida 1 dona bo'lsa ham ism bo'lsa.
#         ism = ismlar.pop() # Ism, ismlar ichidagi har bir elementni birma bir sug'urib oladi.
#         baho = input(f"{ism.title()}ning bahosini kiriting: ") # Baho ga input orqali har bir ismni chaqirib baho qo'yamiz.
#         baholar[ism] = baho # Baholar lug'atiga yangi juftlik qo'shiladi ("ism" : "baho") ko'rinishida.
#     return baholar        
# talabalar = ['ali', 'vali', 'hasan', 'husan'] # Baholanadigan talabalar ismlarini sqlaydi.
# baholar = bahola(talabalar) # Ro'yxatni yuqoridagi funksiyaga uzatadiva natija lug'at shaklida qaytadi.
# print(baholar) # Foydalanuvchi kiritgan baholarni ko'rsatadi.
# Natija: {'husan': '4', 'hasan': '5', 'vali': '4', 'ali': '3'}


# RO'YXATGA O'ZGARTIRISH KIRITISH.
# Funksiyaga ro'yxat uzatganimizda funksiya ro'yxat elementlariga to'g'ridan-to'g'ri murojaat eta oladi. Ro'yxatga funksiya ichida
# kiritilgan oo'zgarishlar funksiya tashqarisidagi asl ro'yxatga ham ta'sir qiladi. Avvalgi misolimizga qaytaylik:
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(talabalar)
# Natija: []

# Yuqoridagi funksiya unga uzatilgan ro'yxat ichidagi talabalarning ismini .pop() yordamida sug'urib olgani uchun bizning asl
# ro'yxatimiz ham bo'shab qoldi. ETIBOR BERING! Funksiya tashqarisidagi va ichidagi ro'yxatlar ikki xil nomlangan bo'lsa-da
# (talabalar va ismlar), ikkalasi ham xotiradagi bitta ro'yxatga bog'langan.

# Ikki o'zgaruvchi ham bitta ro'yxatga bog'langan, talabalar ham va ismlar ham.


# ASL RO'YXATGA O'ZGARTIRISH KIRITISHNI OLDINI OLISH.
# Agar funksiya asl ro'yxatga o'zgartirish kiritishini istamasangiz, funksiyaga ro'yxatning o'zini emas, uning nusxasini uzatish
# mumkin. Buning uchun funksiya parametrini royxat_nomi[:] ko'rinishida yozish kifoya. Bunda [:] operatori ro'yxatdan nusxa olishni
# anglatadi:
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(talabalar)
# Natija: ['ali', 'vali', 'hasan', 'husan']

# AMALIYOT TOPSHIRIQLARI.
#1 - Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya
# yozing.
# def katta_harf(matnlar): # Funksiya yaratib olamiz. Funksiyamiz matnlarni qabul qilib shu matlardagi bosh harflarni kkata harfaga
# # aylantiradi.
#     for matn in range(len(matnlar)): # Matn degan o'zgaruvchi yaratib olami va u range() va len() orqali matlar ro'yxatidagi
# # elementlar sonicha elementga tenglashadi. 
#         matnlar[matn] = matnlar[matn].title() # Endi matnlar ichidagi har matnni title() orqali chiroyli ko'rinishga keltirib
# olamiz.
        
#     print(matnlar) # Matnlar degan o'zgartirilgan ro'yxatimizni konsolga chiqaramiz.
# ismlar = ['ali', 'vali', 'hasan', 'husan'] # Tayyor ro'yxat.
# katta_harf(ismlar) # Ro'yxatni funksiyaga beramiz.
# print(ismlar) # Va uni ham konsolga chiqaramiz.

#2 - Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring
# def katta_harf(matnlar): # Yuqorigidagidek funksiya yaratib olamiz.
#     matnlar = matnlar[:] # Matnlardan nusxa olamiz.
#     for matn in range(len(matnlar)): # Yuqoridagidek matnni har bir element uchun tanglab olamiz.
#         matnlar[matn] = matnlar[matn].title() # Har bir matnni katta harfga o'tkazamiz.
#     return matnlar # Matnlar degan ro'yxatno qaytaramiz.
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# matnlar = katta_harf(ismlar)
# print(ismlar)
# print(matnlar)

#3 - Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan
# faqat lug'at qaytaradigan qilib yozing.
# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"{ism.title()}ni baholang: ")
#         baholar[ism] = baho
#     return baholar
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(talabalar)
# for ism, baho in baholar.items():
#     print(f"Ismi: {ism.title()}, Bahosi: {baho}")

# 20 - DARS TUGADI.