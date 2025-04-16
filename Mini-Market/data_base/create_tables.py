# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 11:12:44 2025

@author: DavrServis
"""

"""
create_tables.py

PostgreSQL bazasida kerakli jadvallarni yaratish uchun skript.
"""

# data_base/create_tables.py

import psycopg2

def create_tables():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="n1282754N",
        port="5433"
    )
    cur = conn.cursor()

    # 1. Kategoriyalar jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS kategoriyalar (
            id SERIAL PRIMARY KEY,
            nomi VARCHAR(100) UNIQUE NOT NULL
        );
    """)

    # 2. Mahsulotlar jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mahsulotlar (
            id SERIAL PRIMARY KEY,
            nomi VARCHAR(255),
            barcode VARCHAR(50) UNIQUE,
            narx NUMERIC(10,2),
            miqdor NUMERIC(10,2),
            amal_muddati DATE,
            kategoriya VARCHAR(100),
            foyda_turi VARCHAR(10),
            foyda_miqdori NUMERIC(10,2),
            o_lov_birligi VARCHAR(20)
        );
    """)

    # 3. Mijozlar jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mijozlar (
            id SERIAL PRIMARY KEY,
            ism VARCHAR(255),
            id_karta VARCHAR(100) UNIQUE
        );
    """)

    # 4. Foydalanuvchilar jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS foydalanuvchilar (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE,
            password VARCHAR(100),
            role VARCHAR(20)
        );
    """)

    # 5. Savdo jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS savdo (
            id SERIAL PRIMARY KEY,
            vaqt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            jami_summa NUMERIC(10,2),
            tolov_turi VARCHAR(20)
        );
    """)

    # 6. Qarzlar jadvali
    cur.execute("""
        CREATE TABLE IF NOT EXISTS qarzlar (
            id SERIAL PRIMARY KEY,
            mijoz_id INTEGER REFERENCES mijozlar(id),
            summa NUMERIC(10,2),
            vaqt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 7. Boshlang‘ich kategoriyalar
    cur.execute("""
        INSERT INTO kategoriyalar (nomi) VALUES
        ('Ichimliklar'),
        ('Shirinliklar'),
        ('Kiloli'),
        ('Go‘sht'),
        ('Yog‘lar'),
        ('Non'),
        ('Sabzavotlar'),
        ('Mevalar'),
        ('Chipslar')
        ON CONFLICT (nomi) DO NOTHING;
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Jadvallar yaratildi va kategoriyalar bazaga qo‘shildi.")

if __name__ == "__main__":
    create_tables()
