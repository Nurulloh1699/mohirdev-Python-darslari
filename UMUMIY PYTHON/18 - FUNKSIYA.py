# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:27:10 2025

@author: DavrServis
"""

# 18 - DARS.
# FUNKSIYA.
# Funksi deb ma'lum vazifani bajarishga mo'ljallangan kodlar yeg'indisidir. Funksiyalar, odatda, ma'lumotlarni qabul qilib oladi,
# ularni qayta ishlaydi va biror natija qaytaradi.

# Biz darslarimiz davomida bi nechta funksiyalardan foydalanib keldik. Misol uchun, print() funksiyasi matn yoki ifoda qabul qiladi
# va uni konsolga chiqaradi, range() funksiyasi esa ma'lum oraliqdagi sonlarni yaratish uchun ishlatiladi.

# Aslida, har qanday funksiyaning ortida ham bir nechta qatordan iborat kod bo'ladi, lekin biz funksiyaga murojaat qilganimizda 
# uning nomini yozamiz, holos. Funksiya ortidagi kod esa biz uchun yashirin bo'lib qolaveradi. Funksiyalarning qilayligi ham shunda.
# Dastur davomida ma'lum bir kodlarni qayta qayta yozmaslik uchun biz ularni jamlab, bitta funksiya ichiga joylashimiz va dastur
# davomida bu kodlarga funksiya nomi orqali murojaat etishimiz mumkin.

# Funksiyalar turlicha bo'ladi, ba'zi funksiyalar sizdan qiymat qabul qilib, konsolga biror ma'lumot chiqaradi, ba'zilari esa
# sizdanqabul qilgan qiymat ustida turli amallar bajarib yangi qiymat qaytaradi. Foydalanuvchidan mutlaqo qiymat qabul qilmaydigan
# funksiyalar ham mavjud.

# Ushbu bobda biz Pythonda yangi funksiya yaratish, unga murojaat etish, tekshirish va to'g'irlashni o'rganamiz. Shuningdek,
# darsimiz yakunida dasturimizni bir nechta fayllarga ajratishni va funksiyalarni alohida modullarga joylashni ham o'rganamiz.


# FUNKSIYA YARATAMIZ.
# Boshlanishiga oddiy, hech qanday qiymat qabul qilmaydigan funksiya yaratishni ko'rib chiqaylik. Bu funksiyaga murojaat
# etkanimizda konsolga "Assalomu Aleykum" degan habarni chiqarsin.
# def salom_ber():
#     """Salomlashuvchi funksiya"""
#     print("Assalomu Aleykum!")
    
# Yuqoridagi kodni tahlil qilamiz:
#   1. Avvalo, DEF operatori yordamida Pythonda funksiya yaratayotganimizni bildirdik. DEF dan so'ng esa funksiyamizga nom nom
# berdik va qavslarni ochib yopdik. Bizning funksiyamiz foydalanuvchidan hech qanday qiymat qabul qilmaydi, shuning uchun ham qavs
# ichi bo'sh. Keyingi misollarda foydalanuvchidan qiymat qabul qiluvchi funksiyalarni ham ko'ramiz.
#   2. DEF qatoridan keyin o'ngga surib yozilgan har qanday funksiyaning badani hisoblanadi. 2 - qatorda biz uchta ketma-ket
# qo'shtirnoq ichida funksiya haqida bilmoqchi bo'lganda aynan shu matnni ko'rsatadi.
#   3. Oxirgi qatorimizda esa "Assalomu Aleykum!" matnini konsolga chiqarishni buyurdik. Sodda funksiyamizning asosiy vazifasi ham
# shu.

# Mana funksiya tayyor. Endi bu funksiyadan foydalanish uchun uni CHAQIRAMIZ. Buning uchun funksiya nomini yozamiz va qavslarni
# ochib-yopamiz. Funksiyamiz hech qanday qiymat qabul qilmaydi, shuning uchun qavslar ichini bo'sh qoldiramiz.

# salom_ber()
# Natija: Assalomu Aleykum!

# ETIBOR BERING! Funksiyaga nom berishta fe'l, ya'ni harakatni bildiruvchi so'zlar yoki jumlalardan foydalaning. Bu bilan siz
# o'zgaruvchi va funksiya va funksiya o'rtasini farqlashingiz oson bo'ladi. Misol uchun, yuqorida biz funksiyamizni salom emas,
# salom_ber deb nomladik.


# QIYMAT QABUL QILUVCHI FUNKSIYA.
# Avvalgi sodda funksiyamiz foydalanuvchidan hech qanday qiymat olmaydi va barchaga birday "Assalomu Aleykum!" deb javob qiladi.
# Keyingi funksiyaga o'zgartirish kiritamiz, funksiya foydalanuvchi ismini qabul qilib, unga ismi bilan bilan murojaat etsin. 
# Buning uchun funksiya nomidan keyin qavs ichida foydalanuvchi berishi kerak bo'lgan qiymatni ko'rsatamiz.
# def salom_ber(ism):
#     """Foydalanuvchiga ismi orqali salom beruvchi funksiya."""
#     print(f"Assalomu Aleykum, hurmatli {ism.title()}!")
# Bunday funksiyaga murojaat etish uchun qavs ichida so'ralgan qiymatni berish talab qilinadi:
# salom_ber("nurulloh")
# Natija: Assalomu Aleykum, hurmatli Nurulloh!

# Agar funksiyaga murojaat etishda unga qiymat bermasak, xatolik vujudga keladi:
# salom_ber()
# Natija: TypeError: salom_ber() missing 1 required positional argument: 'ism'.

# Funksiya yaratishning asl maqsadlaridan biri - biz unga qayta-qayta, yangi qiymatlar bilan murojaat etishimiz mumkin.
# salom_ber("hasan")
# Natija: Assalomu Aleykum, hurmatli Hasan!
# salom_ber("olim")
# Natija: Assalomu Aleykum, hurmatli Olim!


# DOCSTRING.
# Funksiyani yaratishda funksiya qanday ishlashi haqida qisqacha ma'lumot berib ketish o'zimiz uchun ham, kelajakda bizning
# funksiyamizni ishlatadigan boshqa dasturchilar uchun ham juda foydali bo'ladi. Bunday ma'lumotlar DOCSTRING deb ataladi va
# funksiya badaninnig ilk qatorida uchta qo'shtirnoq ichida yoziladi:
# def salom_ber(ism):
#     """Foydalanuvchiga ismi orqali salom beruvchi funksiya.""" # <- DOCSTRING.
#     print(f"Assalomu Aleykum, hurmatli {ism.title()}!")    
 
# Murakkab funksiyalar DOCSTRINGni bir nechta qatorga bo'lib yozish mumkin:
# def salom_ber(ism):
#     """Foydalanuvchini ismini qabul qilib,
#         unga salom beruvchi funksiya.""" # <- DOCSTRING.
#     print(f"Assalomu Aleykum, hurmatli {ism.title()}!")  

