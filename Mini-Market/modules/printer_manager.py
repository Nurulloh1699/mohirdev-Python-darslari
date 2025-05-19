# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 09:23:54 2025

@author: DavrServis
"""

"""
printer_manager.py

Windows printer orqali oddiy matnli kvitansiya (check) chiqarish moduli.
Generic Text Only yoki POS-58 printerlar uchun ishlaydi.
"""

# modules/printer_manager.py

from escpos.printer import Usb
from datetime import datetime
import platform
import os
from dotenv import load_dotenv

# .env faylni o‘qiymiz
load_dotenv()
PRINTER_NAME = os.getenv("PRINTER_NAME", "POS-80")
CURRENCY = os.getenv("CURRENCY", "so'm")


def connect_printer():
    """
    ESC/POS printerga ulanish (USB yoki Windows printer nomi orqali).
    """
    try:
        if platform.system() == "Windows":
            from escpos.printer import Win32Raw
            return Win32Raw(PRINTER_NAME)
        else:
            return Usb(0x0416, 0x5011)  # Misol uchun, Linux USB printer (VendorID, ProductID)
    except Exception as e:
        print("❌ Printerga ulanishda xatolik:", e)
        return None


def format_receipt(items, total, payment_type, bonus=0, change=0):
    """
    Chek matnini formatlash (list tarzida).
    """
    lines = []
    lines.append(" TONGI HILOL MINI-MARKET DO'KONI")
    lines.append("----------------------------")
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    lines.append(f"Sana: {now}")
    lines.append("----------------------------")

    for item in items:
        name = item["name"]
        qty = item["quantity"]
        price = item["price"]
        subtotal = qty * price
        lines.append(f"{name}  {qty} x {int(price)} = {int(subtotal)}")

    lines.append("----------------------------")
    lines.append(f"Jami summa: {int(total):,} {CURRENCY}".replace(",", " "))
    if change > 0:
        lines.append(f"Qaytim: {int(change):,} {CURRENCY}".replace(",", " "))
    if bonus > 0:
        lines.append(f"Bonus: {int(bonus):,} {CURRENCY}".replace(",", " "))

    lines.append(f"To'lov turi: {payment_type}")
    lines.append("Haridingiz uchun Rahmat!")
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

class ReceiptPrinter:
    def __init__(self, printer_name="POS-80"):
        self.printer_name = printer_name
        self.printer = connect_printer()

    def print_receipt(self, sale_id, items, total, payment_type, cash_given=0, change=0):
        if not self.printer:
            print("❌ Printer mavjud emas yoki ulanmadi.")
            return

        width = 40
        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        self.printer.text("🛒 MINI MARKET 🛒".center(width) + "\n")
        self.printer.text(now.center(width) + "\n")
        self.printer.text(f"Chek raqami: #{sale_id}".center(width) + "\n")
        self.printer.text("-" * width + "\n")

        for item in items:
            name = item["name"][:25].ljust(25)
            qty_price = f"{item['quantity']}x{int(item['price'])}".rjust(7)
            total_part = f"{int(item['quantity'] * item['price'])}".rjust(8)
            self.printer.text(f"{name}{qty_price}{total_part}\n")

        self.printer.text("-" * width + "\n")
        self.printer.text(f"To‘lov turi: {payment_type}\n")
        self.printer.text(f"Umumiy: {int(total)} so‘m\n")
        if payment_type == "cash":
            self.printer.text(f"Berilgan: {int(cash_given)} so‘m\n")
            self.printer.text(f"Qaytim: {int(change)} so‘m\n")

        self.printer.text("-" * width + "\n")
        self.printer.text("🤝 RAHMAT!".center(width) + "\n")
        self.printer.cut()

