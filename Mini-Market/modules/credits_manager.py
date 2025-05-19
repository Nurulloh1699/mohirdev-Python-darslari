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
from decimal import Decimal

DEFAULT_DEBT_LIMIT = Decimal("100000")  # float emas, Decimal str ko‘rinishda

# 1. Mijozning qarz chegarasini tekshirish
def check_customer_debt_limit(customer_id, new_amount):
    query = "SELECT current_debt FROM customers WHERE id = %s"
    customer = fetch_one(query, (customer_id,))
    
    if not customer:
        print("❌ Mijoz topilmadi.")
        return False

    current = customer["current_debt"]
    
    if (current + new_amount) <= DEFAULT_DEBT_LIMIT:
        return True
    else:
        print(f"⚠️ Qarz limiti oshadi: {current + new_amount} > {DEFAULT_DEBT_LIMIT}")
        return False



# 2. Mijozga yangi qarz yozish
def register_customer_credit(customer_id, sale_id, amount, user_id, days_due=30):
    today = date.today()
    due_date = today + timedelta(days=days_due)

    query = """
        INSERT INTO credits (customer_id, sale_id, amount, date_taken, date_due, user_id, status)
        VALUES (%s, %s, %s, %s, %s, %s, 'unpaid')
    """
    execute_query(query, (customer_id, sale_id, amount, today, due_date, user_id))

    # 2. mijozning qarz holatini yangilash
    update_query = "UPDATE customers SET current_debt = current_debt + %s WHERE id = %s"
    return execute_query(update_query, (amount, customer_id))


# 3. Mijozning barcha to‘lanmagan qarzlarini olish
def get_customer_credits(customer_id):
    query = """
        SELECT 
            c.customer_id,
            SUM(c.amount - c.paid_amount) AS remaining_debt,
            MIN(s.sale_date) AS first_date,
            MAX(c.date_due) AS last_due
        FROM credits c
        JOIN sales s ON c.sale_id = s.id
        WHERE c.customer_id = %s AND (c.amount - c.paid_amount) > 0
        GROUP BY c.customer_id
    """
    return fetch_all(query, (customer_id,))


# 4. Qarzni to‘lash
def pay_credit(credit_id, amount, customer_id):
    # 1. Avval kredit miqdorini olamiz
    existing = fetch_one("SELECT amount FROM credits WHERE id = %s", (credit_id,))
    if not existing:
        print("❌ Kredit topilmadi.")
        return

    total_amount = existing["amount"]

    # 2. Agar to‘lov to‘liq bo‘lsa — status = 'paid'
    if float(amount) >= float(total_amount):
        update_query = "UPDATE credits SET status = 'paid' WHERE id = %s"
        execute_query(update_query, (credit_id,))
        print("✅ Kredit to‘liq yopildi.")
    else:
        print(f"ℹ️ Qisman to‘landi: {amount}/{total_amount} so‘m")

    # 3. Mijozning qarzini kamaytiramiz
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

def ensure_customer_exists(customer_id):
    existing = fetch_one("SELECT id FROM customers WHERE id = %s", (customer_id,))
    if not existing:
        query = """
            INSERT INTO customers (id, full_name, debt_limit, current_debt)
            VALUES (%s, %s, %s, %s)
        """
        execute_query(query, (customer_id, f"Mijoz {customer_id}", 100000, 0))
        
def handle_payment(self, credit_id, amount_due, customer_id):
    from PyQt5.QtWidgets import QInputDialog, QMessageBox
    from modules.credits_manager import pay_credit

    amount, ok = QInputDialog.getDouble(
        self,
        "To‘lov",
        f"Qarzdorlik: {amount_due} so‘m\nTo‘lanayotgan summa:",
        decimals=2
    )

    if not ok or amount <= 0:
        return

    if amount > amount_due:
        QMessageBox.warning(self, "Xatolik", "Qarzdorlikdan ortiq to‘lov kiritildi.")
        return

    pay_credit(credit_id, amount, customer_id)
    QMessageBox.information(self, "✅ To‘lov", f"{amount} so‘m so‘ndirildi.")
    self.search_credits()  # Jadvalni yangilash

def get_customer_credits_raw(customer_id):
    query = """
        SELECT id AS credit_id, amount, paid_amount
        FROM credits
        WHERE customer_id = %s AND (amount - paid_amount) > 0
        ORDER BY date_due ASC
    """
    return fetch_all(query, (customer_id,))




