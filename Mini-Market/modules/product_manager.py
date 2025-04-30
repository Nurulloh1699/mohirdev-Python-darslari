# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 11:36:09 2025

@author: DavrServis
"""

# modules/product_manager.py

from data_base.database import fetch_one, fetch_all, execute_query, execute_returning_id

# --- Barcha kategoriyalarni olish ---
def get_all_categories():
    query = "SELECT category_name FROM categories ORDER BY category_name"
    rows = fetch_all(query)
    return [row["category_name"] for row in rows]

# --- Mahsulotni barcode orqali olish ---
def get_product_by_barcode(barcode):
    query = "SELECT * FROM products WHERE barcode = %s"
    return fetch_one(query, (barcode,))

# --- Mahsulotni ID bo‘yicha olish ---
def get_product_by_id(product_id):
    query = "SELECT * FROM products WHERE id = %s"
    return fetch_one(query, (product_id,))

# --- Kategoriya nomidan ID topish ---
def get_category_id_by_name(category_name):
    query = "SELECT id FROM categories WHERE category_name = %s LIMIT 1"
    row = fetch_one(query, (category_name,))
    return row["id"] if row else None

# --- Mahsulot qo‘shish yoki yangilash ---
def add_or_update_product(barcode, nomi, sotuv_narxi, miqdor, amal, category_id, foyda_turi, foyda_miqdori, olchov, purchase_price):
    existing = fetch_one("SELECT id FROM products WHERE barcode = %s", (barcode,))
    if existing:
        query = "UPDATE products SET quantity = quantity + %s WHERE barcode = %s"
        execute_query(query, (miqdor, barcode))
    else:
        query = '''
            INSERT INTO products 
            (barcode, name, purchase_price, sale_price, quantity, expiry_date, category_id, profit_type, profit_value, unit, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'active')
        '''
        params = (barcode, nomi, purchase_price, sotuv_narxi, miqdor, amal, category_id, foyda_turi, foyda_miqdori, olchov)
        execute_query(query, params)

# --- Mahsulotlarni toifaga qarab olish ---
def get_products_by_category(category_name):
    query = """
        SELECT p.barcode, p.name, p.sale_price, p.quantity
        FROM products p
        JOIN categories c ON p.category_id = c.id
        WHERE LOWER(c.category_name) = LOWER(%s)
          AND p.sale_price > 0
          AND p.quantity > 0
          AND p.status = 'active'
        ORDER BY p.name
    """
    return fetch_all(query, (category_name.strip(),))


# --- Barcha mahsulotlar ro‘yxatini olish ---
def get_all_products():
    query = "SELECT * FROM products ORDER BY name"
    return fetch_all(query)

# --- Mahsulot qoldig‘ini yangilash ---
def update_stock(product_id, amount):
    query = "UPDATE products SET quantity = quantity + %s WHERE id = %s"
    execute_query(query, (amount, product_id))

# --- Mahsulot ma’lumotlarini yangilash ---
def update_product(product_id, name, sale_price, quantity, category_id):
    query = """
        UPDATE products
        SET name = %s, sale_price = %s, quantity = %s, category_id = %s
        WHERE id = %s
    """
    execute_query(query, (name, sale_price, quantity, category_id, product_id))

# --- Mahsulotni o‘chirish ---
def delete_product(product_id):
    query = "DELETE FROM products WHERE id = %s"
    execute_query(query, (product_id,))
