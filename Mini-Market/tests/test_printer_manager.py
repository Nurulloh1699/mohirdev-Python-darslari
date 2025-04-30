# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 10:00:54 2025

@author: DavrServis
"""

# tests/test_printer_manager.py

import sys
import os
sys.path.append(os.path.abspath(".."))

import unittest
from unittest.mock import patch, MagicMock
from utils import printer_manager
from models import SaleItem

class TestPrinterManager(unittest.TestCase):
    def setUp(self):
        print("\n📦 SaleItem test obyektlari tayyorlanmoqda...")
        self.items = [
            SaleItem(product_id=1, nomi="Pepsi", miqdor=2, narx=7000),
            SaleItem(product_id=2, nomi="Shakar", miqdor=1.5, narx=8000)
        ]
        self.total = sum(item.jami for item in self.items)

    def test_format_receipt_output(self):
        print("🧾 format_receipt funksiyasi test qilinmoqda...")
        receipt = printer_manager.format_receipt(
            items=self.items,
            total=self.total,
            payment_type="naqd",
            bonus=1000,
            change=3000
        )
        self.assertIn("MINI-MARKET", receipt[0])
        self.assertTrue(any("Pepsi" in line for line in receipt))
        self.assertTrue(any("Jami summa" in line for line in receipt))

    @patch("utils.printer_manager.connect_printer")
    def test_print_receipt_mocked(self, mock_connect):
        print("🖨 print_receipt printerga chiqmasdan test qilinmoqda (mock)...")
        mock_printer = MagicMock()
        mock_connect.return_value = mock_printer

        printer_manager.print_receipt(
            items=self.items,
            total=self.total,
            payment_type="naqd",
            bonus=1000,
            change=3000
        )

        self.assertTrue(mock_printer.text.called)
        self.assertTrue(mock_printer.cut.called)

if __name__ == '__main__':
    unittest.main(verbosity=2)
