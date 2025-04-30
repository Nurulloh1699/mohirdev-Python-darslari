# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:34:19 2025

@author: DavrServis
"""

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
        
import unittest
from cars import Car

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test dastur!"""
    def setUp(self):
        make = 'GM'
        self.model = 'Malibu'
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make, self.model, year)
        self.avto2 = Car(make, self.model, year, price = self.price)
        
    def test_create(self):
        # Qiymatlar mavjudligini ssertIsNotNone metodi orqali tekshiramiz:
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertEqual(self.model, self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymatlar mavjud emasligini assertIsNone metodi orqali tekshiramiz:
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEqual metodi orqali tekshiramiz:
        self.assertEqual(0, self.avto1.get_km())
        # avto2 narhini tekshiramiz:
        self.assertEqual(self.price, self.avto2.price) 
        
    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.price)
    
    def test_add_km(self):
        #1 Musbat qiymat berib ko'ramiz:
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km()) # Bu o'rinda biz yana bir narsani tekshirishimiz mumkin (kerak), yuqorida dasturchi 
# km qo'shishda + belgisini esdan chiqargan bo'lishi mumkin agar shunday bo'lsa bizning dastur xato ishlashi mumkin yani shunchaki ohirigi 
# berilgan km ga tenglab qo'yishi mumkin.
        self.avto1.add_km(5000)
        self.assertEqual(15000, self.avto1.get_km()) # + belgisi bo'lmagan holatda xato beradi yani km ni 5000 ga tenglab qo'ya qoladi.
        #2 Manfiy qiymat berib ko'ramiz:
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)

unittest.main()

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