# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:23:50 2025

@author: DavrServis
"""

class Car:
    """(self, make, model, year, km = 0, price = None)"""
    def __init__(self, make, model, year, km = 0, price = None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
        
    def set_price(self, price):
        self.price = price
        
    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas!")
            
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}"
        info += f"{self.year}-yil, {self.__km} km yurgan"
        if self.price:
            info += f" Narhi: {self.price}"
        return info
    
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}"
        info += f"{self.year}-yil, {self.__km}km yurgan"
        if self.price:
            info += f" Narhi: {self.price}"
        return info
    
    def get_km(self):
        return self.__km
    
# Endi bu klassimizni qo'lda tekshirib ko'ramiz:
# avto1 = Car("gm", "malibu", 2020)
# print(avto1.get_info())
# Mana oddiy holatda klassimizdagi get_info() metodini tekshirdik.

# Endi add_km() metodini ham tekshirib ko'ramiz:
# avto1.add_km(5000)
# Endi manfiy qiymat berib ko'ramiz:
# avto1.add_km(-500)
# Natija: ValueError: km manfiy bo'lishi mumkin emas!

# Keling endi har gal qo'lda tekshirishni oldini olish uchun test dastur yozamiz:
