# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:27:03 2025

@author: DavrServis
"""


## SELECTION SORT (RO'YXATLARNI TARTIBLASH).

# Avvalgi darslarimizda biz tartiblangan ro'yxatlar bilan ishlash birmuncha osonroq bo'lishi xaqida xulosa qilgandik.

# SELECTION SORT bu juda sodda va tushinishga qulay algoritm hisoblanadi. 

# SELECTION SORT - bu tartiblash algoritmi bo'lib, u har safar eng kichik sonni topib, o'z joyiga qo'yadi ya'ni tartibsiz ro'yxatni o'sish
# tartibida tartibaydi.

# Qayerda? -->	Nima uchun?
# ✅ Kichik massivlar --> Kam elementlar uchun tez va oddiy ishlaydi.
# ✅ Qo‘shimcha xotira kerak bo‘lmagan holatlar --> Joyida saralaydi, qo‘shimcha xotira ishlatmaydi.
# ✅ Qimmat almashtirish operatsiyalarida --> Kam almashtirish bajargani uchun SSD va EEPROM uchun yaxshi.
# ✅ Eng kichik yoki eng katta bir nechta elementni ajratish --> Faqat kerakli qismni saralaydi.
# ✅ Dasturlashni o‘rganish	--> Oddiy va tushunarli algoritm.

# Misol uchun: Sizda quyidagi tartibsiz sonlar bor.
[64,25,12,22,11]

# SELECTION SORT qanday ishlaydi?

# 1. Eng kichik sonni topamiz va boshiga qo'yamiz.
# --- Butun ro'yxatni qaraymiz: [64,25,12,22,11].
# --- Eng kichik son -11, uni birinchi joyga olib kelamiz:
# [11,25,12,22,64]

# 2. Qolgan qismdan eng kichik sonni topamiz va ikkinchi joyga qo'yamiz.
# --- [11,25,12,22,64] -> Eng kichik son 12, uni ikkinchi joyga qo'yamiz.
#     [11,12,25,22,64]

# 3. Keyingi eng kichik sonni topamiz va o'z joyiga qo'yamiz.
# --- [11,12,25,22,64] -> Eng kichik son 22, uni joyiga qo'yamiz.
#     [11,12,22,25,64]

# 4. Qolgan ikita sonni ha to'g'ri joylashtiramiz.
# --- [11,12,22,25,65] -> Barcha sonlar tartiblangan.


# SELECTION SORT ni ishlash tezligi (BIG O).
# Algoritm qanchalik tez ishlaydi?
# --- Har bir sonni joyiga qo'yish uchun eng kichik sonni topish kerak.
# --- Eng kichik sonni topish uchun butun ro'yxatni ko'zdan kecchiramiz.
# --- Agar 5ta son bo'lsa, bu 5 + 4 + 3 + 2 + 1 = 15 marta solishtirish degani (15ta operatsiya).
# --- Agar 100ta son bo'lsa, bu 5000 ga yaqin solishtirish talab qiladi.
# --- Buni BIG O orqali ifodalasak, O(n²) bo'ladi. Ya'ni, n qancha katta bo'lsa, ishlash vaqti shuncha oshib boradi.

# XULOSA.
# 1. SELECTION SORT har safar eng kichik sonni topib, uni boshiga qo'yadi.
# 2. Har safar kamida n² marta solishtirish bajariladi.
# 3. Katta ma'lumotlar bilan ishlaganda algoritmning ishlash samaradorligi pasayadi, lekin oddiy va tushunarli.
# 4. Tezroq algoritmlar mavjud, masalan, MERGE SORT va QUICK SORT.


