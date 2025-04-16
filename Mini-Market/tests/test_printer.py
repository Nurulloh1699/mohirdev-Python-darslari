# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 09:21:57 2025

@author: DavrServis
"""

"""
test_win32_printer.py

Windowsdagi POS printer orqali matnli kvitansiyani test qilish.
modules/printer_manager.py dagi ReceiptPrinter klassidan foydalanadi.
"""

import sys
import os

# Loyiha papkasini sys.path ga qo‘shamiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.printer_manager import ReceiptPrinter

items = [
    {"name": "Non", "price": 3000, "quantity": 2},
    {"name": "Sut", "price": 8000, "quantity": 1}
]

printer = ReceiptPrinter("POS-58(copy of 3)")  # Windowsdagi mavjud printer nomi

printer.print_receipt(
    items=items,
    total=14000,
    payment_type="Naqd",
    change=1000
)
