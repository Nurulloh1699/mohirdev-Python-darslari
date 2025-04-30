# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:28:50 2025

@author: DavrServis
"""

# 19 - DARS.
# QIYMAT QAYTARUVCHI FUNKSIYA.
# Avvalgi darsimizda yaratgan barcha funksiyalarimiz natijalarni konsolga chiqarayotgan edi. Aslida, aksar holatlarda bu g'ayrioddiy.
# Sababi, dasturchi sifatida biz konsolga chiqqan ma'lumotdan unumli foydalana olmaymiz. Konsoldagi qiymatni o'zgaruvchiga yuklab,
# undan kelajakda foydalanib ham bo'lmaydi. Funksiyadan unumli foydalanish uchun undan biror qiymatni qaytarish maqsadga muvofiq 
# bo'ladi.


# FUNKSIYADAN YAGONA QIYMAT QAYTARISH.
# Avvalgi bo'limdagi toliq_ism funksiyamizga o'zgartirish kiritamiz. Bu safar funksiyamiz natijani konsolga chiqarmasdan, qiymat 
# sifatida qaytaradi. Buning uchun maxsus RETURN operatoridan foydalanamiz.
# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# Yuqoridagi funksiyamizga ahamiyat bersangizx, uning badanida endi print() funksiyasi yo'q. Buning o'rniga funksiyamiz RETURN
# operatori yordamida toliq_ism degan o'zgaruvchining QIYMATINI qaytaradi.

# ETIBOR BERING! Funksiya badani to RETURN operatoriga qadar bajariladi. RETURNdan so'ng yozilgan kodlar funksiya badanida bo'lsa 
# ham, bajarilmaydi.

# Endi funksiyadan foydalanish uchun u qaytargan qiymatni biror o'zgaruvchiga yuklashimiz kerak:
# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov")
# Yuqoridagi kodni bajarganimizda konsolga hech narsa chiqamaydi. talaba1 va talaba2 o'zgaruvchilarining qymatini ko'rish uchun
# esa print() funksiyasidan foydalanamiz.
# print(f"Darsga kelmagan talabalar: {talaba1.title()} va {talaba2.title()}")
# Natija: Darsga kelmagan talabalar Olim Hakimov va Hakim Olimov

# Demak, qiymat qaytaradigan funksiyaning afzalligi shundaki, biz bu qiymatlardan keyin ham bemalol foydalanishimiz mumkin.

# ETIBOR BERING! Funksiya ichidagi o'zgaruvchilar MAHALLIY yoki ICHKI o'zgaruvchilar deyiladi (local veriables). Ichki
# o'zgaruvchilar faqatgina funksiya ichida mavjud bo'ladi, ularga tashqaridan murojaat etib bo'lmaydi. Shuning uchun ham funksiya
# o'zgaruvchi emas qiymat qaytaradi.


# IXTIYORIY ARGUMENTLAR.
# Avvalgi darsimizda funksiyalarga standart parametr berishni ko'rib chiqqan edik. Xuddi shu usul bilan ba'zi argumentlarni
# ixtiyoriy qilishimiz mumkin. Ya'ni funksiya ishlashi uchun bu argumentlarni kiritish majburiy emas, ixtiyoriy bo'ladi.

# Keling, avvalgi funksiyamizni o'zgartiramiz va unga yana bitta otasining_ismi degan parametr qo'shamiz, lekin bu parametr 
# ixtiyoriy bo'ladi. Buning uchun funksiya yaratishda otasining_ismi = '' deb yozib ketamiz.
# def toliq_ism_yasa(ism, familiya, otasining_ismi = ''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi: # Otasining ismi mavjud bo'lsa
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# Yuqoridagi funksiyani tahlil qiladigan bo'lsak, 3 - qatorda biz otasining_ismi parametri bo'sh yoki yo'qligini tekshirdik.
# Pythonda if dan so'ng bo'sh bo'lmagan matn (string) yozsak, bu shart True qaytaradi. Demak, bu ixtiyoriy parametr kiritilgani
# yoki yo'qligiga qarab funksiyamiz turlicha qiymat qaytaradi.
# talaba1 = toliq_ism_yasa("olim", "abrorovich", "olimov")
# talaba2 = toliq_ism_yasa("abror", "olimov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# Natija: Darsga kelmagan talabalar: Olim Olimov Abrorovich va Abror Olimov

# FUNKSIYADAN LUG'AT QAYTARISH.
# Funksiyadan sodda qiymat emas, ro'yxat, lug'at va boshqa ma'lumot turlarini ham qaytarishimiz mumkin. Quyidagi funksiya mashina 
# haqidagi ma'lumotlarni jamlab, ularni lug'at ko'rinishida qaytaradi:
# def avto_info(make, model, color, transmission, year, price = None): # Mashina ma'lumotlarini o'zida jamlaydgan va uni lug'at
# ko'rinishidi qaytaradigan funksiya.
    # avto = { # Yuqorida yozilgan parametrlarni lug'at ko'rinishiga olib kelamiz.
    #     "kompaniya" : make,
    #     "model" : model,
    #     "rang" : color,
    #     "korobka" : transmission,
    #     "yil" : year,
    #     "narx" : price
    #     }
    # return avto # va return yordamida avto degan lug'atni qaytaramiz.

# ETIBOR BERING! narxi nomli parametrga None standart qiymatini berib ketdik. None Pythonda MAVJUD EMAS ma'nosini beradi va if
# yordamida tekshirganda False mantiqiy qiymatini qaytardi.
# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018) # avto1 degan o'zgaruvchiga avto haqidagi ma'lumotlarni yuklaymiz.
# avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2016, 15000) # avto2 degan o'zgaruvchiga avto haqidagi ma'lumotlarni yuklaymiz.
# avtolar = [avto1, avto2] # Yuqorida hosil bo'lgan ikkita lug'atimizni avtolar degan lug'atga saqlaymiz.
# print("Onlayn bozordagi mavjud avtomashinalar: ") # Shu habarni konsolga chiqaramiz.
# for avto in avtolar: # avtolar ichidagi har bir avto uchun.
#     if avto["narx"]: # Agar avtodagi narx degan parametrda bitta bo'lsa ham element bo'lsa.
#         narx = avto["narx"] # Uni narx degan o'zgaruvchiga yuklagin.
#     else: # Aks holda.
#         narx = "Noma'lum" # # narx degan o'zgaruvchiga shu habarni yuklagin.
#     print(f"{avto['rang']} {avto['model']}. Narxi: {narx}") # Konsolga shu habarni chiqar.
# Dastur natijasini tahlil qilishni sizga vazifa sifatida qoldiramiz:
# Natija: Onlayn bozordagi mavjud avtomashinalar: 
#           Qora Malibu. Narxi: Noma'lum
#           Oq Gentra. Narxi: 15000

# FUNKSIYADAN RO'YXAT QAYTARAMIZ.
# Biz avvalroq range() funksiyasi bilan tanishgan edik. Bu funksiya 2ta son qabulqilib, shu ikki son oralig'idagi sonlarni
# qaytaradi. Keling biz oraliq() degan yangi funksiya yaratamiz. range() dan farqli ravishda, funksiyamiz 2 son oralig'idagi 
# sonlarni RO'YXAT ko'rinishida qaytarsin.
# def oraliq(min,max):
#     sonlar = [] # Bo'sh ro'yxat.
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# Funksiyamizni tekshiramiz:
# print(oraliq(0,10))
# print(oraliq(10,20))

# Yuqoridagi funksiyaga uchinchi, qadam deb nomlangan ixtiyoriy parametrini qo'sha olasizmi?
# def oraliq(min,max, qadam): # Bu yerda uchunchi, qadam degan parametr qo'shamiz.
#     sonlar = [] # Bo'sh ro'yxat.
#     while min < max:
#         sonlar.append(min)
#         min += qadam # Bu qatorni += qadamga o'zgartiramiz.
#     return sonlar
# print(oraliq(0,20,2))

# FUNKSIYALARNI SIKLDA ISHLATISH.
# Funksiyalarni takrorlash uchun sikldan foydalanishimiz mumkin. Quyidagi misolda biz WHILE yordamida avvalroq yaratgan avto_info
# funksiyamizni bir necha bor chaqiramiz va salondagi avtomashinalar ro'yxatini shakllantiramiz. Bunda ro'yxatning har bir elementi
# av_info funksiyasidan qaytgan lug'at vo'ladi.
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = [] # Salondagi avtolar uchun bo'sh ro'yxat.
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rang = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narx = input("Narxi: ")
    
# Kiritilgan ma'lumotlardan avto_info yordamida lug'at shakllantirib, ro'yxatga qo'shamiz:
    # avtolar.append(avto_info(kompaniya, model, rang, korobka, yili, narx))
    
# Yana avto qo'shish qo'shmasligini so'raymiz.
#     javob = input("Yana avto qo'shasizmi? (h/y): ")
#     if javob == "y":
#        break
# print("Salonimizda quyidagi mashinalar bor:")
# for avto in avtolar:
#     print(f"{avto['rang'].title()} {avto['model'].title()}, korobkasi {avto['korobka']} va narxi {avto['narx']}$")
# Natija: Salonimizda quyidagi mashinalar bor:
#         Oq Gentra, korobkasi mexanika va narxi 15000$
#         Qora Kamry, korobkasi avtomat va narxi 34000$
#         Sabzirang Vesta, korobkasi avtomat va narxi 25000$  

# AMALIYOT TOPSHIRIQLARI.
#1 - Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib,
# lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni
# ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None): # Funksiya yaratdik va unga parametrlar berdik.
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya""" # Funksiya haqida ma'lumot.
#     mijoz = { # Funksiyamizni ro'yxat shakliga keltirib oldik.
#         "ism": ism,
#         "familiya": familiya,
#         "tyil": tyil,
#         "yoshi": 2024 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#     }
#     return mijoz # return orqali funksiyamizni qaytaryapmiz.


