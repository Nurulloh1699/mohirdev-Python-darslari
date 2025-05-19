# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 11:36:09 2025

@author: DavrServis
"""

"""
product_manager.py

Mahsulotlar va kategoriyalar bilan ishlash moduli:
- Mahsulot qo'shish
- Mahsulot yangilash
- Mahsulot o'chirish (soft delete opsiyasi bilan)
- Kategoriyalarni boshqarish
"""

from data_base.database import fetch_one, fetch_all, execute_query, execute_returning_id

# --- Barcha kategoriyalarni olish ---
def get_all_categories():
    query = "SELECT category_name FROM categories WHERE status = 'active' ORDER BY category_name"
    rows = fetch_all(query)
    return [row["category_name"] for row in rows]

# --- Yangi kategoriya qo‘shish ---
def add_category(category_name, description=None):
    query = """
        INSERT INTO categories (category_name, status, description)
        VALUES (%s, 'active', %s)
        ON CONFLICT (category_name) DO NOTHING;
    """
    return execute_query(query, (category_name, description))

# --- Mahsulotni barcode orqali olish ---
def get_product_by_barcode(barcode):
    query = "SELECT * FROM products WHERE barcode = %s AND status = 'active'"
    return fetch_one(query, (barcode,))

# --- Mahsulotni ID bo‘yicha olish ---
def get_product_by_id(product_id):
    query = "SELECT * FROM products WHERE id = %s AND status = 'active'"
    return fetch_one(query, (product_id,))

# --- Kategoriya nomidan ID topish ---
def get_category_id_by_name(category_name):
    query = "SELECT id FROM categories WHERE LOWER(category_name) = LOWER(%s) AND status = 'active' LIMIT 1"
    row = fetch_one(query, (category_name,))
    return row["id"] if row else None

def get_category_name_by_id(category_id):
    query = "SELECT category_name FROM categories WHERE id = %s AND status = 'active'"
    row = fetch_one(query, (category_id,))
    return row["category_name"] if row else ""

# --- Mahsulot qo‘shish yoki yangilash ---
def add_or_update_product(barcode, name, sale_price, quantity, expiry_date, category_id, profit_type, profit_value, unit, purchase_price):
    existing = fetch_one("SELECT id, sale_price FROM products WHERE barcode = %s", (barcode,))
    if existing:
        # Mahsulot bazada mavjud, miqdorini yangilash va narxni ham tekshirib yangilash
        query = """
            UPDATE products 
            SET quantity = quantity + %s,
                category_id = %s,
                sale_price = %s,
                purchase_price = %s
            WHERE barcode = %s
              AND status = 'active'
        """
        execute_query(query, (quantity, category_id, sale_price, purchase_price, barcode))
    else:
        # Yangi mahsulot qo‘shish
        query = '''
            INSERT INTO products 
            (barcode, name, purchase_price, sale_price, quantity, expiry_date, category_id, profit_type, profit_value, unit, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'active')
        '''
        params = (barcode, name, purchase_price, sale_price, quantity, expiry_date, category_id, profit_type, profit_value, unit)
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
          AND c.status = 'active'
        ORDER BY p.name
    """
    return fetch_all(query, (category_name.strip(),))

# --- Barcha mahsulotlar ro‘yxatini olish ---
def get_all_products():
    query = "SELECT * FROM products WHERE status = 'active' ORDER BY name"
    return fetch_all(query)

# --- Mahsulot qoldig‘ini yangilash ---
def update_stock(product_id, amount):
    query = "UPDATE products SET quantity = quantity + %s WHERE id = %s AND status = 'active'"
    execute_query(query, (amount, product_id))

# --- Mahsulot ma’lumotlarini yangilash ---
def update_product(product_id, name, sale_price, quantity, category_id):
    query = """
        UPDATE products
        SET name = %s, sale_price = %s, quantity = %s, category_id = %s
        WHERE id = %s
          AND status = 'active'
    """
    execute_query(query, (name, sale_price, quantity, category_id, product_id))

# --- Mahsulotni "soft" o‘chirish (real delete emas) ---
def delete_product(product_id):
    query = "UPDATE products SET status = 'inactive' WHERE id = %s"
    execute_query(query, (product_id,))
