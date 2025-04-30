# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 09:51:20 2025

@author: DavrServis
"""

# tests/test_config.py

import sys
import os
sys.path.append(os.path.abspath(".."))

import unittest
from config import DB_CONFIG, PRINTER_NAME, USER_ROLES, SCREEN_SIZE, CURRENCY

class TestConfig(unittest.TestCase):
    def test_db_config(self):
        self.assertIsInstance(DB_CONFIG, dict)
        self.assertIn("host", DB_CONFIG)
        self.assertIn("port", DB_CONFIG)
        self.assertEqual(DB_CONFIG["port"], 5433)

    def test_printer_name(self):
        self.assertIsInstance(PRINTER_NAME, str)
        self.assertTrue(PRINTER_NAME.strip() != "")

    def test_user_roles(self):
        self.assertIn("admin", USER_ROLES)
        self.assertIn("kassir", USER_ROLES)

    def test_screen_size(self):
        self.assertEqual(SCREEN_SIZE["width"], 1024)
        self.assertTrue(SCREEN_SIZE["fullscreen"])

    def test_currency(self):
        self.assertEqual(CURRENCY, "so'm")

if __name__ == '__main__':
    unittest.main()
