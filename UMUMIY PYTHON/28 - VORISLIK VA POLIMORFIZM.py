# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:46:52 2025

@author: DavrServis
"""

# 28 - DARS.
# VORISLIK VA POLIMORFIZM.

# Shaxs degan klass yaratamiz.
# class Shaxs:
#     """Shaxslar haqida ma'lumot""" # nomidan ham ko'rinib turibdiki klassimizning vazifasai shaxslar haqidagi ma'lumotlarni shakllantirish
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
        
#     def get_info(self):
#         """Shaxs haqida ma'lumot""" # Shaxs haqidagi jamlangan ma'lumotlarni chiroyli shaklda konsolga chiqaradi.
#         info = f"{self.ism} {self.familiya}."
#         info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan."
#         return info
#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
# inson = Shaxs("Nurulloh", "Abdurashidov", "FB112233", 1999)
# print(inson.get_info())   
# Natija: Nurulloh Abdurashidov.Passport: FB112233, 1999-yilda tug'ilgan.
# print(inson.get_age(2024))
# Natija: 25
# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         """Talabaning xusussiyatlari"""
#         super().__init__(ism, familiya, passport, tyil) # Yuqoridagi super klassdan shu voris klassga yuqoridagi elementlarni olamiz.
#         self.idraqam = idraqam
#         self.bosqich = 1
        
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    
# talaba1 = Talaba("Nurulloh", "Abdurashidov", "FB112233", 1999, "N000001")
# print(talaba1.get_id()) # Talabaning ID raqamini chaqiramiz.
# Natija: Nurulloh Abdurashidov.Passport: FB112233, 1999-yilda tug'ilgan.
# print(talaba1.get_age(2024)) # Bu metod aslida Talaba metodida yo'q lekin yuqoridagi super klassda bor shunchun bemalol bubga murojaat
# qilsak bo'ladi.
# Natija: 25
# print(talaba1.get_info()) # Bu metod ham xuddi shunday aslida Talabada yo'q lekin super-klassdan meros qilib olgan.
# Natija: Nurulloh Abdurashidov.Passport: FB112233, 1999-yilda tug'ilgan.

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
# talaba1 = Talaba("Nurulloh", "Abdurashidov", "AB112233", 1999, "N00001")
# print(talaba1.get_info())
# Natija: Nurulloh Abdurashidov. 1-bosqich. ID raqami: N00001

# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talabaning xusussiyatlari"""
#         super().__init__(ism, familiya, passport, tyil) # Yuqoridagi super klassdan shu voris klassga yuqoridagi elementlarni olamiz.
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
        
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
# class Manzil:
#     """Manzil saqlash uchun klass"""
#     def  __init__(self, uy, kocha, tuman, viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
        
#     def get_manzil(self):
#         """Manzil ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy."
#         return manzil
# talaba1_manzil = Manzil("1/71", "Navroz", "Oltiariq", "Farg'ona")
# talaba1 = Talaba("Nurulloh", "Abdurashidov", "AB112233", 1999, "N00001", talaba1_manzil)
# print(talaba1.manzil.get_manzil())

# AMALIYOT TOPSHIRIQLARI.
#1 - Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh
# ro'yxatdan iborat bo'lsin (self.fanlar=[])
# class Talaba:
#     """Talaba degan klass yaratamiz"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil, fanlar):
#         """Talaba xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#         self.idraqam = idraqam
#         self.manzil = manzil
#         self.fanlar = []
    
#2 - Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
# class Fan:
#     """Fan degan klass yaratamiz"""
#     def __init__(self, nomi, soat, oqituvchi):
#         """Fan xususiyatlari"""
#         self.nomi = nomi
#         self.soat = soat
#         self.oqituvchi = oqituvchi
        
