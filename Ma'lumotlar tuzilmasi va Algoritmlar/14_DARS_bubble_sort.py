# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 12:47:21 2025

@author: DavrServis
"""

## BUBBLE SORT - bu eng sodda va shu o'rinda sekin ishlaydigan tartiblash algoritmi.
## BUBBLE SORT - bunda har bir element navbatma-navbat o'zidan keyingi element bilan solishtiriladi va kerak bo'lsa joyi almashtiriladi.
## BUBBLE SORT algoritmining n ta element uchun tahminiy qadamlar soni BIG O: O(n²) ga teng bo'ladi va bu TAHMINIY QIYMAT.

## QANDAY ISHLAYDI: Boshqa aksar algoritmlar singari BUBBLE SORT ham ro'yxatni o'sish tartibida tartiblaydi.
## Deylik bizda quyidagi ro'yxat mavjud:
[34, 25, 20, 5, 44]
    ## 1 - qadam -> [(34, 25,) 20, 5, 44] 34 va 25 sonlari solishtiriladi. Birinchi element ikkinchidan katta bo'lsa o'rni almashtiriladi.
    ## 2 - qadam -> [25, (34, 20,), 5, 44] 34 sonining joylashuvi o'zgardi va endi 34 va 20 sonlari solishtiriladi.
    ## 3 - qadam -> [25, 20, (34, 5,) 44] 34 sonining joylashuvi yana o'zgardi va endi 34 va 5 sonlari solishtiriladi.
    ## 4 - qadam -> [25, 20, 5, (34, 44)] endi 34 soni solishtiriladigan sondan ko'ra kichik bo'ldi 34 va 44. Endi joylar o'zgarmaydi.
    ## 5 - qadam -> [(25, 20,) 5, 34, 44] endi algoritm boshqattan boshlanadi va endi u 25 sonini qolgan sonlar bilan solishtirib chiqadi.
    ##
    ##
    ## n - qadam -> [5, 20, 25, 34, 44] n ta (BIG O: O(n²)) qadamdan so'ng esa bizda tartiblangan ro'yxat hosil bo'ladi.
    
    
## AMALIYOT:
def bubble_sort(array):
    """
    BUBBLE SORT algoritmi yordamida massivni tartiblash funksiyasi.
    Har bir qadamda massiv holatini ko'rsatib boradi.
    """
    
    n = len(array) # Massiv uzunligini aniqlaymiz. N massivdagi elementlar soni. Berilgan ARRAY da nechta element bo'lsa n shunga teng.
    step = 1 # Qadamlarni hisoblash uchun o'zgaruvchi. Har bir qadamda qanday amal bajarilishi ko'rib borish uchun.
    
    ## Massivda n - 1 marta takrorlash amalga oshiriladi. Har bir aylanishda ENG KATTA ELEMENT o'z joyiga o'tadi, shuning uchun har safar 
    ## ichki sikl uzunligi 1 taga kamayadi.
    for i  in range(n - 1):
        print(f"\n{i + 1}-chi tashqi aylanish:") # Har bir TASHQI AYLANISH boshlanishida aylanish raqamini ko'rsatadi. i + 1 bo'lishiga 
        ## sabab i aslida 0 dan boshlanadi, lekin o'quvchilar uchun 1 dan boshlab ko'rsatsih qulay.
        
        ## Har bir takrorlashda elemntlarni juft-juft solishtirish.
        for j in range(n - 1 - i): # ICHKI SIKL elementlarini JUFT-JUFT solishtirish uchun ishlatiladi. Har bir tashqi aylanishdan keyin
        ## ichki aylanish uzunligi kamayib boradi (n - 1 - i). Bu esa allaqachon joyiga tushgan elementlarni qayta tekshirmaslikka imkon
        ## beradi. 
            
            ## Joriy va keyingi elementlarni ko'rsatish.
            print(f" Solishtirish: {array[j]} va {array[j + 1]}", end=" ") # Joriy (array[j]) va keyingi (array[j + 1]) elementlarni 
            ## solishtirishdan avval ekranga chiqaradi. end=" " - yangi qatorga o'tmasdan, o'sha qqatorda davom ettiradi.
            
            ## Agar joriy element o'zidan keyingi elementdan katta bo'lsa.
            if array[j] > array[j + 1]: # Agar jot=riy element (array[j]) o'zidan keyingi elementdan (array[j + 1]) katta bo'lsa:
                ## Elementlar o'rnini almashtirish (swap) amalga oshiriladi.
                
                ## Elementlarni joyini almashtirish
                array[j], array[j + 1] = array[j + 1], array[j] # Orin almashtirish (swap) usuli:
                ## Masalan, massiv holati: [64, 32, 25], 64 va 32 o'rnini almashtirish:
                   ## [64, 32, 25] -> [32, 64, 25] Bu usul o'zgaruvchilarning o'rnini almashtirishni oson qiladi.
                print(f"-> O'rni almashtirildi: {array}") # Agar elementlar joyi almashtirilgan bo'lsa, yangilangan massiv holatini ko'rsatadi
            else: # Aks holda.
                print("-> O'rni alamashtirilmadi.")
                
            ## Har bir qadamda massiv holatini ko'rsatish.
            print(f" {step}-qadam: {array}") # Har bir qadamdan so'ng STEP qiymatini 1 ga oshiradi.
            step += 1 # Qadamlar sonini oshirish. Bu orqali har bir qadam raqamlari to'g'ri ketma-ketlikda bo'ladi.
            
    print("\n Yakuniy tartiblangan massiv:", array) # Massiv to'liq tartiblangandan keyin yakuniy natijani ko'rsatadi.
    return array # Funksiya saralangan massivni qaytaradi. Natijani boshqa joyda foydalanish uchun massivni funksiya chiqishi sifatida beradi.

## **Test qilish**
arr = [64, 32, 25, 12, 22, 11, 90] # Saralanishi kerak bo'lgan massiv.
sorted_arr = bubble_sort(arr) # Funksiyani chaqiramiz.