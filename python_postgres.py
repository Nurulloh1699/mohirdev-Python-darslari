# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:55:16 2024

@author: DavrServis
"""

import psycopg2

# PostgreSQL serveriga ulanish
try:
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",  # Ma'lumotlar bazasi nomi
        user="postgres",     # PostgreSQL foydalanuvchi nomi
        password="n1282754N",    # PostgreSQL paroli
        port=5432            # Port raqami
    )
    print("Ulanish muvaffaqiyatli!")

    # Cursor yaratamiz (SQL buyruqlarni bajarish uchun)
    cursor = connection.cursor()
    
    # SQL buyruqni bajarish misoli
    cursor.execute("SELECT version();")  # PostgreSQL versiyasini tekshirish
    db_version = cursor.fetchone()      # Natijani olish
    print("PostgreSQL versiyasi:", db_version)
    
except Exception as error:
    print("Ulanishda xatolik yuz berdi:", error)

finally:
    if connection:
        cursor.close()      # Cursorni yopish
        connection.close()  # Ulanishni yopish
        print("Ulanish yopildi.")
