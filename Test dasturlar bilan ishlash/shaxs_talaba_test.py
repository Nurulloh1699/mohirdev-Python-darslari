# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 02:07:54 2025

@author: DavrServis
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning asosiy ma'lumotlarini saqlash."""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlarini saqlash."""
        super().__init__(ism, familiya, passport, tyil)  # Shaxs konstruktorini chaqirish
        self.idraqam = idraqam
        self.bosqich = 1
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

# Test fayli
import unittest
from shaxs import Shaxs
from talaba import Talaba

class TestShaxsVaTalaba(unittest.TestCase):
    """Shaxs va Talaba klasslarini test qilish uchun sinf."""
    
    def setUp(self):
        """Testdan oldin ishlatiladigan obyektlarni yaratish."""
        self.shaxs1 = Shaxs("Ali", "Valiyev", "AB1234567", 1990)
        self.talaba1 = Talaba("Vali", "Aliyev", "CD7894561", 2000, "T123456")
    
    def test_shaxs_metodlari(self):
        """Shaxs klassining metodlarini test qilish."""
        # get_info metodini test qilish
        expected_info = "Ali Valiyev. Passport:AB1234567, 1990-yilda tug`ilgan"
        self.assertEqual(self.shaxs1.get_info(), expected_info)
        
        # get_age metodini test qilish
        self.assertEqual(self.shaxs1.get_age(2025), 35)
    
    def test_talaba_metodlari(self):
        """Talaba klassining metodlarini test qilish."""
        # get_id metodini test qilish
        self.assertEqual(self.talaba1.get_id(), "T123456")
        
        # get_bosqich metodini test qilish
        self.assertEqual(self.talaba1.get_bosqich(), 1)
    
    def test_isinstance(self):
        """Obyektlarning klasslarga tegishliligini tekshirish."""
        # shaxs1 Shaxs klassiga tegishli
        self.assertTrue(isinstance(self.shaxs1, Shaxs))
        
        # talaba1 ham Shaxsdan meros olgan
        self.assertTrue(isinstance(self.talaba1, Shaxs))
        
        # talaba1 Talaba klassiga tegishli
        self.assertTrue(isinstance(self.talaba1, Talaba))
        
        # shaxs1 Talaba klassiga tegishli emas
        self.assertFalse(isinstance(self.shaxs1, Talaba))
    
    def test_miras_tekshirish(self):
        """Talaba klassi Shaxs klassidan meros olganligini tekshirish."""
        self.assertTrue(issubclass(Talaba, Shaxs))  # Talaba Shaxsdan meros olgan bo'lishi kerak

if __name__ == '__main__':
    unittest.main()




