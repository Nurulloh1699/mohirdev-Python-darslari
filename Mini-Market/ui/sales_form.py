# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 11:36:30 2025

@author: DavrServis
"""

# ui/sales_form.py

from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout,
    QHBoxLayout, QFrame, QStackedLayout, QSizePolicy, QScrollArea
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize
from modules.product_manager import get_products_by_category
from ui.base_form import BaseWindow  # ✅ Qo‘shildi

class SalesWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent  # main.py orqali kelgan parent
        self.setWindowTitle("Mini Market - Savdo")
        self.setGeometry(0, 0, 1280, 1024)
        self.setStyleSheet("background-color: #f8f8f8;")

        self.init_ui()

    def init_ui(self):
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

        self.setLayout(main_layout)

    def create_category_panel(self):
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        label = QLabel("📂 Kategoriyalar")
        label.setFont(QFont("Arial", 32, QFont.Bold))
        layout.addWidget(label)

        categories = [
            ("Ichimliklar", "icons/drinks.png"),
            ("Shirinliklar", "icons/sweets.png"),
            ("Kiloli mahsulotlar", "icons/overweight_products.png"),
            ("Non mahsulotlari", "icons/breads.png"),
            ("Yog'lar", "icons/oil_products.png"),
            ("Chipslar", "icons/chips.png")
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

        # ✅ Baza bo‘limiga o‘tish tugmasi
        btn_to_base = QPushButton("📦 Baza bo‘limi")
        btn_to_base.setFont(QFont("Arial", 14))
        btn_to_base.setStyleSheet("padding: 10px; background-color: #ddd; border-radius: 8px;")
        btn_to_base.clicked.connect(self.open_base)
        layout.addWidget(btn_to_base)

        frame.setLayout(layout)
        return frame

    def create_product_list_panel(self):
        frame = QFrame()
        layout = QVBoxLayout()

        top_layout = QHBoxLayout()
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
        from functools import partial
        for i in reversed(range(self.products_layout.count())):
            self.products_layout.itemAt(i).widget().setParent(None)

        products = get_products_by_category(category_name)

        if not products:
            lbl = QLabel("Mahsulotlar topilmadi")
            lbl.setFont(QFont("Arial", 18))
            self.products_layout.addWidget(lbl)
        else:
            for product in products:
                product_name = product["name"]
                product_price = product["sale_price"]
                btn = QPushButton(f"🛒 {product_name} - {product_price} so'm")
                btn.setFont(QFont("Arial", 18))
                btn.setStyleSheet("padding: 12px; background-color: white; border: 1px solid #ccc; border-radius: 10px;")
                btn.clicked.connect(partial(self.add_to_cart_display, product_name, product_price))
                self.products_layout.addWidget(btn)

        self.category_title.setText(f"📦 {category_name}")
        self.stack_layout.setCurrentIndex(1)

    def add_to_cart_display(self, name, price):
        current_text = self.cart_display.toPlainText()
        new_line = f"{name} - {price} so'm"
        updated = f"{current_text}\n{new_line}" if current_text else new_line
        self.cart_display.setText(updated)

    def create_sales_panel(self):
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setSpacing(20)

        label = QLabel("🛒 Savat")
        label.setFont(QFont("Arial", 28, QFont.Bold))
        layout.addWidget(label)

        self.cart_display = QTextEdit()
        self.cart_display.setFont(QFont("Courier", 18))
        self.cart_display.setReadOnly(True)
        self.cart_display.setText("")
        layout.addWidget(self.cart_display)

        frame.setLayout(layout)
        return frame

    def open_base(self):
        self.hide()
        self.base_window = BaseWindow(self.parent)
        self.base_window.show()


