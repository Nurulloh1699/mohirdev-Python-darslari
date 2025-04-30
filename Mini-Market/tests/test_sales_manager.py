# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 11:57:01 2025

@author: DavrServis
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.sales_manager import (
    start_sale,
    scan_item,
    finalize_sale,
    calculate_change,
    get_sale_by_id,
    get_sale_items_by_sale_id
)


def test_sales_flow():
    print("🛒 Savdo test jarayoni boshlandi")

    # 1. Yangi savdo sessiyasi (naqd to‘lov)
    sale_id = start_sale(payment_type="cash", customer_id=None)
    print("🆕 Yaratilgan savdo ID:", sale_id)

    # 2. Mahsulot skan qilish
    barcode = "1234567890123"  # ⚠️ Bu barcode bazada mavjud bo‘lishi kerak
    item = scan_item(barcode)
    if not item:
        print(f"❌ Mahsulot topilmadi yoki omborda yo'q: {barcode}, test to‘xtatildi")
        return

    item["quantity"] = 2
    total_amount = round(item["quantity"] * item["price"], 2)
    print(f"📦 Mahsulot: {item['name']} x{item['quantity']} = {total_amount} so'm")

    # 3. Naqd to‘lov
    cash_given = 20000
    change = calculate_change(total_amount, cash_given)
    if change is None:
        print("❌ Qaytim hisoblanmadi, test bekor qilindi")
        return

    print(f"💵 Qaytim: {change} so‘m")

    # 4. Savdoni yakunlash
    finalize_sale(
        sale_id=sale_id,
        cart_items=[item],
        total_amount=total_amount,
        payment_type="cash",
        cash_given=cash_given,
        change=change,
        customer_id=None
    )
    print("✅ Savdo yakunlandi!")

    # 5. Savdoni ko‘rish
    sale = get_sale_by_id(sale_id)
    print("🧾 Savdo ma'lumotlari:", sale)

    # 6. Savdoga tegishli mahsulotlar
    items = get_sale_items_by_sale_id(sale_id)
    print("📋 Savdo itemlari:")
    for i in items:
        print(i)


if __name__ == "__main__":
    test_sales_flow()
