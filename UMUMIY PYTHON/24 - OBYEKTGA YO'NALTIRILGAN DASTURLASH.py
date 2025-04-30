# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:42:31 2025

@author: DavrServis
"""

# 24 - DARS.
# OBYEKTGA YO'NALTIRILGAN DASTURLASH.
# Dasturlashni o'rganar ekanmiz, albatta, object oriented programming (OOP), ya'ni obyektga yo'naltirilgan dasturlash tushunchasiga 
# kelamiz. Ko'pchilik uchun bu bosqich biroz tushunarsiz va murakkabdek tuyuladi. Aslida, unday emas. Ushbu bobda object oriented
# programming va unga tegishli tamoyillar haqida gaplashamiz.


# OOP NIMA?

# KLASSIK YOXUD CHIZIQLI DASTURALSH.
# OOPni tushunish uchun avval klassik dasturlashni ko'zdan kechiraylik. Gap shundaki, ilk kompyuterlar va dasturlar matematik muammolarni
# hal etishga qaratilgan. Bunday dasturlar foydalanuvchidan biror ma'lumotni qabul qilib olgan va qat'iy ketma-ketlik, ya'ni tartibga amal
# qilgan holda turli arifmetik amallarni bajarib, Shuning uchun ham bunday dasturlar chiziqli yoki tartibli dasturlar deb ataladi.

# Siz ham dasturlashga ilk qadam qo'yganingizda mana shunday chiziqli dasturlani yozishnio'rganishdan boshlaysiz. Sizning dasturingiz bir
# nechta o'zgarivchilar va funksiyalardan iborat bo'ladi. Bu o'zgaruvchilar va funksiyalar ma'lum ketma-ketlikda bir-biri bilan
# munosabatga kiradi va dastur yakunida esa siz kutkan natijani beradi.


# Dastur kattalashgani sari o'zgaruvchilar va funksiyalar soni ortib boradi. Ular o'rtasidagi munosabatlar ham chigallashib, kodingiz 
# murakkab va tushunishga qiyin bo'lib ketadi. Dasturlash jarayonida bitta funksiyaga o'zgartirish kiritishingiz esa unga bog'liq boshqa
# funksiyalarning ishdan chiqishiga va dasturingiz xato natija berishiga olib kelishi ham mumkin.

# Chiziqli dasturlashning afzalliklari:
    # 1. Dasturlashni o'rganishga qulay.
    # 2. Sodda va tushunarli kod.
    # 3. Dastur algoritmini kuzatish oson.
    # 4. Dastur xotirada kamroq joy egallaydi.
# Chiziqli dasturlashning kamchiliklari:
    # 1. Murakkab dasturlarni chiziqli usulda yozish qiyin (ilojsiz).
    # 2. Bir dastur uchun yozilgan koddan boshqa dasturda qayta foydalanib bo'lmaydi.
    # 3. Dastur ichidagi ma'lumotlar (o'zgaruvchilar) barcha funksiyalar uchun ochiq. 
    # 4. ZAMONAVIY DASTURLAR CHIZIQLI EMAS.
# Vaqt o'tib dasturlarga qo'yilgan talablar murakkablashib borgani sababli chiziqli dasturlash tamoyili zamon talabiga javob bermay qo'ydi
# va 1970-yillarda OOP tamoyili olg'a surila boshlandi.


# OBYEKT NIMA?
# Object oriented dasturlashda o'zaro bog'liq bo'lgan o'zgaruvchilar va funksiyalar bitta konteynerga jamlanadi, bunday konteynerlar 
# obyekt deb ataladi. Bir obyektga tegishli o'zgaruvchilar uning xususiyatlari, unga tegishli funksiyalar esa metodlari deb ataladi.

# Keling misol tariqasida avtomobil degan obyektni ko'rib chiqamiz. Avtomobilning modeli, rangi va narxi uning xususiyatlari. Avtomobilga
# tegishli bo'lgan start(), stop() va tezlashish() kabi amallar esa uning metodlari deyiladi.

# Agar real dasturdam misol keltiradigan bo'lsak, istalgan dastur ichidagi tugma - bu obyekt. Uning shakli, rangi va matni esa
# xususiyatlari bo'ladi. Tugma ustida bajariladigan amallar tugmaning metodlari deyiladi. Misol uchun, tugmani bosish, uzoq bosish,ustiga
# sichqonchani olib borish va hokazo.

# Object oriented dasturlar o'nlab, balki, yuzlab obyektlardan iborat bo'ladi va bunday dasturlar uchun dastur boshiyoki oxiri degan 
# tushunchalar nisbiy.

# Object oriented dasturlar bajarilishida qat'iy ketma-ketlikka amal qilmaydi. Foydalanuvchi istalgan obyektga murojaat etishi, uning
# ustida turli amallar bajarishi mumkin. O'z navbatida, bitta obyektga murojaat ortidan boshqa obyektlar ham faollashishi mumkin.

# Misol uchun, mobil ilovalarda obyektlar dastur ichidagi tugmalar, matnlar, rasmlar va boshqa elementlardir. Foydalanuvchi istalgan
# tugmani bosishi, istalgan matnni ajratib olishi va boshqa amallarni istalgan tartibda bajarishi mumkin. Bunda bitta tugma (ya'ni obyektni)
# bosish bilan boshqa obyekt (masalan, rasm) o'zgarishi mumkin.

# Zamonaviy kompyuter o'yinlari ham minglab obyektlardan iborat. Foydalanuvchi esa virtual o'zyin olamida erkin harakat qilishi, istalgan
# tarafga yurishi, istalgan vaqtda turli obyektlar turli amallar bajarishi mumkin.


# KLASS NIMA?
# Object oriented programming haqida gaplashar ekanmiz, uning fundamental tushunchalaridan biri - klass haqida gapirib o'tmaslikning iloji 
# yo'q. Klass obyekt yaratish uchun shablon yoki qolipdir Bitta klassdan istalgancha nusxa olishimiz va yangi obyektlar yaratishimiz
# mumkin. Demak, obyekt - bu biror klassning xususiy ko'rinishi. Odatda, klasslarning nomi o'zgarmas, undan yaratilgan obyektlar esa 
# istalgancha nomlanishimumkin.

# Dasurimiz yuzlab obyektlardan iborat bo'lishi mumkin. Klasslar esa bizga obyektlarni yaratishni yengillashtiradi. Xoh dastur
# innterfeysidagi o'nlab turli xil tugmalar bo'lsin, xoh komyuter o'yinidagi qahramonlar bo'lsin. Har bir tugma yoki o'yin qahramoni
# va uning harakatlarini qayta-qayta yozmasdan, bir marta yaratilgan klassdan nusxa olib, o'nlab obyektlarni yaratishimiz mumkin.

# 24 - DARS TUGADI.

