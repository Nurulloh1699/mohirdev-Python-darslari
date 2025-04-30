# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:20:05 2025

@author: DavrServis
"""

# # ARRAY - MA'LUMOT TUZILMASI.

# ## Massiv (Array) — bu ma'lumotlar tuzilmasi bo'lib, unda bir xil turdagi elementlar ketma-ket tartibda saqlanadi. Har bir elementga indeks
# ## yordamida murojaat qilish mumkin. Massivda elementlar noldan boshlab tartiblanadi. Murojaat qilishda osongina indeks orqali murojaat 
# ## qilinadi.

# # Oddiy massiv yaratish
# sonlar = [5, 10, 15, 20]

# # Elementlarga indeks orqali murojaat qilish
# print(sonlar[0])  # Natija: 5
# print(sonlar[2])  # Natija: 15

# # Massiv elementini o'zgartirish
# sonlar[1] = 50
# print(sonlar)  # Natija: [5, 50, 15, 20]

# # Yangi element qo'shish
# sonlar.append(25)
# print(sonlar)  # Natija: [5, 50, 15, 20, 25]

# # Elementni o'chirish
# sonlar.pop(2)  # Indeksi 2 bo'lgan elementni o'chiradi (15)
# print(sonlar)  # Natija: [5, 50, 20, 25]



## ARRAY va XOTIRA.

## Agar ARRAY ga yangi element qo'shmoqchi bo'lsak, kompyuter mavjud ARRAY ning yonini tekshiradi va yonma-yon saqlaydi.

## Agar mavjud ARRAY ning o'rtasiga element qo'shmoqchi bo'lsak, protsessor mavjud elementlarni ko'rib ularni o'rtasidan o'ng tomondagilarni
## elementlarni bittadan o'ng tomonga siljitib chiqadi va saqlamoqchi bo'lgan elementimizga joy bo'shatadi, bo'shagan joyga qo'shmoqchi
## bo'lgan elementimizni saqlaydi. Agar ro'yxatning eng boshiga element saqlamoqchi bo'lsak shu jarayon takrorlanadi.Etibor bersangiz har gal
## element saqlanishi uchun siljish amalga oshirilyapti va har bir siljish bitta operatsiya degani.

## Agar biz ARRAY ning ichida biror bir ma'lumotni o'chirib tashlamoqchi bo'lsak, masalan o'rtadagi 5 indeksdagi elementni o'chirmoqchi
## bo'lsak, yuqoridagi protses teskari tomonga qaytariladi va o'chirilgan element tomonga elementlar suriladi. 

## Agar biz element qo'shmoqchi bo'lsagi lekin xotiradagi ohirgi elementdan keyingi yacheyka bo'sh emas, bu holatda kompyuter xotiradan
## yangi 11ta element sig'adigan bo'sh o'rin qidiradi (deylik 10ta elementli ro'yxat boridi va 11 - elementni qo'shmoqchi bo'lyapmiz)
## va topilgan joyga ma'lumotlarni ko'chirib chiqadi.


## ARRAY va BIG O.
## Esingizda bo'lsa BIG O biror amalni bajarish uchun maksimum sarflanadigan operatsiyalar sonini hisoblaydi. Agar biz ARRAY ga biror 
## elementni o'qimoqchi bo'lsak maksimum bitta operatsiya talab qilinadi va aksincha qo'shmoqchi bo'lsa operatsiyalar soni N ga teng bo'ladi.
## Bu holatda N deganda ro'yhatda allaqachon mavjud elementlar soni nazarda tutiladi, chunki element qo'shish uchun ro'yhatdagi elementlar 
## bittadan siljitilishi talab qilinadi. ESLATMA! BIG O bu eng yomon holatdagi operatsiyalar sonini hisoblaydi ya'ni ro'yxatning boshiga
## element qo'shmoqchi bo'lsak va biz agar ro'yxatning boshiga emas balki ohiriga element qo'shishimiz talab qilinsa yoki xotirada bo'sh joy
## topilmasdan ro'yxatni xotiradagi boshqa joyga ko'chirish talab qilinsa oparatsiyalar soni tabiiyki ozayadi.

## Misol ko'radigan bo'lsak. 
## Tasavvur qilamiz sizda foydalanuvchilar ro'yxati bor va kimdir sizning sahifangizga kirmoqchi. 
## Bu holatda u o'zini login va parolini kiritadi, bu paytda kompyuteringiz bu loginni sizning ro'yxatingizda bor yoki yo'qligini tekshiradi
## (BINARY SEARCH ishlatilishi mumkin), bu holatda element o'qish uchun bitta operatsiya bajariladi holos. Lekin deylik sizda 1mln ta
## foydalanuvchi bor va siz yangi foydalanuvchi qo'shmoqchisiz, ana endi yangi foydalanuvchi qo'shish uchun har gal protsessor 1mln ta
## operatsiya bajarishi kerak bo'ladi. Shunday holatda agar bir vaqnint o'zida 10ta odam ro'yxatndan o'tmoqchi bo'lsa kompyuter 10mln ta
## operatsiya bajarishi kerak bo'lib qoladi.

## Shu sababdan, agar bizda biror bir ro'yxat bo'lsaku va bu ro'yxatga qayta-qayta ma'lumot qo'shish talab qilinsa ARRAY dan foydalanish
## tavsiya qilinmaydi va aksincha ro'yxat bo'lsayu unga ma'lumot qo'shish talab qilinmasa, faqat ma'lumot o'qish kerak bo'ladigan bo'lsa 
## ARRAY juda ham foydali malumot tuzilmasi bo'ladi.




