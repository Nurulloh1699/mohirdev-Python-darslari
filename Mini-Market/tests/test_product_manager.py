# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 11:35:19 2025

@author: DavrServis
"""

"""
test_product_manager.py

Mahsulotlar moduli (product_manager.py) funksiyalarini test qilish:
- Yangi mahsulot qo‘shish
- Barcode orqali topish
- Zaxirani yangilash
- Amal muddati yaqin mahsulotlarni aniqlash
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.product_manager import (
    register_new_product,
    update_stock,
    get_product_by_barcode,
    check_expiry_dates
)

# Global test barcode (har testda unique bo‘ladi)
test_barcode = "TEST" + datetime.now().strftime("%H%M%S")


def test_register_new_product():
    print("📦 Yangi mahsulot qo‘shilmoqda...")

    new_id = register_new_product(
        barcode=test_barcode,
        name="Pepsi 1L",
        category_id=1,          # ⚠️ Kategoriya mavjud bo‘lishi kerak
        supplier_id=1,          # ⚠️ Yetkazib beruvchi mavjud bo‘lishi kerak
        purchase_price=5000,
        profit_type="percent",  # yoki 'fixed'
        profit_value=20,
        expiry_date="2025-04-10",
        is_returnable=False
    )

    print(f"✅ Yaratilgan mahsulot ID: {new_id}")


def test_get_product_by_barcode():
    print("🔍 Barcode bo‘yicha mahsulot qidirilmoqda...")
    product = get_product_by_barcode(test_barcode)
    print("📄 Mahsulot ma'lumotlari:", product)


def test_update_stock():
    print("📦 Ombor zaxirasi yangilanmoqda...")
    success = update_stock(test_barcode, 10)
    print("✅ Yangilanish natijasi:", success)


def test_check_expiry():
    print("⏰ Muddati yaqinlashgan mahsulotlar:")
    products = check_expiry_dates()
    for p in products:
        print(p)


if __name__ == "__main__":
    print("=== PRODUCT MANAGER TEST BOSHLANDI ===")
    test_register_new_product()
    test_get_product_by_barcode()
    test_update_stock()
    test_check_expiry()
    print("=== TEST TUGADI ===")
