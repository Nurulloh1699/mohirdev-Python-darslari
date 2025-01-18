# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:47:38 2025

@author: DavrServis
"""

# 29 - DARS.
# INKAPSULYATSIYA VA KLASSGA OID XUSUSIYAT VA METODLAR.
# from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     def __init__(self, make, model, rang, yil, narx, km=0):
#         """Avtomobillarni xusuiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()

# avto1 = Avto("GM", "Malibu", "qora", 2024, 40000, 1000)
# print(avto1.narx)
# Natija: 40000
# print(avto1.km)
# Natija: AttributeError: 'Avto' object has no attribute 'km'
    # def get_km(self):
    #     return self.__km
    
    # def get_id(self):
    #     return self.__id
# avto1 = Avto("GM", "Malibu", "qora", 2024, 40000, 1000)
# print(avto1.get_km())
# Natija: 1000
# print(avto1.get_id())
# Natija: 7d5053c3-0955-4453-b81a-8081ba52435f
    # def add_km(self, km):
    #     """Mashinaga km qo'shish"""
    #     if km >= 0:
    #         self.__km += km
    #     else:
    #         print("""Mashinanig km sini o'zgartirib bo'lmaydi""")
# avto1 = Avto("GM", "Malibu", "qora", 2024, 40000, 1000)
# print(avto1.get_id())
# print(avto1.get_km())
# Natija: 3275fdfb-8776-471d-8d0f-5ce967e4111e
          #1000
# avto1.add_km(2000) # Km qo'shamiz.
# print(avto1.get_km())
# Natija: 3000
# avto1.add_km(-2000) # Manfiy son yozib ko'ramiz.
# print(avto1.get_km())
# Natija: Mashinanig km sini o'zgartirib bo'lmaydi
          # 3000
          
# from uuid import uuid4
# class Avto:
    # __num_avto = 0 # Bu o'rinda biz num_avto ni inkapsulyatsiya qilib qo'ydik.
    # PI = 14159 # Bu o'rinda konstanta qiymat yaratdik va bu qiymatdan ushbu klassni obyektalari foydalanishi
    # mumkin
    # """Avtomobil klassi"""
#     def __init__(self, make, model, rang, yil, narx, km=0):
#         """Avtomobillarni xusuiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1          
    
#     # Quyidagi metod num_avto inkapsulyatsiya qilingandan keyin uni ko'rish imkonini beradi.
#     @classmethod # Dekarator
#     def get_num_avto(cls): # Obyektni emas klass ni uzatkanimiz uchun cls yozildi qavs ichiga. 
#         return cls.__num_avto 
    
#     def get_km(self):
#          return self.__km
     
#     def get_id(self):
#          return self.__id     
    
#     def add_km(self, km):
#          """Mashinaga km qo'shish"""
#          if km >= 0:
#              self.__km += km
#          else:
#              print("""Mashinanig km sini o'zgartirib bo'lmaydi""")
# avto1 = Avto("Chevrolet", "Subaru", "Sariq", 2024, 70000)
# avto2 = Avto("Dodge", "Chalenger", "Qora", 2022, 55000)
# avto3 = Avto("GM", "Malibu", "Qora", 2023, 35000)
# Endi istalgan obyekt orqali yuqoridagi num_avtoga murojaat qilishimiz mumkin.
# print(avto1.num_avto)
# Natija: 3 # Yani Avto degan klassimizdan 3ta obyekt yaratildi degan ma'noda. Bu metod dastur ishga tushgandan 
# beri nechta foydalanuvchi yokida mashina ro'yxatdan o'tdi shuni nazorat qilib borish mumkin.

# num_avto inkapsulyatsiya bo'lgandan keyingi (__num_avto) holat.
# print(avto1.__num_avto)
# Natija: AttributeError: type object 'Avto' has no attribute 'num_avto'

# Endi yuqorida inkapsulyatsiya amallari bajarilgani uchun, num_avto ko'rish uchun quyidagicha yo'l tutamiz:
# print(Avto.get_num_avto())
# Natija: 3 # Bu o'rinda 3 klassdan foydalanishlar sonini ko'rsatadi.

# Bu o'rinda biz num_avto metodiga obyekt orqali murojaat qilsak ham bo'ladi.
# print(avto1.get_num_avto())
# Natija: 3

