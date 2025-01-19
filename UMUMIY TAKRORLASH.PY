# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:25:01 2024

@author: DavrServis
"""
# UMUMIY TAKRORLASH.

# 37 - DARS.
# PYTHON TASHQI KUTUBXONASI.






#  - DARS.
# LOYIHALAR. 
# "SON TOPISH" VA "SO'Z TOPISH" O'YINLARI.

# Ushbu bobda biz ikkita yangi o'yin ustida ishlaymiz. Dasturni yaratish jarayonida avval o'rgangan bilimlarimizni amalda qo'llaymiz.
# Shuningdek, yangi loyiha boshlashda muhim bo'lgan algoritm tushunchasi bilan tanishamiz.

# "SON TOPISH" O'YINI.
# Birinchi dasturimiz sodda "SON TOPISH" o'yini bo'ladi. Bu o'yin quyidagicha o'ynaladi.
#     1. Kompyuter biror berilgan oraliqda (masalan, 1dan 10gacha) son o'ylaydi.
#     2. Foydalanuvchi kompyuter o'ylagan sonni topishga urinadi va biror qiymat taxmin qilib kiritadi.
#     3. Agar taxmin to'g'ri bo'lsa, o'yin tugaydi, agar xato bo'lsa kompyuter foydalanuvchi taxmin qilgan son o'ylangan sondan katta yoki
# kichkligini aytadi va yangi son taxmin qilishni so'raydi.
#     4. Dastur shu zaylda foydalanuvchi to'g'ri sonni topguniga qadar davom etadi.


# ALGORITM.
# Dasturlashning muhim qismi to'g'ri reja qilish va dasturni mayda qadamlarga bo'lib olishdir. Bu Algoritm deyiladi. Xuddi ovqat
# pishirishda retsepdan foydalangandek, dastur yozishda ham Algoritmdan foydalanamiz.

# Yuqoridagi o'yin qoidasini ham bir nechta sodda qadamlarga bo'lib olamiz:
#     1. Kompyuter ma'lum oraliqda son "o'ylaydi": Albatta, kompyuter o'ylashga qodir emas, shuning uchun biz berilgan oraliqda biror 
# tasodifiy sonni qaytarishimiz kifoya (random funksiyasi orqali).
#     2. Foydalanuvchi taxmin qilgan sonni qabul qilib olish (input() orqali bo'ladi).
#     3. Taxmin va tasodifiy sonlarni taqqoslash ("==" sonlarni teng ekanini tekshiramiz).
#     4. Taqqoslash natijasiga ko'ra ("if-else" juftligidan foydalanamiz va natijaga qarab ikki hil yo'l tutamiz (a - b)).
#     a. O'yinni to'xtatish;
#     b. Foydalanuvchiga ishora berish va qayta taxmin qilishni so'rash va yuqoridagi 3 - 4 qadamlarni takrorlash ("while" sikli).
    
# Sodda algoritm tayyor, endi bevosita dastur yozishga kirishsak ham bo'ladi.

# DASTUR.
# Boshlanishiga dastur uchun kompyuterimizda alohida papka yaratamiz va dasturga oid fayllarni (modullarni) shu papkada saqlab boramiz.
# Dastur yozishda asosiy dasturimiz main.py qo'shimcha modullarni esa shu modul ichidagi funksiyaga oid so'zlar bilan nomlash to'g'ri
# bo'ladi.

# Biz ham boshlanishiga sonTop.py faylini yaratamiz va fayl ichiga yuqoridagi algoritm asosida sontop(x) funksiyasini yozamiz.
# Bu funksiyamiz argument sifatida kompyuter o'ylashi kerak bo'lgan sonlar oralig'inining yuqori chegarasini qabul qiladi (0dan x gacha)
# va biz bu parametrga standart 10 qiymatini berib qo'yamiz (ya'ni foydalanuvchi aniq oraliqni ko'rtsatmasa, kompyuter 0 dan 10 gacha
# son "o'ylaydi").

# Funksiyaichida birinchi qiladigan ishimiz - tasodifiy son "o'ylash". Buning uchun random modulidagi randint funksiyasidan foydalanamiz.
# Demak, dastur boshida random modulini import qilishni ham esdan chiqarmaslik kerak: 
# import random 
# def son_top(x = 10):
#     tasodifiy_son = random.randint(1, x) 

# Navbat foydalanuvchidan qiymatlar qabul qilishga. Keling, bundan kompyuter aynan qaysi oraliqda sono'ylaganini ham aytaylik.
    # print(f"Men 1dan {x} gacha son o'yladim. Topa olasizmi?")

# Ana endi bevosita input() funksiyasi yordamida foydalanuvchi kiritgan sonni qabul qilamiz va bu sonni tasodifiy son bilan solishtiramiz.

# Algoritmga ko'ra, biz foydalanuvchining taxminiga qarab turli amallarni bajarishimiz kerak:
    # 1. Agar taxmin tasodifiy sondan kichik bo'lsa, "Kattaroq son ayting";
    # 2. Agar taxmin tasodifiy sondan katta bo'lsa, "Kichikroq son ayting";
    # 3. Agar taxmin to'g'ri bo'lsa, "Yutdingiz!" deb aytishimiz kerak.
    
# O'yin foydalanuvchi yutguniga qadar davom etishi uchun kodimizni while sikli ichiga olamiz.

# Marhamat funksiya tayyor.
# import random 

# def son_top(x=10):
#     tasodifiy_son = random.randint(1, x) 
#     print(f"Men 1dan {x} gacha son o'yladim. Topa olasizmi?")
    
#     while True:
#         taxmin = int(input(">>> "))
#         if taxmin < tasodifiy_son:
#             print("O'ylagan sonim bundan kattaroq!")
#         elif taxmin > tasodifiy_son:
#             print("O'ylagan sonim bundan kichikroq!")
#         else: 
#             print("Topdingiz!")
#             break

# Biz funksiyani alohida modulda saqladik, keling main.py faylini yaratamiz-da, yuqoridagi modul va funksiyani import qilamiz:
# from son_top import son_top
# son_top()

# Faylimiz tarkibi qisqagina bo'ldi. main.py faylini bajaramiz
# Natija: Men 1dan 10 gacha son o'yladim. Topa olasizmi?
# 5
# O'ylagan sonim bundan kattaroq!
# 6
# O'ylagan sonim bundan kattaroq!
# 10
# Topdingiz!
        

# pyWebiO
# Avvalgi bobda pywebiomoduli bilan tanishgan edik, keling, ushbu modul yordamida dasturimizni brauzerda ishlaydigan qilamiz.

# Boshlanishiga modul ichidan input va put_text funksiyalarini chaqirib olamiz. input() funksiyasi bevosita qiymat qabul qilish uchun,
# put_text() esa foydalanuvchiga matn ko'rsatish uchun ishlatiladi.

# Avvalgi dasturda "Men 1 dan 10 gacha son o'yladim. Topa olasizmi?>>>" matnini ikkiga bo'lgan edik, bu safar ikkalasini ham input()
# funksiyasiga joylaymiz. Konsolga chiqarilayotgan matnlarni esa brauzerga chiqarish uchun kodimizdagi print funksiyasini put_text() bilan
# almashtiramiz:
# from pywebio.input import input
# from pywebio.output import put_text
# import random
# def sontop(x = 10):
#     tasodifiy_son = random.randint(1, x)
#     while True:
#     taxmin = int(input(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi? >>> "))
#     if taxmin < tasodifiy_son:
#         put_text("Kattaroq son ayting!")
#     elif taxmin > tasodifiy_son:
#         put_text("Kichikroq son ayting!")
#     else:
#         put_text("Yutdingiz!")
#         break
