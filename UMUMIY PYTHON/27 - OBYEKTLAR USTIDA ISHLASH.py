# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:45:31 2025

@author: DavrServis
"""

# 27 - DARS.
# OBYEKTLAR USTIDA ISHLASH.

# XUSUSIYATLARGA STANDART QIYMAT BERISH.
# Avvalgi bo'limda biz klass yaratish, unga xususiyatlar ca metodlar qo'shishni ko'rib chiqdik. Klassdan obyekt yaratganimizda esa uning
# xususiyatlarini parametr sifatida uzatishni o'rgandik.

# Pythonda obyektning ba'zi xususiyatlarini parametr yordamida uzatmasdan, klass yaratishda unga standart qiymat berib ketishimiz mumkin.
# Keling, Talaba klassimizga qaytamiz. Bu klassimiz 3ta xususiyatga ega edi: ism, familiya, tyil. Biz yana bitta qo'shimcha bosqich nomli
# xususiyat qo'shamiz, va unga standart qiymat sifatida 1 beramiz, e'tibor qiling, bu xususiyat obyekt yaratilishida parametr sifatida
# uzatilmaydi:
# class Talaba:
#     """Talab nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
# Endi Talaba klassidan yangi obyekt yaratganimizda har bir yangi talabaning kursi 1ga teng bo'ladi.

# talaba1 = Talaba ("Nurulloh", "Abdurashidov", 1999)
# print(talaba1.get_info())
# Natija: Nurulloh Abdurashidov. 1-bosqich talabasi.

# STANDART QIYMATNI O'ZGARTIRISH.
# Obyektning standart qiymatiga ham boshqa xususiyatlar kabi nuqta orqali murojaat etishimiz va uningqiymatini almashtirishimniz mumkin:
# talaba1.bosqich = 2
# print(talaba1.bosqich)
# Natija: 2

# Yana boshqa usuli - obyekt xususiyatini yangilovchi metod yozish.
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
    
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
# Metodga murojaat etamiz:
# talaba1 = Talaba("Nurulloh", "Abdurashidov", 1999)
# talaba1.set_bosqich(3)
# print(talaba1.get_info())
# Natija: Nurulloh Abdurashidov. 3-bosqich talabasi.

# Umuman olganda, xususiyatlarni yangilashda turli usullardan foydalanish mumkin. Misol uchun,talabaning bosqichi, odatda, 1 tadan
# ko'payib boradi, shuning uchun quyidagicha metod ham yozishimiz mumkin:
# class Talaba:
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.tyil}-yilda tug'ilgan, {2024 - self.tyil} yoshda. {self.bosqich}-bosqich talabasi."
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod."""
#         self.bosqich = bosqich
#     def update_bosqich(self):
#         """Talabaning bosqichini bittaga ko'tarish."""
#         self.bosqich += 1
# update_bosqich() metodiga murojaat etganimizda talabaning bosqichi oshib boradi:
# talaba1 = Talaba("Olim", "Olimov", 1995)
# talaba2 = Talaba("Husan", "Akbarov", 2004)
# talaba3 = Talaba("Hasan", "Akbarov", 2004)
# print(talaba1.get_info())
# Natija: Olim Olimov. 1995-yilda tug'ilgan, 29 yoshda. 1-bosqich talabasi.

# talaba1.update_bosqich()
# print(talaba1.get_info())
# Natija: Olim Olimov. 1995-yilda tug'ilgan, 29 yoshda. 2-bosqich talabasi. 

# talaba1.update_bosqich()
# print(talaba1.get_info())
# Natija: Olim Olimov. 1995-yilda tug'ilgan, 29 yoshda. 3-bosqich talabasi.


# OBYEKTLAR O'RTASIDAGI MUSOSABAT.
# Obyektga yo'nlatirilgan dasturlashning afzalligi turli obyektlar o'rtasida o'zaro munosabatlarni oson yo'lga qo'yish mumkinligidadir.
# Kleing,yangi Fan degan klass yaratamiz va fanimizga talabalar qo'shish uchun add_student() metodini yozamiz:
# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
        
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
        
# ETIBOR BERING! Fan klassi faqatgina yagona nomi degan parametrga ega. Qolgan xususiyatlariga esa standart qiymat berilgan:
# talabalar_soni = 0, talabalar ro'yxati bo'sh.

