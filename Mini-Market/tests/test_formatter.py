# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 09:54:56 2025

@author: DavrServis
"""

# tests/test_formatter.py

import sys
import os
sys.path.append(os.path.abspath(".."))

import unittest
from datetime import date
from utils.formatter import (
    format_currency, format_date, parse_date,
    is_empty, clean_whitespace
)

class TestFormatter(unittest.TestCase):

    def test_format_currency(self):
        print("\n➡️  Narx formatlash testi: format_currency")
        self.assertEqual(format_currency(12000), "12 000 so'm")
        self.assertEqual(format_currency(5000000), "5 000 000 so'm")

    def test_format_date(self):
        print("\n➡️  Sana formatlash testi: format_date")
        d = date(2025, 4, 12)
        self.assertEqual(format_date(d), "12.04.2025")

    def test_parse_date(self):
        print("\n➡️  Sana matndan date ga: parse_date")
        date_str = "01.01.2024"
        expected = date(2024, 1, 1)
        self.assertEqual(parse_date(date_str), expected)

    def test_is_empty(self):
        print("\n➡️  Bo‘sh stringni tekshirish: is_empty")
        self.assertTrue(is_empty(""))
        self.assertTrue(is_empty("   "))
        self.assertFalse(is_empty("text"))

    def test_clean_whitespace(self):
        print("\n➡️  Bo‘sh joylarni tozalash: clean_whitespace")
        messy = "   salom     dunyo  "
        cleaned = "salom dunyo"
        self.assertEqual(clean_whitespace(messy), cleaned)

if __name__ == '__main__':
    unittest.main(verbosity=2)
