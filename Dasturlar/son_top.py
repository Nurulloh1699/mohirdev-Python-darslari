# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:58:38 2024

@author: DavrServis
"""

# import random 

# def son_top(x=10):
#     tasodifiy_son = random.randint(1, x) 
#     print(f"Men 1dan {x} gacha son o'yladim. Topa olasizmi?")
    
#     while True:
#         taxmin = int(input(">>> "))
#         if taxmin < tasodifiy_son:
#             print("O'ylagan sonim bundan kattaroq!")
#         elif taxmin > tasodifiy_son:
#             print("O'ylagan sonim bundan kichikroq!")
#         else: 
#             print("Topdingiz!")
#             break
        
from pywebio.input import input
from pywebio.output import put_text
import random
def sontop(x = 10):
    tasodifiy_son = random.randint(1, x)
    while True:
        taxmin = int(input(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi? >>> "))
        if taxmin < tasodifiy_son:
            put_text("Kattaroq son ayting!")
        elif taxmin > tasodifiy_son:
            ut_text("Kichikroq son ayting!")
        else:
            put_text("Yutdingiz!")
            break