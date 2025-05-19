# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 11:36:53 2025

@author: DavrServis
"""

# ui/base_form.py

import sys
import os
import subprocess
import platform
sys.path.append(os.path.abspath("."))

from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QComboBox, QDateEdit,
    QPushButton, QVBoxLayout, QFormLayout, QMessageBox, QHBoxLayout, QSizePolicy
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from modules import product_manager

def open_virtual_keyboard():
    if platform.system() == "Windows":
        try:
            subprocess.Popen("osk.exe", shell=True)
        except Exception as e:
            print("❌ Klaviatura ochilmadi:", e)

class BaseWindow(QWidget):
    def __init__(self, parent=None):
        
        def open_main(self):
            self.hide()
            if self.parent:
                self.parent.show()

        super().__init__()
        self.parent = parent
        self.setWindowTitle("Mahsulot qo‘shish oynasi")
        self.setMinimumSize(800, 600)
        self.edit_mode = False
        self.product_id = None
        self.setup_ui()

    def open_main(self):
        self.hide()
        from main import MainWindow
        self.main_window = MainWindow()
        self.main_window.show()

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #e0f7fa, stop:1 #ffffff
                );
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(30)

        # 📦 Sarlavha
        title = QLabel("📦 Mahsulot qo‘shish")
        title.setFont(QFont("Arial", 28, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_layout = QFormLayout()
        form_layout.setSpacing(15)
        
        def styled_input():
            inp = QLineEdit()
            inp.setFont(QFont("Arial", 16))
            inp.setFixedHeight(50)
            inp.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #1976D2;
                    border-radius: 10px;
                    padding: 10px;
                    background-color: #ffffff;
                }
                QLineEdit:focus {
                    background-color: #e3f2fd;
                }
            """)
            return inp

        def styled_combo():
            combo = QComboBox()
            combo.setFont(QFont("Arial", 16))
            combo.setFixedHeight(50)
            combo.setStyleSheet("""
                QComboBox {
                    border: 2px solid #388E3C;
                    border-radius: 10px;
                    padding: 10px;
                    background-color: #f1f8e9;
                }
            """)
            return combo

        def input_with_keyboard(label_text, input_widget):
            label = QLabel(label_text)
            label.setFont(QFont("Arial", 14))

            btn_kb = QPushButton("⌨️")
            btn_kb.setFixedSize(50, 50)
            btn_kb.clicked.connect(open_virtual_keyboard)

            row = QHBoxLayout()
            row.addWidget(input_widget)
            row.addWidget(btn_kb)

            form_layout.addRow(label, row)
            
        # --- Kiritish maydonlari ---
        self.input_barcode = styled_input()
        self.input_barcode.returnPressed.connect(self.check_barcode)
        input_with_keyboard("📠 Barcode:", self.input_barcode)

        self.input_nomi = styled_input()
        input_with_keyboard("📦 Mahsulot nomi:", self.input_nomi)
        
        self.input_narx = styled_input()
        input_with_keyboard("💵 Sotuv narxi:", self.input_narx)
        
        self.input_xarid_narxi = styled_input()
        input_with_keyboard("💸 Xarid narxi:", self.input_xarid_narxi)
        
        self.input_miqdor = styled_input()
        input_with_keyboard("📊 Miqdor:", self.input_miqdor)

        self.combo_foyda_turi = styled_combo()
        self.combo_foyda_turi.addItem("Foiz", "percent")
        self.combo_foyda_turi.addItem("Miqdor", "fixed")
        lbl = QLabel("📈 Foyda turi:")
        lbl.setFont(QFont("Arial", 14))
        form_layout.addRow(lbl, self.combo_foyda_turi)

        self.input_foyda = styled_input()
        input_with_keyboard("💰 Foyda miqdori:", self.input_foyda)
        
        self.combo_olov_birligi = styled_combo()
        self.combo_olov_birligi.addItems(["dona", "kg", "litr"])
        lbl = QLabel("⚖️ O‘lchov birligi:")
        lbl.setFont(QFont("Arial", 14))
        form_layout.addRow(lbl, self.combo_olov_birligi)
            
        self.combo_kategoriya = styled_combo()
        try:
            kategoriyalar = product_manager.get_all_categories()
            self.combo_kategoriya.addItems(kategoriyalar)
        except Exception as e:
            QMessageBox.critical(self, "Xatolik", f"Kategoriya yuklanmadi:\n{str(e)}")
        lbl = QLabel("📂 Kategoriya:")
        lbl.setFont(QFont("Arial", 14))
        form_layout.addRow(lbl, self.combo_kategoriya)

        self.date_amal = QDateEdit()
        self.date_amal.setFont(QFont("Arial", 16))
        self.date_amal.setFixedHeight(50)
        self.date_amal.setCalendarPopup(True)
        self.date_amal.setDate(QDate.currentDate())
        self.date_amal.setStyleSheet("""
            QDateEdit {
                border: 2px solid #FF9800;
                border-radius: 10px;
                padding: 10px;
                background-color: #fff3e0;
            }
        """)
        lbl = QLabel("📅 Amal muddati:")
        lbl.setFont(QFont("Arial", 14))
        form_layout.addRow(lbl, self.date_amal)

        # --- Tugmalar ---
        btn_save = QPushButton("💾 Saqlash")
        btn_save.setFont(QFont("Arial", 16))
        btn_save.setFixedSize(250, 70)
        btn_save.setStyleSheet("background-color: #3498db; color: white; border-radius: 10px;")
        btn_save.clicked.connect(self.save_product)

        btn_to_sales = QPushButton("🛒 Savdo bo‘limi")
        btn_to_sales.setFont(QFont("Arial", 16))
        btn_to_sales.setFixedSize(250, 70)
        btn_to_sales.setStyleSheet("background-color: #2ecc71; color: white; border-radius: 10px;")
        btn_to_sales.clicked.connect(self.open_sales)
        
        button_row = QHBoxLayout()
        button_row.setAlignment(Qt.AlignCenter)
        button_row.setSpacing(30)
        button_row.addWidget(btn_save)
        button_row.addWidget(btn_to_sales)

        # --- Tartibga keltirish ---
        layout.addLayout(form_layout)
        layout.addLayout(button_row)
        self.setLayout(layout)
        
        
    def check_barcode(self):
        barcode = self.input_barcode.text()
        existing = product_manager.get_product_by_barcode(barcode)
        if existing:
            self.input_nomi.setText(existing["name"])
            self.input_nomi.setDisabled(True)
            category_name = product_manager.get_category_name_by_id(existing["category_id"])
            self.combo_kategoriya.setCurrentText(category_name)
            self.combo_kategoriya.setDisabled(False)
        else:
            self.input_nomi.clear()
            self.input_nomi.setDisabled(False)
            self.combo_kategoriya.setDisabled(False)

    def save_product(self):
        try:
            barcode = self.input_barcode.text().strip()
            nomi = self.input_nomi.text().strip()
            sotuv_narxi = float(self.input_narx.text())
            xarid_narxi = float(self.input_xarid_narxi.text())
            miqdor = float(self.input_miqdor.text())
            foyda_turi = self.combo_foyda_turi.currentData()
            foyda_miqdori = float(self.input_foyda.text())
            olchov = self.combo_olov_birligi.currentText()
            kategoriya_nomi = self.combo_kategoriya.currentText()
            category_id = product_manager.get_category_id_by_name(kategoriya_nomi)
            amal = self.date_amal.date().toPyDate()

            if self.edit_mode and self.product_id:
                product_manager.update_product(
                    self.product_id, nomi, sotuv_narxi, miqdor, category_id
                )
            else:
                product_manager.add_or_update_product(
                    barcode, nomi, sotuv_narxi, miqdor, amal, category_id,
                    foyda_turi, foyda_miqdori, olchov, xarid_narxi
                )

            QMessageBox.information(self, "✅ Muvaffaqiyatli", "Mahsulot saqlandi yoki yangilandi.")
            self.clear_form()

        except Exception as e:
            QMessageBox.critical(self, "Xatolik", f"Saqlashda xatolik:\n{str(e)}")

    def clear_form(self):
        self.input_barcode.clear()
        self.input_nomi.clear()
        self.input_narx.clear()
        self.input_xarid_narxi.clear()
        self.input_miqdor.clear()
        self.input_foyda.clear()
        self.input_nomi.setDisabled(False)
        self.combo_kategoriya.setDisabled(False)
        self.edit_mode = False
        self.product_id = None

    def open_sales(self):
        from ui.sales_form import SalesWindow
        self.sales_window = SalesWindow(current_user_id=None)
        self.hide()
        self.sales_window.showMaximized()