# Fanimizga talaba qo'shish uchun add_student() metodini chaqiramiz. Bu metod parametr sifatida Talaba klassiga oid obyektni qabul qiladi
# va unitalabalar ro'yxatiga qo'shadi. Shuningdek, bu metod yangi talaba qo'shilganda talabalar_soni ni bittaga oshirib qo'yadi.

# Keling, boshlanishiga yangi fan obyektini va bir nechta talabalarni yaratamiz:
# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Olim", "Olimov", 1995)
# talaba2 = Talaba("Husan", "Akbarov", 2004)
# talaba3 = Talaba("Hasan", "Akbarov", 2004)

# # Talabalarni yangi fanimizga qo'shamiz:
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# Mana fanimiz tayyor, talabalar qo'shildi. Keling, endi fan haqida ma'lumotlarni olamiz:
# print(matematika.talabalar_soni)
# Natija: 3

# Fanimizga 3ta talaba qo'shilibti. Talabalar haqida ma'lumot olsak bo'ladimi?
# print(matematika.talabalar)
# Natija: [<__main__.Talaba object at 0x0000025598EDB3E0>,
          # <__main__.Talaba object at 0x0000025598B47BF0>,
          # <__main__.Talaba object at 0x0000025598D76060>]     
    
# Talabalarning ism-familiyasi o'rniga qandaydir tushunarsiz ma'lumorlar. Aslida, hammasi to'g'ri, yuqorida fanimizga yangi talabalarni
# obyekt sifatida qo'shgan edik, yuqoridagi natija esa matemarika.talabalar ro'yxatida Talaba klassiga oid 3ta obyekt borligini
# ko'rsatmoqda.

# Fanimizga yozilgan talabalar haqida tushunarli ma'lumot olish uchun Fan klassiga yangi get_students() metodini qo'shamiz. Bu metod
# talabalar ichidagi har bir talaba obyektiga murojaat etib, get_info() metodi yordamida talabaning ma'lumotlarini oladi, ro'yxatga
# qo'shadi va shu ro'yxatni qaytaradi:
# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
        
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
    
# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Olim", "Olimov", 1995)
# talaba2 = Talaba("Husan", "Akbarov", 2004)
# talaba3 = Talaba("Hasan", "Akbarov", 2004)

# Talabalarni yangi fanimizga qo'shamiz:
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
# Shu o'rinda Pythonda ro'yxatlar bilan ishlashning qulayliklaridan birini ham ko'rsatib o'tsak. get_students() metodiga e'tibor
# bersangiz, biz yangi ro'yxat shakllantirishda 1 qator koddan foydalandik:
# [talaba.get_info() for talaba in self.talabalar]

# Kodimizni tahlil qilsak, self.talabalar ichidagi har bir talaba uchun get_info() metodini bajar degan ma'no kelib chiqadi. Kodni 
# kvadrat qavslar ichiga olganimiz uchun har bir sikl natijasi avtomatik ravishda ro'yxatga qo'shib boriladi.

# Mana, endi metodga murojaat etib, talabalar haqida ma'lumot olishimiz mumkin:
# mat_talabalar = matematika.get_students()
# print(mat_talabalar)
# Natija: ["Olim Olimov. 1995-yilda tug'ilgan, 29 yoshda. 1-bosqich talabasi.",
          # "Husan Akbarov. 2004-yilda tug'ilgan, 20 yoshda. 1-bosqich talabasi.",
          # "Hasan Akbarov. 2004-yilda tug'ilgan, 20 yoshda. 1-bosqich talabasi."]

# Shunday qilib, ikki bir-biriga bog'liq bo'lmagan obyektlar ustida turli munosabatlar o'rnatishimiz mumkin


# NUQTA YOKI METOD ?
# Pythondagi obyektlarning o'ziga xos xususiyatlarridan biri - obyektning xususiyatiga nuqta orqali to'g'ridan to'g'ri murojaat etish
# mumkin. Misol uchun, avval yaratilgan talaba1 obyektining ismini bilish uchun talaba1.ism deb yozish kifoya.

# Bu ancha qulay bo'lsa-da, mazkur usuldan foydalanishtavsiya etilmaydi. Sababi, vaqt o'tib klassingiz takomillashishi, uning ba'zi
# xususiyatlari o'zgarishi, o'chirilishi yoki almashishi mumkin. Shunday holatlarda nuqta orqali murojaat etish siz kutkan natijani
# bermasligi va dastur xato ishlashiga olib kelishi tabiiy. Bunday holatlarning oldini olish uchun esa obyektning xususiyatlariga
# murojaat etish yoki ularni o'zgartirishni metod orqali  yo'lga qo'yishni odat qilish kerak.