# Endi biz bu klasslarni modullarga ajratishni ko'rib chiqamiz. Yuqorida yozilgan klasslarni endi alohida 
# faylga joylaymiz va dasturimizni bemalol yangi va bo'sh muhitda yozib boramiz. 

# Biz endi yangi muhitda ishlay turib bu muhitga yaratilgan faylni import qilib olishimiz kerak bo'ladi.
# import avto
# avto1 = Avto("Chevrolet", "Subaru", "Sariq", 2024, 70000)
# avto2 = Avto("Dodge", "Chalenger", "Qora", 2022, 55000)
# avto3 = Avto("GM", "Malibu", "Qora", 2023, 35000)

# AMALIYOT TOPSHIRIQLARI.
#1 - Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing va ularning
# qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
# class Shaxs:
    
#     """Shaxslar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif
    
#     def __init__(self, ism, familiya, passport, tyil):
#         # Shaxsni yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         self.ism = ism  # Shaxsning ismi (ochiq xususiyat)
#         self.familiya = familiya  # Shaxsning familiyasi (ochiq xususiyat)
#         self.__passport = passport  # Shaxsning pasport raqami (yopiq xususiyat)
#         self.tyil = tyil  # Shaxsning tug'ilgan yili (ochiq xususiyat)
        
#     def get_info(self):
#         """Shaxs haqida umumiy ma'lumot qaytaruvchi metod"""
#         info = f"{self.ism} {self.familiya}."  # Ism va familiya
#         info += f" Passport: {self.__passport}, {self.tyil}-yilda tug'ilgan."  # Pasport va tug'ilgan yil haqida ma'lumot
#         return info  # To'plangan ma'lumotni qaytaradi

#     def get_age(self, yil):
#         """Shaxsning yoshini hisoblab qaytaruvchi metod"""
#         return yil - self.tyil  # Joriy yil va tug'ilgan yil farqini qaytaradi

#     # Passport uchun getter va setter metodlar
#     def get_passport(self):
#         """Yopiq pasport qiymatini qaytaruvchi metod"""
#         return self.__passport
    
#     def set_passport(self, yangi_passport):
#         """Pasport qiymatini yangilovchi metod"""
#         self.__passport = yangi_passport


# class Talaba(Shaxs):
    
#     """Talabalar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif

#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         # Talabani yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         super().__init__(ism, familiya, passport, tyil)  # Superklassning atributlarini chaqirish
#         self.__idraqam = idraqam  # Talabaning ID raqami (yopiq xususiyat)
#         self.bosqich = 1  # Talabaning o'qish bosqichi (ochiq xususiyat)
        
    
#     def get_id_raqam(self):
#         """"""

#     def set_id(self, yangi_idraqam):
#         """ID raqam qiymatini yangilovchi metod"""
#         self.__idraqam = yangi_idraqam

#     def get_bosqich(self):
#         """O'qish bosqichini qaytaruvchi metod"""
#         return self.bosqich

#2 - Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
# class Shaxs:
#     odamlar_soni = 0
#     """Shaxslar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif
    
#     def __init__(self, ism, familiya, passport, tyil):
#         # Shaxsni yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         self.ism = ism  # Shaxsning ismi (ochiq xususiyat)
#         self.familiya = familiya  # Shaxsning familiyasi (ochiq xususiyat)
#         self.__passport = passport  # Shaxsning pasport raqami (yopiq xususiyat)
#         self.tyil = tyil  # Shaxsning tug'ilgan yili (ochiq xususiyat)
#         Shaxs.odamlar_soni += 1
#     def get_info(self):
#         """Shaxs haqida umumiy ma'lumot qaytaruvchi metod"""
#         info = f"{self.ism} {self.familiya}."  # Ism va familiya
#         info += f" Passport: {self.__passport}, {self.tyil}-yilda tug'ilgan."  # Pasport va tug'ilgan yil haqida ma'lumot
#         return info  # To'plangan ma'lumotni qaytaradi

#     def get_age(self, yil):
#         """Shaxsning yoshini hisoblab qaytaruvchi metod"""
#         return yil - self.tyil  # Joriy yil va tug'ilgan yil farqini qaytaradi

#     # Passport uchun getter va setter metodlar
#     def get_passport(self):
#         """Yopiq pasport qiymatini qaytaruvchi metod"""
#         return self.__passport
    
