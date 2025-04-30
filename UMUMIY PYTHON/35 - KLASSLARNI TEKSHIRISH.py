# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:51:14 2025

@author: DavrServis
"""

# 35 - DARS.
# KLASSLARNI TEKSHIRISH.

# Klasslarni tekshirish uchun avval oldingi darsda ko'rgan klasslarimizdan birini yaratib olamiz.
# class Car:
#     """(self, make, model, year, km = 0, price = None)"""
#     def __init__(self, make, model, year, km = 0, price = None):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price
#         self.__km = km
        
#     def set_price(self, price):
#         self.price = price
        
#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             raise ValueError("km manfiy bo'lishi mumkin emas")
            
#     def get_info(self):
#         info = f"{self.make.upper()} {self.model.title()}"
#         info += f"{self.year}-yil, {self.__km} km yurgan"
#         if self.price:
#             info += f" Narhi: {self.price}"
#         return info
    
#     def get_info(self):
#         info = f"{self.make.upper()} {self.model.title()}"
#         info += f"{self.year}-yil, {self.__km}km yurgan"
#         if self.price:
#             info += f" Narhi: {self.price}"
#         return info
    
#     def get_km(self):
#         return self.__km
# Endi bu klassimizni alohida modulga joylaymiz.

# QUYIDA BIZ DASTURIMIZNI CAR.PY MODULIDA SAQLAYMIZ:
# class Car:
#     """(self, make, model, year, km = 0, price = None)"""
#     def __init__(self, make, model, year, km = 0, price = None):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price
#         self.__km = km
        
#     def set_price(self, price):
#         self.price = price
        
#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             raise ValueError("km manfiy bo'lishi mumkin emas!")
            
#     def get_info(self):
#         info = f"{self.make.upper()} {self.model.title()}"
#         info += f"{self.year}-yil, {self.__km} km yurgan"
#         if self.price:
#             info += f" Narhi: {self.price}"
#         return info
    
#     def get_info(self):
#         info = f"{self.make.upper()} {self.model.title()}"
#         info += f"{self.year}-yil, {self.__km}km yurgan"
#         if self.price:
#             info += f" Narhi: {self.price}"
#         return info
    
#     def get_km(self):
#         return self.__km
    
# Endi bu klassimizni qo'lda tekshirib ko'ramiz:
# avto1 = Car("gm", "malibu", 2020)
# print(avto1.get_info())
# Mana oddiy holatda klassimizdagi get_info() metodini tekshirdik.

# Endi add_km() metodini ham tekshirib ko'ramiz:
# avto1.add_km(5000)
# Endi manfiy qiymat berib ko'ramiz:
# avto1.add_km(-500)
# Natija: ValueError: km manfiy bo'lishi mumkin emas!

# Keling endi har gal qo'lda tekshirishni oldini olish uchun test dastur yozamiz:


# QUYIDA BERILGAN TESTLAR CAR_TEST.PY MODULIDA SAQLANGAN BO'LADI. 
# import unittest
# from cars import Car

# class CarTest(unittest.TestCase):
#     """Car klassini tekshirish uchun test dastur!"""
#     def setUp(self):
#         make = 'GM'
#         model = 'Malibu'
#         year = 2020
#         self.price = 40000
#         self.km = 10000
#         self.avto1 = Car(make, model, year)
#         self.avto2 = Car(make, model, year, price = self.price)
        
#     def test_create(self):
#         # Qiymatlar mavjudligini ssertIsNotNone metodi orqali tekshiramiz:
#         self.assertIsNotNone(self.avto1.make)
#         self.assertIsNotNone(self.avto1.model)
#         self.assertIsNotNone(self.avto1.year)
#         # Qiymatlar mavjud emasligini assertIsNone metodi orqali tekshiramiz:
#         self.assertIsNone(self.avto1.price)
#         # Qiymat tengligini assertEqual metodi orqali tekshiramiz:
#         self.assertEqual(0, self.avto1.get_km())
#         # avto2 narhini tekshiramiz:
#         self.assertEqual(self.price, self.avto2.price)
        
# Test dasturimizni tekshirib ko'ramiz:
# unittest.main()
# Natija: Ran 1 test in 0.001s

        # OK

# Ba'zi holatlarda shoshganda masalan: model ga make ning qiymati biriktirilishi va yoki teskarisi bo'lgan holatlar bo'lishi mumkin. Bunday
# holatlarda hozirgi testimiz xato qaytarmaydi chunki biz faqat qiymat berilgan yoki yo'qligini tekshiryapmiz.
# Bunday holatlarda testga qo'shimcha qiymatni tekshirish uchun test qatorini qo'shib qo'yishimiz mumkin
        
# import unittest
# from cars import Car

# class CarTest(unittest.TestCase):
#     """Car klassini tekshirish uchun test dastur!"""
#     def setUp(self):
#         make = 'GM'
#         self.model = 'Malibu'
#         year = 2020
#         self.price = 40000
#         self.km = 10000
#         self.avto1 = Car(make, self.model, year)
#         self.avto2 = Car(make, self.model, year, price = self.price)
        
#     def test_create(self):
#         # Qiymatlar mavjudligini ssertIsNotNone metodi orqali tekshiramiz:
#         self.assertIsNotNone(self.avto1.make)
#         self.assertIsNotNone(self.avto1.model)
#         self.assertEqual(self.model, self.avto1.model)
#         self.assertIsNotNone(self.avto1.year)
#         # Qiymatlar mavjud emasligini assertIsNone metodi orqali tekshiramiz:
#         self.assertIsNone(self.avto1.price)
#         # Qiymat tengligini assertEqual metodi orqali tekshiramiz:
#         self.assertEqual(0, self.avto1.get_km())
#         # avto2 narhini tekshiramiz:
#         self.assertEqual(self.price, self.avto2.price) 
        
#     def test_set_price(self):
#         new_price = 45000
#         self.avto2.set_price(new_price)
#         self.assertEqual(new_price, self.avto2.price)
    
#     def test_add_km(self):
#         #1 Musbat qiymat berib ko'ramiz:
#         self.avto1.add_km(self.km)
#         self.assertEqual(self.km, self.avto1.get_km()) # Bu o'rinda biz yana bir narsani tekshirishimiz mumkin (kerak), yuqorida dasturchi 
# km qo'shishda + belgisini esdan chiqargan bo'lishi mumkin agar shunday bo'lsa bizning dastur xato ishlashi mumkin yani shunchaki ohirigi 
# berilgan km ga tenglab qo'yishi mumkin.
#         self.avto1.add_km(5000)
#         self.assertEqual(15000, self.avto1.get_km()) # + belgisi bo'lmagan holatda xato beradi yani km ni 5000 ga tenglab qo'ya qoladi.
#         #2 Manfiy qiymat berib ko'ramiz:
#         new_km = -5000
#         try:
#             self.avto1.add_km(new_km)
#         except ValueError as error:
#             self.assertEqual(type(error), ValueError)

# unittest.main()

# class Car:
#     """(self, make, model, year, km = 0, price = None)"""
#     def __init__(self, make, model, year, km = 0, price = None):
#         self.make = make
#         self.model = make # Shu qatordagi xato tufayli bu holatda biz xato natija oldik.
#         self.year = year
#         self.price = price
#         self.__km = km


# Yuqorida biz test_set_price(self) testini qo'shdik va bu orqali biz set_price degan metodimizni tekshiramiz bu metodimiz mashinaning
# narxini belgilaydi.

# Endi biz yuqorida add_km() metodi uchun test yozamiz bu biroz murakkabroq va bu o'rinda biz ikkita test yozishimiz kerak bo'ladi ya'ni
# bitta testimiz musbat qiymat berib va manfiy qimat berib tekshiramiz.


# ANALIYOT TOPSHIRIQLARI:
#1 - 30 - darsimizda Shaxs va Talaba klasslarini yaratgan edik. Shu ikki klassning xususiyatlari va metodlarini tekshiruvchi test dasturlar
# yozing.

# BU YERDA SHAXS KLASSI ASOSIY KODI KELTIRILGAN:
# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil

# TEST DASTURI:
# import unittest
# from shaxs import Shaxs  # Shaxs klassini import qilamiz

# class TestShaxs(unittest.TestCase):
#     """Shaxs klassining metodlarini test qilish uchun sinf."""
    
#     def setUp(self):
#         """Har bir testdan oldin bajariladigan metod."""
#         # Test uchun Shaxs obyektini yaratamiz
#         self.shaxs1 = Shaxs("Ali", "Valiyev", "AB1234567", 1990)
    
#     def test_get_info(self):
#         """get_info metodini test qilish."""
#         # Kutilgan natija
#         expected_info = "Ali Valiyev. Passport:AB1234567, 1990-yilda tug`ilgan"
#         # get_info metodi natijasini tekshiramiz
#         self.assertEqual(self.shaxs1.get_info(), expected_info)
#         # Izoh: get_info metodi to'g'ri natija qaytarsa, test muvaffaqiyatli o'tadi.
    
#     def test_get_age(self):
#         """get_age metodini test qilish."""
#         # 2025 yilda Shaxsning yoshini tekshiramiz
#         expected_age = 2025 - 1990  # 35 yosh
#         self.assertEqual(self.shaxs1.get_age(2025), expected_age)
#         # Izoh: get_age metodi kutilgan yoshni qaytarsa, test muvaffaqiyatli o'tadi.

# if __name__ == '__main__':
#     unittest.main()

# BU YERDA TALABA KLASSI ASOSIY KODI KELTIRILGAN:
# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil,idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
    
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    
# # TEST DASTURI:
# import unittest
# from shaxs import Shaxs  # Shaxs klassini import qilamiz
# from talaba import Talaba  # Talaba klassini import qilamiz

# class TestTalaba(unittest.TestCase):
#     """Talaba klassining metodlarini test qilish uchun sinf."""
    
#     def setUp(self):
#         """Har bir testdan oldin bajariladigan metod."""
#         # Test uchun Talaba obyektini yaratamiz
#         self.talaba1 = Talaba("Ali", "Valiyev", "AB1234567", 2000, "T123456")
    
#     def test_get_id(self):
#         """get_id metodini test qilish."""
#         # Kutilgan ID raqam
#         expected_id = "T123456"
#         # get_id metodi natijasini tekshiramiz
#         self.assertEqual(self.talaba1.get_id(), expected_id)
#         # Izoh: get_id metodi to'g'ri ID raqamni qaytarsa, test muvaffaqiyatli o'tadi.
    
#     def test_get_bosqich(self):
#         """get_bosqich metodini test qilish."""
#         # Kutilgan bosqich
#         expected_bosqich = 1
#         # get_bosqich metodi natijasini tekshiramiz
#         self.assertEqual(self.talaba1.get_bosqich(), expected_bosqich)
#         # Izoh: get_bosqich metodi to'g'ri bosqichni qaytarsa, test muvaffaqiyatli o'tadi.
    
#     def test_inheritance(self):
#         """Shaxs klassidan meros olishni test qilish."""
#         # Talaba obyektining Shaxs klassiga tegishli metodlarini tekshiramiz
#         self.assertEqual(self.talaba1.get_info(), "Ali Valiyev. Passport:AB1234567, 2000-yilda tug`ilgan")
#         # Izoh: get_info metodi Shaxs klassidan meros bo'lib o'tganini tasdiqlaydi.
#         self.assertEqual(self.talaba1.get_age(2025), 25)
#         # Izoh: get_age metodi Talaba obyektida ham to'g'ri ishlaydi.

# if __name__ == '__main__':
#     unittest.main()

#2 - Ikki klass uchun yagona test yoza olasizmi? (isInstance() funksiyasini eslang)
# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning asosiy ma'lumotlarini saqlash."""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         """Talabaning xususiyatlarini saqlash."""
#         super().__init__(ism, familiya, passport, tyil)  # Shaxs konstruktorini chaqirish
#         self.idraqam = idraqam
#         self.bosqich = 1
    
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich

# Eslatma! Ikkala klass uchun test dasturini keyinchalik yozamiz.

# 35 - DARS TUGADI.