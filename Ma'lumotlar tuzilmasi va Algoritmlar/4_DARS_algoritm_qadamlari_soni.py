# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:54:58 2025

@author: DavrServis
"""

## ALGORITM QADAMLARI SONI.

## Linear search.
## N ta elementdan iborat ro'yxat uchun:
    # Maksimum qadamlar soni N ga teng.
    
## Yani agar qidirilayotgan element ro'yhatimizda 100 - indeksda bo'lsa, biz bu elementni 100ta qadam orqali topamiz.


## Binary search.
## N ta elementdan iborat ro'yxat uchun:
    ## Maksimum qadamlar soni (log2(N)(Logorifm ikki asosga ko'ra N ga teng)). 
    ## Logorifm bu odatda darajaning teskarisi, ya'ni 2² = 4 bo'lsa, logorifmda bu log₂(4) = 2 ga teng bo'ladi.
    ## Misol uchun: log₂(16) = 4, ya'ni ro'yxatimizdagi elementlar soni 16 ta bo'lsa, maksimum qadamlar soni 4 tani tashkil qiladi degani.
    
## Xulosa qilib shuni aytish mumkinki, bu ikki qidirish algoritmlaridan bizga ma'quli Binary search ekan:
    ## Linear search = 4096 elementli ro'yxat uchun 4096 ta qadam sarflaydi.
    ## Binar search = 4096 lementli ro'yxat uchun 12 (log₂(4096) = 12) ta qadam sarflaydi.
    ## Binary search to'g'ri ishlashi uchun lug'at to'g'ri tahlangan bo'lishi lozim, Linear search esa bu narsaga muhtoj emas u ishlayveradi.
    
## Misollar:
    
    # Linear search.
def linear_search(arr, target):
    # Funksiya 'linear_search' ro'yxat (arr) ichidan qidirilayotgan 'target' lementni topish uchun yaratilgan.
    for index, value in enumerate(arr):
        # 'enumerate(arr)' yordamida ro'yxatning har bir elementini indeks (index) va qiymat (value) bilan olamiz.
        if value == target:
            # Agar hozirgi element 'target' ga teng bo'lsa: 
            return index # Topilgan elemntni indeksini qaytaramiz.
    return -1 # Agar butun ro'yxat tekshirilsa va 'target' topilmasa, -1 qaytaramiz.

## Misol uchun:
numbers = [3, 5, 2, 4, 9, 1] # Qidiriladigan sonlar ro'yxati.
target = 4 # Qidirilayotgan element
result = linear_search(numbers, target) # Linear_searchfunksiyasini chaqiramiz va natijani 'result' ga saqlaymiz.

if result != -1:
    # Agar natija -1 bo'lmasa, demak element ro'yxatda topilgan.
    print("Element topildi, indeksi:", result)
else:
    # Agar natija -1 bo'lsa, element ro'yxatda mavjud emas
    print("Element topilmadi.")
## Tahlil:
    # 1. for index, value in enumerate(arr): Ro'txatning har bir elementini indeks va qiymat bilan ketma-ket oladi.
    # 2. if value == target: Har bir elementni 
    # 3. return index: Agar mos element topilsa, uning indeksini qaytaradi.
    # 4. return -1: Agar ro'yxat tekshirilsa va mos elememnt topilmasa, -1 qaytaradi.

    # Binary search.
    # ESLATMA!!!: Binary search algoritmi faqat tartiblangan ro'yxatlar uchun ishlaydi.
def binary_search(arr,  target):
    # Funksiya 'binary_search' tartiblangan ro'yxatda qidirilayotgan 'target' elementini topish uchun yaratilgan.
    left, right = 0, len(arr) -1
    # 'left' ro'yxat boshidagi indeks, 'right' esa ro'yxat ohiridagi indeksni bildiradi.
    
    while left <= right:
        # Toki qidirilayotgan qism 'left' va 'right' indekslari orasida ekan, qidiruv davom etadi.
        mid = (left + right) // 2
        # 'mid' o'rtasidagi indeksni hisoblaydi (butun qism)
        
        
        if arr[mid] == target:
            # Agar o'rta element 'target' ga teng bo'lsa:
            return mid # Topilgan elementni indeksini qaytaramiz.
        elif arr[mid] < target: 
            # Agar o'rta element 'target' dan kichik bo'lsa, demak qidiralayotgan element ro'yxatning o'ng yarim qismida.
            left = mid + 1 # 'left' indeksini o'rta elementdan keyingi indeksga yangilaymiz.
        else:
            # Aks holda, o'rta element 'target' dan katta bo'ladi va qidiriv chap yarimda davom etadi.
            right = mid - 1 # 'right' indeksini o'rta elementdan oldingi indeksga yangilaymiz.
    return -1 # Agar while loop tugasa va element topilmasa, -1 qaytaramiz.
## Misol uchun:
numbers = [1,2,3,4,5,6,7,8,9] # Trtiblangan sonlar ro'yxati.
target = 9 # Qidirilayotgan element.
result = binary_search(numbers, target) # binary_searchfunksiyasini chaqiramiz va natijani 'result' ga saqlaymiz.

if result != -1:
    # Agar natija -1 bo'lmasa, demak element topilgan.
    print("Element topildi, indeksi:", result)
else:
    # Agar natija -1 bo'lsa, element ro'yxatda mavjud emas.
    print("Element topilmadi")
    
## Tahlil:
    # 1. left, right = 0, len(arr) - 1: Boshlang'ich indekslar, ro'yxatning boshidan oxirigacha bo'lgan diapazonni belgilaydi.
    # 2. while left <= right: Qidiruvni davom ettirish sharti: chap indeks(left) o'ng indeks(right) dan kichik yoki teng bo'lishi kerak.
    # 3. mid = (left + right) // 2: O'rta indeksni hisoblaydi.
    # 4. if arr[mid] == target: Orta element 'target' ga tengligini tekshiradi.
    # 5. elif arr[mid] < target: Agar o'rta element 'target' dan kichik bo'lsa, qidiruvni ro'yxatning o'ng qismiga cheklaydi.
    # 6. else: Aka holda, qidiruv chap qismga cheklanadi.
    # 7. return -1: Element topilmasa, -1 qaytariladi.

    