# DOCSTRINGni konsolga chiqarish uchun quyidagi buyruqni yozamiz: (funksiya_nomi.__doc__).
# print(salom_ber.__doc__)
# Natija: Foydalanuvchini ismini qabul qilib, unga salom beruvchi funksiya.

# Odatda, dasturlash muhitlari funksiya nomini yozishingiz bilan DOCSTRING ichidagi matnni ko'rsatadi:
# salom_ber() shu ko'rinishda funksiya nomi yozilishi bilan, ekranda mini oyna paydo bo'ladi va unda funksiya haqidagi
# ma'lumotlarni ko'rish mumkin.


# ARGUMENT VA PARAMETR.
# Funksiya yaratishda qavs ichida berilgan, funksiya to'g'ri ishlashi uchun uzatiladigan qiymat PARAMETR deb ataladi.
# Sodda bir misol keltiramiz:
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,
#         unga salom beruvchi funkiya"""
#     print(f"Assalomu Aleykum, hurmatli {ism.title()}!")

# Yuqoridagi misolda ism - salom ber funksiyasining parametri. Parametrlarga mazmunli nom berishni odat qiling:
#   ❎ salom_ber(n)
#   ✅ salom_ber(name)
#   ✅ salom_ber(ism)
# Foydalanuvchi funksiyaga murojaat etishda funksiyaga uzatgan qiymat ARGUMENT deb ataladi. salom_ber('hasan') kodida
# 'hasan' - ARGUMENT.

# Demak parametr va argument bitta narsaga ikki xil qarash ekan, xolos.

# ETIBOR BERING! Ba'zi manbalarda ARGUMENT va PARAMETR so'zlari almashtirib ishlatilishi ham kuzatiladi.


# FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH.
# Ba'zi funksiyalar bir emas, bir nechta parametr talab qilinishi mumkin, foydalanuvchi esa, o'z navbatida, bir nechta argumentlar
# taqdim qilishi kerak. Funksiyaga argument uzatishning bir necha usuli bor, keling ular bilan birma-bir tanishamiz.

