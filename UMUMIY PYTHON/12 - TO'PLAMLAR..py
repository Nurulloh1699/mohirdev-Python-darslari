# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 02:10:39 2025

@author: DavrServis
"""

# 12 - DARS.
# TO'PLAMLAR.

# Pythonda to'plam (set) yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta elementlarmni saqlashda
# qo'llaniladi. 
# To'plam yaratish uchunha lug'atlardagi kabi katta (jingalak) qavsdan foydalanamiz.
# sonlar = {1,2,3}
# print(sonlar)

# ismlar ={"Alijon", "Valijon", "Boqijon"}
# print(ismlar)
# To'plam bir xil elementni saqlamaydi.

# sonlar = {1,2,2,3,4,5,1,1,9} # Bir hil sonlar ishtirok etkan to'plam.
# print(sonlar) # Natija esa butkul boshqacha bo'ladi.

# ETIBOR BERING! Yuqoridagi kodning 1 - qatorida biz 3, 4 va 5 qiymatlarini 2 martadan takrorlab yozganimizga
# qaramay, to'plam ichida bu sonlar bir martadan saqlandi, xolos.
# Bo'shto'plam yaratish uchun set() funksiyasidan foydalanamiz:
# a = set() # Bo'sh to'plam yaratildi.

# Ro'yxatdan farqli o'laroq, set ichidagi elementlar biror tartibda saqlanmaydi va ularga indeks orqali murojaat qilib
# bo'lmaydi.
# sonlar = {1,2,3,4,5,6} # Oddiy to'plam.
# print(sonlar[0]) # Yuqoridagi to'plamni 1 - elementini chaqirishga urunsak. Xatolik beradi.

# Avvalgi bo'limda ko'rganimizdek, to'plamlar biror ro'yxatdan qaytarilgan elementlarni o'chirib tashlash uchun
# juda qulay:
# mevalar = ['olma', 'anjir', 'olma', 'uzum', 'olma', 'uzum'] # Elementlar bir necha bor qaytarilgan ro'yxat. 
# mevalar = set(mevalar) # Mevalar ro'yxatimizni set() ga o'zgartirdik.
# print(mevalar) # Bu ro'yxatni set() orqali konsolga chiqarsak barcha qaytarilgan elementlardan faqat bittadan 
# element qoldi.

# Yuqoridagi misolda mevalar ro'yxatida olma va uzum bir necha bor takrorlangan edi, biz set() funksiyasi yordamida 
# ro'yxatni to'plamga o'zgartirdik va ortiqcha elementlardan xolos bo'ldik.
# Agar to'plamni yana ro'yxatga o'tkazish talab qilinsa, list() funksiyasiga murojaat qilamiz:
# mevalar = list(mevalar) # Qaytadan mevalar ro'yxatimizni asl holiga qaytaramiz.
# print(mevalar) # Natija.

# TO'PLAMGA ELEMENT QO'SHISH.
# To'plamga yagona element qo'shish uchun .add() metodidan, bir nechta element qo'shish uchun esa .update() 
# metodidan foydalanamiz.
# mevalar = {'anjir', 'olma', 'uzum'} # Oddiy to'plam yaratib olamiz.
# mevalar.add('banan') # Bittagina element qo'shamiz.
# print(mevalar) # Natijani chiqaramiz.

# mevalar.update(['anor', 'qovun']) # To'plamimizga bir nechta element qo'shamiz.
# print(mevalar) # Natijani ko'ramiz.

# .update() metodidan foydalanganda parametr sifatida ro'yxat yoki lug'at uzatishimiz mumkin.

# TO'PLAMDAN ELEMENT O'CHIRISH.
# To'plamdan element o'chirish uchun .discard() va .remove() metodlari mavjud.
# mevalar = {'olma', 'banan', 'anjir', 'olma', 'uzum', 'olma', 'uzum'} # Oddiy to'plam.
# mevalar.discard('anjir') # .discard() metodi orqali bitta elementni o'chiramiz.
# print(mevalar) # Natija.

# mevalar.remove('banan') # .remove() metodi orqali bitta elementni o'chiramiz.
# print(mevalar) # Natija

# Yuqoridagi ikki metod bir vazifani bajaradi, ularning o'rtasidagi farq shundaki, agar biz o'chirmoqchi bo'lgan
# element to'plamda mavjud bo'lmasa .remove() metodi xato qaytaradi, .discard() esa xato qaytarmaydi.
# sonlar = {1,2,3,4,5,6} # Sonlar to'plami.
# sonlar.remove(7) # Yo'q sonni kiritkanimiz uchun xato qaytaradi.

# sonlar = {1,2,3,4,5,6} # Sonlar to'plami.
# sonlar.discard(7) # Yuqoridagi natijadan farqli o'laroq bunda xato qaytarmaydi.

# To'plamdan element o'chirishning (sug'urib olishning) yana bir usuli .pop() metodidir. Lekin to'plam elementlari
# indeksi mavjid bo'lmagani sababli .pop() metodi to'plamdan tasodifiy elementni sug'urib oladi:
# sonlar = {1,2,3,4,5,6,7} # Oddiy to'plam.
# son = sonlar.pop() # .pop() metodi orqali to'plamimizdan tasodifiy raqamni o'chiramiz (Sug'urib olamiz).
# print(son) # Natija.

# TO'PLAMALAR USTIDA AMALLAR.
# To'plamalar matematikada ham keng qo'llanilgani uchun ularning ustida  o'ziga xos matematik amallar bajarish mumkin.
# Misol uchun, ikki to'plamni birlashtirish uchun | operatori yoki .union() metodidan foydalanamiz.
# A = {1,2,3,4} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# B = {3,4,5,6} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# C = A|B # Endi ularni | operatori yordamida birlashtiramiz.
# print(C) # Natijani ko'ramiz.

# A = {1,2,3,4} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# B = {3,4,5,6} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# D = A.union(B) # Endi ularni .union() metodi bilan birlashtiramiz.
# print(D) # Natija.

# Ikki to'plamning kesishmasini (bir xil elementlarini) topish uchun esa & operatori yoki .intersection() metodidan
# foydalanamiz:
# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# c = a&b # Endi ularni & operatori orqali ikki to'plamning bir xil elementlarini topamiz.
# print(c) # Natija.

# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# d = a.intersection(b) # .intersection() metodi yordamida ikki to'plamning bir xil elementlarini topamiz.
# print(d) # Natija.

# Ikki to'plam o'rtasidagi farqni topish uchun esa ayirish (-) operatori yoki .difference metodidan foydalanamiz.
# B to'plamning A to'plamdan farqi deganda (A-B) Ato'plamga kiruvchi, lekin B to'plamda yo'q elementlar tushuniladi.
# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# print(a-b) # Natija a-b yani aytib o'tkanimizday a da bor b da esa yo'q elementlar tushuniladi.

# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# print(b.difference(a)) # Natija, endi esa b da bor a da esa yoq elementlar chiqadi.

# To'plamlar o'rtasidagi simmetrik farqni topish uchun ^ operatori yoki .symmetric_difference() metodidan foydalanamiz.
# Simmetrik farq deb A va B to'plamga kiradigan, lekin bir vaqtda ikkalasiga kirmaydigan elementlar tushuniladi.
# Quyidagi misolda {3,4} elementlari ikkala to'plamda bo'lgani uchun simmetrik farqqa kirmaydi.
# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# c = a^b
# print(c)

# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# d = a.symmetric_difference(b)
# print(d)

# AMALIYOT TOPSHIRIQLARI.
#1 - uch xil ranglar saqlangan to'plam yarating.
# colors = {'sariq', 'qizil', 'qora'}
# print(colors)

#2 - To'plamga .add() va .update() metodlari yordamida ranglar qo'shing.
# colors.add('yashil')
# colors.update(['kumush', 'binafsha'])
# print(colors)

#3 - Quyidagi ikki to'plam uchun umumiy elementlarni ajratib olib, yangi to'plam yarating:
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# set3 = set1 & set2
# print(set3)

#4 - Yuqoridagi ikki to'plam orasidagi farqlarni konsolga chiqaring.
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# set3 = set1 - set2
# print(set3)
# set4 = set2 - set1
# print(set4)

#5 - Ikki to'plam orasidagi simmetrik farqni toping.
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# set3 = set1 ^ set2
# print(set3)

#6 - Sizdaquyidagi ro'yxat bor:
# bozorlik = ['choy', 'non', 'kortoshka', 'tuxum', 'sut']
# mahsulotlar = ['non', 'sut', 'tuxum', 'olma', 'un', 'tuz']
# bozorlik - siz sotib olishingiz kerak bo'lgan narsalar;
# mahsulotlar - do'kondagi mavjud mahsulotlar.

#7 - Sotib olishingiz kerak bo'lgan mahsulotlarning qay biri do'konda bor ekanini alohida ro'yxat (list) saqlang.
# obm = []
# for n in bozorlik:
#     if n in mahsulotlar:
#         obm.append(n)
# print(f"Do'konda bor mahsulotlar quyidagilar: {obm}")
        
#8 - Do'konda mavjud bo'lmagan mahsulotlar ro'yxatini yarating.
# dmbm = []
# for n in bozorlik:
#     if n not in mahsulotlar:
#         dmbm.append(n)
# print(f"Do'konda mavjud bo'lmagan mahsulotlar quyidagilar: {dmbm}")
 
#9 - Do'kon egasi siz so'ragan mahsulotlarni olib keldi. Mahsulotlar ro'yxatiga yangi mahsulotlarni qo'shing.
# mahsulotlar.append('choy')
# mahsulotlar.append('kortoshka')
# print(mahsulotlar)

# 12 - DARS TUGADI.