# ETIBOR BERING! Umuman olganda, obyektning xususiyatlariga to'g'ridan to'g'ri murojaat etishni taqiqlash uchun inkapsulyatsiyadan 
# foydalanamiz. Bu haqida kelgusi bo'limda batafsil to'xtalamiz. Bu haqida kelgusi bo'limda batafsil to'xtalamiz.

# Dasturchilar orasida obyektning xususiyatlarini o'zgartiradigan metodlarni set(o'zgartirish) so'zi bilan, xususiyatlarni qaytaradigan
# metodlarni esa get (olish) so'zi bilan boshlash qoida qilib olingan. Masalan: set_name() va get_name() kabi.

# Agar yuqoridagi qoidalarga amal qilgan holda Talaba klassimizni yangilaydigan bo'lsak, u shunday ko'rinishga ega bo'ladi:
# class Talaba:
#     """Talaba nomli klass yaratamiz""" 
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil 
#         self.bosqich = 1
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
#     def update_bosqich(self):
#         """Talabaning bosqichini 1 taga ko'paytirish"""
#         self.bosqich += 1
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
#     def get_name(self):
#         """Talabaning ismini qaytaradi."""
#         return self.ism
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi."""
#         return self.familiya
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi."""
#         return f"{self.ism} {self.familiya}."
#     def get_age(self, jyil):
#         """Talabaning yoshini qaytaruvchi dastur."""
#         return jyil - self.tyil
    
