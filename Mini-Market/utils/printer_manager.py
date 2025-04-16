# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 09:59:35 2025

@author: DavrServis
"""

# utils/printer_manager.py

from escpos.printer import Usb
from datetime import datetime
from config import PRINTER_NAME, CURRENCY
import platform

# Agar Windows bo‘lsa, `win32print` orqali ham ulanishni qo‘shamiz (fallback variant)

def connect_printer():
    """
    ESC/POS USB printerga ulanish.
    Bu funksiya foydalanuvchi tomonidan o‘rnatilgan printer nomiga asoslanadi.
    """
    try:
        if platform.system() == "Windows":
            from escpos.printer import Win32Raw
            return Win32Raw(PRINTER_NAME)
        else:
            # Agar kerak bo‘lsa, bu yerga Linux/USB ulanishi ham qo‘shiladi
            return Usb(0x0416, 0x5011)  # misol uchun VendorID, ProductID (o‘zgartiriladi)
    except Exception as e:
        print("❌ Printerga ulanishda xatolik:", e)
        return None

def format_receipt(items, total, payment_type, bonus=0, change=0):
    """
    Chek matnini formatlash (list tarzida).
    """
    lines = []
    lines.append("    MINI-MARKET DO'KONI")
    lines.append("----------------------------")
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    lines.append(f"Sana: {now}")
    lines.append("----------------------------")

    for item in items:
        name = item.nomi
        qty = item.miqdor
        price = item.narx
        subtotal = qty * price
        lines.append(f"{name}  {qty} x {int(price)} = {int(subtotal)}")

    lines.append("----------------------------")
    lines.append(f"Jami summa: {int(total):,} {CURRENCY}".replace(",", " "))
    if change > 0:
        lines.append(f"Qaytim: {int(change):,} {CURRENCY}".replace(",", " "))
    if bonus > 0:
        lines.append(f"Bonus: {int(bonus):,} {CURRENCY}".replace(",", " "))

    lines.append(f"To'lov turi: {payment_type}")
    lines.append("Rahmat!")
    return lines

def print_receipt(items, total, payment_type, bonus=0, change=0):
    """
    Printerga chekni yuborish.
    """
    printer = connect_printer()
    if printer is None:
        print("❌ Printer mavjud emas yoki ulanmadi.")
        return

    lines = format_receipt(items, total, payment_type, bonus, change)
    try:
        for line in lines:
            printer.text(line + "\n")
        printer.cut()
        print("✅ Chek muvaffaqiyatli chiqarildi.")
    except Exception as e:
        print("❌ Chop etishda xatolik:", e)