#     def get_fan_info(self):
#         """Fan haqida ma'lumot"""
#         return f"Fan: {self.nomi}, Soatlar: {self.soat}. O'qituvchi: {self.oqituvchi}."
# Turli fanlar uchun obyektlar yaratish.
# matematika = Fan("Oliy Matematika", 48, "Ibrohimov Anvar")
# fizika = Fan("Fizika", 60, "Abdurashidova Mavludaxon")
# informatika = Fan("Informatika", 80, "Abdurashidov Nurulloh")

# Fanlar haqidagi ma'lumotlarni chiqaramiz.
# print(matematika.get_fan_info())
# print(fizika.get_fan_info())
# print(informatika.get_fan_info())

#3 - Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib
# olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
# class Talaba:
#     """Talaba degan klass yaratamiz"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talaba xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#         self.idraqam = idraqam
#         self.manzil = manzil
#         self.fanlar = []  # Bo'sh ro'yxat
    
#     def fanga_yozil(self, fan):
#         """Talabani fanga yozish"""
#         self.fanlar.append(fan)  # Tekshiruvsizlik qo'shish

#     def get_fanlar(self):
#         """Talabaning fanlari haqida ma'lumot"""
#         return [fan.get_fan_info() for fan in self.fanlar]


# class Fan:
#     """Fan degan klass yaratamiz"""
#     def __init__(self, nomi, soat, oqituvchi):
#         """Fan xususiyatlari"""
#         self.nomi = nomi
#         self.soat = soat
#         self.oqituvchi = oqituvchi
        
#     def get_fan_info(self):
#         """Fan haqida ma'lumot"""
#         return f"Fan: {self.nomi}, Soatlar: {self.soat}. O'qituvchi: {self.oqituvchi}."


# Misol
# Fan obyektlari
# fan1 = Fan("Matematika", 60, "Olimov Anvar")
# fan2 = Fan("Fizika", 40, "Karimova Dilnoza")

# Talaba obyekti
# talaba1 = Talaba("Ali", "Valiyev", "AA123456", 2000, 1, "Toshkent")

# Talabani fanga yozamiz
# talaba1.fanga_yozil(fan1)
# talaba1.fanga_yozil(fan2)

# Talabaning fanlari haqida ma'lumot
# print(talaba1.get_fanlar())

#4 - Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan
# uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.
# class Talaba:
#     """Talaba degan klass yaratamiz"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talaba xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#         self.idraqam = idraqam
#         self.manzil = manzil
#         self.fanlar = []  # Bo'sh ro'yxat
    
#     def fanga_yozil(self, fan):
#         """Talabani fanga yozish"""
#         self.fanlar.append(fan)

#     def remove_fan(self, fan):
#         """Talabaning fanlari ro'yxatidan fanni o'chirish"""
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#             return f"{fan.nomi} fani ro'yxatdan o'chirildi."
#         return "Siz bu fanga yozilmagansiz."

#     def get_fanlar(self):
#         """Talabaning fanlari haqida ma'lumot"""
#         return [fan.get_fan_info() for fan in self.fanlar]


# class Fan:
#     """Fan degan klass yaratamiz"""
#     def __init__(self, nomi, soat, oqituvchi):
#         """Fan xususiyatlari"""
#         self.nomi = nomi
#         self.soat = soat
#         self.oqituvchi = oqituvchi
        
#     def get_fan_info(self):
#         """Fan haqida ma'lumot"""
#         return f"Fan: {self.nomi}, Soatlar: {self.soat}. O'qituvchi: {self.oqituvchi}."


# Misol
# Fan obyektlari
# fan1 = Fan("Matematika", 60, "Olimov Anvar")
# fan2 = Fan("Fizika", 40, "Karimova Dilnoza")
# fan3 = Fan("Kimyo", 50, "Rahmonov Shavkat")

# Talaba obyekti
# talaba1 = Talaba("Ali", "Valiyev", "AA123456", 2000, 1, "Toshkent")

# Talabani fanga yozamiz
# talaba1.fanga_yozil(fan1)
# talaba1.fanga_yozil(fan2)

# Talabaning fanlari haqida ma'lumot
# print("Talabaning fanlari:")
# print(talaba1.get_fanlar())