# Xuddi shu kabi, Fan klassimizning yakuniy ko'rinishi quyidagicha bo'ladi:
# class Fan():
#     """Fan nomli klass"""
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabar = []
#     def add_students(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi 
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot."""
#         return [x.get_info() for x in self.talabar]
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni
    
# OBYEKTNING XUSUSIYATLARI VA METODLARINI KO'RISH.
# Obyektlar bilan ishlaganda, o'z-o'zidan, shu obyektga tegishli xususiyatlar va metodlarni bilish talab qilinadi. Agar obyekt tegishli
# bo'lgan klassni o'zimiz yaratgan bo'lsak, istalgan payt klass ichini ko'rib olishimiz mumkin. Lekin klass juda ham uzun bo'lsa yoki
# boshqalar yaratgan klass haqida ma'lumot olish talab qilinsa, buning bir nechta yo'li bor.

# dir() FUNKSIYASI.
# dir() funksiyasi yordamida istalgan obyekt yoki klassning metodlarini ko'rib olishimiz mumkin:
# print(dir(Talaba))
# Natija: ['__class__',
          # '__delattr__',
          # '__dict__',
          # '__dir__',
          # '__doc__',
          # '__eq__',
          # '__format__',
          # '__ge__',
          # '__getattribute__',
          # '__getstate__',
          # '__gt__',
          # '__hash__',
          # '__init__',
          # '__init_subclass__',
          # '__le__',
          # '__lt__',
          # '__module__',
          # '__ne__',
          # '__new__',
          # '__reduce__',
          # '__reduce_ex__',
          # '__repr__',
          # '__setattr__',
          # '__sizeof__',
          # '__str__',
          # '__subclasshook__',
          # '__weakref__',
          # 'get_age',
          # 'get_fullname',
          # 'get_info',
          # 'get_lastname',
          # 'get_name',
          # 'set_bosqich',
          # 'update_bosqich']
          
# Lekin bunda har bir klass bilan keluvchi maxsus DUNDER METODLAR ham chiqib keldi. Dunder metodlar ikki pastki chiziq (__) bilan 
# boshlanadi va maxsus holatlar uchun sqlab qo'yilgan. Biz hozircha faqat __init__ metodi bilan tanishdik, qolganlari bilan keyingi
# darslarimizda yana ko'rishamiz. Dunder metodlardan keyin esa biz murojaat etishimiz mumkin bo'lgan metodlar ro'yxati kelgan.

# Kelin, dunder metodlarni tashlab, bizga kerak metodlarni qaytaruvchi sodda funksiya yozamiz:
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]
# # Funksiya yordamida Talaba klassining metodlarini ko'ramiz:
# print(see_methods(Talaba))
# Natija: ['get_age',
          # 'get_fullname',
          # 'get_info',
          # 'get_lastname',
          # 'get_name',
          # 'set_bosqich',
          # 'update_bosqich']
# Agar dir() funksiyasiga klass emas, obyekt uzatsak, metodlardan tashqari xususiyatlar ham chiqib keladi:
# print(see_methods(talaba1))
# Natija: ['get_age',
          # 'get_fullname',
          # 'get_info',
          # 'get_lastname',
          # 'get_name',
          # 'set_bosqich',
          # 'update_bosqich']

     #    ['bosqich',
     # 'familiya',
     # 'get_info',
     # 'ism',
     # 'set_bosqich',
     # 'tyil',
     # 'update_bosqich']
     
     
# __dict__ METODI.
# Yuqorida zikr qilingan dunder metodlardan biri __dict__ metodi bo'lib, bu metod OBYEKTNING xususiyatlarini lug'at ko'rinishida
# qaytaradi:
# print(talaba1.__dict__)
# Natija: {'ism': 'Olim', 'familiya': 'Olimov', 'tyil': 1995, 'bosqich': 1}

# Natijadan faqatgina kalitlarni ajratib olsak, obyektning xususiyatlari chiqadi:
# print(talaba1.__dict__.keys())
# Natija: dict_keys(['ism', 'familiya', 'tyil', 'bosqich'])

# AMALIYOT TOPSHIRIQLARI.
#1 - Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo)
# qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0).
# class Avto:
#     def __init__(self, model, rang, korobka, narx):
#         self.model = model
#         self.rang = rang
#         self.korobka = korobka
#         self.narx = narx
#         self.km = 0
#     def set_km(self, km):
#         """Avtomobilni km sini yangilaydigan metod"""
#         self.km = km
#     def update_km(self):
#         """Avtomobilni yurgan km sini yangilaydigan metod"""
#         self.km += 10

#2 -  Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing get_info() metodi avti haqida to'liq ma'lumotni matn
# ko'rinishida qaytarsin.       
#     def get_info(self):
#         """Avtomo9billar haqida to'liq ma'lumotni qaytaradi"""
#         return f"{self.model} modelidagi mashina, {self.rang} rangda, korobkasi {self.korobka}, narx {self.narx} va yurgan km si {self.km} km."        
# avto1 = Avto("Jentra", "qora", "avtomat", 15000)
# print(avto1.get_info())
# Natija: Jentra modelidagi mashina, qora rangda, korobkasi avromat, narx 15000 va yurgan km si 0 km.

#3 - Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing. update_km() metodi son qabul qilib olib, avtomobilning
# yurgan kilometrajini yangilab borsin.
# avto1 = Avto("Jentra", "qora", "avtomat", 15000)
# print(avto1.get_info())
# avto1.km = 100
# print(avto1.get_info())
# avto1.update_km()
# print(avto1.get_info())

#4 - Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar
# va hokazo).
# class Avtosalon:
#     def __init__(self, nomi, manzili):
#         self.nomi = nomi
#         self.manzili = manzili
#         self.avtolar_soni = 0
#         self.s_avtomobillar = []
        
#5 - Avtosalonga yangi avtomobillar qo'shish uchun metod yozing.
    # def add_avto(self, avto):
    #     """Salonga avtolar qo'shish uchun metod"""
    #     self.s_avtomobillar.append(avto)
    #     self.avtolar_soni += 1

#6 - Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
    # def get_avtolar(self):
    #    """Salondagi avtomobillar haqida ma'lumot qaytaruvchi metod"""
    #    return [avto.get_info() for avto in self.s_avtomobillar]

#7 - Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring.
# avto1 = Avto("Jenta", "qora", "avtomat", 15000) 
# avto2 = Avto("Malibu", "qora", "mexanika", 33000) 
# avto3 = Avto("Gelenwagen", "oq", "korobka", 400000) 

# avtosalon = Avtosalon("LUX Avtosalon", " Tahskent")
# avtosalon.add_avto(avto1)
# avtosalon.add_avto(avto2)
# avtosalon.add_avto(avto3)
# for avto_info in avtosalon.get_avtolar():
#     print(avto_info)

#7 - dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini
# toping (dir(str), dir(int) va hokazo)
# print("Avtosalon sinfining atributlari va metodlari")
# print(dir(Avtosalon))
# print("\nAvtosalon obyektining holati: (__dict__):")
# print(avtosalon.__dict__)


# 27 - DARS TUGADI.