#     def set_passport(self, yangi_passport):
#         """Pasport qiymatini yangilovchi metod"""
#         self.__passport = yangi_passport
        
    
    
        
# class Talaba(Shaxs):
#     talabalar_soni = 0
#     """Talabalar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif

#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         # Talabani yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         super().__init__(ism, familiya, passport, tyil)  # Superklassning atributlarini chaqirish
#         self.__idraqam = idraqam  # Talabaning ID raqami (yopiq xususiyat)
#         self.bosqich = 1  # Talabaning o'qish bosqichi (ochiq xususiyat)
#         Talaba.talabalar_soni += 1
    
#     def get_id_raqam(self):
#         """"""

#     def set_id(self, yangi_idraqam):
#         """ID raqam qiymatini yangilovchi metod"""
#         self.__idraqam = yangi_idraqam

#     def get_bosqich(self):
#         """O'qish bosqichini qaytaruvchi metod"""
#         return self.bosqich
    
    
#3 - Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing 
# class Shaxs:
#     odamlar_soni = 0
#     """Shaxslar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif
    
#     def __init__(self, ism, familiya, passport, tyil):
#         # Shaxsni yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         self.ism = ism  # Shaxsning ismi (ochiq xususiyat)
#         self.familiya = familiya  # Shaxsning familiyasi (ochiq xususiyat)
#         self.__passport = passport  # Shaxsning pasport raqami (yopiq xususiyat)
#         self.tyil = tyil  # Shaxsning tug'ilgan yili (ochiq xususiyat)
#         Shaxs.odamlar_soni += 1
#     def get_info(self):
#         """Shaxs haqida umumiy ma'lumot qaytaruvchi metod"""
#         info = f"{self.ism} {self.familiya}."  # Ism va familiya
#         info += f" Passport: {self.__passport}, {self.tyil}-yilda tug'ilgan."  # Pasport va tug'ilgan yil haqida ma'lumot
#         return info  # To'plangan ma'lumotni qaytaradi

#     def get_age(self, yil):
#         """Shaxsning yoshini hisoblab qaytaruvchi metod"""
#         return yil - self.tyil  # Joriy yil va tug'ilgan yil farqini qaytaradi

#     # Passport uchun getter va setter metodlar
#     def get_passport(self):
#         """Yopiq pasport qiymatini qaytaruvchi metod"""
#         return self.__passport
    
#     def set_passport(self, yangi_passport):
#         """Pasport qiymatini yangilovchi metod"""
#         self.__passport = yangi_passport
        
#     @classmethod
#     def get_odamlar_soni(cls):
#         """Hozirgi vaqtda yaratilgan shaxslar sonini qaytaradi"""
#         return cls.odamlar_soni

#     # Klassga oid xususiyatni o'zgartiruvchi metod
#     @classmethod
#     def reset_odamlar_soni(cls):
#         """Shaxslar sonini noldan boshlash"""
#         cls.odamlar_soni = 0
        
# class Talaba(Shaxs):
#     talabalar_soni = 0
#     """Talabalar haqida ma'lumot"""  # Klassning vazifasini aniqlovchi qisqacha tavsif

#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         # Talabani yaratishda boshlang'ich ma'lumotlarni qabul qilish va saqlash
#         super().__init__(ism, familiya, passport, tyil)  # Superklassning atributlarini chaqirish
#         self.__idraqam = idraqam  # Talabaning ID raqami (yopiq xususiyat)
#         self.bosqich = 1  # Talabaning o'qish bosqichi (ochiq xususiyat)
#         Talaba.talabalar_soni += 1
    
#     def get_id_raqam(self):
#         """"""

#     def set_id(self, yangi_idraqam):
#         """ID raqam qiymatini yangilovchi metod"""
#         self.__idraqam = yangi_idraqam

#     def get_bosqich(self):
#         """O'qish bosqichini qaytaruvchi metod"""
#         return self.bosqich
    
#     @classmethod
#     def get_talabalar_soni(cls):
#         """Hozirgi vaqtda yaratilgan talabalar sonini qaytaradi"""
#         return cls.talabalar_soni

#     # Klassga oid xususiyatni o'zgartiruvchi metod
#     @classmethod
#     def reset_talabalar_soni(cls):
#         """Talabalar sonini noldan boshlash"""
#         cls.talabalar_soni = 0

# 29 - DARS TUGADI.