# Fanni ro'yxatdan o'chirish
# print(talaba1.remove_fan(fan2))  # Fizika fani o'chiriladi
# print(talaba1.remove_fan(fan3))  # Kimyo fani mavjud emas

# Yangilangan fanlar ro'yxati
# print("Yangilangan fanlar ro'yxati:")
# print(talaba1.get_fanlar())

#5 - Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)        
# class Shaxs:
#     """Shaxs degan umumiy klass"""
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}, Passport: {self.passport}, Tug'ilgan yil: {self.tyil}"

#     def get_age(self, yil):
#         """Shaxsning yoshini hisoblash"""
#         return yil - self.tyil


# Professor klassi
# class Professor(Shaxs):
#     """Professor klassi"""
#     def __init__(self, ism, familiya, passport, tyil, kafedra):
#         super().__init__(ism, familiya, passport, tyil)
#         self.kafedra = kafedra

#     def get_info(self):
#         """Professor haqida ma'lumot"""
#         return f"{super().get_info()}, Kafedra: {self.kafedra}"


# Foydalanuvchi klassi
# class Foydalanuvchi(Shaxs):
#     """Foydalanuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, username, email):
#         super().__init__(ism, familiya, passport, tyil)
#         self.username = username
#         self.email = email

#     def get_info(self):
#         """Foydalanuvchi haqida ma'lumot"""
#         return f"{super().get_info()}, Username: {self.username}, Email: {self.email}"


# Sotuvchi klassi
# class Sotuvchi(Shaxs):
#     """Sotuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, dokon):
#         super().__init__(ism, familiya, passport, tyil)
#         self.dokon = dokon

#     def get_info(self):
#         """Sotuvchi haqida ma'lumot"""
#         return f"{super().get_info()}, Do'kon: {self.dokon}"


# Mijoz klassi
# class Mijoz(Shaxs):
#     """Mijoz klassi"""
#     def __init__(self, ism, familiya, passport, tyil, manzil, xaridlar_soni):
#         super().__init__(ism, familiya, passport, tyil)
#         self.manzil = manzil
#         self.xaridlar_soni = xaridlar_soni

#     def get_info(self):
#         """Mijoz haqida ma'lumot"""
#         return f"{super().get_info()}, Manzil: {self.manzil}, Xaridlar soni: {self.xaridlar_soni}"


# Misollar
# professor = Professor("Anvar", "Olimov", "AA123456", 1975, "Fizika")
# foydalanuvchi = Foydalanuvchi("Ali", "Valiyev", "BB654321", 1995, "ali123", "ali@mail.com")
# sotuvchi = Sotuvchi("Dilnoza", "Karimova", "CC789101", 1988, "Bozor do'koni")
# mijoz = Mijoz("Murod", "Bekmurodov", "DD543210", 1990, "Toshkent, Chilonzor", 12)

# Ma'lumotlarni chiqarish
# print(professor.get_info())
# print(foydalanuvchi.get_info())
# print(sotuvchi.get_info())
# print(mijoz.get_info())

#6 - Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
# class Shaxs:
#     """Shaxs degan umumiy klass"""
#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"
    
#     def get_age(self, yil):
#         """Shaxsning yoshini hisoblash"""
#         return yil - self.tyil


# Professor klassi
# class Professor(Shaxs):
#     """Professor klassi"""
#     def __init__(self, ism, familiya, passport, tyil, fanlar, daraja):
#         super().__init__(ism, familiya, passport, tyil)
#         self.fanlar = fanlar  # Professor o'qitadigan fanlar ro'yxati
#         self.daraja = daraja  # Professorlik darajasi (PhD, Doktor, va h.k.)
    
#     def get_professor_info(self):
#         """Professor haqida ma'lumot"""
#         fanlar = ", ".join(self.fanlar)
#         return f"{self.get_info()}, Fanlari: {fanlar}, Ilmiy daraja: {self.daraja}"


