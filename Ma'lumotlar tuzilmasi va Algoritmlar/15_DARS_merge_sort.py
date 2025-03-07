# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 15:47:52 2025

@author: DavrServis
"""

## MERGE SORT TARTIBLASH ALGORITMI.

## MERGE SORT - bu DIVIDE and CONQUER usuli yordamida ishlaydigan tartiblash algoritmi.
## Berilgan ro'yxatni ikkiga bo'lib, ikki tarafni alohida tartiblab jamlash asosida ishlaydi.

## ISHLASH PRINSIPINI KO'RAMIZ.

## 1 - BOSQICH. Biz bergan ARRAY ni ikki teng qismga bo'ladi
## 2 - BOSQICH. Hosil bo'lgan bo'laklarni yana ikki teng qismlarga bo'ladi va bu tioki bo'laklarda 1 tadan element qolguncha davom etadi.
## Bu bizning to'xtash shartimiz bo'ladi (REKURSIYA).
## 3 - BOSQICH. Hosil bo'lgan kichik bo'limlarni REKURSIV ravishda saralaydi. 
## 4 - BOSQICH. Har bir kichik qismni tartiblangan holda birlashtiradi.
## 5 - BOSQICH. Ikkita tartiblangan qismni solishtirib, yangi katta tartiblangan massiv hosil bo'ladi. 

## AMALAIYOT:
def merge_sort(array):
    """MERGE SORT yordamida xarid ro'yxatini alfavit tartibida saralaydi"""
    
    ## Bazaviy holat: agar ro'yxatda bitta yoki umuman element bo'lmasa, u allaqachon tartiblangan.
    if len(array) <= 1:
        return array
    ## Massivni o'rta nuqtasini aniqlash.
    mid = len(array) // 2
    
    ## Massivni ikkiga bo'lish (DIVIDE bosqichi).
    left_half = array[:mid]
    right_half = array[mid:]
    
    ## Har ikkila qismini ham REKURSIV usulda saralaymiz (CONQUER bosqichi).
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    ## Saralangan qismlarni tartiblangan holda birlashtiramiz (COMBINE bosqichi).
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """Ikkita tartiblangan ro'yxatni birlashtiruvchi yordamchi funksiya"""
    sorted_array = [] # Natijaviy tartiblangan ro'yxat.
    left_index, right_index = 0, 0 # Har ikkala ro'yxat uchun boshlang'ich indekslar.
    
    ## Ikkala ro'yxatda elementlar bor ekan, solishtirib, kichigini qo'shamiz.
    while left_index < len(left) and right_index < len(right):
        if left[left_index].lower() < right[right_index].lower():
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
            
    ## Qolgan elementlarni qo'shamiz (agar mavjud bo'lsa).
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])
    
    return sorted_array

## **Hayotiy misol: xarid ro'yxatini alfavit tartibida saralash**
shopping_list = [
    "Apple", "Banan", "Orange", "Grapes", "Milk"
    "Bread", "Eggs", "Cheese", "Tomato", "Cucumber"
    ]            

print("Xarid ro'yxati: (aralash tartibda):")
print(shopping_list)
sorted_shoppin_list = merge_sort(shopping_list)

print("Xarid ro'yxati: (alifbo tartibida):")
print(sorted_shoppin_list)