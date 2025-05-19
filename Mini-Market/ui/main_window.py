# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 02:35:17 2025

@author: DavrServis
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from ui.sales_form import SalesWindow
from ui.base_form import BaseWindow
from modules.shift_manager import is_shift_open


class ModeSelectionWindow(QWidget):
    def __init__(self, current_user, current_role, current_user_id, parent=None):
        super().__init__(parent)
        self.current_user = current_user
        self.current_role = current_role
        self.current_user_id = current_user_id

        self.sales_window = None
        self.base_window = None

        self.setWindowTitle("🛒 Rejim tanlash")
        self.setFixedSize(650, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                                  stop:0 #f0fdf4, stop:1 #ffffff);
            }
        """)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)
        layout.setAlignment(Qt.AlignTop)

        self.label_info = QLabel(f"👤 Foydalanuvchi: {self.current_user} ({self.current_role})")
        self.label_info.setFont(QFont("Arial", 20, QFont.Bold))
        self.label_info.setAlignment(Qt.AlignCenter)
        self.label_info.setStyleSheet("""
            color: #1b5e20;
            background-color: #d0f8ce;
            padding: 16px;
            border-radius: 14px;
            border: 2px solid #a5d6a7;
        """)
        layout.addWidget(self.label_info)

        layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed))

        self.btn_sales = QPushButton("🛒  Savdo qilish")
        self.btn_base = QPushButton("📦  Mahsulot Bazasi")
        button_style = """
            QPushButton {
                background-color: #ffffff;
                color: #333333;
                border: 2px solid #9e9e9e;
                border-radius: 10px;
                padding: 12px;
                font-size: 24px;
                qproperty-iconSize: 40px;
                text-align: center;
            }
            QPushButton:hover {
                border: 2px solid #1976D2;
                background-color: #f0f0f0;
            }
        """  

        for btn in [self.btn_sales, self.btn_base]:
            btn.setStyleSheet(button_style)
            btn.setFont(QFont("Arial", 28, QFont.Bold))
            btn.setMinimumHeight(120)
            btn.setMinimumWidth(400)
            layout.addWidget(btn, alignment=Qt.AlignHCenter)

        layout.addStretch()
        self.setLayout(layout)

        self.btn_sales.clicked.connect(self.open_sales)
        self.btn_base.clicked.connect(self.open_base)
        
    def open_sales(self):
        self.sales_window = SalesWindow(current_user_id=self.current_user_id)
        self.hide()
        self.sales_window.showMaximized()

    def open_base(self):
        self.base_window = BaseWindow(parent=self)
        self.hide()
        self.base_window.showMaximized()

    