# Mijoz klassi
# class Mijoz(Shaxs):
#     """Mijoz klassi"""
#     def __init__(self, ism, familiya, passport, tyil, mijoz_id, buyurtmalar):
#         super().__init__(ism, familiya, passport, tyil)
#         self.mijoz_id = mijoz_id  # Mijoz identifikatori
#         self.buyurtmalar = buyurtmalar  # Buyurtmalar ro'yxati
    
#     def add_order(self, buyurtma):
#         """Mijozga yangi buyurtma qo'shish"""
#         self.buyurtmalar.append(buyurtma)
    
#     def get_mijoz_info(self):
#         """Mijoz haqida ma'lumot"""
#         orders = ", ".join(self.buyurtmalar)
#         return f"{self.get_info()}, Mijoz ID: {self.mijoz_id}, Buyurtmalari: {orders}"


# Foydalanuvchi klassi
# class Foydalanuvchi(Shaxs):
#     """Foydalanuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, login, email):
#         super().__init__(ism, familiya, passport, tyil)
#         self.login = login  # Foydalanuvchi login
#         self.email = email  # Foydalanuvchi elektron pochta
    
#     def change_email(self, new_email):
#         """Emailni o'zgartirish"""
#         self.email = new_email
    
#     def get_foydalanuvchi_info(self):
#         """Foydalanuvchi haqida ma'lumot"""
#         return f"{self.get_info()}, Login: {self.login}, Email: {self.email}"


# Sotuvchi klassi
# class Sotuvchi(Shaxs):
#     """Sotuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, dokon_nomi, savdo_hisoboti):
#         super().__init__(ism, familiya, passport, tyil)
#         self.dokon_nomi = dokon_nomi  # Sotuvchining do'koni nomi
#         self.savdo_hisoboti = savdo_hisoboti  # Sotuv hisobotlari ro'yxati
    
#     def add_sale(self, savdo):
#         """Yangi savdo qo'shish"""
#         self.savdo_hisoboti.append(savdo)
    
#     def get_sotuvchi_info(self):
#         """Sotuvchi haqida ma'lumot"""
#         sales = ", ".join(self.savdo_hisoboti)
#         return f"{self.get_info()}, Dokon nomi: {self.dokon_nomi}, Savdo hisobotlari: {sales}"
#7 - Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
# class Shaxs:
#     """Shaxs degan umumiy klass"""
#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida umumiy ma'lumot"""
#         return f"{self.ism} {self.familiya}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Professor klassi
# class Professor(Shaxs):
#     """Professor klassi"""
#     def __init__(self, ism, familiya, passport, tyil, fanlar, daraja):
#         super().__init__(ism, familiya, passport, tyil)
#         self.fanlar = fanlar  # Professor o'qitadigan fanlar ro'yxati
#         self.daraja = daraja  # Professorlik darajasi (PhD, Doktor, va h.k.)
    
#     def get_info(self):
#         """Professor haqida ma'lumot"""
#         fanlar = ", ".join(self.fanlar)
#         return f"Professor: {self.ism} {self.familiya}, Daraja: {self.daraja}, Fanlari: {fanlar}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Mijoz klassi
# class Mijoz(Shaxs):
#     """Mijoz klassi"""
#     def __init__(self, ism, familiya, passport, tyil, mijoz_id, buyurtmalar):
#         super().__init__(ism, familiya, passport, tyil)
#         self.mijoz_id = mijoz_id  # Mijoz identifikatori
#         self.buyurtmalar = buyurtmalar  # Buyurtmalar ro'yxati
    
#     def get_info(self):
#         """Mijoz haqida ma'lumot"""
#         orders = ", ".join(self.buyurtmalar)
#         return f"Mijoz: {self.ism} {self.familiya}, ID: {self.mijoz_id}, Buyurtmalar: {orders}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Foydalanuvchi klassi
# class Foydalanuvchi(Shaxs):
#     """Foydalanuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, login, email):
#         super().__init__(ism, familiya, passport, tyil)
#         self.login = login  # Foydalanuvchi login
#         self.email = email  # Foydalanuvchi elektron pochta
    
