# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:25:41 2025

@author: DavrServis
"""

# ARRAY vs LINKED LISTS.

# ARRAY - har bir elementi xotirada ketma-ket joylashgan bo'lishi kerak. Agar element qo'shmoqchi bo'lsak, har bir elementni bittadan surib
# chiqishimiz kerak bo'ladi (ro'yxat boshiga yoki o'rtasiga element qo'shmoqchi bo'lsak). Agar ro'yxat joylashgan joydagi element surilishi
# kerak bo'lgan yacheyka band bo'lsa, mavjud ro'yxat va yangi element ham sig'adigan boshqa joyga ko'chirishimiz kerak bo'ladi va albatta bu
# ish juda ko'p vaqt oladi. 

# LINKED LISTS - ARRAY dan farqli ravishda elementlari xotirada ketma-ket joylashishi shart emas, xotirada bo'sh bo'lsa kifoya. Yngi element
# qo'shishda ham bir qator qulayliklar bor, ya'ni yuqorida ARRAY elementlarni bittadan surib chiqish, agar elementlar sig'may yangi joy talab
# qilinish holatlari bo'lmaydi. Biz shunchaki hohlagan bo'sh joyimizga element qo'shib shuchaki unga yo'lni ko'rsatib (bog'lab) qo'yamiz
# holos.

# SOLISHTIRAMIZ:

# ELEMENT O'QISH:
# --- ARRAY dan o'qish bitta operatsiya talab qiladi va oson (kam vaqt va resurs talab qiladi, chunki ular indekslangan bo'ladi).
# --- LINKED LISTS da o'qish  N ta operatsiya talab qiladi (chunki biz dasturchi sifatida faqat birinchi element manzilini bilamiz holos).

# ELEMENT QO'SHISH:
# Bu yerda aksincha LINKED LISTS ustun.
# --- ARRAY ga element qo'shish uchun biz har bir element bilan ishlashimizga to'g'ri keladi.
# --- LINKED LISTS ga element qo'shishimiz uchun ortiqcha vaqt talab qilinmaydi, shunchaki bo'sh joy bo'lishi kifoya qiladi.

# O'CHIRISH:
# Agar xotirangizda joy qolmagan bo'lsa va siz bir necha ming yoki mln ta elementdan iborat ma'lumotni xotiraga olib kelmoqchisiz. ARRAYda
# buni imkoni yo'q. Sizga bu ma'lumotlardan bor yog'i boshidagi 10tasi kerak bo'lsa ham siz avval hamma elementlarni xotiraga joylashingiz 
# kerak va buni ARRAY bilan qila olmaysiz.

# LINKED LISTS esa sizga buni qilishingizga imkon yaratadi. Bu holatda LINKED LISTS ning afzalligi shundaki, o'sha katta hajmdagi ma'lumotni
# siqqan qismini olib kelishingiz mumkin, ya'ni sizning dasturingiz LINKED LISTS da bo'lsa ayni o'sha vaqtda xotiraga qancha ma'lumot sig'sa
# shunchasini olib kira olasiz.

## QAYSI HOLATLARDI QAYSI MA'LUMOT TUZILMASINI IHSLATISH TAVSIYA QILINADI.
# 🔥 ARRAY va LINKED LIST qachon ishlatiladi? (Jadval)
# Xususiyat	Array	Linked List
# Tezkor kirish (Random Access)	--> ✅ Ha (O(1)) - ❌ Yo‘q (O(n))
# Qo‘shish/o‘chirish	--> ❌ Sekin (O(n)) - ✅ Tez (O(1))
# O‘lchamni oldindan bilish	--> ✅ Ha (oldindan aniqlanadi) - ❌ Yo‘q (dinamik)
# Qo‘shimcha xotira 	--> ❌ Ko‘p joy talab qiladi - ✅ Samarali
# Ko‘p qidirish	--> ✅ Tez (O(log n) Binary Search) - ❌ Sekin (O(n))
# Ma’lumotlar doimiy o‘zgarib tursa	 --> ❌ Yomon - ✅ Yaxshi

# 🔥 Xulosa: Qaysi holatda qaysi biri?
# Holat	Qaysi biri yaxshi?
# ✅ Qidirish va indeks bo‘yicha tez kirish -->	 Array
# ✅ Tez-tez qo‘shish yoki o‘chirish	--> Linked List
# ✅ Dinamik ravishda o‘sadigan ma’lumotlar	--> Linked List
# ✅ O‘zgarmaydigan, statik ma’lumotlar	--> Array
# ✅ Ko‘p saralash va qidirish talab qilingan joylar --> Array
# ✅ Stack va Queue kabi ma’lumotlar tuzilmalari	--> Linked List

## Agar oddiy misol bilan tushuntirish kerak bo‘lsa:

# Array → Bu o‘rindiqlar qatori (maktabda yoki samolyotda). Har bir o‘rindiq o‘z joyiga ega, lekin o‘rindiq qo‘shish yoki olib tashlash qiyin.
# Linked List → Bu avtobusdagi odamlar. Odamlar avtobusga osongina chiqib, tushib ketishadi, lekin o‘rtadagi odamni topish vaqt talab qiladi.