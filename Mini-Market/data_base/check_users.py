# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:37:29 2025

@author: DavrServis
"""

from database import get_connection

def check_users():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, username, role, full_name FROM users;")
                users = cur.fetchall()
                if users:
                    print("✅ Baza ichidagi foydalanuvchilar:")
                    for user in users:
                        print(f"ID: {user[0]}, Username: {user[1]}, Role: {user[2]}, Full Name: {user[3]}")
                else:
                    print("❌ Hozircha users jadvalida hech qanday foydalanuvchi yo'q.")
    except Exception as e:
        print(f"❌ Xatolik: {e}")

if __name__ == "__main__":
    check_users()