#     def get_info(self):
#         """Foydalanuvchi haqida ma'lumot"""
#         return f"Foydalanuvchi: {self.ism} {self.familiya}, Login: {self.login}, Email: {self.email}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Sotuvchi klassi
# class Sotuvchi(Shaxs):
#     """Sotuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, dokon_nomi, savdo_hisoboti):
#         super().__init__(ism, familiya, passport, tyil)
#         self.dokon_nomi = dokon_nomi  # Sotuvchining do'koni nomi
#         self.savdo_hisoboti = savdo_hisoboti  # Sotuv hisobotlari ro'yxati
    
#     def get_info(self):
#         """Sotuvchi haqida ma'lumot"""
#         sales = ", ".join(self.savdo_hisoboti)
#         return f"Sotuvchi: {self.ism} {self.familiya}, Dokon: {self.dokon_nomi}, Savdo hisobotlari: {sales}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"

#8 - Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating. 
# class Admin(Foydalanuvchi):
#     """Admin klassi - Foydalanuvchi klassidan voris"""
#     def __init__(self, ism, familiya, passport, tyil, login, email, admin_huquqlari):
#         """Admin xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil, login, email)
#         self.admin_huquqlari = admin_huquqlari  # Adminning huquqlari ro'yxati
    
#     def add_permission(self, huquq):
#         """Yangi huquq qo'shish"""
#         if huquq not in self.admin_huquqlari:
#             self.admin_huquqlari.append(huquq)
    
#     def remove_permission(self, huquq):
#         """Huquqni olib tashlash"""
#         if huquq in self.admin_huquqlari:
#             self.admin_huquqlari.remove(huquq)
#         else:
#             return "Bunday huquq yo'q."
    
#     def get_permissions(self):
#         """Admin huquqlari ro'yxatini qaytarish"""
#         return f"{self.ism} {self.familiya}ning admin huquqlari: {', '.join(self.admin_huquqlari)}"
    
#     def get_info(self):
#         """Admin haqida ma'lumot"""
#         permissions = ", ".join(self.admin_huquqlari)
#         return f"Admin: {self.ism} {self.familiya}, Login: {self.login}, Email: {self.email}, Huquqlari: {permissions}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Sinov dasturi
# admin = Admin("Anvar", "Valiyev", "EE1234567", 1987, "admin_user", "admin@gmail.com", ["Foydalanuvchilarni boshqarish", "Sahifalarni o'chirish"])
# print(admin.get_info())  # Admin haqida to'liq ma'lumot

# Yangi huquq qo'shish
# admin.add_permission("Hisobotlarni ko'rish")
# print(admin.get_permissions())  # Yangi huquqlar ro'yxati

# Mavjud huquqni olib tashlash
# admin.remove_permission("Sahifalarni o'chirish")
# print(admin.get_permissions())  # Yangilangan huquqlar ro'yxati

# Sinov dasturi
# professor = Professor("Olim", "Qodirov", "AA1234567", 1980, ["Matematika", "Fizika"], "PhD")
# mijoz = Mijoz("Dilnoza", "Karimova", "BB7654321", 1990, "M12345", ["Telefon", "Noutbuk"])
# foydalanuvchi = Foydalanuvchi("Jasur", "Akmalov", "CC4567890", 1995, "jasur_ak", "jasur@gmail.com")
# sotuvchi = Sotuvchi("Salim", "Sobirov", "DD0987654", 1985, "TechStore", ["Telefon: 5 ta", "Kompyuter: 3 ta"])

# Har bir obyekt haqida yangi get_info() metodi orqali ma'lumot
# print(professor.get_info())
# print(mijoz.get_info())
# print(foydalanuvchi.get_info())
# print(sotuvchi.get_info())


