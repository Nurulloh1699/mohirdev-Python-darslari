# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 14:19:34 2025

@author: DavrServis
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton,
    QLabel, QListWidget, QListWidgetItem, QLineEdit, QScrollArea, QFrame
)
from PyQt5.QtCore import Qt

class SalesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Market - Savdo")
        self.setGeometry(0, 0, 1280, 1024)
        self.showFullScreen()  # To‘liq ekran rejimi

        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Chap panel: Kategoriyalar
        category_panel = self.create_category_panel()
        main_layout.addWidget(category_panel, 2)  # 2/5 ulushi

        # O‘ng panel: Savatcha
        sales_panel = self.create_sales_panel()
        main_layout.addWidget(sales_panel, 3)  # 3/5 ulushi

    def create_category_panel(self):
        panel = QWidget()
        layout = QVBoxLayout()
        panel.setLayout(layout)

        label = QLabel("Kategoriyalar")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # Kategoriya tugmalar ro'yxati (hozircha statik)
        categories = [
            "Ichimliklar", "Shirinliklar", "Go'sht", "Sabzavotlar", "Mevalar",
            "Yog‘lar", "Non mahsulotlari", "Sut", "Yarim tayyor", "Konserva"
        ]

        for cat in categories:
            btn = QPushButton(cat)
            btn.setFixedHeight(60)
            layout.addWidget(btn)

        layout.addStretch()
        return panel

    def create_sales_panel(self):
        panel = QWidget()
        layout = QVBoxLayout()
        panel.setLayout(layout)

        label = QLabel("Savat")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.cart_list = QListWidget()
        layout.addWidget(self.cart_list)

        # Qidiruv maydoni
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Barcode yoki mahsulot nomi...")
        layout.addWidget(self.search_input)

        layout.addStretch()
        return panel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SalesForm()
    window.show()
    sys.exit(app.exec_())
