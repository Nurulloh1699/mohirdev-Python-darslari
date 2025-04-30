# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 08:55:32 2025

@author: DavrServis
"""

# models/user.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    username: str
    parol: str
    rol: str  # 'admin' yoki 'kassir'
