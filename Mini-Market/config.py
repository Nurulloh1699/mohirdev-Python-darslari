# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 09:50:26 2025

@author: DavrServis
"""

# config.py

# 💾 PostgreSQL baza konfiguratsiyasi
DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "user": "postgres",
    "password": "n1282754N",
    "database": "postgres"
}

# 🖨 Printer nomi (Windows uchun foydalanuvchi o‘rnatgan printer nomi)
PRINTER_NAME = "80-VI-UL"

# 👥 Foydalanuvchi rollari
USER_ROLES = ["admin", "kassir"]

# 🖥 GUI uchun ekran o‘lchami (1280x1024 vertical touchscreen)
SCREEN_SIZE = {
    "width": 1024,
    "height": 1280,
    "fullscreen": True
}

# 💸 Valyuta birligi
CURRENCY = "so'm"
