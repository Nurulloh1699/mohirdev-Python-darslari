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

# Ma’lumotlar bazasi konfiguratsiyasi (KEYINGI BOSQICHDA .env faylga o‘tkaziladi)
DB_CONFIG = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "n1282754N",
    "port": "5433"
}

# Ma’lumotlar bazasiga ulanish uchun kontekst menejeri
def get_connection():
    return psycopg2.connect(**DB_CONFIG)

# SELECT uchun — barcha natijalarni olish
def fetch_all(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                return cur.fetchall()
    except Exception as e:
        print("❌ fetch_all xatolik:", e)
        return []

# SELECT uchun — faqat bitta natija
def fetch_one(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                return cur.fetchone()
    except Exception as e:
        print("❌ fetch_one xatolik:", e)
        return None

# INSERT/UPDATE/DELETE uchun
def execute_query(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()
                return True
    except Exception as e:
        print("❌ execute_query xatolik:", e)
        return False

# INSERT bilan ID qaytarish (masalan, yangi mahsulot ID'si)
def execute_returning_id(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                new_id = cur.fetchone()[0]
                conn.commit()
                return new_id
    except Exception as e:
        print("❌ execute_returning_id xatolik:", e)
        return None
