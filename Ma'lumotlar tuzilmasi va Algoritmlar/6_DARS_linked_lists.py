# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:34:07 2025

@author: DavrServis
"""

## LINKED LISTS.

## LINKED LIST ning tarjimasi bog'langan ro'yxat degan ma'noni beradi.

## --- LINKED LIST - bu ketma-ketligi xotiradagi joylashuviga bog'liq bo'lmagan chiziqli ma'lumotlar to'plami. ARRAY bilan farqi
## LINKED LIST elementlar xotirada ketma-ket joylashmaydi, CHIZIQLI deyishimizga sabab bu elementlar bir-biriga ketma-ket bog'langan
## bo'ladi.

## --- Ro'yxatning har-bir elementi keyingi elementga ishora qiladi. Bog'langan deb aytdik bu bog'lanishi bir biriga ishora qilib turadi.

## --- Ma'lumotlar tuzilmasi sifatida LL ni bir-biriga bog'langan tugunlar ko'rinishida tasavvur qilamiz.

## --- Har bir tugun o'z qiymatini va keyingi element manzilini saqlaydi. Ya'ni misol uchun birinchi elementda, birinchi elementning qiymati
## va undan tashqari keyingi elementning manzili ham saqlanadi. Shu yo'sinda ikkinchi, uchinchi va hokazo davom etadi. Shu o'rinda aytish
## kerak eng ohirgi element hech qayerga ishora qilmaydi (None)


## LINKED LISTS turlari.

## --- SINGLY LINKED LISTS - bir tomonlama ro'yxat.
## Elementlar ketma-ket bog'langan bo'ladi va ohirgi element hech qayerga bog'lanmaydi.

## --- CIRCULAR LINKED LISTS - aylana ro'yxat.
## Elementlar ketma-ket bog'langan bo'ladi va ohirgi element ham kelib birinchi elementga bog'lanadi.

## --- DOUBLE LINKED LISTS - ikki tomonlama ro'yxat.
## Elementlar ketma-ket bog'langan bo'ladi va har bir element o'zidan oldingi va keyingi element manzilini saqlaydi ya'ni ikki tomonlama 
## bog'langan bo'ladi.


## ABSTRAKT MA'LUMOT TURLARI - yuqorida olinayotgan bilimlarni biror-bir dasturlash tiliga bog'lamagan holda umumiy ko'rinishda o'rganish
## yoki qabul qilish.


## LINKED LISTSda amaliyot.

# class Node: # LINKED LISTS uchun kerak bo'ladigan birinchi obyektimiz ya'ni tugun.
#     """Tugun (Node) obyekti"""
#     def __init__(self, data): # Node obyektining konstruktori.
#         self.data = data # Tugunning qiymati (data) ni saqlash.
#         self.next = None # Keyingi tugunga havola, hozircha yo'q (None)
        
# class LinkedList: # Bu sinf barcha tugunlarni bog'lovchi LINKED LISTS obyekti hisoblanadi.
#     """Linked List obyekti"""
#     def __init__(self): # LINKED LIST obyekti konstruktori.
#         self.head = None   # Ro'yxat boshida hech qanday tugun yo'q, shuning uchun head = None.

