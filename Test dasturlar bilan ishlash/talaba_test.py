# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 02:03:03 2025

@author: DavrServis
"""

import unittest
from shaxs import Shaxs  # Shaxs klassini import qilamiz
from talaba import Talaba  # Talaba klassini import qilamiz

class TestTalaba(unittest.TestCase):
    """Talaba klassining metodlarini test qilish uchun sinf."""
    
    def setUp(self):
        """Har bir testdan oldin bajariladigan metod."""
        # Test uchun Talaba obyektini yaratamiz
        self.talaba1 = Talaba("Ali", "Valiyev", "AB1234567", 2000, "T123456")
    
    def test_get_id(self):
        """get_id metodini test qilish."""
        # Kutilgan ID raqam
        expected_id = "T123456"
        # get_id metodi natijasini tekshiramiz
        self.assertEqual(self.talaba1.get_id(), expected_id)
        # Izoh: get_id metodi to'g'ri ID raqamni qaytarsa, test muvaffaqiyatli o'tadi.
    
    def test_get_bosqich(self):
        """get_bosqich metodini test qilish."""
        # Kutilgan bosqich
        expected_bosqich = 1
        # get_bosqich metodi natijasini tekshiramiz
        self.assertEqual(self.talaba1.get_bosqich(), expected_bosqich)
        # Izoh: get_bosqich metodi to'g'ri bosqichni qaytarsa, test muvaffaqiyatli o'tadi.
    
    def test_inheritance(self):
        """Shaxs klassidan meros olishni test qilish."""
        # Talaba obyektining Shaxs klassiga tegishli metodlarini tekshiramiz
        self.assertEqual(self.talaba1.get_info(), "Ali Valiyev. Passport:AB1234567, 2000-yilda tug`ilgan")
        # Izoh: get_info metodi Shaxs klassidan meros bo'lib o'tganini tasdiqlaydi.
        self.assertEqual(self.talaba1.get_age(2025), 25)
        # Izoh: get_age metodi Talaba obyektida ham to'g'ri ishlaydi.

if __name__ == '__main__':
    unittest.main()
