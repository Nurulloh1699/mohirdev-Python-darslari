# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:32:01 2025

@author: DavrServis
"""

def linear_search(arr, target):
    # Massivda linear search yordamida qidirish.
    # Agar target massiv ichida bo'lsa, uning indeksini qaytaradi,
    # bo'lmasa - 1 ni qaytaradi.
    
    # Massivni boshidan ohirigacha ko'rib chiqamiz:
    for index, value in enumerate(arr): # "enumerate massiv elementlarini va indekslarini birga beradi.
        if value == target: # Agar joriy qiymat "target" ga teng bo'lsa.
            return index # Indexni qaytar.
    return None

# Qidiriladigan massiv:
myList = [1, 3, 4, 6, 7, 8, 10, 12, 23, 445, 56, 78, 99]


# Qidirilayotgan qiymat:
target = 10 # Qidirilayotgan qiymatimiz 10.

# Funksiyani chaqiramiz:
result = linear_search(myList, target)

# Natijani ekranga chiqaramiz:
if result != None: # Agar natija None teng bo'lmasa, demak qiymat topilgan.
    print(f"Qiymat {target}, {result} - indeksda topildi.") # Indeks va topilgan qiymatni chiqaramiz.
else: # Aks holda.
    print(f"Qiymat {target} massiv ichida topilmadi.") # Topilmadi deb chaqiramiz.
    
