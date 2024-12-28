# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:15:53 2024

@author: DavrServis
"""

from uuid import uuid4
class Avto:
    __num_avto = 0 # Bu o'rinda biz num_avto ni inkapsulyatsiya qilib qo'ydik.
    # PI = 14159 # Bu o'rinda konstanta qiymat yaratdik va bu qiymatdan ushbu klassni obyektalari foydalanishi
    # mumkin
    """Avtomobil klassi"""
    def __init__(self, make, model, rang, yil, narx, km=0):
        """Avtomobillarni xusuiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1          
    
    # Quyidagi metod num_avto inkapsulyatsiya qilingandan keyin uni ko'rish imkonini beradi.
    @classmethod # Dekarator
    def get_num_avto(cls): # Obyektni emas klass ni uzatkanimiz uchun cls yozildi qavs ichiga. 
        return cls.__num_avto 
    
    def get_km(self):
         return self.__km
     
    def get_id(self):
         return self.__id     
    
    def add_km(self, km):
         """Mashinaga km qo'shish"""
         if km >= 0:
             self.__km += km
         else:
             print("""Mashinanig km sini o'zgartirib bo'lmaydi""")