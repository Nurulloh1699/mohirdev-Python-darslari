# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:44:46 2025

@author: DavrServis
"""

# 26 - DARS.
# KLASSLAR
# Klasslar object oriented dasturlashning poydevorlaridan biridir Klasslar bizga dasturlashga va dastur elementlariga real hayotdagi
# buyumlarga (obyektlarga) yondoshgandek yondoshi9sh imkonini beradi.

# Klasslar, obyektlar va ularning qanday ishlashini tushungan dasyurchi mantiqiy fikrlashda ham kuchli bo'ladi. Mukammal va kompleks
# muammolarga ham yechimni ko'ra biladi.


# PYTHONDA KLASSLAR.
# Klass tushunchasi siz uchun yangi bo'lishi mumkin, lekin biz shu vaqtgacha ulardan doimiy ravishda foydalanib keldik.

# Keling, x o'zgaruvchi yaratamiz, unga biror qiymat yuklaymiz va type() funksiyasi yordamiz uning turini ko'ramiz:
# x = 10
# print(type(x))
# # Natija: <class 'int'>
# matn = "salom"
# print(type(matn))
# Natija: <class 'str'>
# Ko'ryapmizki, x int klassidagi, matn esa str klassidagi obyektlar ekan. Demak, biz o'zgaruvchi yaratganimizda, aslida, Python int
# yoki str klassidan foydalangan holda yangi obyektlar yaratib kelayotgan ekan.

# Xuddi shu kabi, agar yangi funksiya yaratib, uning ham turini tekshirsak, funksiyamiz function klassiga tegishli obyekt bo'lib chiqadi.
# def salom_ber():
#     print("Assalomu Aleykum")
# print(type(salom_ber))
# Ntija: <class 'function'>
# Demak, Pythondagi har qanday o'zgaruvchi, funksiya va boshqa elementlar, aslida, obyektlar ekan.


# METODLAR.
# Har bir obyekt uning ustida bajarish mumkin bo'lgan funksiyalar bilan keladi. Bu funksiyalar obyekt ichida yashirin bo'ladi, Biz ularga
# nuqta va funksiya nomi orqali murojaat etishimiz mumkin. Bunday funksiyalar shu klassga (yoki obyektga) tegishli METODLAR deyiladi.

# Ba'zi metodlar bilan avvalgi darslarimizda tanishdik. bir klassga tegishli metodlar boshqa klassdagi obyektlar uchun mavjud bo'lmasligi
# tabiiy. Masalan, matnlar uchun mavjud metodlarni butun yoki o'nlik sonlarga qo'llab bo'lmaydi.
# matn = "salom"
# print(matn.upper()) 
# Natija: SALOM
# son = 20
# print(son.lower())
# Natija: AttributeError: 'int' object has no attribute 'lower'


# KLASS YARATISH.
# Yangi klass yaratish uchun class operatoridan foydalanamiz va klassimizga tugunarli nom beramiz. Esingizda bo'lsin, klass hali obyekt
# emas, obyekt uchun shablondir. Shuning uchun klass yaratishda mazkur klassdagi obyektlar uchun umumiy bo'lgan xususiyatlar va
# funksiyalarni o'ylashimiz kerak.

# Keling. Talaba degan klass yaratamiz:
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familya, tyil):
#         """Talaba xususiyatlari"""
#         self.ism = ism
#         self.familiya = familya
#         self.tyil = tyil
# Yuqoridagi kodimizni tahlil qilamiz:
# class Talaba  - Talaba nomli klass yaratdik. Klasslarga nom berishda uning birinchi harfini bosh harfdan boshlash tavsiya etiladi. 
# Agar klass nomi 2 va undan ko'p so'zdan iborat bo'lsa, har bir so'zni bosh harf bilan boshlang.

# def __init__(self) - klassga tegishli xususiyatlarni saqlovchi maxsus metod (funksiya). self so'zi ingliz tilidan "o'zi" deb tarjima
# qilinadiva bu klassdan yaratilgan obyektning o'ziga ishora qiladi. Ya'ni keyinchalik biz obyekt ichidagi metodga murojaat etganimizda
# shu obyektning o'zi birinchi bo'lib funksiyaga argument sifatida uzatiladi, obyekt ustida turli amallar bajarish imkonini beradi.

# def __init__(self, ism, familiya, tyil) - yaratayotgan klassimizga xos xususiyatlarni def __init__(self) funksiyasiga argument
# sifatida uzatamiz. Bizning Talaba klassimiz ism, familiya, va tug'ilgan yilga (tyil) ega bo'ladi.

# Keyingi qatorda esa self.xususiyat = argument komandasi yordamida uzatilgan argumentlarni klassning xususiyatlari bilan bog'laymiz. 
# Bu yerda xususiyat nomi uzatilgan argument nomi bilan mos tushishi shart emas, xususiyatga istalgan nom berishimiz mumkin (masalan,
# self.name = ism) 

# ETIBOR BERING! def __init__ metodi yozilishida init so'zidan avval va keyin ikki pastki chiziq yoziladi.


# KLASSDAN OBYEKT YARATISH.
# Klassimiz tayyor, keling, endi klassimizdan yangi obyekt yaratamiz.
# talaba1 = Talaba("Alijon", "Valiyev", 2000)

# Mana talaba obyektimiz tayyor. Obyektni yaratish uchun Talaba klassiga murojaat etdik va talabaning ismi, familiyasi va tug'ilgan
# yilini parametr sidatida uzatdik.

# OBYEKTNING XUSUSIYATLARINI KO'RISH.
# Obyerktning xususiyatlarini ko'rish uuchun nuqta orqali murojaat etishimiz mumkin.
# print(talaba1.ism)
# Natija: Alijon
# print(talaba1.familiya)
# Natija: Valiyev

# KLASSDAN BIR NECHTA OBYEKTLAR YARATISH.
# Yuqoridagi klassdan istalgancha obyektlar yaratishimiz mumkin:
# talaba2 = Talaba("Olim", "Olimov", 1995)
# talaba3 = Talaba("Husan", "Akbarov", 2004)
# talaba4 = Talaba("Hasan", "Akbarov", 2004)

# Bunda har bir obyekt o'zining alohida xususiyatlariga ega bo'ladi.
# print(talaba2.ism)
# Natija: Olim
# print(talaba4.familiya)
# Natija: Akbarov


# KLASSGA METODLAR QO'SHAMIZ.
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
        
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}."
#               f"{self.tyil}-yilda tug'ilganman, yoshim {2024-self.tyil} da."
#               )

# Boshlanishiga klassimizga bitta, tanishtir metodini qo'shdik. Bu metodimiz, ko'rib turganingizdek, bitta self (ya'ni obyektning o'zini)
# argumentini qabul qiladi va talaba haqidagi ma'lumotlarni konsolga chiqaradi.

# OBYEKTING METODLARIGA MUROJAAT ETAMIZ.
# Obyekt ichidagi funksiyaga, ya'ni obyektning metodiga murojaat etamiz:
# talaba4 = Talaba("Husan", "Akbarov", 2004) 
# talaba4.tanishtir()   
# Natija: Ismim Husan Akbarov.2004-yilda tug'ilganman, yoshim 20 da.

# Klassimiz istalgancha metodlarga ega bo'lishi mumkin. Yuqoridagi klassga yana obyektlar qo'shamiz:
# class Talaba :
#     """Tlaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyi = tyil
    
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#     def get_fullname(self):
#         """Talabaning to'liq ismini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
# Metodlarni tekshirib ko'ramiz.
# talaba1 = Talaba("Alijon", "Valiyev", 1999) 
# print(talaba1.get_fullname())
# Natija: Alijon Valiyev
# print(talaba1.get_lastname())
# Natija: Valiyev

