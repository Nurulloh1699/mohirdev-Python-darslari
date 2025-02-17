# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:04:58 2025

@author: DavrServis
"""

def binary_search(arr, target):
    """
    Binary search usuli bilan massivdan qiymat qidirish.
    Agar target massiv ichida bo'lsa, uning indeksini qaytaradi.
    Aks holda -1 qaytaradi
    """
    
    left = 0 # Qidiruvni boshlash indeksi.
    right = len(arr) - 1 # Qidiruvni tugatish indeksi
    
    while left <= right: # Davom etadi, toki left <= right sharti bajarilmaguncha.
        mid = (left + right) // 2 # O'rta indeksni hisoblash.
        if arr[mid] == target: # Agar o'rta qiymat qidirilayotgan qiymatga teng bo'lsa.
            return mid # Indeksni qaytar.
        elif arr[mid] < target: # Agar o'rta qiymat qidirilayotgan qiymatdan kichik bo'lsa .
            left = mid + 1 # Chap chegarani o'rta qiymatdan keyingi indeksga sur.
        else: # Aks holda, o'rta qiymat qidirilayotgan qiymatdan katta bo'lsa.
            right = mid - 1 # O'ng chegarani o'rta qiymatdan oldingi indeksga sur.
    return -1 # Agar target topilmasa, -1 qaytaradi.


# Massiv.
myList = [1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99]

# Qidirilayotgan qiymat.
target = 45

# Funksiyani chaqirish
result = binary_search(myList, target)

# Natijani chiqarish.
if result != -1:
    print(f"Qiymat {target} indeks {result} da topildi.")
else:
    print(f"Qiymat {target} massiv ichida topilmadi.")