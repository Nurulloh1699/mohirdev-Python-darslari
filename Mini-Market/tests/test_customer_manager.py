# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 00:01:03 2025

@author: DavrServis
"""

"""
test_customer_manager.py

customer_manager modulini test qilish:
- mijoz qo‘shish
- qidirish
- yangilash
- o‘chirish
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.customer_manager import (
    add_customer,
    get_customer_by_id,
    get_customer_by_card_number,
    update_customer_info,
    delete_customer
)


def test_add_customer():
    print("➕ Yangi mijoz qo‘shilmoqda...")
    unique_card = "BB" + datetime.now().strftime("%H%M%S")  # dinamik ID raqam
    new_id = add_customer(
        full_name="Ali Karimov",
        id_card_number=unique_card,
        phone="+998991234567",
        address="Farg‘ona",
        debt_limit=50000
    )
    print("✅ Mijoz ID:", new_id)
    return new_id, unique_card


def test_get_customer_by_id(customer_id):
    print("🔍 ID orqali mijoz qidirilmoqda...")
    result = get_customer_by_id(customer_id)
    print("🧾 Mijoz:", result)


def test_get_customer_by_card(card_number):
    print("🔍 ID karta raqami orqali mijoz qidirilmoqda...")
    result = get_customer_by_card_number(card_number)
    print("🧾 Mijoz:", result)


def test_update_customer(customer_id):
    print("✏️ Mijoz ma’lumotlari yangilanmoqda...")
    success = update_customer_info(
        customer_id,
        full_name="Ali K. (yangilangan)",
        phone="+998991112233",
        address="Yangilangan manzil",
        debt_limit=80000
    )
    print("✅ Yangilandi:", success)


def test_delete_customer(customer_id):
    print("❌ Mijoz o‘chirilmoqda...")
    success = delete_customer(customer_id)
    print("✅ O‘chirish natijasi:", success)


if __name__ == "__main__":
    print("=== CUSTOMER MANAGER TEST BOSHLANDI ===")
    customer_id, card_number = test_add_customer()
    test_get_customer_by_id(customer_id)
    test_get_customer_by_card(card_number)
    test_update_customer(customer_id)
    test_get_customer_by_id(customer_id)
    # test_delete_customer(customer_id)  # faqat sinovdan so‘ng faollashtiring
    print("=== TEST TUGADI ===")