#2 - Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring.
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
# print("Mijoz haqida ma'lumotlarni kiriting.") # Yuqoridagi kodni sikl shakliga keltirib olamiz (while) orqali.
# mijozlar = [] # Bo'sh ro'yxat yaratib olamiz.
# while True: # Sikl boshladik (True) qiymat berdik.
#     ism = input("Ismi: ") # Quyida har bir parametrni birma key-value ga aylantirib olamiz.
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon)) # Yuqorida lug'at ko'rinishiga kelib qolgan
# malumotlarni mijozlar degan bo'sh ro'yxatimizga qo'shib olamiz.
#     
#     javob = input("Davom etasizmi? (ha/yo'q)") # Foydalanuvchidan yan ma'lumot qo'shishi (yangi sikl boshlashi) haqida so'raymiz.
#     if javob != "ha": # Agar javob ha bo'lmasa.
#         break # Sikl uziladi quyiroqdagi kodlar bajariladi.

# print("Mijozlar:") # Birinchi shu qatorni konsolga chiqarib olamiz.
# for mijoz in mijozlar: # Mijozlar ichidagi har bir mijoz uchun.
#     print( # Quyidagi habarni konsolga chiqar.
#         f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#         f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
#     )
# Natija: Mijoz haqida ma'lumotlarni kiriting.
          # Ismi: nurulloh
          # Familiyasi: abdurashidov
          # Tug'ilgan yili: 1999
          # Tug'ilgan joyi: oltiariq
          # Email: nurik9.99@bk.ru
          # Telefon raqami: 902731699
          # Davom etasizmi? (ha/yo'q)y
          # Mijozlar:
          # Nurulloh Abdurashidov,25 yoshda, telefoni: 902731699
            
