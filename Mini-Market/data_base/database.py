# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 23:00:59 2025

@author: DavrServis
"""

"""
database.py

Ushbu modul PostgreSQL bilan xavfsiz va qulay ishlash uchun umumiy ulanish va query bajarish funksiyalarini taqdim etadi.
Barcha boshqa modullar (mahsulotlar, savdo, mijozlar) ushbu modul orqali bazaga murojaat qiladi.
"""

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
import logging
# database.py
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


# 1. Logger sozlamalari
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="database.log",
    filemode="a"
)

# 2. .env fayldan ma'lumotlarni yuklash
load_dotenv()
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# 3. Ma’lumotlar bazasi konfiguratsiyasi
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_NAME", "mini_market"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "n1282754N"),
    "port": os.getenv("DB_PORT", "5432")
}

# 4. Ma’lumotlar bazasiga ulanish uchun kontekst menejeri
def get_connection():
    return psycopg2.connect(**DB_CONFIG)

# 5. SELECT uchun — barcha natijalarni olish
def fetch_all(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                return cur.fetchall()
    except Exception as e:
        logging.error(f"fetch_all xatolik: {e}")
        return []

# 6. SELECT uchun — faqat bitta natija olish
def fetch_one(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                return cur.fetchone()
    except Exception as e:
        logging.error(f"fetch_one xatolik: {e}")
        return None

# 7. INSERT/UPDATE/DELETE uchun
def execute_query(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()
                return True
    except Exception as e:
        logging.error(f"execute_query xatolik: {e}")
        return False

# 8. INSERT bilan ID qaytarish (masalan, yangi mahsulot ID'si)
def execute_returning_id(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                new_id = cur.fetchone()[0]
                conn.commit()
                return new_id
    except Exception as e:
        logging.error(f"execute_returning_id xatolik: {e}")
        return None
