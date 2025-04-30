# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 08:42:57 2025

@author: DavrServis
"""

"""
test_user_manager.py

Foydalanuvchilarni boshqarish moduli (user_manager.py) funksiyalarini test qilish:
- Foydalanuvchi yaratish
- Login
- Parolni o‘zgartirish
- Mavjudligini tekshirish
"""

import sys
import os

# Loyihaning ildizini import yo‘liga qo‘shamiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.user_manager import (
    create_user,
    login,
    get_user_by_username,
    change_password,
    user_exists
)


def test_user_exists(username):
    print(f"🔎 '{username}' foydalanuvchisi mavjudmi?")
    exists = user_exists(username)
    print("✅ Mavjud:" if exists else "❌ Mavjud emas")


def test_create_user(username="admin1", password="adminpass", role="admin"):
    print("👤 Foydalanuvchi yaratilmoqda...")
    user_id = create_user(username, password, role)
    print("✅ Yaratilgan foydalanuvchi ID:", user_id)
    return user_id


def test_login(username, password):
    print(f"🔐 Login test: {username}")
    result = login(username, password)
    if result:
        print("✅ Login muvaffaqiyatli:", result)
    else:
        print("❌ Login muvaffaqiyatsiz")


def test_get_user(username):
    print(f"🔍 Foydalanuvchini qidirish: {username}")
    user = get_user_by_username(username)
    print("🧾 Foydalanuvchi:", user)


def test_change_password(username, new_password="newpass123"):
    print(f"🔁 {username} uchun parol o‘zgartirilmoqda...")
    result = change_password(username, new_password)
    print("✅ Parol o‘zgartirildi:", result)


if __name__ == "__main__":
    print("=== USER MANAGER TEST BOSHLANDI ===")
    username = "admin1"
    password = "adminpass"
    new_password = "newpass123"

    test_user_exists(username)
    test_create_user(username, password)
    test_login(username, password)
    test_get_user(username)
    test_change_password(username, new_password)
    test_login(username, new_password)
    print("=== TEST TUGADI ===")