#3 - Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing.
# def eng_katta_son(x, y, z): # Funksiyamizga 3ta parametr qo'shib olamiz.
#     """Sonlar ichidagi eng kattasini qaytaruvchi dastur."""
#     max = x # max (eng katta qiymat) = x ga.
#     if y >= max: # Agar y katta yoki teng bo'lsa max ga.
#         max = y # max (eng katta qiymat) = y ga.  
#     if z >= max: # Agar z katta yoki teng bo'lsa max ga.
#         max = z # max (eng katta qiymat) = z ga.
#     return max # return orqali max ni qaytaramiz.
# print(eng_katta_son(10, 24, 12)) # Konsolga eng katta qiymatni chiqaramiz.2
# Natija: 24

#4 - Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida
# qaytaruvchi funksiya yozing.
# def aylana(radius,pi = 3.14159): # Funksiyamizga parametrlar qo'shib olyapmiz (pi ga CONSTANT qiymat berdik).
    
#      aylana = { # Aylana deb nomlangan lug'at yaratib oldik.
#          "radius" : radius,  
#          "diametr" : 2 * radius,
#          "perimetr" : 2 * radius * pi,
#          "yuza" : pi * radius ** 2
#          }
#      return aylana
# print(aylana(35)) # Agar aylana radiusini 35 qilib kiritganimizda.
# Natija: {'radius': 35, 'diametr': 70, 'perimetr': 219.91129999999998, 'yuza': 3848.44775}

#5 - Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz
# bo'linuvchi, 1 dan katta musbat sonlar).
# def tub_sonlar_top(min, max): # Funksiyamizga parametrlar qo'shib olyapmiz.
#     tub_sonlar = [] # Bo'sh ro'yxat.
#     for n in range(min, max + 1): # n range() orqali yaratilgan sonlar ketma-ketligidagi har bir son uchun.
#         tub = True # tub degan o'zgaruvchiga True qiymat berdik. 
#         if n == 1: # Agar n, 1ga teng bo'lsa. 
#             tub = False # Yuqoridagi tub degan o'zgaruvchi qiymati False ga teng bo'lsin.
#         elif n == 2: # Yoki n, 2ga teng bo'lsa (Eng birinchi tub son 2).
#             tub = True # Tub degan o'zgaruvchi qiymati True qiymatda bo'lsin.
#         else: # Aks holda.
#             for x in range(2, n): x range() orqali 2dan boshlab n gacha bo'lgan har bir son uchun. 
#                 if n % x == 0: # n bo'linganda x ga qoldiq 0 bo'lsa.
#                     tub = False # Tub degan o'zgaruvchi qiymati yana False bo'lsin.
#         if tub:# Agar tub bo'lsa (yani yuqoridagi shart bajarilmasa).
#             tub_sonlar.append(n) # tub_sonlar degan yuqoridagi bo'sh ro'yxatimizga qo'shgin.

#     return tub_sonlar 
# print(tub_sonlar_top(10, 50)) # 10 bilan 50 sonlari oralig'idagi tub sonlarni qidiramiz.
# Natija: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

#6 - Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi
# funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik
# Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  
# def fibonacci(n): # Funksiyamizga parametr berib olamiz.
#     sonlar = [] # Bo'sh ro'yxat.
#     for x in range(n): # x ni foydalanuvchi kiritadigan n sonigacha bo'lgan sonlarning har biriga tenglaymiz.
#         if x == 0 or x == 1: # agar x teng bo'lsa 0 ga yoki x teng bo'lsa 1ga.
#             sonlar.append(1) # 
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar


# print(fibonacci(10))

# 19 - DARS TUGADI.