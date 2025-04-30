# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 12:50:12 2025

@author: DavrServis
"""

import sys
import os

# Bazaviy katalogni sys.path ga qo‘shamiz
directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if directory not in sys.path:
    sys.path.append(directory)
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout,
    QMessageBox, QComboBox, QDateEdit, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QDate

# --- YANGI STRUKTURAGA MOS IMPORTLAR ---
from modules.product_manager import register_new_product  # modul yo‘liga moslashtirildi

class ProductRegistrationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🛠 Baza bo‘limi - Yangi mahsulot qo‘shish")
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.resize(1280, 1024)
        self.setStyleSheet("background-color: #f4f4f4;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(100, 50, 100, 50)
        layout.setSpacing(30)

        title = QLabel("Yangi mahsulot qo‘shish")
        title.setFont(QFont("Arial", 36, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form = QFormLayout()
        form.setHorizontalSpacing(50)
        form.setVerticalSpacing(30)

        font_label = QFont("Arial", 20)
        font_input = QFont("Arial", 20)

        self.barcode_input = QLineEdit()
        self.barcode_input.setFont(font_input)
        self.barcode_input.returnPressed.connect(self.process_barcode_input)

        self.name_input = QLineEdit()
        self.name_input.setFont(font_input)

        self.category_input = QComboBox()
        self.category_input.setFont(font_input)
        self.category_input.addItems([
            "Sut mahsulotlari",
            "Go'sht va kolbasa mahsulotlari",
            "Mevalar",
            "Sabzavotlar",
            "Ichimliklar",
            "Shirinliklar",
            "Kiloli mahsulotlar",
            "Non mahsulotlari",
            "Yog'lar"
        ])

        self.purchase_price_input = QLineEdit()
        self.purchase_price_input.setFont(font_input)

        self.profit_input = QLineEdit()
        self.profit_input.setFont(font_input)
        self.profit_type = QComboBox()
        self.profit_type.setFont(font_input)
        self.profit_type.addItems(["foiz", "so'mda"])
        profit_layout = QHBoxLayout()
        profit_layout.addWidget(self.profit_input)
        profit_layout.addWidget(self.profit_type)

        self.quantity_input = QLineEdit()
        self.quantity_input.setFont(font_input)
        self.quantity_unit = QComboBox()
        self.quantity_unit.setFont(font_input)
        self.quantity_unit.addItems(["dona", "kg", "litr"])
        quantity_layout = QHBoxLayout()
        quantity_layout.addWidget(self.quantity_input)
        quantity_layout.addWidget(self.quantity_unit)

        self.expiry_input = QLineEdit()
        self.expiry_input.setFont(font_input)
        self.expiry_date = QDateEdit()
        self.expiry_date.setFont(font_input)
        self.expiry_date.setCalendarPopup(True)
        self.expiry_date.setDate(QDate.currentDate())
        expiry_layout = QHBoxLayout()
        expiry_layout.addWidget(self.expiry_input)
        expiry_layout.addWidget(self.expiry_date)

        form.addRow(self._form_label("📦 Barcode:"), self.barcode_input)
        form.addRow(self._form_label("📝 Nomi:"), self.name_input)
        form.addRow(self._form_label("📁 Kategoriya:"), self.category_input)
        form.addRow(self._form_label("💰 Kelgan narxi:"), self.purchase_price_input)
        form.addRow(self._form_label("📈 Foyda:"), profit_layout)
        form.addRow(self._form_label("🔢 Miqdor:"), quantity_layout)
        form.addRow(self._form_label("⏰ Amal muddati:"), expiry_layout)

        layout.addLayout(form)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        save_btn = QPushButton("💾 Saqlash")
        save_btn.setFont(QFont("Arial", 24, QFont.Bold))
        save_btn.setFixedHeight(80)
        save_btn.setStyleSheet("background-color: #27ae60; color: white; padding: 20px; border-radius: 16px;")
        save_btn.clicked.connect(self.save_product)
        layout.addWidget(save_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def _form_label(self, text):
        lbl = QLabel(text)
        lbl.setFont(QFont("Arial", 20, QFont.Bold))
        return lbl

    def process_barcode_input(self):
        barcode = self.barcode_input.text()
        if barcode:
            self.barcode_input.setText(barcode)
            self.barcode_input.setCursorPosition(len(barcode))
            self.barcode_input.setFocus()

    def save_product(self):
        barcode = self.barcode_input.text()
        name = self.name_input.text()
        category = self.category_input.currentText()
        purchase_price = self.purchase_price_input.text()
        profit = self.profit_input.text()
        profit_type = self.profit_type.currentText()
        quantity = self.quantity_input.text()
        quantity_unit = self.quantity_unit.currentText()
        expiry = self.expiry_input.text() or self.expiry_date.date().toString("yyyy-MM-dd")

        print("✅ Saqlanyapti:", barcode, name, category, purchase_price, profit, profit_type, quantity, quantity_unit, expiry)
        QMessageBox.information(self, "Saqlash", "Mahsulot saqlandi (test rejimida).")
        self.clear_fields()

    def clear_fields(self):
        self.barcode_input.clear()
        self.name_input.clear()
        self.purchase_price_input.clear()
        self.profit_input.clear()
        self.quantity_input.clear()
        self.expiry_input.clear()
        self.expiry_date.setDate(QDate.currentDate())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductRegistrationUI()
    window.show()
    sys.exit(app.exec_())
