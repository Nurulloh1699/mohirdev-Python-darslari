# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 23:59:31 2025

@author: DavrServis
"""

"""
customer_manager.py

Mijozlar bilan ishlash:
- Yangi mijoz qo‘shish
- ID yoki karta raqami bo‘yicha topish
- Ma'lumotlarini yangilash
- Mijozni o‘chirish
"""

from data_base.database import fetch_one, fetch_all, execute_query, execute_returning_id


# 1. Yangi mijoz qo‘shish
def add_customer(full_name, id_card_number, phone=None, address=None, debt_limit=0):
    query = """
        INSERT INTO customers (full_name, id_card_number, phone, address, debt_limit)
        VALUES (%s, %s, %s, %s, %s) RETURNING id
    """
    params = (full_name, id_card_number, phone, address, debt_limit)
    return execute_returning_id(query, params)


# 2. Mijozni ID bo‘yicha topish
def get_customer_by_id(customer_id):
    query = "SELECT * FROM customers WHERE id = %s"
    return fetch_one(query, (customer_id,))


# 3. Mijozni ID karta raqami bo‘yicha topish
def get_customer_by_card_number(card_number):
    query = "SELECT * FROM customers WHERE id_card_number = %s"
    return fetch_one(query, (card_number,))


# 4. Mijoz ma’lumotlarini yangilash
def update_customer_info(customer_id, full_name=None, phone=None, address=None, debt_limit=None):
    updates = []
    params = []

    if full_name:
        updates.append("full_name = %s")
        params.append(full_name)
    if phone:
        updates.append("phone = %s")
        params.append(phone)
    if address:
        updates.append("address = %s")
        params.append(address)
    if debt_limit is not None:
        updates.append("debt_limit = %s")
        params.append(debt_limit)

    if not updates:
        return False  # hech nima yangilanmadi

    query = f"UPDATE customers SET {', '.join(updates)} WHERE id = %s"
    params.append(customer_id)

    return execute_query(query, tuple(params))


# 5. Mijozni o‘chirish (real delete)
def delete_customer(customer_id):
    query = "DELETE FROM customers WHERE id = %s"
    return execute_query(query, (customer_id,))
