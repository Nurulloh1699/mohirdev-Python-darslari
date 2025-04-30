# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 09:44:08 2025

@author: DavrServis
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout,
    QHBoxLayout, QFrame, QStackedLayout, QSizePolicy, QScrollArea
)
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

# --- YANGI TUZILMA IMPORTLARI ---
from modules.product_manager import get_products_by_category  # mavjud bo'lsa
from modules.cart_manager import CartManager  # yangi modul bo'lib qo'shiladi

class MiniMarketTouchUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Market POS - Touch UI")
        self.setGeometry(0, 0, 1280, 1024)
        self.setStyleSheet("background-color: #f8f8f8;")

        self.cart = CartManager()  # 🛒 Savat obyekti
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()

        self.stack_layout = QStackedLayout()
        self.category_panel = self.create_category_panel()
        self.product_panel = self.create_product_list_panel()
        self.stack_layout.addWidget(self.category_panel)
        self.stack_layout.addWidget(self.product_panel)
        self.stack_layout.setCurrentIndex(0)

        stack_container = QFrame()
        stack_container.setLayout(self.stack_layout)
        main_layout.addWidget(stack_container, 2)

        sales_panel = self.create_sales_panel()
        main_layout.addWidget(sales_panel, 3)

        central_widget.setLayout(main_layout)

    def create_category_panel(self):
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        label = QLabel("\U0001F4C2 Kategoriyalar")
        label.setFont(QFont("Arial", 32, QFont.Bold))
        layout.addWidget(label)

        categories = [
            ("Sut mahsulotlari", "icons/milk_products.png"),
            ("Go'sht va kolbasa mahsulotlari", "icons/sousages.png"),
            ("Mevalar", "icons/fruits.png"),
            ("Sabzavotlar", "icons/vegetables.png"),
            ("Ichimliklar", "icons/drinks.png"),
            ("Shirinliklar (shkalat va pechenyelar)", "icons/sweets.png"),
            ("Kiloli mahsulotlar (guruch, shakar, un)", "icons/overweight_products.png"),
            ("Non mahsulotlari", "icons/breads.png"),
            ("Yog'lar", "icons/oil_products.png")
        ]

        for name, icon_path in categories:
            btn = QPushButton(name)
            btn.setFont(QFont("Arial", 16))
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(48, 48))
            btn.setFixedHeight(90)
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding-left: 20px;
                    background-color: white;
                    border: 2px solid #ddd;
                    border-radius: 12px;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
            """)
            btn.clicked.connect(lambda checked, category=name: self.show_products(category))
            layout.addWidget(btn)

        frame.setLayout(layout)
        return frame

    def create_product_list_panel(self):
        frame = QFrame()
        layout = QVBoxLayout()

        top_layout = QHBoxLayout()

        back_btn = QPushButton("\u25C0\uFE0F")
        back_btn.setFont(QFont("Arial", 18))
        back_btn.setFixedSize(60, 60)
        back_btn.setStyleSheet("border-radius: 30px; background-color: #ddd;")
        back_btn.clicked.connect(self.back_to_categories)
        top_layout.addWidget(back_btn)

        self.category_title = QLabel("")
        self.category_title.setFont(QFont("Arial", 28, QFont.Bold))
        top_layout.addWidget(self.category_title)
        top_layout.addStretch()

        layout.addLayout(top_layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        self.products_layout = QVBoxLayout()
        scroll_content.setLayout(self.products_layout)
        scroll.setWidget(scroll_content)

        layout.addWidget(scroll)
        frame.setLayout(layout)
        return frame

    def show_products(self, category_name):
        for i in reversed(range(self.products_layout.count())):
            self.products_layout.itemAt(i).widget().setParent(None)

        for i in range(5):
            lbl = QLabel(f"\U0001F6D2 {category_name} mahsuloti {i+1}")
            lbl.setFont(QFont("Arial", 18))
            lbl.setStyleSheet("padding: 10px; background-color: white; border: 1px solid #ccc; border-radius: 10px;")
            self.products_layout.addWidget(lbl)

        self.category_title.setText(f"\U0001F4E6 {category_name}")
        self.stack_layout.setCurrentIndex(1)

    def back_to_categories(self):
        self.stack_layout.setCurrentIndex(0)

    def create_sales_panel(self):
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setSpacing(20)

        label = QLabel("\U0001F6D2 Savat")
        label.setFont(QFont("Arial", 28, QFont.Bold))
        layout.addWidget(label)

        self.cart_display = QTextEdit()
        self.cart_display.setFont(QFont("Courier", 18))
        self.cart_display.setReadOnly(True)
        self.cart_display.setText("")
        layout.addWidget(self.cart_display)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(30)
        btn_layout.setAlignment(Qt.AlignCenter)

        btn_menu = QPushButton("Bosh menyu")
        btn_menu.setFont(QFont("Arial", 18))
        btn_menu.setFixedSize(250, 100)
        btn_menu.setStyleSheet("background-color: #e0e0e0; border-radius: 12px;")
        btn_layout.addWidget(btn_menu)

        btn_remove = QPushButton("Olib tashlash")
        btn_remove.setFont(QFont("Arial", 18))
        btn_remove.setFixedSize(250, 100)
        btn_remove.setStyleSheet("background-color: #e74c3c; color: white; border-radius: 12px;")
        btn_layout.addWidget(btn_remove)

        btn_purchase = QPushButton("Xarid qilish")
        btn_purchase.setFont(QFont("Arial", 18))
        btn_purchase.setFixedSize(250, 100)
        btn_purchase.setStyleSheet("background-color: #3498db; color: white; border-radius: 12px;")
        btn_layout.addWidget(btn_purchase)

        layout.addLayout(btn_layout)

        frame.setLayout(layout)
        return frame

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiniMarketTouchUI()
    window.show()
    sys.exit(app.exec_())
