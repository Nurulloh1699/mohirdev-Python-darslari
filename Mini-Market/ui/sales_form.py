# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 11:36:30 2025

@author: DavrServis
"""

# ui/sales_form.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import subprocess
import platform


from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QFrame, QStackedLayout, QScrollArea,
    QInputDialog, QMessageBox, QComboBox, QDialog,
    QFormLayout, QLineEdit, QGridLayout, QSizePolicy, QApplication
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize, QTimer
from functools import partial
from decimal import Decimal
from datetime import datetime

from modules.shift_manager import is_shift_open
from modules.product_manager import get_products_by_category, get_product_by_barcode
from modules.sales_manager import start_sale, finalize_sale
from modules.printer_manager import ReceiptPrinter
from ui.base_form import BaseWindow
from ui.credits_form import CreditsWindow  # yangi tugmani ochish uchun kerak

class SalesWindow(QWidget):
    def __init__(self, parent=None, current_user_id=None):
        super().__init__(parent)
        print("🟢 SalesWindow __init__ boshlandi")
        self.current_user_id = current_user_id
        self.parent = parent
        self.cart = {}

        self.setWindowTitle("🛒 Mini Market Savdo")
        self.setStyleSheet("background-color: #f5f5f5;")
        self.init_ui()

        self.barcode_input.clear()
        self.barcode_input.setFocus()
        self.showMaximized()
        print("✅ SalesWindow __init__ tugadi")
        self.show()  # showMaximized dan tashqari, faqat show() ham bo‘lsin
        print("📢 SalesWindow show() chaqirildi")
        print("SalesWindow SHOW EVENT!")  # 🔍 Logging
        self.setWindowModality(Qt.NonModal)  # ⚠️ Child modal emas



    def showEvent(self, event):
        print("🟢 SalesWindow SHOW EVENT!")  # terminalga chiqadi
        super().showEvent(event)
        
    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()

    def open_main(self):
        from ui.role_based_main_window import RoleBasedMainWindow
        self.main_window = RoleBasedMainWindow(current_user="kassir", current_role="kassir", current_user_id=self.current_user_id)
        self.main_window.show()
        self.close()

    def init_ui(self):
        print("🟢 SalesWindow __init__ boshlandi")

        # 🔳 Asosiy layoutlar
        main_layout = QHBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # 🧩 Kategoriya paneli va mahsulotlar paneli (chap)
        self.stack_layout = QStackedLayout()
        self.category_panel = self.create_category_panel()
        self.product_panel = self.create_product_list_panel()
        self.stack_layout.addWidget(self.category_panel)
        self.stack_layout.addWidget(self.product_panel)
        self.stack_layout.setCurrentIndex(0)
        
        stack_container = QFrame()
        stack_container.setLayout(self.stack_layout)
        main_layout.addWidget(stack_container, 2)  # ⚖️ 2/5 joy

        # 🛒 Savat paneli (o‘ng)
        sales_panel = self.create_sales_panel()
        main_layout.addWidget(sales_panel, 3)  # ⚖️ 3/5 joy
    
        
    
        # 📦 Barcha layoutlarni o‘rash
        wrapper_layout = QVBoxLayout()
        wrapper_layout.addLayout(main_layout)
        self.setLayout(wrapper_layout)

        # 🔁 Fokusni doimiy tekshirish
        self.focus_timer = QTimer()
        self.focus_timer.timeout.connect(self.ensure_barcode_focus)
        self.focus_timer.start(1000)

        print("✅ SalesWindow __init__ tugadi")

    def open_virtual_keyboard(self):  # ✅ SHU YERDA BO‘LSIN
        if platform.system() == "Windows":
            subprocess.Popen("osk.exe", shell=True)

    
    def closeEvent(self, event):
        self.focus_timer.stop()
        event.accept()

    
    def open_credits(self):
        from ui.credits_form import CreditsWindow
        self.credits_window = CreditsWindow()
        self.credits_window.show()

        
    def open_main(self):
        self.close()        # yoki self.hide()
        if self.parent:
            self.parent.show()


    def create_category_panel(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setAlignment(Qt.AlignTop)

        label = QLabel("📂 Kategoriyalar")
        label.setFont(QFont("Arial", 24, QFont.Bold))
        layout.addWidget(label)

        # Grid layout: tugmalarni 3 ustunli panjarada joylash
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        categories = [
            ("Ichimliklar", "icons/drinks.png"),
            ("Shirinliklar", "icons/sweets.png"),
            ("Kiloli mahsulotlar", "icons/overweight_products.png"),
            ("Non mahsulotlari", "icons/breads.png"),
            ("Yog'lar", "icons/oil_products.png"),
            ("Chipslar", "icons/chips.png"),
            ("Kanservalar", "icons/canned_food.png"),
            ("Makaronlar", "icons/pasta.png"),
            ("Tuz va shakar", "icons/sugars.png"),
            ("Mayanezlar", "icons/mayonnaise.png"),
            ("Kashalar", "icons/cereal_products.png"),
            ("O'yinchoqlar", "icons/toys.png"),
            ("Ximiya", "icons/chemistry.png"),
            ("Sutli mahsulotlar", "icons/milk_products.png"),
            ("Choylar", "icons/tea.png"),
            ("Ziravorlar", "icons/spices.png"),
            ("Kolbasalar", "icons/sousages.png"),
            ("Semechkalar", "icons/sunflower_seeds.png")
        ]

        columns = 3  # ✅ 3 ta tugma har bir qatorga
        for idx, (name, icon_path) in enumerate(categories):
            btn = QPushButton(name)
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(64, 64))
            btn.setFixedSize(220, 100)
            btn.setFont(QFont("Arial", 13))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #e3f2fd;
                    border: 2px solid #64b5f6;
                    border-radius: 10px;
                    font-size: 22px;
                    text-align: center;
                }
                QPushButton:hover {
                    background-color: #eaeaea;
                }
            """)
            btn.clicked.connect(lambda _, c=name: self.show_products(c))
            row = idx // columns
            col = idx % columns
            self.grid.addWidget(btn, row, col)

        layout.addLayout(self.grid)
        scroll_area.setWidget(container)
        return scroll_area



    def create_product_list_panel(self):
        frame = QFrame()
        layout = QVBoxLayout()

        # 📦 Kategoriya sarlavhasi va orqaga tugmasi
        top_layout = QHBoxLayout()
        self.category_title = QLabel("")
        self.category_title.setFont(QFont("Arial", 24, QFont.Bold))
        top_layout.addWidget(self.category_title)
        top_layout.addStretch()

        back_btn = QPushButton("⬅️")
        back_btn.setFixedSize(70, 70)
        back_btn.setFont(QFont("Arial", 22))
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: #fff3e0;
                border: 2px solid #ffb74d;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ffe0b2;
            }
        """)
        back_btn.clicked.connect(self.back_to_categories)
        top_layout.addWidget(back_btn)
        

        layout.addLayout(top_layout)
        
        # 🔍 Qidiruv qatori
        self.search_input = QLineEdit()
        self.search_input.setFont(QFont("Arial", 16))
        self.search_input.setFixedHeight(70)
        self.search_input.setPlaceholderText("🔍 Mahsulot nomini yozing...")
        self.search_input.returnPressed.connect(self.filter_products)
        
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #43A047;
                border-radius: 12px;
                padding: 12px;
            }
            QLineEdit:focus {
                background-color: #e8f5e9;
                border: 2px solid #1B5E20;
            }
        """)


        btn_clear = QPushButton("❌")
        btn_clear.setFixedSize(70, 70)
        btn_clear.clicked.connect(lambda: self.search_input.clear())
        
        btn_clear.setStyleSheet("""
            QPushButton {
                background-color: #fbe9e7;
                border: 2px solid #ef5350;
                border-radius: 10px;
                font-size: 22px;
                color: #b71c1c;
            }
            QPushButton:hover {
                background-color: #ffcdd2;
            }
        """)


        kb_btn_search = QPushButton("⌨️")
        kb_btn_search.setFixedSize(70, 70)
        kb_btn_search.clicked.connect(self.open_virtual_keyboard)
        
        kb_btn_search.setStyleSheet("""
            QPushButton {
                background-color: #e3f2fd;
                border: 2px solid #64b5f6;
                border-radius: 10px;
                font-size: 22px;
            }
            QPushButton:hover {
                background-color: #bbdefb;
            }
        """)


        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(btn_clear)
        search_layout.addWidget(kb_btn_search)
        layout.addLayout(search_layout)

        
    
        # 🔽 Mahsulotlar ro‘yxati (scroll + grid)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        self.products_grid = QGridLayout()
        self.products_grid.setSpacing(10)
        self.products_grid.setAlignment(Qt.AlignTop)
        scroll_content.setLayout(self.products_grid)
        scroll.setWidget(scroll_content)

        layout.addWidget(scroll)
        frame.setLayout(layout)
        return frame




    def back_to_categories(self):
        self.stack_layout.setCurrentIndex(0)
        

    def show_products(self, category_name):
        from modules.product_manager import get_products_by_category

        # 🧹 Eski tugmalarni tozalash
        for i in reversed(range(self.products_grid.count())):
            widget = self.products_grid.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        products = get_products_by_category(category_name)

        # 🔍 Qidiruv filtri
        query = self.search_input.text().strip().lower()
        if query:
            products = [p for p in products if query in p["name"].lower()]

        if not products:
            lbl = QLabel("❌ Mahsulot topilmadi")
            lbl.setFont(QFont("Arial", 16))
            self.products_grid.addWidget(lbl, 0, 0)
        else:
            row = 0
            col = 0
            for product in products:
                barcode = product["barcode"]
                name = product["name"]
                price = product["sale_price"]
                
                btn = QPushButton(f"{name}\n{int(price)} so'm")
                btn.setFont(QFont("Arial", 11))  # Kichikroq font
                btn.setFixedSize(200, 90)
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: white;
                        border: 1px solid #ccc;
                        border-radius: 10px;
                        text-align: left;
                        padding: 6px;
                        }
                    QPushButton:hover {
                        background-color: #f0f0f0;
                        }
                    """)

                btn.clicked.connect(partial(self.add_to_cart, barcode))

                self.products_grid.addWidget(btn, row, col)

                col += 1
                if col == 2:  # Har 2 tugmadan keyin yangi qator
                    col = 0
                    row += 1

        # 📦 Kategoriya sarlavhasi
        self.category_title.setText(f"📦 {category_name}")
        self.stack_layout.setCurrentIndex(1)

        
    def add_to_cart(self, barcode):
        print(f"➕ Savatga qo‘shilmoqda: {barcode}")  # TEST QATOR
        from modules.product_manager import get_product_by_barcode  # ehtiyotkorlik uchun

        product = get_product_by_barcode(barcode)
        if not product:
            QMessageBox.warning(self, "❗ Tovar topilmadi", f"Barcode: {barcode} bazada mavjud emas.")
            return

        name = product["name"]
        price = float(product["sale_price"])

        if barcode in self.cart:
            self.cart[barcode]["quantity"] += 1
        else:
            self.cart[barcode] = {"name": name, "price": price, "quantity": 1}

        self.refresh_cart_display()



    def change_quantity(self, barcode, delta):
        if barcode in self.cart:
            self.cart[barcode]["quantity"] += delta
            if self.cart[barcode]["quantity"] <= 0:
                del self.cart[barcode]
            self.refresh_cart_display()

    def clear_cart(self):
        self.cart.clear()
        self.refresh_cart_display()

    def refresh_cart_display(self):
        # Eski elementlarni tozalash
        for i in reversed(range(self.cart_layout.count())):
            widget = self.cart_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        for barcode, item in self.cart.items():
            name = item["name"]
            price = item["price"]
            quantity = item["quantity"]
            
            row = QHBoxLayout()
            row.setSpacing(10)

            label = QLabel(f"{name} | {quantity} x {price} = {int(quantity * price)} so'm")
            label.setFont(QFont("Arial", 14))
            label.setStyleSheet("color: #333;")

            minus_btn = QPushButton("➖")
            plus_btn = QPushButton("➕")

            for btn in (minus_btn, plus_btn):
                btn.setFixedSize(40, 40)
                btn.setFont(QFont("Arial", 16))
                btn.setStyleSheet("background-color: #eee; font-size: 14pt;")

            minus_btn.clicked.connect(lambda _, b=barcode: self.change_quantity(b, -1))
            plus_btn.clicked.connect(lambda _, b=barcode: self.change_quantity(b, 1))

            row.addWidget(label)
            row.addWidget(minus_btn)
            row.addWidget(plus_btn)

            container = QWidget()
            container.setLayout(row)
            container.setStyleSheet("""
                QWidget {
                    background-color: #f9f9f9;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    padding: 6px;
                    }
                """)

            self.cart_layout.addWidget(container)
        total_sum = sum(item["price"] * item["quantity"] for item in self.cart.values())
        self.total_label.setText(f"Umumiy: {int(total_sum)} so'm")



    def handle_barcode_entered(self):
        barcode = self.barcode_input.text().strip()
        print(f"🟡 Skanerlangan barcode: {barcode}")  # ✅
        if not barcode:
            return

        product = get_product_by_barcode(barcode)
        print("📦 Topilgan mahsulot:", product)  # ✅
        if not product:
            response = QMessageBox.question(
                self,
                "Mahsulot topilmadi",
                f"📦 Bu shtrix kod ({barcode}) bo‘yicha mahsulot topilmadi.\nYangi mahsulot qo‘shilsinmi?",
                QMessageBox.Yes | QMessageBox.No
            )
            if response == QMessageBox.Yes:
                from ui.base_form import BaseWindow
                # self.hide()
                self.setEnabled(False)  # faqat vaqtincha interaktiv bo‘lmasin
                self.base_window = BaseWindow(self.parent)
                self.base_window.input_barcode.setText(barcode)  # 🔁 Avtomatik barcode o‘tkaziladi
                self.base_window.show()
            self.barcode_input.clear()
            return

        self.add_to_cart(barcode)
        self.barcode_input.clear()
        self.barcode_input.setFocus()
        
    def ensure_barcode_focus(self):
        if hasattr(self, "search_input") and hasattr(self, "barcode_input"):
            if self.search_input and self.search_input.hasFocus():
                return
            if self.barcode_input and not self.barcode_input.hasFocus():
                self.barcode_input.setFocus()



    def create_sales_panel(self):
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # 🛒 Sarlavha
        label = QLabel("🛒 Savat")
        label.setFont(QFont("Arial", 28, QFont.Bold))
        layout.addWidget(label)
    
        # 📠 Shtrix kod kiritish paneli — SAVAT USTIGA joylashadi
        self.barcode_input = QLineEdit()
        self.barcode_input.setFont(QFont("Arial", 16))
        self.barcode_input.setFixedHeight(60)
        self.barcode_input.setPlaceholderText("📠 Shtrix kodni kiriting...")
        self.barcode_input.returnPressed.connect(self.handle_barcode_entered)
        self.barcode_input.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #1976D2;
                border-radius: 12px;
                padding: 12px;
                font-size: 18px;
            }
            QLineEdit:focus {
                background-color: #e3f2fd;
                border: 2px solid #0D47A1;
            }
        """)

        kb_btn = QPushButton("⌨️")
        kb_btn.setFixedSize(60, 60)
        kb_btn.setStyleSheet("""
            QPushButton {
                background-color: #e3f2fd;
                border: 2px d #64b5f6;
                border-radius: 10px;
                font-size: 22px;
            }
            QPushButton:hover {
                background-color: #bbdefb;
            }
        """)
        kb_btn.clicked.connect(self.open_virtual_keyboard)

        barcode_row = QHBoxLayout()
        barcode_row.addWidget(self.barcode_input)
        barcode_row.addWidget(kb_btn)
        layout.addLayout(barcode_row)
        
        # 🧺 Savatdagi mahsulotlar (scroll)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        self.cart_layout = QVBoxLayout()
        self.cart_layout.setAlignment(Qt.AlignTop)
        content.setLayout(self.cart_layout)
        scroll.setWidget(content)
        layout.addWidget(scroll)

        # 🧮 Umumiy summa
        self.total_label = QLabel("Umumiy: 0 so'm")
        self.total_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.total_label.setAlignment(Qt.AlignRight)
        self.total_label.setStyleSheet("color: green;")
        layout.addWidget(self.total_label)

        # 🔘 Tugmalar
        btn_clear = QPushButton("🗑️ Tozalash")
        btn_credits = QPushButton("📋 Qarzdorlar")
        btn_base = QPushButton("📦 Baza bo‘limi")
        self.btn_checkout = QPushButton("✅ Savdoni yakunlash")

        for btn in [btn_clear, btn_credits, btn_base, self.btn_checkout]:
            btn.setFont(QFont("Arial", 16, QFont.Bold))
            btn.setMinimumSize(220, 70)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        btn_clear.setStyleSheet("background-color: #f0f0f0; color: black;")
        btn_credits.setStyleSheet("background-color: #64B5F6; color: white;")
        btn_base.setStyleSheet("background-color: #FFB74D; color: white;")
        self.btn_checkout.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 30px;
                font-weight: bold;
                padding: 20px;
                border-radius: 12px;
                border: 2px solid #388E3C;
            }
            QPushButton:hover {
                background-color: #66BB6A;
                border: 2px solid #2E7D32;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
         """)

        btn_clear.clicked.connect(self.clear_cart)
        btn_credits.clicked.connect(self.open_credits)
        btn_base.clicked.connect(self.open_base)
        self.btn_checkout.clicked.connect(self.finalize_sale)
    
        # 🔳 Tugmalar paneli
        left_btns = QHBoxLayout()
        left_btns.addWidget(btn_clear)
        left_btns.addWidget(btn_credits)
        left_btns.addWidget(btn_base)

        main_btn_row = QHBoxLayout()
        main_btn_row.addLayout(left_btns)
        main_btn_row.addStretch()
        main_btn_row.addWidget(self.btn_checkout)
        
        layout.addLayout(main_btn_row)
        frame.setLayout(layout)
        return frame


    def finalize_sale(self):
        if not is_shift_open():
            QMessageBox.warning(self, "❗ Smena ochilmagan", "Avval smenani ochishingiz kerak.")
            return

        if not self.cart:
            QMessageBox.warning(self, "❗ Diqqat", "Savat bo‘sh! Mahsulot qo‘shing.")
            return

        total = sum(item["price"] * item["quantity"] for item in self.cart.values())
        customer_id = None

        dialog = QDialog(self)
        dialog.setWindowTitle("💳 To‘lov usuli")
        dialog.setFixedSize(420, 320)

        dialog.setStyleSheet("""
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #fefefe, stop:1 #e8f5e9);
                border-radius: 15px;
            }
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #2e7d32;
            }
            QPushButton {
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
                border-radius: 10px;
                background-color: #66bb6a;
                color: white;
            }
            QPushButton:hover {
                background-color: #43a047;
            }
        """)

        layout = QVBoxLayout(dialog)

        title = QLabel("To‘lov usulini tanlang:")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # 🔽 3ta tugma bilan tanlash osonroq
        selected_type = {"value": None}

        def set_type(val):
            selected_type["value"] = val
            dialog.accept()

        btn_cash = QPushButton("Naqd")
        btn_card = QPushButton("Karta")
        btn_credit = QPushButton("Qarzga")

        for btn, val in [(btn_cash, "cash"), (btn_card, "card"), (btn_credit, "debt")]:
            btn.setMinimumHeight(70)
            btn.clicked.connect(lambda _, v=val: set_type(v))
            layout.addWidget(btn)

        layout.addStretch()

        if dialog.exec_() != QDialog.Accepted:
            return

        payment_type = selected_type["value"]
        if not payment_type:
            return

        if payment_type == "debt":
            customer_id, ok = QInputDialog.getText(self, "ID karta", "Mijozning ID-kartasi:")
            if not ok or not customer_id.strip():
                QMessageBox.warning(self, "⚠️ Diqqat", "ID karta kiritilmadi. Qarzga savdo bekor qilindi.")
                return

            from modules.credits_manager import ensure_customer_exists
            ensure_customer_exists(customer_id)

        cash_given = total
        change = 0

        if payment_type == "cash":
            cash_given = self.show_cash_input_dialog(total)
            if not cash_given:
                return
            if cash_given < total:
                QMessageBox.warning(self, "❗ Yetarli emas", "Berilgan summa yetarli emas.")
                return
            change = int(cash_given) - int(total)

        try:
            sale_id = start_sale(payment_type, self.current_user_id, customer_id)
            cart_items = []
            for barcode, item in self.cart.items():
                product = get_product_by_barcode(barcode)
                cart_items.append({
                    "product_id": product["id"],
                    "price": item["price"],
                    "quantity": item["quantity"]
                })

            finalize_sale(
                sale_id=sale_id,
                cart_items=cart_items,
                total_amount=total,
                payment_type=payment_type,
                cash_given=cash_given,
                change=change,
                customer_id=customer_id
            )

            if payment_type == "debt":
                from modules.credits_manager import register_customer_credit, check_customer_debt_limit
                if not check_customer_debt_limit(customer_id, Decimal(str(total))):
                    QMessageBox.warning(self, "⚠️ Limitdan oshib ketdi", "Ushbu mijoz uchun ruxsat etilgan qarz limiti oshib ketadi.")
                    return
                register_customer_credit(
                    customer_id=customer_id,
                    sale_id=sale_id,
                    amount=total,
                    user_id=self.current_user_id
                )

            self.print_receipt(
                sale_id=sale_id,
                cart_items=[{
                    "name": item["name"],
                    "quantity": item["quantity"],
                    "price": item["price"]
                } for barcode, item in self.cart.items()],
                total=total,
                payment_type=payment_type,
                cash_given=cash_given,
                change=change
            )

            QMessageBox.information(self, "✅ Savdo yakunlandi",
                f"To‘lov turi: {payment_type.capitalize()}\nUmumiy: {int(total)} so‘m\n"
                f"Berilgan: {int(cash_given)} so‘m\nQaytim: {int(change)} so‘m")

            self.clear_cart()

        except Exception as e:
            QMessageBox.critical(self, "Xatolik", f"Savdoni saqlashda xatolik:\n{str(e)}")

            
    
            
    def show_cash_input_dialog(self, total):
        dialog = QDialog(self)
        dialog.setWindowTitle("Naqd to‘lov")
        dialog.resize(600, 500)
        dialog.setStyleSheet("QDialog { background-color: white; }")
    
        layout = QVBoxLayout(dialog)

        # 💰 Umumiy summa sarlavhasi
        label_title = QLabel(f"💰 Umumiy: {int(total)} so‘m")
        label_title.setFont(QFont("Arial", 30, QFont.Bold))
        label_title.setAlignment(Qt.AlignCenter)
        label_title.setStyleSheet("color: green; background-color: #e0ffe0; padding: 16px; border-radius: 10px;")
        layout.addWidget(label_title)

        # 🔘 Tez to‘lov summalari
        amounts = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]
        selected_amount = {"value": None}

        def make_handler(amount):
            def handler():
                selected_amount["value"] = amount
                dialog.accept()
            return handler

        grid = QGridLayout()
        grid.setSpacing(15)
        
        for idx, amt in enumerate(amounts):
            btn = QPushButton(str(amt))
            btn.setFont(QFont("Arial", 20, QFont.Bold))
            btn.setFixedSize(130, 70)
            btn.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 8px;")
            btn.clicked.connect(make_handler(amt))
            row = idx // 4
            col = idx % 4
            grid.addWidget(btn, row, col)

        layout.addLayout(grid)

        # ✍️ Qo‘lda summa kiritish + virtual klaviatura tugmasi
        input_row = QHBoxLayout()
        
        manual_input = QLineEdit()
        manual_input.setPlaceholderText("✍️ Yozib kiriting...")
        manual_input.setFont(QFont("Arial", 18))
        manual_input.setFixedHeight(60)
        manual_input.setStyleSheet("padding: 10px; border: 2px solid #ccc; border-radius: 8px;")
        
        btn_keyboard = QPushButton("⌨️")
        btn_keyboard.setFixedSize(60, 60)
        btn_keyboard.setFont(QFont("Arial", 18))
        btn_keyboard.setStyleSheet("background-color: #eeeeee;")
        btn_keyboard.clicked.connect(self.open_virtual_keyboard)

        input_row.addWidget(manual_input)
        input_row.addWidget(btn_keyboard)
        layout.addLayout(input_row)

        # ✅ Tasdiqlash tugmasi
        btn_manual = QPushButton("✅ Tasdiqlash")
        btn_manual.setFont(QFont("Arial", 20, QFont.Bold))
        btn_manual.setFixedHeight(70)
        btn_manual.setStyleSheet("background-color: #2E7D32; color: white; padding: 14px; border-radius: 10px;")
        btn_manual.clicked.connect(lambda: self.manual_amount_input(manual_input, selected_amount, dialog))
        layout.addWidget(btn_manual)

        # 📍 MARKAZDAN BIR OZ YUQORIGA KO‘TARISH — klaviatura bilan to‘qnashmasin
        dialog.adjustSize()  # ← o‘lchamlar to‘liq aniqlansin
        
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        dialog_geometry = dialog.frameGeometry()
        dialog_geometry.moveCenter(screen_geometry.center())
        
        # 🔼 120px yuqoriga siljitamiz
        new_top = dialog_geometry.top() - 120
        if new_top < 0:
            new_top = 0

        dialog.move(dialog_geometry.left(), new_top)

        # 🔄 Fokusni faollashtirish
        dialog.raise_()
        dialog.activateWindow()
        
        dialog.exec_()
        return selected_amount["value"]


    def manual_amount_input(self, input_field, selected_amount, dialog):
        try:
            val = int(input_field.text())
            if val <= 0:
                raise ValueError
            selected_amount["value"] = val
            dialog.accept()
        except ValueError:
            QMessageBox.warning(dialog, "⚠️ Xatolik", "Iltimos, to‘g‘ri summa kiriting!")
    
    def print_receipt(self, sale_id, cart_items, total, payment_type, cash_given, change):
        width = 40  # 80mm printerlar uchun ideal kenglik
        lines = []

        # 🛒 Chek sarlavhasi
        lines.append("🛒 MINI MARKET 🛒".center(width))
        lines.append(datetime.now().strftime("%Y-%m-%d %H:%M").center(width))
        lines.append(f"Chek raqami: #{sale_id}".center(width))
        lines.append("-" * width)

        # 📦 Mahsulotlar ro‘yxati
        for item in cart_items:
            name = item["name"]
            quantity = item["quantity"]
            price = item["price"]
            subtotal = quantity * price

            # Nom va narxlarni joylashtirish
            name_part = f"{name}"[:25].ljust(25)  # nomi 25 belgigacha
            qty_price_part = f"{quantity}x{int(price)}".rjust(7)
            total_part = f"{int(subtotal)}".rjust(8)
            line = f"{name_part}{qty_price_part}{total_part}"
            lines.append(line)

        lines.append("-" * width)

        # 💵 To‘lov turi va umumiy summa
        lines.append(f"To‘lov turi: {payment_type.capitalize()}".ljust(width))
        lines.append(f"Umumiy: {int(total)} so'm".ljust(width))

        if payment_type == "cash":
            lines.append(f"Berilgan: {int(cash_given)} so'm".ljust(width))
            lines.append(f"Qaytim: {int(change)} so'm".ljust(width))

        lines.append("-" * width)
        lines.append("🤝 RAHMAT!".center(width))
        lines.append("\n")

        # 🖨️ Chekni faylga yozish (printer uchun tayyor)
        with open("receipt.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        
        # 👀 Konsolda ko‘rsatish
        print("\n".join(lines))

        # Chekni printerga yuborish
        printer = ReceiptPrinter(printer_name="POS-80")
        printer.print_receipt(
            sale_id=sale_id,
            items=[{
                "name": item["name"],
                "quantity": item["quantity"],
                "price": item["price"]
            } for barcode, item in self.cart.items()],
            total=total,
            payment_type=payment_type,
            cash_given=cash_given,
            change=change
        )

    
    

    def filter_products(self):
        current_category = self.category_title.text().replace("📦 ", "")
        self.show_products(current_category)
    
    def open_base(self):
        # self.hide()
        self.base_window = BaseWindow(self.parent)
        self.base_window.showMaximized()

        
    


