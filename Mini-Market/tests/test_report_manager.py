# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 09:16:47 2025

@author: DavrServis
"""
import sys
import os
sys.path.append(os.path.abspath(".."))  # Bu test fayl `tests/` ichida bo‘lsa, ildizga chiqadi


from data_base.database import fetch_all, fetch_one
from modules import report_manager
from datetime import date


def run_all_report_tests():
    print("🔍 Test: Eng ko‘p sotilgan mahsulotlar")
    top_products = report_manager.get_top_selling_products(5)
    for p in top_products:
        print(f"- {p['name']}: {p['total_sold']} dona")

    print("\n📅 Test: Bugungi savdo statistikasi")
    today = date.today()
    daily_stats = report_manager.get_daily_sales_summary(today)
    if daily_stats:
        print(f"Umumiy savdolar: {daily_stats['total_sales']} ta")
        print(f"Jami tushum: {daily_stats['total_revenue']} so'm")
        print(f"Naqd: {daily_stats['cash_sales']}, Karta: {daily_stats['card_sales']}, Qarz: {daily_stats['debt_sales']}")
    else:
        print("Bugungi kunda savdo mavjud emas.")

    print("\n📦 Test: Kategoriya bo‘yicha savdo")
    cat_sales = report_manager.get_sales_by_category()
    for cat in cat_sales:
        print(f"- {cat['category_name']}: {cat['total_items_sold']} ta")

    print("\n📋 Test: Qarzdor mijozlar")
    debtors = report_manager.get_debtors_list()
    for d in debtors:
        print(f"- {d['full_name']}: {d['current_debt']} / Limit: {d['debt_limit']}")

    print("\n👤 Test: Foydalanuvchilar bo‘yicha savdolar")
    sales_by_user = report_manager.get_sales_by_user()
    for u in sales_by_user:
        print(f"- {u['full_name']}: {u['sales_count']} ta, {u['total_sales']} so'm")

    print("\n💳 Test: Foydalanuvchilar bo‘yicha qarzlar")
    credits_by_user = report_manager.get_credits_by_user()
    for u in credits_by_user:
        print(f"- {u['full_name']}: {u['credit_count']} ta, {u['total_credit']} so'm")

    print("\n💰 Test: To‘lov turlari bo‘yicha savdo")
    payments = report_manager.get_sales_by_payment_type()
    for p in payments:
        print(f"- {p['payment_type']}: {p['count']} ta, {p['total']} so'm")


if __name__ == "__main__":
    run_all_report_tests()
