# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 09:53:15 2025

@author: DavrServis
"""

# utils/formatter.py

from datetime import date, datetime

def format_currency(amount: float) -> str:
    """
    Narxni 12 000 so'm ko‘rinishda chiqaradi.
    """
    return "{:,.0f} so'm".format(amount).replace(",", " ")

def format_date(d: date) -> str:
    """
    Sanani 12.04.2025 ko‘rinishida chiqaradi.
    """
    return d.strftime("%d.%m.%Y") if d else ""

def parse_date(date_str: str) -> date:
    """
    '12.04.2025' ko‘rinishidagi stringni date ga aylantiradi.
    """
    return datetime.strptime(date_str, "%d.%m.%Y").date()

def is_empty(value: str) -> bool:
    """
    String bo‘sh yoki faqat bo‘sh joylardan iboratligini tekshiradi.
    """
    return not value or value.strip() == ""

def clean_whitespace(value: str) -> str:
    """
    Keraksiz bo‘sh joylarni olib tashlaydi.
    """
    return " ".join(value.strip().split())