# TO'G'RI TARTIBDA UZATISH.
# Bu usulda funksiya parametrlari qaysi tartibda yozilgan bo'lsa, argumentlar ham aynan shu ketma- ketlikda uzatilishi shart. Bitta
# misol keltiramiz. Quyidagi funksiyha foydalanuvchining ismi va familyasini parametr sifatida qabul qilib, ularni jamlab habar chiqaradi.
# def toliq_ism(ism, familya):
#     """Ism va familyani jamlab chiqaruvchi funksiya."""
#     print(f"Foydalanuvchining ismi: {ism.title()}\n"
#           f"Foydalanuvchining familyasi: {familya.title()}")
# Yuqoridagi funksiya to'g'ri natija chiqarishi uchun argumentlarni ism va familya ketma-ketligida kiritishimiz lozim.
# toliq_ism("nurulloh", "abdurashidov")
# Natija: Foydalanuvchining ismi: Nurulloh
#         Foydalanuvchining familyasi: Abdurashidov

# Agar argumentlarni noto'g'ri  ketma-ketlikda bersak natija ham biz kutkanday chiqmaydi:
# toliq_ism("abdurashidov", "nurulloh")
# Natija: Foydalanuvchining ismi: Abdurashidov
#         Foydalanuvchining familyasi: Nurulloh

# Ko'p holatlarda esa argumentlarni noto'g'ri tartibda uzatish xatolikka ham olib kelishi mumkin.
# def yosh_hisobla(ism, tugilgan_yil):
    # """Foydalanuvchini yoshini hisoblovchi funksiya."""
    # print(f"{ism.title()} {2024 - tugilgan_yil} yoshda")
# Funksiyani chaqiramiz:
# yosh_hisobla("olim", 1999)
# Natija: Olim 25 yoshda

# Endi argumentlarni o'rnini almashtirib yozib ko'ramiz:
# yosh_hisobla(1999, "olim")
# Natija: AttributeError: 'int' object has no attribute 'title'

# PARAMETR NOMI BILAN UZATISH.
# Yuqoridagi kabi hplatlarning oldini olish uchun argumentlarni parametr nomi bilan qo'shib uzatishimiz mumkin. Buning uchun 
# funksiyaga o'zgartirish kiritish talab qilinmaydi.
# def yosh_hisobla(tugilgan_yil = 1999, ism = 'olim'):
#     """Foydalanuvchini yoshini hisoblovchi dastur."""
#     print(f"{ism.title()} {2024 - tugilgan_yil} yoshda!")
    
# yosh_hisobla()
# Natija: Olim 25 yoshda!

# Yuqoridagi misolda funksiyani chaqirishda biz parametrlar ketme-ketligiga rioya qimlmagan bo'lsak-da, argumentlarni
# parametr = qiymat ko'rinishida yozganimiz sababli funksiya to'g'ri ishladi.

# Xuddi shu kabi yuqoridagi toliq_ism funksiyasiga ham murojaat etishimiz mumkin:
# def toliq_ism(ism = 'nurulloh', familya = 'abdurashidov'):
#     """Ism va familyani jamlab chiqaruvchi funksiya."""
#     print(f"Foydalanuvchining ismi: {ism.title()}\n"
#           f"Foydalanuvchining familyasi: {familya.title()}")
    
# toliq_ism()
# Natija: Foydalanuvchining ismi: Nurulloh
#         Foydalanuvchining familyasi: Abdurashidov

# ETIBOR BERING! Bu usuldan foydalanganda parametr nomi to'g'ri yozilishiga e'tibor bering!


# STANDART QIYMAT. 
# Funksiya yaratishda istalgan paramtr uchun standart qiymat ko'rsatib ketishimiz mumkin. Agar foydalanuvchi shu parametr uchun
# qiymat (argument) kiritmasa, funksiya bajarilishi jarayonida standart qiymat ishlatiladi. Standart qiymat funksiya yaratish 
# vaqtida parametr = qiymat ko'rinishida beriladi.

# Quyidagi misolda yosh_hisobla funksiyasida joriy_yil parametriga stardart qiymat beramiz:
# def yosh_hisobla(tugilgan_yil, joriy_yil = 2024):
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz!")

# yosh_hisobla(1999, 2024)
# Natija: Siz 25 yoshdasiz!    

# Endi esa faqat bitta argument (tugilgan_yil) bilan chaqiramiz:
# yosh_hisobla(1999)
# Natija: Siz 25 yoshdasiz!

# Bu safar  foydalanuvchi joriy_yil nikiritmagani sababli standart qiymat - 2024 ishlatildi.


# FUNKSIYAGA MUROJAAT ETISHDA XATOLIKLAR.
# Funksiyalarga murojaat etishda turli xatoliklarga yo'l qo'yishimiz tabiiy. Bunday holatlarda Python qaytargan xatoni sinchiklab 
# o'qib, xato qayerdaligini topishimiz va uni to'g'irlashimiz zarur. Quyida men turli funksiyalar yaratib, ularga xato usullar
#  bilan murojaat etaman. Xatolar nimada ekanini topa olasizmi?

