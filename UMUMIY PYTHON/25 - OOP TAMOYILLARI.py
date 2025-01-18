# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:43:03 2025

@author: DavrServis
"""

# 25 - DARS.
# OOP TAMOYILLARI.

# INKAPSULYATSIYA.
# Biz object oriented dasturlash haqida gapira turib ma'lum bir obyektga tegishli bo'lgan xususiyatlar va metodlarni bitta konteynerga
# joylaylmiz dedik. Bu jarayon INKAPSULYATSIYA (ya'ni kapsulaga solish) deb ataladi. Inkapsulyatsiya bizga klasslar yaratish va
# keyinchalik bu klasslardan boshqa obyektlarni yaratishga yordam beradi.

# ABSTRAKSIYA. 
# Abstraksiya yordamida biz kodimizning ichki tuzilishini yashiramiz. Ya'ni tashqaridan obyektimiz 2ta parametr va 2ta metoddan iborat
# bo'lish mumkin, lekin obyekt to'g'ri ishlashi uchun uning ichida o'nlab boshqa o'zgaruvchilar va funksiyalar yashirin bo'ladi. Klassdan
# foydalanishda esa uning ichki tuzilishi va qanday ishlashini bilish talab etilmaydi. Bu o'zimizga ham, boshqa dasturchilarga ham mazkur
# klassdan foydalanishda qulayliklar yaratadi.

# VORISLIK.
# Dasturlash jarayonida biz bir klassdan boshqa klasslar yaratishimiz mumkin. Misol uchun, bizda transport klassi bor, biz bi klassdan
# qo'shimcha avtomobil, avtobus, kema, poyezd kabi klasslarni yaratishimiz mumkin. Bundabizning asl klassimiz ota yoki super-klass deb
# ataladi, undan yaratilgan klasslar esa voris klasslar deyiladi.

# ETIBOR BERING! Voris klasslar ota klassning va'zi yoki barcha xususiyatlari va metodlariga ega bo'ladi.

# POLIMORFIZM.
# Voris klass super-klassdan o'zlashtirgan metodning nomini saqlagan holda uning ishlashini o'zgartirishi POLIMORFIZ deyiladi.

# Keling, bie misol ko'raylik, Biz kompyuter o'yini yaratish jarayonida o'yin qahramoni uchun super-klass yaratamiz. Qahramon bir nechta
# xususiyatlarga va metodlarga ega. Jumladan attack(), ya'ni hujum qilish metodi qahramonni hujum qilishga undaydi. Endi biz bu 
# super-klassdan boshqa voris klasslarni yaratamiz.
    # 1. Birinchi qahramonimiz - Qilichboz, u hujum qilganda qilichdan foyalanadi.
    # 2. Ikkinchi qahramonimiz - Jangchi, u qurolsiz bo'lgani sababli qo'l va oyoqlari bilan hujum qiladi.
    # 3. Uchunchi qahramonimiz - Pistolet bilan qurollangan.
    # 4. To'rtinchi qahramonimiz - kamon va yoylar bilan qurollangan 
# To'rt qahramonimiz ham super-klassdan attack() metodini meros oladi, lekin bu metodni biz har bir qahramonlar va turli hujum turlari
# uchun alohida metodlar yozishdan qutqaradi.

# Manashu yuqorida keltirilgan ma'lumotlar OOPning asosiy tamoyillari ekan.

# OOP AFZALLIKLARI VA KAMCHILIKLARI.
# Keling darsimiz yakunida OOPning afzalliklari va kamchiliklariga to'htalib o'taylik.

# Afzalliklari:
    # 1. Parallel dasturlash - bir loyihaning turli qismlari bir vaqtda yaratilishi mumkin.
    # 2. Vorislik tamoyili klasslardan qayta foydalanish imkonini beradi.
    # 3. Polimorfizm tamoyili klasslarni moslashuvchan qiladi.
    # 4.Klasslardan boshqa dastur va loyihalarda qayta-qayta foydalanish mumkin.
# Kamchiliklari.
    # 1. Dasturlashga yangi qadam qo'yganalr uchun biroz tushunarsiz.
    # 2. Har doim ham samarali emas.
    # 3. Ba'zida dasturimizni haddan tashqari murakkablashtirib yuborishi mumkin.
    
# OOP bilan qisqacha tanishuvimiz shundan iborat edi. Endi esa Python OOP bilan tanishuvni boshlasak ham bo'ladi.

# 25 - DARS TUGADI.