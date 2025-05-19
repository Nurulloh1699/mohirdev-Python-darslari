# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 21:48:14 2025

@author: DavrServis
"""

from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout, QFormLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from modules.login_manager import authenticate_user
from ui.role_based_main_window import RoleBasedMainWindow
from ui.main_window import ModeSelectionWindow

class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("🛒 Mini Market Login")
        self.setFixedSize(650, 450)
        self.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #e3f2fd, stop:1 #ffffff);")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(60, 40, 60, 40)
        layout.setSpacing(30)

        title = QLabel("🛒 Mini Market Login")
        title.setFont(QFont("Arial", 30, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_layout = QFormLayout()
        form_layout.setSpacing(20)

        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("👤 Foydalanuvchi nomi")
        self.input_username.setFont(QFont("Arial", 18))
        self.input_username.setFixedHeight(60)
        self.input_username.setStyleSheet("""
            QLineEdit {
                background-color: #f9f9f9;
                border: 2px solid #9e9e9e;
                border-radius: 12px;
                padding: 12px;
                font-size: 18px;
            }
            QLineEdit:focus {
                border: 2px solid #1976D2;
                background-color: #ffffff;
            }
        """)
        login_label = QLabel("👤 Login:")
        login_label.setFont(QFont("Arial", 18, QFont.Bold))
        form_layout.addRow(login_label, self.input_username)

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("🔒 Parol")
        self.input_password.setFont(QFont("Arial", 18))
        self.input_password.setFixedHeight(60)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 12px;
                padding-left: 12px;
                background-color: white;
                font-size: 18px;
            }
            QLineEdit:focus {
                border: 2px solid #2196F3;
            }
        """)

        self.toggle_password_btn = QPushButton("👁")
        self.toggle_password_btn.setCheckable(True)
        self.toggle_password_btn.setFixedSize(60, 60)
        self.toggle_password_btn.setStyleSheet("""
            QPushButton {
                background-color: #f5f5f5;
                border: 1px solid #ccc;
                border-radius: 10px;
                font-size: 22px;
            }
            QPushButton:checked {
                background-color: #e0e0e0;
            }
        """)

        def toggle_password():
            if self.toggle_password_btn.isChecked():
                self.input_password.setEchoMode(QLineEdit.Normal)
                self.toggle_password_btn.setText("🚫")
            else:
                self.input_password.setEchoMode(QLineEdit.Password)
                self.toggle_password_btn.setText("👁")

        self.toggle_password_btn.clicked.connect(toggle_password)

        password_row = QHBoxLayout()
        password_row.addWidget(self.input_password)
        password_row.addWidget(self.toggle_password_btn)
        password_label = QLabel("🔑 Parol:")
        password_label.setFont(QFont("Arial", 18, QFont.Bold))
        form_layout.addRow(password_label, password_row)

        layout.addLayout(form_layout)

        btn_login = QPushButton("✅ Kirish")
        btn_login.setFont(QFont("Arial", 30, QFont.Bold))
        btn_login.setFixedHeight(70)
        btn_login.setStyleSheet("""
            QPushButton {
                background-color: #43a047;
                color: white;
                border-radius: 14px;
                font-size: 22px;
                padding: 16px;
            }
            QPushButton:hover {
                background-color: #388e3c;
            }
        """)
        btn_login.clicked.connect(self.handle_login)
        layout.addWidget(btn_login)

        layout.addStretch()
        self.setLayout(layout)

    def handle_login(self):
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "⚠️ Xatolik", "Iltimos, login va parolni kiriting.")
            return

        user = authenticate_user(username, password)

        if user:
            user_id = user.get("id")
            user_role = user.get("role")
            user_full_name = user.get("full_name", "")

            QMessageBox.information(self, "✅ Kirish", f"Xush kelibsiz, {user_full_name} ({user_role})!")
            self.close()

            if user_role == "admin":
                self.main_window = ModeSelectionWindow(
                    current_user=username,
                    current_role=user_role,
                    current_user_id=user_id
                )
            elif user_role == "kassir":
                self.main_window = RoleBasedMainWindow(
                    current_user=username,
                    current_role=user_role,
                    current_user_id=user_id
                )
            else:
                QMessageBox.critical(self, "❌ Xatolik", "Noto‘g‘ri foydalanuvchi roli!")
                return

            self.main_window.show()
        else:
            QMessageBox.critical(self, "❌ Xatolik", "Login yoki parol noto‘g‘ri!")





        

