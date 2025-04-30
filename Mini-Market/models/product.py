# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 08:54:27 2025

@author: DavrServis
"""

# models/product.py

from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Product:
    id: Optional[int]
    nomi: str
    barcode: str
    narx: float
    miqdor: float
    amal_muddati: Optional[date]
    kategoriya: str
    foyda_turi: str  # 'foiz' yoki 'miqdor'
    foyda_miqdori: float
    o_lov_birligi: str  # kg, dona, litr va h.k.