# Dastur sinovi
# professor = Professor("Olim", "Qodirov", "AA1234567", 1980, ["Matematika", "Fizika"], "PhD")
# mijoz = Mijoz("Dilnoza", "Karimova", "BB7654321", 1990, "M12345", ["Telefon", "Noutbuk"])
# foydalanuvchi = Foydalanuvchi("Jasur", "Akmalov", "CC4567890", 1995, "jasur_ak", "jasur@gmail.com")
# sotuvchi = Sotuvchi("Salim", "Sobirov", "DD0987654", 1985, "TechStore", ["Telefon: 5 ta", "Kompyuter: 3 ta"])

# Har bir obyekt haqida ma'lumot
# print(professor.get_professor_info())
# print(mijoz.get_mijoz_info())
# print(foydalanuvchi.get_foydalanuvchi_info())
# print(sotuvchi.get_sotuvchi_info())

# Dastur sinovi davomida yangilash
# mijoz.add_order("Televizor")
# foydalanuvchi.change_email("jasur_akmalov@gmail.com")
# sotuvchi.add_sale("Monitor: 2 ta")

# Yangilangan ma'lumotlar
# print(mijoz.get_mijoz_info())
# print(foydalanuvchi.get_foydalanuvchi_info())
# print(sotuvchi.get_sotuvchi_info())

#9 - Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn
# chiqarsin.
# class Admin(Foydalanuvchi):
#     """Admin klassi - Foydalanuvchi klassidan voris"""
#     def __init__(self, ism, familiya, passport, tyil, login, email, admin_huquqlari):
#         """Admin xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil, login, email)
#         self.admin_huquqlari = admin_huquqlari  # Adminning huquqlari ro'yxati
    
#     def add_permission(self, huquq):
#         """Yangi huquq qo'shish"""
#         if huquq not in self.admin_huquqlari:
#             self.admin_huquqlari.append(huquq)
    
#     def remove_permission(self, huquq):
#         """Huquqni olib tashlash"""
#         if huquq in self.admin_huquqlari:
#             self.admin_huquqlari.remove(huquq)
#         else:
#             return "Bunday huquq yo'q."
    
#     def get_permissions(self):
#         """Admin huquqlari ro'yxatini qaytarish"""
#         return f"{self.ism} {self.familiya}ning admin huquqlari: {', '.join(self.admin_huquqlari)}"
    
#     def ban_user(self, foydalanuvchi):
#         """Foydalanuvchini bloklash"""
#         print(f"Foydalanuvchi {foydalanuvchi} bloklandi.")
    
#     def unban_user(self, foydalanuvchi):
#         """Foydalanuvchining blokini yechish"""
#         print(f"Foydalanuvchi {foydalanuvchi} blokdan chiqarildi.")
    
#     def reset_password(self, foydalanuvchi):
#         """Foydalanuvchi parolini qayta o'rnatish"""
#         print(f"Foydalanuvchi {foydalanuvchi} paroli qayta o'rnatildi.")
    
#     def get_info(self):
#         """Admin haqida ma'lumot"""
#         permissions = ", ".join(self.admin_huquqlari)
#         return f"Admin: {self.ism} {self.familiya}, Login: {self.login}, Email: {self.email}, Huquqlari: {permissions}, Passport: {self.passport}, Tug'ilgan yili: {self.tyil}"


# Sinov dasturi
# admin = Admin("Anvar", "Valiyev", "EE1234567", 1987, "admin_user", "admin@gmail.com", ["Foydalanuvchilarni boshqarish", "Sahifalarni o'chirish"])
# print(admin.get_info())  # Admin haqida to'liq ma'lumot

# Foydalanuvchini bloklash va blokdan chiqarish
# admin.ban_user("Aliyev Zokir")
# admin.unban_user("Aliyev Zokir")

# Foydalanuvchi parolini qayta o'rnatish
# admin.reset_password("Karimov Aziz")
# Natija: Farg'ona viloyati, Oltiariq tumani, Navroz ko'chasi, 1/71-uy.
# 28 - DARS TUGADI.