#1 - misol.
# def yosh_hisobla(tugilgan_yil, joriy_yil = 2024):
#     """Tug'ilgan yildan yoshini hisoblaymiz"""
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz")
    
# tyil = input("Tug'ilgan yilingizni kiriting: ") # Shu qatorda tyil integerga olinmagani uchun xato yuz beradi.
# yosh_hisobla(tyil)
# Natija: TypeError: unsupported operand type(s) for -: 'int' and 'str'
  
#2 - misol.
# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz!")
# yosh_hisobla(1993) # Bu qatorda ikkinchi argument berilmayotkani uchun dastur xato qaytaradi.

# Natija: TypeError: yosh_hisobla() missing 1 required positional argument: 'joriy_yil'

#3 - misol.
# def salom_ber(): # Bu qatirda argument kiritilmagan.
#     """Salom beruvchi funksiya"""
#     print(f"Assalomu Aleykum! hurmatli {ism.title()}") # Bu qatorda ham foydalanuvchiga murojaatni mukammallashtirish mumkin.
    
# salom_ber("hasan")
# Natija: TypeError: salom_ber() takes 0 positional arguments but 1 was given.

#4 - misol.
# def toliq_ism(ism, familya):
#     print(f"Foydalanuvchi simi: {ism.title()}/n"
#           f"Foydalanuvchi familyasi: {familya.title()}")
# toliq_ism("olim hakimov") # Bu yerda bitta argument qolib ketdi.
# Natija: TypeError: toliq_ism() missing 1 required positional argument: 'familya'

# AMALIYOT TOPSHIRIQLARI.
#1 - Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def yil_hisobla(ism, yosh):
#     """Foydalanuvchidan ism va yoshini so'rab,
#         uning tug'ilgan yilini hisoblaydigan funksiya"""
#     print(f"{ism.title()}, siz {2024 - yosh} - yilda tug'ilgansiz!")
    
# yil_hisobla("nurulloh", 25)

#2 - Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kv_kub_hisobla(son):
#     """Foydalanuvchidan son qabul qilib,
#     uni kvadrati va kubini hisoblovchi funksiya."""
#     print(f"Siz kiritgan sonning kvadrati {son**2} ga, kubi esa {son**3} ga teng!")
    
# kv_kub_hisobla(25)

#3 - Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def son_top(son):
#     """Foydalanuvchidan son qabul qilib olib,
#     uni toq yoki juft ekanini hisoblovchi funksiya"""
#     if son%2 == 0:
#         print(f"Siz kiritgan {son} soni juft son!")
#     else:
#         print(f"Siz kiritgan {son} soni toq son!")
# son_top(26)

#4 - Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa
# "Sonlar teng" degan xabarni chiqaring.
# def son_taqqosla(son1, son2):
#     """Foydalanuvchidan ikki son qabul qilib,
#     ularni taqqoslaydigan funksiya."""
#     if son1 == son2:
#         print(f"{son1} va {son2} sonlari o'zaro teng!")
#     elif son1 > son2:
#         print(f"{son1}, {son2} dan katta!")
#     elif son1 < son2:
#         print(f"{son1}, {son2} dan kichik!")
#     else:
#         print(f"{son1} va {son2} sonlari o'zaro teng emas!")
        
# son_taqqosla(12, 1)

#5 - Foydalanuvchidan x va y sonlarini olib, x kvadratida y ni konsolga chiqaruvchi funksiya yozing.
# def kv_hisobla(x, y):
#     """Foydalanuvchidan x va y sonlarini olib,
#     x kvadratida y ni topadigan funksiya."""
#     print(f"x ning y darajasi {x**y} ga teng!")
# kv_hisobla(12, 2)
# kv_hisobla(96, 3)

#6 - Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def kv_hisobla(x, y = 2):
#     """Foydalanuvchidan x va y sonlarini olib,
#     x kvadratida y ni topadigan funksiya."""
#     print(f"x ning kvadrati {x**y} ga teng!")
# kv_hisobla(12)

#7 - Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
# Natijalarni konsolga chiqaring.
# def qoldiqsiz_bol(son):
#     """Foydalanuvchidan son qabul qilib,
#     sonni 2 dan 10 gacha bo'lgan sonlar ichida qaysilariga qoldiqsiz bo'linishini tekshiruvchi funksiya."""
#     for n in range(2, 11):
#         if not son%n:
#             print(f"{son}, {n} ga qoldiqsiz bo'linadi!")
            
# qoldiqsiz_bol(100)

# 18 - DARS TUGADI.