# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 11:52:23 2025

@author: DavrServis
"""

## YAKUNIY DARS.

## Bu darsda kurs davomida ko'rilmagan, lekin ko'rib chiqishga tavsiya etiladigan ba'zi bir algoritmlar va ma'lumotlar tuzilmalariga 
## to'htalib o'tamiz.

## 1 - KO'RADIGAN MA'LUMOTLAR TUZILMASI BU TREE.

## Kurs boshida ARRAY ma'lumotlar tuzilmasi bilan tanishgan edik.
    ## AFZALLIGI: Binary Search yordamida tez qidirish.
    ## KAMCHILIGI: Har ma'lumot qo'shgandan so'ng ARRAY ni tartiblash (sorting).
    
## MUAMMO: Ma'lumotlarni tartiblangan holda qo'shish mumkinmi?
## Yechim: Binary Search Tree ma'lumotlar tuzilmasi.

## Binary Search Tree qanday ishlashini ko'ramiz:
    ## Deylik bizda ro'yxat bor. Bu ro'yxatda TOHIR degan element bor va biz yangi MOHIR degan o'zgaruvchi qo'shmoqchimiz.
    ## Bilamizki M harfi T harfidan oldin keladi, demak yangi elementimiz ro'yxatda birinchida bo'lishi kerak.
    ## Shu tarzda davom etadi, ya'ni yangi qo'shilgan element avtomatik ravishda alifbo tartibida tartiblanadi va ro'yxatimizda o'z joyini
    ## egallaydi.

## Qidirish osonligi:
    ## Ro'yxatimiz tartiblangan bo'lganligi uchun qidirish ham birmuncha tez bo'ladi ya'ni ortiqcha vat olmaydi.
    ## Binary Search da odatda element qo'shish qiyinroq (ya'ni yangi element qo'shish uchun mavjud elementlarni birma-bir surib chiqishimiz
    ## kerak edi).
    ## Binary Search Tree esa bunday emas huddi qidirish kabi qo'shish ham ko'p vaqt olmaydi.
    

## BINARY SEARCH TREE TURLARI:
    ## Boshqa (tree) shajara turlari.
        ## 1. Red-black tree (o'zini muvozanatga keltiradi).
        ## 2. B-tree (ma'lumotlar bazasida ishlatiladi).
        ## 3. Heap.
        ## 4. Splay tree.


## 2 - KO'RADIGAN MA'LUMOTLAR TUZILMASI BU INVERTED INDEXES.

## Tasavvur qiling bizda 3ta internet sahifasi bor va ular quyidagi ma'lumotlarni o'zida saqlaydi:
    ## Mohir.dev
        ## 1. Python.
        ## 2. JavaScript.
        ## 3. Data Science.
        ## 4. HTML.
        
    ## Sariq.dev
        ## 1. Python.
        ## 2. Django.
        ## 3. Sql.
        ## 4. Data Science.
        
    ## Mayoq.uz
        ## 1. JavaScript.
        ## 2. HTML.
        ## 3. Bootstrap.
        ## 4. Css.
        
## Demak bular har bir sahifaga tegishli bo'lgan kalit so'zlar. Endi tasavvur qiling siz Google ni toki Yandex ni ochtingizda Python degan 
## so'rovni beryapsiz. So'rovingizga javoban brauzer sizga minglab natijalarni qaytaradi. Aynan shuni qidirish algoritmlari INVERTED INDEXES
## ma'lumotlar tuzilmasi yordamida qiladi.

## Keling buni qanday ishlashini ko'ramiz:
    ## Avvaliga bu so'zlarning har biri uchun hash jadvalini yaratamiz.
        ## KALIT            QIYMAT
        ## python
        ## javascript
        ## data science
        ## html
        ## django
        ## sql
        ## bootstrap
        ## css