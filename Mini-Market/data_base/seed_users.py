# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:25:12 2025

@author: DavrServis
"""
from database import get_connection
from dotenv import load_dotenv
import os
import hashlib

load_dotenv()  # .env faylni yuklaydi

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def seed_users():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                users = [
                    (
                        os.getenv('ADMIN_USERNAME'),
                        os.getenv('ADMIN_PASSWORD'),
                        os.getenv('ADMIN_ROLE'),
                        os.getenv('ADMIN_FULLNAME')
                    ),
                    (
                        os.getenv('KASSIR_USERNAME'),
                        os.getenv('KASSIR_PASSWORD'),
                        os.getenv('KASSIR_ROLE'),
                        os.getenv('KASSIR_FULLNAME')
                    )
                ]
                for username, password, role, full_name in users:
                    password_hash = hash_password(password)
                    cur.execute("""
                        INSERT INTO users (username, password_hash, role, full_name)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (username) DO NOTHING;
                    """, (username, password_hash, role, full_name))
                conn.commit()
                print("✅ Admin va kassir foydalanuvchilar yaratildi.")
    except Exception as e:
        print(f"❌ Xatolik: {e}")

if __name__ == "__main__":
    seed_users()


