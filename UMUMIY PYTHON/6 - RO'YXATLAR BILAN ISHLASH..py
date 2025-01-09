# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:24:39 2025

@author: DavrServis
"""

# 6 - DARS.
# RO'YXATLAR BILAN ISHLASH.

# Bazi holatlarda ro'yxat elementlarini alifbo ketma-ketligida tartiblash talab qilinishi mumkin. Buning uchun maxsus 
# .sort() metodidan foydalanamiz. 
# cars = ['damas', 'jiguli', 'matiz', 'tico', 'nexia'] # <- oddiy ro'yxat.
# cars.sort() # Alifbo ketma-ketligida tartiblaymiz.
# print(cars) # Natija.

# Tartiblashda bosh harf kichik harfdan oldin kelishini etiborga oling. Agar ro'yxatdagi so'zlarning bosh harfi katta
# kichik aralash yozilgan bo'lsa ularni bir tartibga keltirib olish maqsadga muvofiq.
# moshinalar = ['damas', 'jiguli', 'matiz', 'GM', 'tico', 'nexia'] # Bu ro'yxatda endi bosh harfli so'zlar ham bor.
# moshinalar.sort() # Tartiblaymiz.
# print(moshinalar) # Natija.
# Bu holatda endi 'GM' eng birinchiga chiqib qoladi buni oldini olish uchun ro'yxatni bir hil ko'rinishga keltirib olish
# lozim.

# RO'YXATNI TESKARI TARTIBLASH.
# moshinalar = ['damas', 'jiguli', 'matiz', 'gm', 'tico', 'nexia'] # Oddiy ro'yxat.
# moshinalar.sort(reverse=True) # Ro'yxatni teskari tartiblaymiz.
# print(moshinalar) # Natija.

# RO'YXATNING ESKI HOLATIGA TEGMAGAN HOLDA TARTIBLASH.
# guests = ['Bahodir', 'Rahmatjon', 'Anvar', 'Farrux', 'Hasan', 'Husan', 'Shodmon'] # Oddiy ro'yxat.
# print(".sorted() qaytargan natijadagi ro'yxat: ", sorted(guests), "\n") # .sorted yordamida tartiblangan ro'yxat.
# print(".sorted() funksiyasi yordamida teskari tartiblangan ro'yxat: ", sorted(guests, reverse=True), "\n") # .sorted()
# yoedamida teskari tartiblangan ro'yxat.
# print("Asl holatdagi ro'yxat: ", guests, "\n") # Asl ro'yxat.

# Yuqoridagi ikki usul orqali sonlarni ham tartiblashimiz mumkin.
# ages = [21, 24, 45, 25, 79, 1] # <- Oddiy tartibsiz ro'yxat.
# print(ages) # Asl ro'yxat.
# print(sorted(ages)) # Tartiblangan.
# print(sorted(ages, reverse=True)) # Teskari tartiblangan.

# RO'YXATLARNI AYLANTIRISH.
# Buning uchun bizga .reverse() metodidan foydalanamiz.
# fruits = ['pear', 'apple', 'apricot', 'watermelon', 'lemon'] # Oddiy ro'yxat.
# fruits.sort() # Alifbo bo'yicha tartiblangan.
# print(fruits) # Natija.
# fruits.reverse() # Teskari tartiblangan.
# print(fruits) # Natija.

# RO'YXARNING UZUNLIGINI TOPISH YANI UNING ICHIDAGI ELEMENTLAR SONINI ANIQLASH.
# Buning uchun bizga len() funksiyasi kerak bo'ladi.
# fruits = ['pear', 'apple', 'apricot', 'watermelon', 'lemon'] # Oddiy ro'yxat.
# print(fruits) # Ro'yxat elementlari.
# print("FRUITS ro'yxatidagi elementlar soni: ", len(fruits)) # Elementlar soni.

# RANGE() FUNKSIYASI.
# RANGE() funksiyasi oraqli biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. 
# sonlar = list(range(0,10)) # Bu o'rinda yaratilgan sonlar ketma-ketligini list orqali ro'yxatga yuklab oldik.
# print(sonlar) # Aytib o'tish kerakki range() funksiyasi belgilangan sonlar ketma-ketligini yaratar ekan ohirgi sonni 
# qiymatini olmaydi yani bizning holatda 10 sonini olmaydi.

# RANGE() orqali biz qadamniham berishimiz mumkin. Quyida buni misollar bilan ko'rib chiqamiz.
# juft_sonlar = list(range(0,20,2)) # 0dan 20gacha 2 qadam bilan. (juft sonlar)
# toq_sonlar = list(range(1,20,2)) # 1dan 20gacha 2 qadam bilan. (toq sonlar)
# print(juft_sonlar) # 0dan 20 gacha bo'lgan juft sonlar ro'yxati aytkanimizdek 20 sonining o'zi bu ro'yxatga kirmaydi.
# print(toq_sonlar) # 0dan 20 gacha bo'lgan toq sonlar ro'yxati, agar shu yerda biz 20 o'rniga 21 kiritib toq sonlarni 
# so'raganimizda toq sonlar ro'yxatiga kira olmas edi yuqoridagi qoidaga muvofiq.

# Agar sonlar ketma ketligi 0dan boshlansa, range() funksiyasida ikkinchi argumentni ko'rsatish kifoya. 
# a = list(range(0,10))
# b = list(range(10))
# print(a)
# print(b)
# Yuqoridagi kodning natijasi bir hil bo'laveradi.

# SONLI RO'YXATLAR USTIDA SODDA AMALLAR.
# Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham amalga oshirishimiz mumkin. Masalan, ro'yxatdagi eng katta
# sonni topish max() funksiyasidan, eng kichigini topish uchun min() funksiyasidan va sonlarning yeg'indisini topish
# sum() funksiyasidan foydalanamiz.
# narxlar = [12000, 25000, 240000, 12300000, 5000, 97000] # Oddiy ro'yxat.
# print("NARXLAR ro'yxatidagi eng kichin son: ", min(narxlar), "\n") # Eng kichigini topish.
# print("NARXLAR ro'yxatidagi eng katta son: ", max(narxlar), "\n") # Eng kattasini topish.
# print("NARXLAR ro'yxatining sonlar yeg'indisi: ", sum(narxlar), "\n") # Umumiy yeg'indisini topish.

# Yuqoridagi kodni boshqacha ko'rinishda yozsak ham bo'ladi.
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)

# print("Eng arzon narx: ", arzon, \
#       "\nEng qimmat narx: ", qimmat, \
#           "\nJami narxlar yeg'indisi: ", jami)
# Shu o'rinda aytib o'tish kerakki kodingiz rasayam uzun bo'lib ketsa kodni (\) shu belgi orqali qatorni bir-necha
# qatorlarga bo'lishingixz mumkin.

# RO'YXATNI KESISH. 
# Bazida ro'yxatnimng ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin. 
# Deylik, biz quyidagi cars degan ro'yxatdan birinchi 3ta elementni ajratib olmoqchimiz, buning uchun boshlang'ich va
# ohirgi indekslarni beramiz: 
# cars = ['damas','niva', 'jiguli', 'matiz', 'tico', 'nexia'] # <- oddiy ro'yxat.
# my_cars = cars[0:3] # 0dan boshlab uchta elementni ajratib olamiz.
# print(my_cars) # Natija.
# Pythonda ro'yxatni kesishda 2-ko'rsatilgan indeksdan bitta avval to'xtaydi. Yuqoridagi misolda ham 0, 1, 2-elementlar
# ajratib olindi range() funksiyasi bolan bir hil ishlaydi.


# Yuqoridagi usul bilan ro'yxatni istalgan joyidan bo'lishimiz mumkin:
# print(cars[2:5]) # Natijada 2-indeksdan 5-ineksgacha bo'lgan elementlar kesib olinadi.

# Agar boshlang'ich indeksni bermasangiz, Python avtotmatik ravishda 0-indeksdan boshlab kesadi. Agar 2-indeksni
# kiritmasangiz, ro'yxatning ohirigacha kesadi:
# print(cars[:4]) # Ro'yxatning boshidan 4ta elementni ajratish.
# print(cars[3:]) # 3-elementdan ro'yxat ohirigacha kesish.

# RO'YXATDAN NUSXA OLISH.
# Dastur davomida biror ro'yxatdan nusxa olish talab qulinishi mumkin. Buning uchun tenglik (=) belgisidan foydalansak bo'ladm?
# Quyidagi misolga etibor bering:
# sonlar1 = [1, 2, 3, 4, 5] # Sonlar degan ro'yxat yaratamiz.
# sonlar2 = sonlar1 # Sonlar2 degan ro'yxatni sonlar1ga tenglaymiz.
# sonlar2.append(6) # Sonlar2 degan ro'yxatimizga 6 sinini qo'shamiz.
# sonlar2.append(7) # Sonlar2 degan ro'yxatimizga 7 sinini qo'shamiz.
# print("Bu sonlar1 ro'yxati: ", sonlar1)
# print("Bu sonlar2 ro'yxati: ", sonlar2)
# Bunda natija biz kutkandek chiqmaydi chunki sonlar2 = sonlar1 deb yozgan komandamiz yangi ro'yxat yaratish o'rniga 
# ikkala o'zgaruvchini ham xotirasidagi bitta ro'yxatga bog'lab (yo'naltirib) qo'ydi. Yani bitta ro'yxat ikkita
# nomga ega bo'lib qoldi. 

# Endi biz aslida qanday yo'l tutishimiz kerak edi shuni ko'rib chiqamiz.
# sonlar1 = [1, 2, 3, 4, 5] # Sonlar degan ro'yxat yaratamiz.
# sonlar2 = sonlar1[:] # Bu o'rinda endi haqiqatdan ham nusxa oldik.
# sonlar2.append(6) # Sonlar2 degan ro'yxatimizga 6 sinini qo'shamiz.
# sonlar2.append(7) # Sonlar2 degan ro'yxatimizga 7 sinini qo'shamiz.
# print("Bu sonlar1 ro'yxati: ", sonlar1)
# print("Bu sonlar2 ro'yxati: ", sonlar2)
# Nusxa olish shu ko'rinishda amalga oshiriladi.

# TUPLES - O'ZGARMAS RO'YXATLAR.
# Dastur davomida o'zgarmas ro;yxatlar tuzish talab qilinishi mumkin. Pythonda bunday ro'yxatlar TUPLES deb yuriladi.
# TUPLE ichidagi qiymatlar bir marta beriladi dasturning boshida, so'ngra o'zgartirib bo'lmaydi. TUPLE elon qilishda
# listdan farqli o'laroq [] kvadarat qavslardan emas balki oddiy qavslar () ishlatiladi.

# tomonlar = (20, 30, 55.2)
# print(tomonlar)
# TUPLE elementlariga xuddi ro'yxat elementlariga murojaat etilgani kabi indeks bilan murojaat qilinadi.

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# Keling TUPLE ichidagi biror elementni o'zgartirib ko'ramiz.
# toys[3] = 'dragon' # Bu holatda albatta xatolik beradi chunki aytkanimizday o'zgarmas ro'yxatga faqat dastur boshida 
# o'zgartirish kirita olamiz keyinchalik (qo'shish, o'zgartirish, olib tashlash) o'zgartira olmaymiz.

# Mobodo bizdan TUPLE ni o'zgartirish talab qilinsa u holda avval TUPLE ni LIST ga o'zgartirishimiz kerak bo'ladi.
# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard') # TUPLE yaratib oldik.
# toys = list(toys) # TUPLE ni oddiy LIST ga o'tkazamiz.
# Endi o'zgarishlar kiritishimiz mumkin.
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'myQueen'
# Ro'yxatni qaytadan o'zgarmas ro'yxatga o'tkazamiz.
# toys = tuple(toys) # Shu ko'rinishda.
# print(toys) # Ko'rib turganingizday hammasi joyida.

# AMALIY TOPSHIRIQLAR.
#1 - O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# countries = ["o'zbekiston", 'qatar', 'rossiya', 'ispaniya']
# print("Countries ro'yxati ichida ", countries, "shu davlatlar bor.\n")

#2 - Ro'yxatning uzunligini konsolga chiqaring.
# print("Countries ro'yxatida: ", len(countries), "ta element bor\n")

#3 - sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring.
# print("Countries ro'yxatidagi elementlarnig tartiblangan holati: ", sorted(countries), "shunday bo'ladi\n")

#4 - sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring.
# print("Countries ro'yxatidagi elementlarnig teskari tartiblangan holati: ", sorted(countries, reverse=True),\
# "shunday bo'ladi\n")
    
#5 - Asl ro'yxatni qaytadan konsolga chiqaring.
# print("Countries ro'yxatining asl ko'rinishi: ", countries,"shu ko'rinishda.\n")

#6 - reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring.
# countries.reverse()
# print("Asl ro'yxatning teskari ko'rinishi: ", countries, "shu ko'rinishda.\n")

#7 - sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

#8 - 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
# j_sonlar = list(range(120,1200,2))
# print("120dan 1200gacha bo'lgan juft sonlar: ", j_sonlar, "dan iborat.\n")

#9 - Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring.
# print("j_sonlar ro'yxatidagi sonlar yeg'indisi: ", sum(j_sonlar), "ga teng.\n")

#10 - Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring.
# print("j_sonlar ro'yxatidagi eng katta va eng kichik son o'rtasidagi ayirma: ", max(j_sonlar) - min(j_sonlar), "ga teng.\n")

#11 - Ro'yxatdagi elementlar sonini hisoblang.
# print("j_sonlar ro'yxatidagi elementlar soni: ", len(j_sonlar), "taga teng.\n")

#12 - Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring.
# print(j_sonlar[0:21],"\n")
# print(j_sonlar[260:281],"\n")
# print(j_sonlar[520:541],"\n")

#13 - taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting.
# foods = ['osh', 'somsa', 'kabob', 'shirguruch', 'shorva']

#14 - nonushta degan yangi ro'yxatga taomlardan nusxa oling.
# nonushta = foods[:]

#15 - Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing.
# nonushta.remove('osh')
# nonushta.remove('kabob')
# nonushta.remove('shorva')
# nonushta.append('non va qaymoq')
# nonushta.append('m_kasha')


#16 - Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(foods,"\n")
# print(nonushta,"\n")

#17 - Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat
# berib ko'ring.
# nonushta = tuple(nonushta)
# nonushta[0] = 'osh'

# 6 - DARS TUGADI.