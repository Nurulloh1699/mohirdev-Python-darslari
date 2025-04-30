# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 18:14:21 2025

@author: DavrServis
"""

"""
test_credits_manager.py

credits_manager.py modulini test qilish: qarz yozish, tekshirish, olish, to‘lash.
"""

import sys
import os

# modules papkasini import yo‘liga qo‘shamiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.credits_manager import (
    check_customer_debt_limit,
    register_customer_credit,
    get_customer_credits,
    pay_credit,
    get_all_pending_credits
)

def test_debt_limit_check():
    print("🔎 Qarz limiti tekshirilyapti...")
    result = check_customer_debt_limit(customer_id=1, new_amount=50000)
    print("✅ Chegara ruxsat etadimi?", result)

def test_register_credit():
    print("📝 Qarz yozilmoqda...")
    result = register_customer_credit(
        customer_id=1,
        sale_id=6,
        amount=30000,
        days_due=10
    )
    print("✅ Qarz yozish natijasi:", result)

def test_get_customer_credits():
    print("📋 Mijozning qarzlari:")
    credits = get_customer_credits(customer_id=1)
    for c in credits:
        print(c)

def test_all_pending_credits():
    print("🧾 Barcha to‘lanmagan qarzlar:")
    all_credits = get_all_pending_credits()
    for c in all_credits:
        print(c)

def test_pay_credit():
    print("💸 Qarzni to‘lash testi...")

    credit_id = 3       # mavjud ID bo'lishi kerak
    amount = 30000
    customer_id = 1

    result = pay_credit(credit_id, amount, customer_id)
    print("✅ Qarzni to‘lash natijasi:", result)

if __name__ == "__main__":
    print("=== CREDIT MANAGER TEST BOSHLANDI ===")
    test_debt_limit_check()
    test_register_credit()
    test_get_customer_credits()
    test_all_pending_credits()
    test_pay_credit()
    print("=== TEST TUGADI ===")
