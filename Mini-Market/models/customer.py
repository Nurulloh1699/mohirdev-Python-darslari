# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 08:55:05 2025

@author: DavrServis
"""

# models/customer.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class Customer:
    id: Optional[int]
    ism: str
    id_karta: str
    telefon: Optional[str]
