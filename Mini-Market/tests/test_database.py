# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 23:01:36 2025

@author: DavrServis
"""

"""
test_database.py

Ushbu fayl data_base/database.py modulini test qilish uchun yozilgan.
Jadvalga ma’lumot qo‘shish, o‘qish funksiyalari ishlayaptimi — tekshiriladi.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_base.database import fetch_all, fetch_one, execute_query, execute_returning_id
from datetime import datetime


def test_insert_category():
    query = "INSERT INTO categories (category_name, description) VALUES (%s, %s) RETURNING id"
    params = ("Ichimliklar", "Sovuq va issiq ichimliklar")
    new_id = execute_returning_id(query, params)
    print("✅ Yangi kategoriya ID:", new_id)


def test_select_categories():
    query = "SELECT * FROM categories"
    results = fetch_all(query)
    print("📋 Kategoriyalar ro'yxati:")
    for row in results:
        print(row)


def test_fetch_one_category():
    query = "SELECT * FROM categories WHERE category_name = %s"
    result = fetch_one(query, ("Ichimliklar",))
    print("🔍 Bitta kategoriya:", result)


def test_insert_supplier():
    query = "INSERT INTO suppliers (name, phone, address) VALUES (%s, %s, %s) RETURNING id"
    params = ("Pepsi Uzbekistan", "+998901234567", "Toshkent")
    new_id = execute_returning_id(query, params)
    print("✅ Yetkazib beruvchi qo‘shildi. ID:", new_id)


def test_insert_customer():
    query = """
        INSERT INTO customers (full_name, id_card_number, phone, address, debt_limit)
        VALUES (%s, %s, %s, %s, %s) RETURNING id
    """
    params = ("Test Mijoz", "AA1234567", "+998901234567", "Toshkent", 100000)
    new_id = execute_returning_id(query, params)
    print("✅ Mijoz qo‘shildi. ID:", new_id)


def test_insert_sale():
    query = """
        INSERT INTO sales (sale_date, payment_type, customer_id, total_amount, cash_given, change, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id
    """
    params = (
        datetime.now(),  # savdo vaqti
        "debt",          # qarz asosida
        1,               # customer_id
        30000,           # total_amount
        0,               # cash_given
        0,               # change
        "success"
    )
    new_id = execute_returning_id(query, params)
    print("✅ Savdo qo‘shildi. ID:", new_id)


if __name__ == "__main__":
    print("=== DATABASE TEST BOSHLANDI ===")
    test_insert_category()
    test_insert_supplier()
    test_insert_customer()
    test_insert_sale()
    test_select_categories()
    test_fetch_one_category()
    print("=== TEST TUGADI ===")
