# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 11:12:44 2025

@author: DavrServis
"""

'''
create_tables.py

Ushbu modul `mini_market` database uchun kerakli barcha jadvallarni yaratadi:
- Mahsulotlar
- Kategoriyalar
- Mijozlar
- Savdolar
- Qarzdorliklar
- Smena
- Xarajatlar
- Foydalanuvchilar
- Narxlar tarixi

Barcha jadvallar professional tarzda: Primary Key, Foreign Key, Default qiymatlar va xavfsiz tarzda yaratiladi.
'''

import psycopg2
from database import get_connection
import sys
import os
# .env va modules papkani tan olish uchun bazaviy katalogni aniqlaymiz
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
from database import get_connection





# --- Jadval yaratish funksiyasi ---
def create_tables():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                # 1. Kategoriyalar jadvali
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS categories (
                        id SERIAL PRIMARY KEY,
                        category_name VARCHAR(255) UNIQUE NOT NULL,
                        status VARCHAR(20) DEFAULT 'active',
                        description TEXT
                    );
                """)

                # 2. Mahsulotlar jadvali
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS products (
                        id SERIAL PRIMARY KEY,
                        barcode VARCHAR(100) UNIQUE NOT NULL,
                        name VARCHAR(255) NOT NULL,
                        purchase_price NUMERIC(12,2) DEFAULT 0,
                        sale_price NUMERIC(12,2) DEFAULT 0,
                        quantity NUMERIC(12,2) DEFAULT 0,
                        expiry_date DATE,
                        category_id INTEGER REFERENCES categories(id),
                        profit_type VARCHAR(20),
                        profit_value NUMERIC(12,2) DEFAULT 0,
                        unit VARCHAR(20),
                        status VARCHAR(20) DEFAULT 'active'
                    );
                """)

                # 3. Mijozlar jadvali
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS customers (
                        id SERIAL PRIMARY KEY,
                        full_name VARCHAR(255) NOT NULL,
                        id_card_number VARCHAR(100) UNIQUE,
                        phone VARCHAR(20),
                        address TEXT,
                        debt_limit NUMERIC(12,2) DEFAULT 0,
                        current_debt NUMERIC(12,2) DEFAULT 0
                    );
                """)

                # 4. Foydalanuvchilar jadvali
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(100) UNIQUE NOT NULL,
                        password_hash VARCHAR(255) NOT NULL,
                        role VARCHAR(50) NOT NULL,
                        full_name VARCHAR(255)
                    );
                """)

                # 5. Savdo umumiy jadvali
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS sales (
                        id SERIAL PRIMARY KEY,
                        sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        payment_type VARCHAR(20) NOT NULL,
                        total_amount NUMERIC(12,2) DEFAULT 0,
                        cash_given NUMERIC(12,2) DEFAULT 0,
                        change NUMERIC(12,2) DEFAULT 0,
                        customer_id INTEGER REFERENCES customers(id),
                        user_id INTEGER REFERENCES users(id),  --  Yangi ustun
                        status VARCHAR(20) DEFAULT 'completed'
                    );
                """)

                # 6. Savdo itemlari (har bir mahsulot)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS sales_items (
                        id SERIAL PRIMARY KEY,
                        sale_id INTEGER REFERENCES sales(id) ON DELETE CASCADE,
                        product_id INTEGER REFERENCES products(id),
                        quantity NUMERIC(12,2) DEFAULT 1,
                        price NUMERIC(12,2) DEFAULT 0,
                        subtotal NUMERIC(12,2) DEFAULT 0
                    );
                """)

                # 7. Qarzdorliklar jadvali
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS credits (
                        id SERIAL PRIMARY KEY,
                        customer_id INTEGER REFERENCES customers(id),
                        sale_id INTEGER REFERENCES sales(id),
                        amount NUMERIC(12,2) DEFAULT 0,
                        paid_amount NUMERIC(12,2) DEFAULT 0,
                        date_taken DATE DEFAULT CURRENT_DATE,
                        date_due DATE,
                        user_id INTEGER REFERENCES users(id),  -- Yangi ustun
                        status VARCHAR(20) DEFAULT 'unpaid'
                    );
                """)

                # 8. Smena (shift) jadvali
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS shifts (
                        id SERIAL PRIMARY KEY,
                        opened_by INTEGER REFERENCES users(id),
                        opened_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        closed_by INTEGER REFERENCES users(id),
                        closed_at TIMESTAMP,
                        status VARCHAR(20) DEFAULT 'open'
                    );
                """)

                # 9. Xarajatlar jadvali
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS expenses (
                        id SERIAL PRIMARY KEY,
                        expense_name VARCHAR(255) NOT NULL,
                        amount NUMERIC(12,2) NOT NULL,
                        expense_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        description TEXT
                    );
                """)

                # 10. Narxlar tarixi jadvali (price change history)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS price_history (
                        id SERIAL PRIMARY KEY,
                        product_id INTEGER REFERENCES products(id),
                        old_price NUMERIC(12,2),
                        new_price NUMERIC(12,2),
                        changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)

                conn.commit()
                print("Barcha jadvallar muvaffaqiyatli yaratildi.")

    except Exception as e:
        print(f"Xatolik: {e}")

# --- Asosiy bajariladigan qism ---
if __name__ == "__main__":
    create_tables()
