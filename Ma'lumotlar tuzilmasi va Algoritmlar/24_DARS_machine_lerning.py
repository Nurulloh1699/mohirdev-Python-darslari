# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 15:15:56 2025

@author: DavrServis
"""

## MACHINE LEARNING.

## Machine Learning bu - mavjud ma'lumotlar asosida kompyuterlarni (odamlarni emas) turli muammolarga algoritm tuzishga o'rgatish.

## Machine Learning zamonaviy SUN'IY INTELEKT dasturlarining asosi hisoblanadi.

## K-NN Machine Learning da keng qo'llanuvhci algoritmlardan biri.


# MISOL KELTIRAMIZ.
## OCR (optical character recognition) - rasmni yoki qo'lyozmani kompyuter matniga o'zgartirish texnologiyasi.
## Shu OCR texnologiyasida ham K-NN algoritmi ishlatiladi. Parametr sifatida belgidagi to'g'ri va egri CHIZIQLAR va KESISHMALAR olinadi.

## YANA BIR MISOL COMPUTER VISION deb ataladi.
## Bu holatda, tasvirdagi (video yoki rasm bo'lishi mumkin) obyektlarni aniqlash, nafaqat aniqlash balki tanib olish ham bo'lishi mumkin.
## Bu yerda ham K-NN algoritmi ishlatiladi. Bu yerada ham parametr sifatida chiziqlar burchaklar va xokazolar orqali obyektni nima ekanini
## aniqlashimiz mukin bo'ladi.

## NAVBATDAGI MISOL SPAM FILTERLAR.
## Hozirgi zamonaviy mail hizmatlari sizning manzilingizga kelayotkan habarlarni tartiblay oladi, ya'ni ma'lum talabga javob berganlarni
## oddiy xatlar qatoriga boshqalarini esa spam (musr) qiladi. Bu holatda ham K-NN algoritmi ishlaydi yan'ni spamda mavjud xatlar o'rganiladi
## va ularni yangi kelgan habarlarga solishtirish orqali ularni tartiblay oladi.

## NAVBATDAGI MISOL REGRESSIYA YORDAMIDA JARAYONLARNI BASHORAT QILISH.
## Biz REGRESSIYA yordamida bir foydalanuvchi biror kinoga nechchi ball bilan baholashi mumkin ekanini ko'rgan edik. Aslida REGRESSIYA 
## yordamida nibatan murakkabroq muammolarga ham yechim topishimiz mukin. Jarayonlarni bashorat qilish:
    ## 1. Do'llarning o'sishi yoki tushishi.
    ## 2. Har xil aksiyalar.
    ## 3. Qimmatbaho metal narxlari va xokazo.
## Bularni aniqlashda ishlatiladigan parametrlar esa har xil o'zgarishlar (bozoedagi, jamiyatdagi ) ni hisobga olishimiz kerak bo'ladi.