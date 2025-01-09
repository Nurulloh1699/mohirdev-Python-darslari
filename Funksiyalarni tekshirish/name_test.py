# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:01:45 2025

@author: DavrServis
"""

import unittest
from name import get_full_name

class NameTest(unittest.TestCase): 
    def test_toliq_ism(self): # To'liq ismni test qiluvchi metod.
        name = get_full_name('nurulloh', 'abdurashidov') # Funksiyadan qiymat olyapmiz.
        self.assertEqual(name, 'Nurulloh Abdurashidov') # Qiymat biz kiritgan qiymatga mos bo'lsa.
        
    def test_otasining_ismi(self):
        name = get_full_name('nurulloh', 'abdurashidov', "yorqinjonovich")
        self.assertEqual(name, 'Nurulloh Yorqinjonovich Abdurashidov')
        
unittest.main() # Tekshirish uchun yozilgan kod.
# Natija: Ran 1 test in 0.001s

        # OK
        