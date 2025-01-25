# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:22:48 2025

@author: DavrServis
"""

# Yuqoridagi o'yin qoidasini ham bir nechta sodda qadamlarga bo'lib olamiz:
#     1. Kompyuter ma'lum oraliqda son "o'ylaydi": Albatta, kompyuter o'ylashga qodir emas, shuning uchun biz berilgan oraliqda biror 
# tasodifiy sonni qaytarishimiz kifoya (random funksiyasi orqali).
#     2. Foydalanuvchi taxmin qilgan sonni qabul qilib olish (input() orqali bo'ladi).
#     3. Taxmin va tasodifiy sonlarni taqqoslash ("==" sonlarni teng ekanini tekshiramiz).
#     4. Taqqoslash natijasiga ko'ra ("if-else" juftligidan foydalanamiz va natijaga qarab ikki hil yo'l tutamiz (a - b)).
#     a. O'yinni to'xtatish;
#     b. Foydalanuvchiga ishora berish va qayta taxmin qilishni so'rash va yuqoridagi 3 - 4 qadamlarni takrorlash ("while" sikli).

import random

def son_top(x):
    print("1dan 10 gacha son o'yladim topa olasizmi?")
    taxminlar = 0
    son = random.randint(1, x)
    while True:    
        
        try:
            y = int(input("Taxmin qilib ko'ring: "))
            taxminlar += 1
            if son > y:
                print("Men o'ylagan son bundan kattaroq!")
            elif son < y:
                print("Men o'ylagan son bundan kichikroq!")
            else:
                print(f"Tabriklayman siz topdingiz, men o'ylagan son {son} edi!")
                print(f"Siz {taxminlar} ta urinishta topdingiz!")
                break
        except ValueError:
                print("Siz butun son kiritmadingiz!")
        
        # play_again = input("Yana o'ynashni hohlaysizmi? (h/y): ")
        # if play_again == 'h':
        #     print("O'yin davom etadi, yangi son o'yladim tahmin qilib ko'ring!")
        # else:
        #     print("Rahmat o'yin uchun, o'yin tugadi!")
        #     break  
    return taxminlar



def sontop_pc(x):
    input(f"1dan {x} gacha bo'gan oraliqda son o'ylang va istalgan tugmani bosing! Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
            print(f"Siz {taxmin} sonini o'yladingiz!")
        else:
            taxmin = quyi
        
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"{taxminlar} ta tahmin bilan toptim!")
    return taxminlar

# Endi ikki funksiyamizni navbat va navbat chaqiramiz:
def play(x = 10):
    yana = True
    while yana:
        taxminlar_user = son_top(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print("Tabriklayman siz yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0): "))
            
            


