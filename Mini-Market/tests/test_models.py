# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 09:46:55 2025

@author: DavrServis
"""

# tests/test_models.py

import sys
import os
sys.path.append(os.path.abspath(".."))

import unittest
from datetime import date
from models import Product, Customer, User, SaleItem

class TestModels(unittest.TestCase):
    def test_product_creation(self):
        print("\n🧪 Mahsulot obyektini yaratish testi: Product")
        product = Product(
            id=None,
            nomi="Pepsi 1L",
            barcode="1234567890123",
            narx=7000.0,
            miqdor=50.0,
            amal_muddati=date(2025, 12, 31),
            kategoriya="Ichimliklar",
            foyda_turi="foiz",
            foyda_miqdori=10.0,
            o_lov_birligi="litr"
        )
        self.assertEqual(product.nomi, "Pepsi 1L")

    def test_customer_creation(self):
        print("\n🧪 Mijoz obyektini yaratish testi: Customer")
        customer = Customer(id=1, ism="Ali Valiyev", id_karta="AB1234567", telefon="998901234567")
        self.assertEqual(customer.ism, "Ali Valiyev")

    def test_user_creation(self):
        print("\n🧪 Foydalanuvchi obyektini yaratish testi: User")
        user = User(id=1, username="admin", parol="admin123", rol="admin")
        self.assertEqual(user.username, "admin")

    def test_sale_item_total(self):
        print("\n🧪 Savatdagi mahsulot umumiy summasi: SaleItem.jami")
        item = SaleItem(product_id=1, nomi="Shakar", miqdor=3.5, narx=8000.0)
        self.assertEqual(item.jami, 28000.0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
