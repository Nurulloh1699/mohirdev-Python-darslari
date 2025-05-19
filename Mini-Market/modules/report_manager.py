# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 09:15:02 2025

@author: DavrServis
"""

# modules/report_manager.py

"""
Hisobot va tahlil moduli:
- Eng ko‘p sotilgan mahsulotlar
- Kunlik savdo statistikasi
- Kategoriya bo‘yicha savdo tahlili
- Qarzdor mijozlar ro‘yxati
- Foydalanuvchi bo‘yicha savdo/qarzlar
"""

from data_base.database import fetch_all, fetch_one
from datetime import date


# 1. Eng ko‘p sotilgan mahsulotlar
def get_top_selling_products(limit=5):
    query = """
        SELECT p.name, SUM(sd.quantity) AS total_sold
        FROM sales_items sd
        JOIN products p ON sd.product_id = p.id
        WHERE p.status = 'active'
        GROUP BY p.name
        ORDER BY total_sold DESC
        LIMIT %s
    """
    return fetch_all(query, (limit,))


# 2. Kunlik savdo statistikasi
def get_daily_sales_summary(sale_date: date):
    query = """
        SELECT COUNT(*) AS total_sales,
               SUM(total_amount) AS total_revenue,
               SUM(CASE WHEN payment_type = 'cash' THEN total_amount ELSE 0 END) AS cash_sales,
               SUM(CASE WHEN payment_type = 'card' THEN total_amount ELSE 0 END) AS card_sales,
               SUM(CASE WHEN payment_type = 'debt' THEN total_amount ELSE 0 END) AS debt_sales
        FROM sales
        WHERE DATE(sale_date) = %s
    """
    return fetch_one(query, (sale_date,))


# 3. Kategoriya bo‘yicha savdo tahlili
def get_sales_by_category():
    query = """
        SELECT c.category_name, SUM(sd.quantity) AS total_items_sold
        FROM sales_items sd
        JOIN products p ON sd.product_id = p.id
        JOIN categories c ON p.category_id = c.id
        WHERE p.status = 'active' AND c.status = 'active'
        GROUP BY c.category_name
        ORDER BY total_items_sold DESC
    """
    return fetch_all(query)


# 4. Qarzdor mijozlar ro‘yxati
def get_debtors_list():
    query = """
        SELECT cu.full_name, cu.phone, cu.current_debt, cu.debt_limit
        FROM customers cu
        WHERE cu.current_debt > 0
        ORDER BY cu.current_debt DESC
    """
    return fetch_all(query)


# 5. Har bir foydalanuvchining savdo statistikasi
def get_sales_by_user():
    query = """
        SELECT u.full_name, COUNT(s.id) AS sales_count, SUM(s.total_amount) AS total_sales
        FROM sales s
        JOIN users u ON s.user_id = u.id
        GROUP BY u.full_name
        ORDER BY total_sales DESC;
    """
    return fetch_all(query)


# 6. Har bir foydalanuvchining yozgan qarzlari
def get_credits_by_user():
    query = """
        SELECT u.full_name, COUNT(c.id) AS credit_count, SUM(c.amount) AS total_credit
        FROM credits c
        JOIN users u ON c.user_id = u.id
        GROUP BY u.full_name
        ORDER BY total_credit DESC;
    """
    return fetch_all(query)


# 7. To‘lov turi bo‘yicha umumiy savdo statistikasi
def get_sales_by_payment_type():
    query = """
        SELECT payment_type, COUNT(*) AS count, SUM(total_amount) AS total
        FROM sales
        GROUP BY payment_type
        ORDER BY total DESC;
    """
    return fetch_all(query)
