# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 11:41:33 2025

@author: DavrServis
"""

## DIVIDE_and_CONQUER.

## MISOL KO'RAMIZ.
    ## Berilgan ARRAY elementlari yeg'indisini hisoblash: [5, 8, 12, 22].

## BAJARILADIGAN ISH:
    ## 1. To'xtash shartini aniqlaymiz.
        ## Agar ARRAYda 1ta element bo'lsa, shu elementni qaytaramiz.
        ## Agar ARRAYda element bo'lmasa, 0ni qaytaramiz.
    ## 2. To'xtash shartiga yetish uchun har qadamda muammoni kichraytirish yo'lini topamiz.
        # Har qadamda 0ta elementdan iborat ARRAYga yaqinlashamiz.
def array_sum(arr):
    """REKURSIYA yordamida massiv (ARRAY) elementlari yeg'indisini hisoblaydi"""
    # Bazaviy holat: Agar massiv bo'sh bo'lsa, yig'indi 0ga teng.
    if not arr:
        return 0
    
    ## Birinchi elementni olib, qolgan elementlar yeg'indisini REKURSIV hisoblash.
    return arr[0] + array_sum(arr[1:])

## **Test qilish**
arr = [5, 8, 12, 22] # Hisoblash uchun massiv.
print(f"Massiv elementlari yeg'indisi: {array_sum(arr)}") # Natijani chiqarish.

## Qanday ishlaydi?
    ## arr[0]:
    ## arr — bu massiv (ro'yxat).
    ## arr[0] orqali massivning birinchi elementi olinadi.
## Masalan, agar arr = [5, 8, 12, 22] bo'lsa, arr[0] = 5.
    ## arr[1:]:
    ## arr[1:] — bu slice (kesim) operatori.
    ## 1: bu yerda massivni 1-indeksdan boshlab oxirigacha oladi.
## Masalan, arr = [5, 8, 12, 22] bo'lsa, arr[1:] = [8, 12, 22].
    ## Har bir rekursiya chaqiruvida massiv bir elementga qisqaradi.
    ## array_sum(arr[1:]):
    ## array_sum() — bu rekursiv funksiya, ya'ni o'zi o'zini chaqiradi.
    ## Funksiya arr[1:] qisqartirilgan massiv bilan yana o'zini chaqiradi.