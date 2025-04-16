# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 09:16:47 2025

@author: DavrServis
"""

"""
test_report_manager.py

report_manager modulidagi hisobot funksiyalarini test qilish:
- Eng ko‘p sotilgan mahsulotlar
- Kunlik savdo statistikasi
- Kategoriya bo‘yicha savdo
- Qarzdor mijozlar ro‘yxati
"""

import sys
import os
from datetime import date

# Bazaviy loyihani sys.path ga qo‘shamiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.report_manager import (
    get_top_selling_products,
    get_daily_sales_summary,
    get_sales_by_category,
    get_debtors_list
)


def test_top_selling_products():
    print("🔥 Eng ko‘p sotilgan mahsulotlar:")
    results = get_top_selling_products(5)
    for row in results:
        print(f"📦 {row['name']} - {row['total_sold']} dona")


def test_daily_sales_summary():
    print("📆 Kunlik savdo statistikasi:")
    today = date.today()
    results = get_daily_sales_summary(today)
    for row in results:
        print(f"🔹 Savdolar soni: {row['total_sales']}")
        print(f"💵 Umumiy tushum: {row['total_revenue']}")
        print(f"🪙 Naqd: {row['cash_sales']} | 💳 Karta: {row['card_sales']} | 🧾 Qarz: {row['debt_sales']}")


def test_sales_by_category():
    print("📊 Kategoriya bo‘yicha savdo:")
    results = get_sales_by_category()
    for row in results:
        print(f"📁 {row['category_name']} - {row['total_items_sold']} dona")


def test_debtors_list():
    print("💸 Qarzdor mijozlar:")
    results = get_debtors_list()
    for row in results:
        print(f"👤 {row['full_name']} | 📞 {row['phone']} | Qarz: {row['current_debt']} / Limit: {row['debt_limit']}")


if __name__ == "__main__":
    print("=== REPORT MANAGER TEST BOSHLANDI ===\n")
    test_top_selling_products()
    print()
    test_daily_sales_summary()
    print()
    test_sales_by_category()
    print()
    test_debtors_list()
    print("\n=== TEST TUGADI ===")