# ARGUMENT QABUL QILUVCHI METODLAR.
# Avvalgi misolimizda barcha metodlar faqatgina self parametrini qabul qilyapti. Aslida, boshqa funksiyalar kabi klass ichidagi metodlar
# ham argumentlar qabul qilishi mumkin. Yuqoridagi Talaba klassimizga yangi get_age() metodini qo'shamiz:
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#     def get_lastname(self):
#         """Tlabaning familiyasini qaytaradi"""
#         return self.familiya
#     def get_fullname(self):
#         """Talabaning to'liq ismini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil
# get_age() metodi obyektning o'zidan tashqari qo'shimcha yil argumentini ham qabul qiladi va talabaning yoshini qaytaradi.
# talaba1 = Talaba("Nurulloh", "Abdurashidov", 1999)
# print(talaba1.get_age(2024))
# Natija: 25

# pass OPERATORI.
# Pythonda hech qanday vazifani bajarmaydigan pass operatori mavjud. Bu operatordan bo'sh metodlar yaratishda foydalanish mumkin. Misol
# uchun, siz klassingiz uchun muhim metodlarni bilasiz, lekin metod badani hali tayyor emas. Agar metod badanini bo'sh qoldirsangiz,
# Python IndentationError xatosini qaytaradi. Shunday holatlarda funksiya badaniga pass operatorini qo'yib ketishimiz mumkin:
# class User:
#     def __init__(self, name, username, email):
#         self.name = name
#         self.uname = username
#         self.mail = email
#     def describe():
#         pass
#     def get_email():
#         pass
# Yuqoridagi klassimizda describe() va get_mail() funksiyalar badani hali tayyor emas, bo'shliqni to'ldirish uchun esa pass operatorodan
# foydalanamiz.

# ETIBOR BERING! pass operatori bilan if-else, for, while bloklarini ham vaqtinchalik to'ldirib turish mumkin.

# AMALIYOT TOPSHIRIQLARI:
#1 - Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab
# qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo).
# class User:
#     def __init__(self, username, login, password, email):
#         self.username = username
#         self.login = login
#         self.password = password
#         self.email = email
        
#2 - Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib
# chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).        

    # def get_info(self):
    #     return f"Foydalanuvchi {self.username}ning logini:{self.login}, paroli:{self.password} va emaili: {self.email}."
# user1 = User("Nurulloh", "nur", "n1282754N", "nurik9.99@bk.ru")
# print(user1.get_info())

#3 - Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
#     def get_username(self):
#         return f"Foydalanuvchining username mi:{self.username}."
    
#     def get_login(self):
#         return f"{self.username} userining logini: {self.login}"

# user1 = User("Nurulloh", "nur", "n1282754N", "nurik9.99@bk.ru")
# user2 = User("Mavluda", "mav", "m2730209N", "mav9.99@bk.ru")
# user3 = User("Abdurahmon", "abu", "a1276464A", "abu9.99@bk.ru")
    
# print(user1.get_info())
# print(user2.get_username())
# print(user3.get_login())

# 26 - DARS TUGADI.