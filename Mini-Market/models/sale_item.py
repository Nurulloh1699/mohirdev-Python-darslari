# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 08:56:02 2025

@author: DavrServis
"""

# models/sale_item.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class SaleItem:
    product_id: int
    nomi: str
    miqdor: float
    narx: float

    @property
    def jami(self) -> float:
        return self.miqdor * self.narx
