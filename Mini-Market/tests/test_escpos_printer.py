# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 11:38:17 2025

@author: DavrServis
"""

"""
escpos_test.py

ESC/POS printer (USB orqali) bilan chek chiqarishni test qilish.
"""

from escpos.printer import Usb

# Printeringizning VID va PID qiymatlari:
# Masalan: VID=0x0416, PID=0x5011 (Siz bergan)

try:
    printer = Usb(0x0416, 0x5011)  # ✅ O'zingizning printeringiz uchun VID/PID
    printer.text("ESC/POS test kvitansiyasi\n")
    printer.text("--------------------------\n")
    printer.text("Non x2    6000 so'm\n")
    printer.text("Sut x1    8000 so'm\n")
    printer.text("Jami:     14000 so'm\n")
    printer.text("Rahmat!\n\n\n")
    printer.cut()

    print("✅ Check printerga yuborildi.")
except Exception as e:
    print(f"[Xatolik] Check chiqarishda: {e}")
