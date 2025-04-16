# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 08:41:33 2025

@author: DavrServis
"""

"""
user_manager.py

Foydalanuvchilarni boshqarish moduli:
- Yangi foydalanuvchi yaratish (parol hash bilan)
- Login qilish
- Parolni o‘zgartirish
- Foydalanuvchini tekshirish
"""

from data_base.database import fetch_one, fetch_all, execute_query, execute_returning_id
import hashlib


# 0. Parolni SHA-256 orqali hashlash
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# 1. Username orqali ma'lumot olish
def get_user_by_username(username):
    query = "SELECT * FROM users WHERE username = %s"
    return fetch_one(query, (username,))


# 2. Foydalanuvchi mavjudligini tekshirish
def user_exists(username):
    return get_user_by_username(username) is not None


# 3. Yangi foydalanuvchi yaratish
def create_user(username, password, role):
    if user_exists(username):
        print(f"⚠️ Username '{username}' allaqachon mavjud.")
        return None

    password_hash = hash_password(password)
    query = """
        INSERT INTO users (username, password_hash, role)
        VALUES (%s, %s, %s) RETURNING id
    """
    return execute_returning_id(query, (username, password_hash, role))


# 4. Login qilish
def login(username, password):
    password_hash = hash_password(password)
    query = """
        SELECT * FROM users WHERE username = %s AND password_hash = %s
    """
    return fetch_one(query, (username, password_hash))


# 5. Parolni o‘zgartirish
def change_password(username, new_password):
    password_hash = hash_password(new_password)
    query = "UPDATE users SET password_hash = %s WHERE username = %s"
    return execute_query(query, (password_hash, username))
