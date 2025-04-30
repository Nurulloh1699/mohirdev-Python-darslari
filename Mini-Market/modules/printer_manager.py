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

import win32print


class ReceiptPrinter:
    def __init__(self, printer_name="POS-58(copy of 3)"):
        self.printer_name = printer_name

    def print_receipt(self, items, total, payment_type="Naqd", change=0):
        try:
            # Printerga ulanish
            hprinter = win32print.OpenPrinter(self.printer_name)
            win32print.StartDocPrinter(hprinter, 1, ("Check", None, "RAW"))
            win32print.StartPagePrinter(hprinter)

            # Chek matni tuziladi
            text = "        MINI MARKET\n"
            text += "------------------------\n"
            for item in items:
                name = item.get("name", "Noma'lum")
                price = item.get("price", 0)
                qty = item.get("quantity", 1)
                subtotal = price * qty
                text += f"{name[:14]:14} x{qty}  {subtotal:>7,.0f} so'm\n"

            text += "------------------------\n"
            text += f"Jami:        {total:,.0f} so'm\n"
            text += f"To‘lov:       {payment_type}\n"
            if payment_type.lower() == "naqd":
                text += f"Qaytim:       {change:,.0f} so'm\n"
            text += "------------------------\n"
            text += "Tashrifingiz uchun rahmat!\n\n\n"

            # Chop etish
            win32print.WritePrinter(hprinter, text.encode("latin-1"))
            win32print.EndPagePrinter(hprinter)
            win32print.EndDocPrinter(hprinter)
            win32print.ClosePrinter(hprinter)

            print("✅ Kvitansiya chiqarildi.")
        except Exception as e:
            print(f"[Xatolik] Check chiqarishda: {e}")




