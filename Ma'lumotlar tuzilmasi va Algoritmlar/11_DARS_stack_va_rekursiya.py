# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 08:27:04 2025

@author: DavrServis
"""

## STACK va REKURSIYA.

## Aslida REKURSIV funksiyalar ham STACK asosida ishlaydi va dasturlashda bu CALL STACK yoki PROGRAM STACK deyiladi. Biz hozir STACKga faqat
## ma'lumotlarni saqlayapmiz, aslida faqatgina ma'lumotlarni emas balki, bir nechta funksiyalarni bajarilish ketma-ketligini ham STACK 
## yordamida nazorat qilish mumkin, STACK va REKURSIYA yordamida.

## MISOL KO'RAMIZ.
## Esingizda bo'lsabiz avalgi darsimizda FAKTORIAL funksiyasini yozdik va bu orqali N faktorialni hisoblashni o'rgangan edik.
def fact(n): # Faktorial hisoblovchi funksiya.
    if n == 1: # Agar uzatilgan qiymat 1 ga teng bo'lsa.
        return 1 # 1 ni o'zini qaytaradi.
    else: # Aks holda.
        return n * fact(n - 1) # n qiymatini ko'paytiradi toki n 1ga teng bo'lib qolmaguncha (har gal ko'paytirish amalaga oshirilganda 
## qiymatdan 1 ayirilib boriladi). 
    
print(fact(5))

## KODNI TAHLIL QILAMIZ:
## Bu holatda CALL STACK yuzaga keladi, ya'ni funksiyamizdan qiymat qaytishi uchun avval qiymatimiz 1ga teng bo'lmaguncha qolgan amallarni 
## xotiradi saqlab turadi.

## 1. Uzatilgan qiymat tekshiriladi
## 2. IF sharti qanoatlantirilmasa ELSE shartiga o'tib ketadi.
## 3. ELSE dan olingan qiymat hisoblanadi n * fact(n - 1) = fact 4.
## 4. Endi CALL STACK boshlanadi, ya'ni sikl boshqattan boshlanadi. Yana shart tekshiriladi yana 1ga teng emas va shu tariqa 1ga teng
## bo'lguncha.
## 5. Qiymat 1ga teng bo'lgan endi qiymatni hisoblashga beriladi, qaytgan 1 qiymati, ohirgi qaytgan qiymat fact(2) uzatiladi.
## Bizda 2 * 1 = 2 degan misol paydo bo'ladi. Endi bu qiymat ham fact(3) ga uzatiladi va 3 * 2 = 6. Davomida olingan qiymat fact(4) ga 
## uzatiladi, endi bizda 4 * 6 = 24 degan qiymat bor va ohirgi amal, olingan qiymat fact(5) ga uzatiladi. Endi bizda 5 * 24 = 120 degan 
## qiymat hosil bo'ladi. Berilgan qiymat 5 bo'lgani uchun suklimiz tugaydi va olingan qiymat 120 ko'rinishida konsolga chiqadi.
