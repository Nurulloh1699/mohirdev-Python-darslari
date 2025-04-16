# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 12:22:29 2025

@author: DavrServis
"""

"""
credits_manager.py

Ushbu modul mijozlarga beriladigan qarzlarni boshqaradi:
- Qarzni yozish
- Chegarani tekshirish
- To‘lanmagan qarzlarni olish
- Qarzlarni to‘lash
"""

"""
credits_manager.py

Ushbu modul mijozlarga beriladigan qarzlarni boshqaradi:
- Qarzni yozish
- Chegarani tekshirish
- To‘lanmagan qarzlarni olish
- Qarzlarni to‘lash
"""

from data_base.database import fetch_one, fetch_all, execute_query, execute_returning_id
from datetime import date, timedelta


# 1. Mijozning qarz chegarasini tekshirish
def check_customer_debt_limit(customer_id, new_amount):
    query = "SELECT debt_limit, current_debt FROM customers WHERE id = %s"
    customer = fetch_one(query, (customer_id,))
    
    if not customer:
        print("❌ Mijoz topilmadi.")
        return False

    max_limit = customer["debt_limit"]
    current = customer["current_debt"]
    
    if (current + new_amount) <= max_limit:
        return True
    else:
        print("⚠️ Qarz chegarasi oshib ketadi!")
        return False


# 2. Mijozga yangi qarz yozish
def register_customer_credit(customer_id, sale_id, amount, days_due=30):
    today = date.today()
    due_date = today + timedelta(days=days_due)

    # 1. credits jadvaliga yozish
    query = """
        INSERT INTO credits (customer_id, sale_id, amount, date_taken, date_due, status)
        VALUES (%s, %s, %s, %s, %s, 'unpaid')
    """
    execute_query(query, (customer_id, sale_id, amount, today, due_date))

    # 2. mijozning qarz holatini yangilash
    update_query = "UPDATE customers SET current_debt = current_debt + %s WHERE id = %s"
    return execute_query(update_query, (amount, customer_id))


# 3. Mijozning barcha to‘lanmagan qarzlarini olish
def get_customer_credits(customer_id):
    query = """
        SELECT c.id AS credit_id, s.id AS sale_id, s.sale_date, c.amount, c.date_due, c.status
        FROM credits c
        JOIN sales s ON c.sale_id = s.id
        WHERE c.customer_id = %s AND c.status = 'unpaid'
        ORDER BY c.date_due ASC
    """
    return fetch_all(query, (customer_id,))


# 4. Qarzni to‘lash
def pay_credit(credit_id, amount, customer_id):
    # 1. Qarzni to‘langan deb belgilaymiz
    update_query = """
        UPDATE credits
        SET status = 'paid'
        WHERE id = %s
    """
    execute_query(update_query, (credit_id,))

    # 2. Mijozning current_debt ni kamaytiramiz
    reduce_query = "UPDATE customers SET current_debt = current_debt - %s WHERE id = %s"
    return execute_query(reduce_query, (amount, customer_id))


# 5. Barcha to‘lanmagan qarzlar ro‘yxati (hisobot uchun)
def get_all_pending_credits():
    query = """
        SELECT c.id AS credit_id, c.customer_id, s.sale_date, c.amount, c.date_due
        FROM credits c
        JOIN sales s ON c.sale_id = s.id
        WHERE c.status = 'unpaid'
        ORDER BY c.date_due ASC
    """
    return fetch_all(query)
