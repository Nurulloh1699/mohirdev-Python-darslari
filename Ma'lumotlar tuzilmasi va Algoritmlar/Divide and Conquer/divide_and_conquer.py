# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 12:20:38 2025

@author: DavrServis
"""
## 1. Array elementlari sonini qaytaruvchi funksiya:
def count_elements(arr):
    """DIVIDE and CONQUER metodi yordamida massiv (ARRAY) elementlari sonini hisoblaydi"""
    ## Bazaviy holat: Agar massiv bo'sh bo'lsa, elementlar soni 0ga teng bo'ladi.
    if not arr:
        return 0 
    
    ## Massivni kichik qismlarga ajratish: Birinchi element + qolgan elementlar soni.
    return 1 + count_elements(arr[1:])

## **Test qilish**
arr = [5, 8, 12, 22]
print(f"Berilgan ARRAY elementlari soni: {count_elements(arr)} taga teng.")

## Berilgan ARRAY elementlari soni: 4 taga teng.

## Qanday ishlaydi?
    ## Massiv arr = [5, 8, 12, 22] da:

        ## 1 + count_elements([8, 12, 22])
        ## 1 + (1 + count_elements([12, 22]))
        ## 1 + (1 + (1 + count_elements([22])))
        ## 1 + (1 + (1 + (1 + count_elements([]))))
        ## 0 (bo'sh massivda)



## 2. Arrayning eng katta elementini qaytaruvchi funksiya.
def find_max(arr):
    """DIVIDE and CONQUER usuli yordamida massivning eng katta elementini topadi"""
    ## Bazaviy holat: Agar massivda 1ta element bo'lsa, o'sha element eng katta hisoblanadi.
    if len(arr) == 1:
        return arr[0]
    
    ## Massivni ikkiga bo'lib, chap va o'ng qismlarda REKURSIV ravishda eng katta elementni topish.
    mid = len(arr) // 2
    left_max = find_max(arr[:mid]) # Chap qismning maksimal qiymati.
    right_max = find_max(arr[mid:]) # O'ng qismning maksimal qiymati.
    
    ## Ikkala qismning eng katta elementlaridan kattasini qaytarish.
    return max(left_max, right_max)

## **Test qilish**
arr = [5, 8, 12, 22]
print(f"Berilgan ARRAYning eng katta elementi: {find_max(arr)} ga teng ekan")

## Natija: Berilgan ARRAYning eng katta elementi: 22 ga teng ekan.

 

    
## 3. Binary Search qidirish algoritmi.
def binary_search(arr, target, low = 0, high = None):
    """DIVIDE and CONQUER usuli yordamida Binary Search algoritmi
       Massiv (ARRAY) elementlari oldindan saralangan (tartiblangan) bo'lishi kerak 
    """
    if high is None:
        high = len(arr) - 1
        
    ## Bazaviy holat: Agar qidiruv oralig'i bo'sh bo'lsa, element topilmadi degan habar konsolga chiqariladi.
    if low > high:
        return -1
    
    ## O'rta indeksni topish.
    mid = (low + high) // 2
    
    ## Agar maqsadli qiymat o'rta elementga teng bo'lsa, indeksni qaytarish.
    if arr[mid] == target:
        return mid

    ## Maqsad o'rta elementdan kichik bo'lsa, chap qismini qidirish.
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)

    ## Agar maqsad o'rta elementdan katta bo'lsa, o'ng qismini qidirish.
    else:
        return binary_search(arr, target, mid + 1, high)
    
## **Test qilish**
arr = [5, 8, 12, 22]
target = 12
print(f"Qidirilayotgan {target} elementining indeksi: {binary_search(arr, target)}") 

## Natija: Qidirilayotgan 12 elementining indeksi: 2