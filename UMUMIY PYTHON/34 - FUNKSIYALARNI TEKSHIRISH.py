# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:49:35 2025

@author: DavrServis
"""

# 34 - DARS.
# FUNKSIYALARNI TEKSHIRISH.

# Bu dars orqali biz dasturimizni tekshirishni o'rganishni davom etamiz. Biz dasturimiz davomida
# turli hil finksiyalar va obyektlar yaratishimiz tabiiy va albatta o'z-o'zidan yozgan ko'dimizni 
# joyidayoq tekshirib ketishimiz kerak bo'ladi.

# Bu darsda biz qanday qilib bu tekshirishlarni avtomatlashtirishni o'rganamiz.

# Oddiy funksiyani tekshirishdan boshlaymiz:
# def get_full_name(ism, familiya):
#     return f"{ism} {familiya}".title()

# print(get_full_name('alijon', 'valiyev'))
# Natija: Alijon Valiyev
# Yuqoridagi kod ishladi va xatolarsiz

# Biz endi funksiyalarni UNITTEST orqali test qilishni boshlaymiz.
# Aslida quyida keltirilgan misollar alohida modullarda bajariladi lekin misol sifatida
# darsimizda yozib qo'yamiz.

# Deylik bu yerda xatolik bo'ldi va biz kutgan natija chiqmadi. Etibor bersangiz biz funksiyani 
# qo'lda tekshiryapmiz, lekin odatda Pythonda buni avtomatlashtirish mumkin va dastur o'zini-o'zi
# tekshiradigan qilib dastur yozishimiz mumkin.

# Bunday amalni amalga oshirish uchun Pythonda UNITTEST degan modul mavjud. Bu modul orqali biz 
# dasturimiz ustida bir nechta testlarni amalga oshirishimiz mumkin, agar bitta test amalga
# oshirsak, bu TEST CASE dev ataladi.

# Endi biz o'zimizga kerakli bo'lgan funksiyalarni alohida modulda saqlaymiz.

# name_test.py modulida yozilgan kodlar.
# import unittest # Bu qism ham standart shablon desak bo'ladi.
# from name import get_full_name # Bu qism test qilinayotkan obyektga qarab o'zgaradi.

# class NameTest(unittest.TestCase): # Test qilish uchun qo'llaniladigan standart shablon.
# Endi biz bu yerda etiboe beradigan narsamiz oddiy class ning ichida yozilgan metodlar funksiyani
# test qilish uchun yozilgani uchun ularni nomini boshiga test so'zini qo'shib ketamiz. Bu bizga 
# test dasturimizni bajarganimizda qo'l keladi va Python ham avval test so'zi bilan yozilgan 
# dasturlarni qidiradi va birma-bir bajarib chiqadi.
#     def test_toliq_ism(self): # To'liq ismni test qiluvchi metod.
#         name = get_full_name('nurulloh', 'abdurashidov') # Funksiyadan qiymat olyapmiz.
#         self.assertEqual(name, 'Nurulloh Abdurashidov') # Qiymat biz kiritgan qiymatga mos bo'lsa.
        
# unittest.main() # Tekshirish uchun yozilgan kod.
# Natija: Ran 1 test in 0.001s

        # OK
        
# Endi vaqt o'toshi bilan bizning funksiyamiz o'zgardi.
# def get_full_name(ism, otasi, familiya):  # Tartib: ism, otasi, familiya
#     return f"{ism} {otasi} {familiya}".title()

# print(get_full_name('alijon', 'olimovich', 'valiyev'))

# Test funksiyamizni o'zgartirganimiz yo'q. Agar endi tekshirsak quyidagicha javob olamiz:
# Natija: Ran 1 test in 0.002s

        # FAILED (errors=1)
# Ko'rib turganingizdek xato kelib chiqti.

# Nima qilishimiz mumkin? Bu xatoni to'g'irlash uchun biz full_name funksiyamizga o'zgartirish
# kiritamiz:
# def get_full_name(ism, familiya, otasi = ''):
#     if otasi:
#         return f"{ism} {otasi} {familiya}".title()
#     else:
#         return f"{ism} {otasi} {familiya}".title()
    
# Natija: Ran 1 test in 0.001s

        # OK

# Endi kodimiz yana testdan o'tdi.

# Bu holatda funksiyamiz qo'shimcha qiymat qo'shib qo'qganimiz uchun, testimizga ham qo'shimcha 
# qilishimiz kerak.
# def test_otasining_ismi(self):
#     name = get_full_name('nurulloh', 'abdurashidov', "yorqinjon o'g'li")
#     self.assertEqual(name, 'Nurulloh', 'Abdurashidov', "Yorqinjon o'g'li")
    
# Endi tekshirib ko'rsak.
# Natija: Ran 2 tests in 0.002s

        # FAILED (errors=1)
        
# Ikki marta test qilindi va bittasi xato deyapti.

# Xatoni to'g'irladik.
# Natija: Ran 2 tests in 0.003s

        # OK
# Endi hammasi joyida.

# Biz yuqorida matnlar bilan ishladik endi sonlar va raqamlar bilan ishlab ko'ramiz.
# def getArea(r, pi = 3.14159):
#     """Doiraning yuzini qaytaruvchi funksiya"""
#     return pi*(r**2)

# def getPerimeter(r, pi = 3.14159):
#     """Doiraning perometrini qaytaruvchi dastur"""
#     return 2 * pi * r
# Endi bu funksiyalarni test qilib ko'ramiz va buni yangi test moduli orqali qilamiz:
# import unittest
# from circle import getArea, getPerimeter

# class CircleTest(unittest.TestCase):
#     def test_area(self):
#         self.assertEqual(getArea(5), 78.53975)
#         self.assertEqual(getArea(10), 314.159)
        
# unittest.main()

# Aslida yuqorida matematik yechimlar uchun assertEqual tengligini ishlatishimiz noto'g'ri,
# chunki, nuqta verguligacha aniq natijalar olishimiz kam uchraydi va aynan shuning uchun 
# assertAlmostEquel tengligini ishlatganimiz maqsadga muvofiq bo'ladi Almost so'zining tarjimasi
# deyarli degan manoni beradi. Bu tenglik orqali butun son va undan keyin nuqta va nuqtadan 
# keyingi 7ta songacha tekshiradi agar hohlasak uzunlikni o'zimiz berishimiz ham mumkin.

# Shu tarzda endi biz Perimetrni ham tekshiramiz:

# Agar funksiya mantiqiy qiymat qaytarsa, bunday funksiyalarni assertTrue() va assertFalse() metodlari yordamida tekshirishimiz mumkin. 

# Quyidagi funksiyamiz kiritilgan son tub yoki yo'q ekanini tekshiradi:

# def tubSonmi(n):
#     if n==2 or n==3: return True
#     if n%2==0 or n<2: return False
#     for i in range(3, int(n**0.5)+1, 2):   # faqat toq sonlarni tekshiramiz
#         if n%i==0:
#             return False   
#     return True
# Funksiyani alohida tubSonmi.py fayliga saqlaymiz. Funksiyani tekshirish uchun tubSon_test.py dasturini yozamiz:

# import unittest
# from tubSonmi import tubSonmi

# class tubSonTest(unittest.TestCase):
#     def test_true(self):
#         self.assertTrue(tubSonmi(7))
#         self.assertTrue(tubSonmi(193))
#         self.assertTrue(tubSonmi(547))
#     def test_false(self):
#         self.assertFalse(tubSonmi(6))
#         self.assertFalse(tubSonmi(265))
#         self.assertFalse(tubSonmi(489))
        
# unittest.main()
# Test davomida tubSonmi() funksiyasini bir nechta tub (7, 193, 547) va tub bo'lmagan (6, 265, 489) sonlar bilan chaqirdik. Bunda assertTrue() metodi funksiyamiz haqiqatdan ham True qiymatini qaytarishini, assertFalse() metodi esa funksiyamiz False qiymat qaytarishini tekshiradi.

# TAQQOSLASH METODLARI
# TestCase klassi tarkibidagi boshqa taqqoslash metodlari ham mavjud:

# Metod
# Nimani taqqoslaydi?

# assertEqual(a, b) -> a == b

# assertNotEqual(a, b) -> a != b

# assertTrue(x) -> x ning qiymati True

# assertFalse(x) -> x ning qiymati False

# assertIs(a, b) -> a bu b

# assertIsNot(a, b) -> a bu b emas

# assertIsNone(x) -> x ning qiymati None

# assertIsNotNone(x) -> x ning qiymati None emas

# assertIn(a, b) -> a b ning ichida

# assertNotIn(a, b) -> a b ning ichida emas

# assertIsInstance(a, b) -> a b ning vorisi

# assertNotIsInstance(a, b) -> a b ning vorisi emas

# AMALIYOT TOPSHIRIQLARI:
#1 - Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya.
# def find_max(a, b, c):
#     return max(a, b, c)

# print(find_max(10, 20, 21))
# # Natija: 21

# # Test dasturi:
# class TestFindMax(unittest.TestCase):
#     def test_find_max(self):
#         self.assertEqual(find_max(10, 20, 15), 20)
#         self.assertEqual(find_max(5, 3, 8), 8)
#         self.assertEqual(find_max(-10, -5, -7), -5)


# unittest.main()

# #2 - Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta
# # harfga o'zgatiruvchi funksiya
# def capitalize_first_letters(strings):
#     capitalized_list = []
#     for string in strings:
#         capitalized_list.append(string.capitalize())
#     return capitalized_list
# texts = ['olma', 'shaftoli', 'banan']
# result = capitalize_first_letters(texts)
# print(result)
# # Natija: ['Olma', 'Shaftoli', 'Banan']

# # Test dasturi:
# class TestCapitalizeFirstLetters(unittest.TestCase):
#     def test_capitalize_first_letters(self):
#         self.assertEqual(capitalize_first_letters(['salom', 'dunyo']), ['Salom', 'Dunyo'])
#         self.assertEqual(capitalize_first_letters(['python', 'dasturlash']), ['Python', 'Dasturlash'])
#         self.assertEqual(capitalize_first_letters([]), [])


# unittest.main()

# #3 - Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya.
# def filter_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]   

# nums = [1,2,3,4,5,6,7,8,9]
# result = filter_even_numbers(nums)
# print(result)
# # Natija: [2, 4, 6, 8]

# # Test dasturi:
# class TestFilterEvenNumbers(unittest.TestCase):
#     def test_filter_even_numbers(self):
#         self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
#         self.assertEqual(filter_even_numbers([10, 11, 12, 13]), [10, 12])
#         self.assertEqual(filter_even_numbers([1, 3, 5]), [])
    
# unittest.main()

# #4 - Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) qaytaruvchi
# # funksiya yozing.
# import math
# def is_fibonachi(n):
#     def is_perfect_square(x):
#         s = int(math.sqrt(x))
#         return s * s == x
    
#     return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# print(is_fibonachi(21))
# # Natija: True

# # Test dasturi:
# import unittest

# class TestFibonachi(unittes.TestCase):
#     def test_is_fibonachi(self):
#         self.assertTrue(is_fibonachi(8))
#         self.assertTrue(is_fibonachi(13))
#         self.assertTrue(is_fibonachi(15))
    
# unittest.main()

# 34 - DARS TUGADI.