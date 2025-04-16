# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 11:56:15 2025

@author: DavrServis
"""

"""
sales_manager.py

Savdo jarayonini boshqaruvchi modul:
- Savdoni boshlash
- Mahsulot skan qilish
- Savdoni yakunlash
- Qaytim hisoblash
- Savdoni ID orqali olish
"""

from data_base.database import execute_query, execute_returning_id, fetch_one, fetch_all, get_connection
from datetime import datetime

# Mahsulotni barcode orqali topish (foydalanish uchun)
def get_product_by_barcode(barcode):
    query = "SELECT * FROM products WHERE barcode = %s"
    return fetch_one(query, (barcode,))

# 1. Yangi savdo sessiyasini boshlash
def start_sale(payment_type, customer_id=None):
    query = """
        INSERT INTO sales (payment_type, customer_id, total_amount, cash_given, change)
        VALUES (%s, %s, 0, 0, 0) RETURNING id
    """
    return execute_returning_id(query, (payment_type, customer_id))

# 2. Mahsulotni skan qilish — vaqtinchalik ro‘yxatga qo‘shish uchun GUI moduli ishlatadi
def scan_item(barcode):
    product = get_product_by_barcode(barcode)
    if product is None:
        print("❌ Mahsulot topilmadi!")
        return None
    if product["quantity"] <= 0:
        print("⚠️ Mahsulot omborda qolmagan!")
        return None
    return {
        "product_id": product["id"],
        "name": product["name"],
        "price": product["sale_price"]
    }

# 3. Savdoni yakunlash (tranzaksiya bilan)
def finalize_sale(sale_id, cart_items, total_amount, payment_type,
                  cash_given=0, change=0, customer_id=None):

    if payment_type == "cash" and change is None:
        print("❌ Qaytim xato, savdo yakunlanmaydi.")
        return

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                # 3.1 Savdo asosiy jadvalini yangilaymiz
                update_query = """
                    UPDATE sales
                    SET total_amount = %s,
                        cash_given = %s,
                        change = %s,
                        customer_id = %s,
                        payment_type = %s,
                        sale_date = %s
                    WHERE id = %s
                """
                cur.execute(update_query, (
                    total_amount, cash_given, change, customer_id,
                    payment_type, datetime.now(), sale_id
                ))

                for item in cart_items:
                    # Ombordagi miqdorni tekshirish
                    stock_check = "SELECT quantity FROM products WHERE id = %s"
                    cur.execute(stock_check, (item["product_id"],))
                    available = cur.fetchone()[0]
                    if available < item["quantity"]:
                        print(f"❌ Omborda yetarli mahsulot yo‘q: ID={item['product_id']}")
                        continue

                    # 3.2 Savdo itemlarini yozish
                    item_query = """
                        INSERT INTO sales_items (sale_id, product_id, quantity, price, subtotal)
                        VALUES (%s, %s, %s, %s, %s)
                    """
                    subtotal = round(item["quantity"] * item["price"], 2)
                    cur.execute(item_query, (
                        sale_id, item["product_id"], item["quantity"], item["price"], subtotal
                    ))

                    # Omborni kamaytirish
                    stock_update = "UPDATE products SET quantity = quantity - %s WHERE id = %s"
                    cur.execute(stock_update, (item["quantity"], item["product_id"]))

    except Exception as e:
        print("❌ Savdo yakunlanmadi:", e)
    finally:
        conn.close()

# 4. Qaytim hisoblash (naqd to‘lovda)
def calculate_change(total_amount, cash_given):
    if cash_given >= total_amount:
        return round(cash_given - total_amount, 2)
    else:
        print("❌ Yetarli naqd pul emas")
        return None

# 5. Mavjud savdoni olish (test yoki hisobot uchun)
def get_sale_by_id(sale_id):
    query = "SELECT * FROM sales WHERE id = %s"
    return fetch_one(query, (sale_id,))

# 6. Savdoga tegishli itemlarni olish
def get_sale_items_by_sale_id(sale_id):
    query = "SELECT * FROM sales_items WHERE sale_id = %s"
    return fetch_all(query, (sale_id,))
