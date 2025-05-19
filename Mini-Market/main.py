# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 11:26:06 2025

@author: DavrServis
"""

# main.py

# main.py
import sys
from PyQt5.QtWidgets import QApplication
from ui.login_form import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

