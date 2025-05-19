# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 12:32:48 2025

@author: DavrServis
"""

# ui/credits_form.py

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont
from modules.credits_manager import get_customer_credits

class CreditsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # ✅ parent uzatish to‘g‘ri
        self.setWindowTitle("🧾 Qarzdor mijozlar")
        self.setMinimumSize(800, 600)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        title = QLabel("🧾 Qarzdorlikni ko‘rish")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        self.layout.addWidget(title)

        # 🔍 ID karta kiritish
        id_layout = QHBoxLayout()
        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("ID kartani kiriting")
        self.btn_search = QPushButton("Qidirish")
        self.btn_search.clicked.connect(self.search_credits)
        id_layout.addWidget(self.input_id)
        id_layout.addWidget(self.btn_search)
        self.layout.addLayout(id_layout)

        # 📋 Jadval
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Credit ID", "Sale ID", "Sana", "Miqdor", "To‘lov sanasi", ""])
        self.layout.addWidget(self.table)

    def search_credits(self):
        customer_id = self.input_id.text().strip()
        if not customer_id:
            QMessageBox.warning(self, "⚠️ Diqqat", "Iltimos, ID kartani kiriting.")
            return

        credits = get_customer_credits(customer_id)
        self.table.setRowCount(0)

        if not credits:
            QMessageBox.information(self, "🔍 Natija", "Bu ID bo‘yicha qarzdorlik topilmadi.")
            return

        self.table.setRowCount(len(credits))
        for row, credit in enumerate(credits):
            customer_id = credit["customer_id"]
            remaining_debt = credit["remaining_debt"]
            first_date = credit["first_date"]
            last_due = credit["last_due"]

            self.table.setItem(row, 0, QTableWidgetItem(str(customer_id)))
            self.table.setItem(row, 1, QTableWidgetItem(str(int(remaining_debt))))
            self.table.setItem(row, 2, QTableWidgetItem(str(first_date)))
            self.table.setItem(row, 3, QTableWidgetItem(str(last_due)))

            # 💵 To‘lash tugmasi
            btn_pay = QPushButton("💵 To‘lash")
            btn_pay.setStyleSheet("background-color: #2ecc71; color: white;")
            btn_pay.clicked.connect(
                lambda _, cust=customer_id, amt=remaining_debt:
                self.handle_payment(None, amt, cust)  # credit_id endi kerak emas
                )
            self.table.setCellWidget(row, 4, btn_pay)


    def handle_payment(self, customer_id, amount_due):
        from PyQt5.QtWidgets import QInputDialog, QMessageBox
        from modules.credits_manager import pay_credit, get_customer_credits

        # To‘lov miqdorini so‘rash
        amount, ok = QInputDialog.getDouble(
            self,
            "To‘lov",
            f"Qolgan qarz: {int(amount_due)} so‘m\nTo‘lov summasini kiriting:",
            decimals=2
            )

        if not ok or amount <= 0:
            return

        if amount > amount_due:
            QMessageBox.warning(self, "Xatolik", "To‘lov summasi mavjud qarzdan ko‘p bo‘lmasligi kerak.")
            return

        # 🔄 Barcha qarzlarni yuklab olish
        credits = get_customer_credits_raw(customer_id)  # 👇 pastda aniqlanadi

        remaining = amount
        for credit in credits:
            credit_id = credit["credit_id"]
            to_pay = float(credit["amount"] - credit["paid_amount"])
            if to_pay <= 0:
                continue

            if remaining <= to_pay:
                pay_credit(credit_id, remaining, customer_id)
                break
            else:
                pay_credit(credit_id, to_pay, customer_id)
                remaining -= to_pay

        QMessageBox.information(self, "✅ To‘lov bajarildi", f"{amount} so‘m qarz so‘ndirildi.")
        self.search_credits()



