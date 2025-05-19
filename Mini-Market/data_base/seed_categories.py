# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 17:30:10 2025

@author: DavrServis
"""

from modules.product_manager import add_category

def seed_categories():
    kategoriyalar = [
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

    for nomi, ikona_yol in kategoriyalar:
        add_category(nomi, ikona_yol)

    print("✅ Barcha kategoriyalar muvaffaqiyatli qo‘shildi!")

if __name__ == "__main__":
    seed_categories()
