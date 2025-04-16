# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 11:26:06 2025

@author: DavrServis
"""

# main.py

import sys
import os

# Loyihaning ildiz papkasini sys.path ga qo‘shish
BASE_DIR = os.path.abspath(".")
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget,
    QVBoxLayout, QLabel, QMessageBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

from ui.sales_form import SalesWindow
from ui.base_form import BaseWindow  # Baza oynasi uchun

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Market - Rejim tanlang")
        self.setGeometry(100, 100, 1024, 1280)
        self.setWindowState(Qt.WindowMaximized)

        # Asosiy interfeys
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        label = QLabel("🛒 Dastur rejimini tanlang:")
        label.setStyleSheet("font-size: 32pt; margin-bottom: 40px;")
        layout.addWidget(label)

        # Savdo tugmasi
        btn_sales = QPushButton("  Savdo rejimi")
        btn_sales.setIcon(QIcon("icons/sales.png"))
        btn_sales.setIconSize(QSize(96, 96))
        btn_sales.setStyleSheet("font-size: 28pt; padding: 40px; text-align: left;")
        btn_sales.clicked.connect(self.open_sales)

        # Baza tugmasi
        btn_base = QPushButton("  Baza rejimi")
        btn_base.setIcon(QIcon("icons/base.png"))
        btn_base.setIconSize(QSize(96, 96))
        btn_base.setStyleSheet("font-size: 28pt; padding: 40px; text-align: left;")
        btn_base.clicked.connect(self.open_base)

        layout.addWidget(btn_sales)
        layout.addWidget(btn_base)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_sales(self):
        self.sales_window = SalesWindow()
        self.sales_window.setWindowTitle("Savdo Rejimi")
        self.sales_window.showMaximized()
        self.hide()

    def open_base(self):
        self.base_window = BaseWindow()
        self.base_window.setWindowTitle("Mahsulot Bazasi")
        self.base_window.showMaximized()
        self.hide()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Chiqish",
            "Haqiqatan dasturdan chiqmoqchimisiz?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
