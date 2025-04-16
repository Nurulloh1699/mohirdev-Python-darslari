# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 11:36:09 2025

@author: DavrServis
"""

# modules/product_manager.py

from data_base.database import fetch_one, fetch_all, execute_query, execute_returning_id
from data_base.database import execute_query, fetch_one, fetch_all, execute_returning_id
from data_base.database import fetch_all  # bu import yuqorida bo'lishi kerak
from data_base.database import fetch_one, execute_query, execute_returning_id

def get_all_categories():
    query = "SELECT nomi FROM kategoriyalar ORDER BY nomi"
    rows = fetch_all(query)
    return [row["nomi"] for row in rows]

# --- Mahsulot qo‘shish ---
def add_product(barcode, name, sale_price, quantity, category):
    query = """
        INSERT INTO products (barcode, name, sale_price, quantity, category)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
    """
    return execute_returning_id(query, (barcode, name, sale_price, quantity, category))

# --- Mahsulotni ID bo‘yicha olish ---
def get_product_by_id(product_id):
    query = "SELECT * FROM products WHERE id = %s"
    return fetch_one(query, (product_id,))

# --- Mahsulotni barcode orqali olish (sotuvda kerak) ---
def get_product_by_barcode(barcode):
    query = "SELECT * FROM products WHERE barcode = %s"
    return fetch_one(query, (barcode,))

# --- 🆕 Mahsulot qo‘shish yoki yangilash (MIQDOR) ---
def add_or_update_product(barcode, nomi, narx, miqdor, amal, category_id, foyda_turi, foyda_miqdori, olchov):
    existing = fetch_one("SELECT id FROM products WHERE barcode = %s", (barcode,))
    if existing:
        query = "UPDATE products SET quantity = quantity + %s WHERE barcode = %s"
        execute_query(query, (miqdor, barcode))
    else:
        query = '''
            INSERT INTO products 
            (barcode, name, sale_price, quantity, expiry_date, category_id, profit_type, profit_value)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = (barcode, nomi, narx, miqdor, amal, category_id, foyda_turi, foyda_miqdori, olchov)
        

# --- Mahsulotlarni toifaga qarab olish ---
def get_products_by_category(category_name):
    query = """
        SELECT p.id, p.name, p.sale_price, p.quantity
        FROM products p
        JOIN categories c ON p.category_id = c.id
        WHERE c.category_name = %s
        ORDER BY p.name
    """
    return fetch_all(query, (category_name,))

def get_category_id_by_name(nomi):
    query = "SELECT id FROM categories WHERE category_name = %s"
    row = fetch_one(query, (nomi,))
    return row["id"] if row else None

# --- Barcha mahsulotlar ro‘yxatini olish ---
def get_all_products():
    query = "SELECT * FROM products ORDER BY name"
    return fetch_all(query)

# --- Mahsulot qoldig‘ini yangilash ---
def update_stock(product_id, amount):
    query = "UPDATE products SET quantity = quantity + %s WHERE id = %s"
    execute_query(query, (amount, product_id))

# --- Mahsulot ma’lumotlarini yangilash ---
def update_product(product_id, name, sale_price, quantity, category):
    query = """
        UPDATE products
        SET name = %s, sale_price = %s, quantity = %s, category = %s
        WHERE id = %s
    """
    execute_query(query, (name, sale_price, quantity, category, product_id))

# --- Mahsulotni o‘chirish ---
def delete_product(product_id):
    query = "DELETE FROM products WHERE id = %s"
    execute_query(query, (product_id,))
