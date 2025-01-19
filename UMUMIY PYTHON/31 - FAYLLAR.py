# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:46:47 2025

@author: DavrServis
"""

# 31 - DARS.
# FAYLLAR.
# Faylni ochish va o'qish
# with open(r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\test.txt') as file:
#     pi = file.read()  # Fayl ichidagi barcha matnni o'qib, `pi` o'zgaruvchisiga saqlash

# Fayldan o'qilgan matnni konsolga chiqarish
# print(pi)

# Matn oxiridagi bo'sh joylar va yangi qator belgilarini olib tashlash
# pi = pi.rstrip()

# Matndagi barcha yangi qator (`\n`) belgilarini olib tashlash
# pi = pi.replace('\n', '')

# Matnni float turiga o'zgartirish
# pi = float(pi)

# Float qiymatni konsolga chiqarish
# print(pi)

# Endi boshqa fayl misolida ko'ramiz:
# filename = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\talabalar.txt'
# with open(filename) as file:  # `filename` o'zgaruvchisida ko'rsatilgan faylni ochadi
#     for line in file:  # Fayldagi har bir qatorni ketma-ket ko'rib chiqadi
#         print(line)  # Har bir qatorni ekranga chiqaradi

# Endi bu talabalarni ismlarini har birini bittadan obyekt sifatida saqlashni ko'rib chiqamiz:
# with open(filename) as file:  # `filename` o'zgaruvchisida ko'rsatilgan faylni ochadi
#     talabalar = file.readlines()  # Fayldagi barcha qatorlarni ro'yxat (list) sifatida o'qiydi

# O'qilgan qatorlar ro'yxatini konsolga chiqarish
# print(talabalar)  # `talabalar` ro'yxatini ekranga chiqaradi

# Keling endi talaba ma'lumotlari ohiridagi \n belgisini olib tashlashni ko'rib chiqamiz:
# talabalar = [talaba.rstrip() for talaba in talabalar]

# print(talabalar)

# Biz yuqorida faqat fayllarni o'qishni ko'rdik, endi ularga yozishni ko'rib chiqamiz.
# faylnomi = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\new_file.txt'
# ism = "Nurulloh"
# tyil = 1999
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism + '\n')
#     fayl.write(str(tyil) + '\n')
# print(faylnomi)
# Yuqoridagi usul orqali fayldagi eski ma'lumotlar o'chirilib ustidan yangi ma'lumotlar yoziladi, buni oldini olish uchun quyidagicha yo'l
# tutamiz:
# faylnomi = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\new_file.txt'

# with open(faylnomi, 'a') as fayl:
#     fayl.write("Anvarov" + "\n")
#     fayl.write("2004" + "\n")
    
# Biz matnlarni fayllarga saqladik, endi fayllarga lug'atlar va o'zgaruvchilar saqlashni ko'rib o'tamiz.
# import pickle # Bu usulda yaratilgan fayllar faqatgina Pythonning o'zida ochish mumkin bo'ladi boshqa hech qanday usul bilan ochib
# bo'lmaydi.

# talaba1 = {"ism":"Hasan", "familiya":"Husanov", "tyil":2003, "kurs":2}
# talaba2 = {"ism":"Alijon", "familiya":"Valiyev", "tyil":2004, "kurs":1}

# with open('info', 'wb') as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)
    
# Faylimizni tayorlab oldik keling endi uni o'qishga harakat qilamiz:
# import pickle

# with open('info', 'rb') as file:
#     talaba1 = pickle.load(file)
#     talaba1 = pickle.load(file)

# print(talaba1)
# print(talaba2)

# AMALIYOT TOPSHIRIQLARI:
#1 - Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching.
# import pickle  # pickle moduli import qilinmoqda, lekin hozircha bu kodda ishlatilmayapti

# Fayl manzilini belgilash
# filename = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\topshiriq1.txt'

# Faylni ochish va uning ichidagi qatorlarni o'qish
# with open(filename) as file:  # Faylni ochadi. "with" konstruktsiyasi faylni ishlatib bo'lgandan keyin yopishni ta'minlaydi.
#     for line in file:  # Fayldagi har bir qatorni ketma-ket ko'rib chiqadi
#         print(line)  # O'qilgan qatorni ekranga chiqaradi

#2 - Quyidagi pi_million_digits.txt faylini yuklab oling (faylda π  soni nuqtadan so'ng million xona aniqlik bilan yozilgan). 
# Sizning tug'ilgan kuningiz π soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz
# 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.
# import pickle
# pitop = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\pi_million_digits.txt'
# with open(pitop) as file:
#     pi = file.read()
# pi = pi.rstrip()
# pi = pi.replace('\n', '')
# pi = pi.replace(' ', '')

# bdate = '16031999' or '03161999' or '19991603'
# # print(pi)
# print(bdate in pi)

# #4 - Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.
# pi = float(pi)
# print(pi)

# with open('pi','wb') as file:
#     pickle.dump(pi,file)

# 31 - DARS TUGADI.