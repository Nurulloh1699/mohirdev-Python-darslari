# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 01:30:41 2025

@author: DavrServis
"""

import unittest
from shaxs import Shaxs  # Shaxs klassini import qilamiz

class TestShaxs(unittest.TestCase):
    """Shaxs klassining metodlarini test qilish uchun sinf."""
    
    def setUp(self):
        """Har bir testdan oldin bajariladigan metod."""
        # Test uchun Shaxs obyektini yaratamiz
        self.shaxs1 = Shaxs("Ali", "Valiyev", "AB1234567", 1990)
    
    def test_get_info(self):
        """get_info metodini test qilish."""
        # Kutilgan natija
        expected_info = "Ali Valiyev. Passport:AB1234567, 1990-yilda tug`ilgan"
        # get_info metodi natijasini tekshiramiz
        self.assertEqual(self.shaxs1.get_info(), expected_info)
        # Izoh: get_info metodi to'g'ri natija qaytarsa, test muvaffaqiyatli o'tadi.
    
    def test_get_age(self):
        """get_age metodini test qilish."""
        # 2025 yilda Shaxsning yoshini tekshiramiz
        expected_age = 2025 - 1990  # 35 yosh
        self.assertEqual(self.shaxs1.get_age(2025), expected_age)
        # Izoh: get_age metodi kutilgan yoshni qaytarsa, test muvaffaqiyatli o'tadi.

if __name__ == '__main__':
    unittest.main()
    