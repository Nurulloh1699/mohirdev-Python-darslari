# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 11:36:53 2025

@author: DavrServis
"""

# ui/base_form.py

import sys
import os
sys.path.append(os.path.abspath("."))

from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QComboBox, QDateEdit,
    QPushButton, QVBoxLayout, QFormLayout, QMessageBox
)
from PyQt5.QtCore import Qt, QDate
from modules import product_manager

class BaseWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent  # 🔁 main oynasi orqali parent saqlanadi
        self.setWindowTitle("Mahsulot qo‘shish oynasi")
        self.setMinimumSize(800, 600)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.input_barcode = QLineEdit()
        self.input_barcode.returnPressed.connect(self.check_barcode)
        form_layout.addRow("📠 Barcode:", self.input_barcode)

        self.input_nomi = QLineEdit()
        form_layout.addRow("📦 Mahsulot nomi:", self.input_nomi)

        self.input_narx = QLineEdit()
        form_layout.addRow("💵 Narxi:", self.input_narx)

        self.input_miqdor = QLineEdit()
        form_layout.addRow("📊 Miqdor:", self.input_miqdor)

        self.combo_foyda_turi = QComboBox()
        self.combo_foyda_turi.addItems(["foiz", "miqdor"])
        form_layout.addRow("📈 Foyda turi:", self.combo_foyda_turi)

        self.input_foyda = QLineEdit()
        form_layout.addRow("💰 Foyda miqdori:", self.input_foyda)

        self.combo_olov_birligi = QComboBox()
        self.combo_olov_birligi.addItems(["dona", "kg", "litr"])
        form_layout.addRow("⚖️ O‘lchov birligi:", self.combo_olov_birligi)

        self.combo_kategoriya = QComboBox()
        try:
            kategoriyalar = product_manager.get_all_categories()
            self.combo_kategoriya.addItems(kategoriyalar)
        except Exception as e:
            QMessageBox.critical(self, "Xatolik", f"Kategoriya yuklanmadi:\n{str(e)}")
        form_layout.addRow("📂 Kategoriya:", self.combo_kategoriya)

        self.date_amal = QDateEdit()
        self.date_amal.setCalendarPopup(True)
        self.date_amal.setDate(QDate.currentDate())
        form_layout.addRow("📅 Amal muddati:", self.date_amal)

        btn_save = QPushButton("💾 Saqlash")
        btn_save.setStyleSheet("font-size: 16pt; padding: 10px;")
        btn_save.clicked.connect(self.save_product)

        # ✅ Savdo bo‘limiga qaytish tugmasi
        btn_to_sales = QPushButton("🛒 Savdo bo‘limi")
        btn_to_sales.setStyleSheet("padding: 10px; background-color: #ddd; border-radius: 8px;")
        btn_to_sales.clicked.connect(self.open_sales)

        layout.addLayout(form_layout)
        layout.addWidget(btn_save)
        layout.addWidget(btn_to_sales)
        self.setLayout(layout)

    def check_barcode(self):
        barcode = self.input_barcode.text()
        existing = product_manager.get_product_by_barcode(barcode)
        if existing:
            self.input_nomi.setText(existing["name"])
            self.input_nomi.setDisabled(True)
            self.combo_kategoriya.setCurrentText(existing["category"])
            self.combo_kategoriya.setDisabled(True)
        else:
            self.input_nomi.clear()
            self.input_nomi.setDisabled(False)
            self.combo_kategoriya.setDisabled(False)

    def save_product(self):
        try:
            barcode = self.input_barcode.text().strip()
            nomi = self.input_nomi.text().strip()
            narx = float(self.input_narx.text())
            miqdor = float(self.input_miqdor.text())
            foyda_turi = self.combo_foyda_turi.currentText()
            foyda_miqdori = float(self.input_foyda.text())
            olchov = self.combo_olov_birligi.currentText()
            kategoriya_nomi = self.combo_kategoriya.currentText()
            category_id = product_manager.get_category_id_by_name(kategoriya_nomi)
            amal = self.date_amal.date().toPyDate()

            product_manager.add_or_update_product(
                barcode, nomi, narx, miqdor, amal, category_id,
                foyda_turi, foyda_miqdori, olchov
            )

            QMessageBox.information(self, "✅ Muvaffaqiyatli", "Mahsulot bazaga saqlandi.")
            self.clear_form()

        except Exception as e:
            QMessageBox.critical(self, "Xatolik", f"Saqlashda xatolik:\n{str(e)}")

    def clear_form(self):
        self.input_barcode.clear()
        self.input_nomi.clear()
        self.input_narx.clear()
        self.input_miqdor.clear()
        self.input_foyda.clear()
        self.input_nomi.setDisabled(False)
        self.combo_kategoriya.setDisabled(False)

    def open_sales(self):
        from ui.sales_form import SalesWindow  # 🛠️ Circular import oldini olish
        self.hide()
        self.sales_window = SalesWindow(self.parent)
        self.sales_window.show()
