# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 01:55:32 2025

@author: DavrServis
"""

# modules/login_manager.py

import hashlib
from data_base.database import fetch_one
from modules.user_manager import login as user_login



def authenticate_user(username, password):
    user = fetch_one("SELECT * FROM users WHERE username = %s", (username,))
    if not user:
        return None

    input_password_hash = hashlib.sha256(password.encode()).hexdigest()
    if input_password_hash == user["password_hash"]:
        return user
    return None
