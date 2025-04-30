# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:57:10 2025

@author: DavrServis
"""

def Natija(a, b): # Ikkita sonni yeg'indisini hisoblovchi dastur.
    summa = a + b # Ikkita son qo'shiladi va yeg'indi summa ga tenglanadi.
    return summa # Funksiya summa ni qaytaradi.

print(Natija(2, 6))


def getLargest(a, b, c): # 3ta sondan eng kattasini topadigan funksiya.
    if a > b: # Agar a katta bo'lsa b dan.
        if a > c: # Agar a katta bo'lsa c dan. 
            return a # Yuqoridagi ikkita shart qanoatlantirilsa a ni konsolga chiqar. 
        else: # Aks holda.
            return c # c ni konsolga chiqar.
    else: # Aks holda.
        if b > c: # Agar b katta c dan.
            return b # b ni konsolga chiqar.
        else: # Aks holda. 
            return c # c ni konsolga chiqar.
        
print(getLargest(8, 16, 89))


def Faktorial(N): # Kiritilgan sonnong faktorialini hisoblovchi funksiya.
    i = 1 
    fakt = 1
    while i != N + 1: # i teng bo'lmasa N ga, N ga 1 qo'shilsin va sikl boshqattan bajarilsin.sikl i 1dan N gacha bo'lgan qiymatni qabul
    # qiladi.
        fakt = fakt * i # fakt ga fakt va i ko'paytmasini tenglaymiz.
        i += 1 # i ga +1 qo'shib boramiz.
    return fakt # Natijani fakt ko'rinishida qaytaramiz.

print(Faktorial(5))

