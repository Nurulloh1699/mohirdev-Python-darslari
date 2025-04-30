# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:51:48 2025

@author: DavrServis
"""

## REKURSIYA.

# REKURSIYA - bu ma'lum bir funksiyani ichida qaytarib yana shu funksiyani chaqirishga aytiladi.

# Keling buni bir misol orqali tushunishga harakat qilamiz:
# Deylik sizda sandiq bor va bu sandiqni ichida qutular bor. Bizga shu qutilarning birida yashiringan kalit (key) kerak. Bizga bu kalitni
# tooish sharti qo'yilgan.

# Buni 2 xil yo'l bilan amalga oshirishimiz mumkin buning uchun WHILE sikli yoki REKURSIYA orqali amalga oshirishimiz mumkin bo'ladi.
# Quyida bu ikki usulni ko'rib chiqamiz:

## WHILE sikli.
class Box:
    """Quti obyektini yaratish"""
    def __init__(self, items):
        self.items = items # Qutidagi elementlar.

    def make_a_pile_to_look_through(self):
        """Qutining ichidagi narsalarni olish"""
        return self.items # Ichki elementlar ro'yxatini qaytarish.
    
def look_for_key(main_box):
    """DFS (Chuqur bo'yicha qidirish) orqali kalitni topish"""
    pile = main_box.make_a_pile_to_look_through() # Qutilar to'plami
    while pile: # Qutilarbo'sh bo'lmaguncha 
        box = pile.pop() # Stack usulida oxirgi qutini olamiz.
        # for item in box: # Ichki elementlarni tekshiramiz.
        if isinstance(box, Box): # Agar quti bo'lsa.
            pile.extend(box.make_a_pile_to_look_through()) # Ichki elemntlarni pile ga qo'shamiz.
        elif box == "KEY": # Agar kalit bo'lsa.
            print("🔑 Found the key!") # Kalit topildi.
            return # Qidirishni to'xtatamiz.
    print("❌ Key not found!") # Agar kalit topilmasa, xabar beramiz.
    
# ## ✅ **Test qilish**
small_box = Box(["paper", "pen"]) # Kalit yo'q.
medium_box = Box(["notebook", small_box]) # Ichida kichik quti bor.
big_box = Box(["clothes", "shoes", medium_box, "KEY"]) # Kalit mavjud.

look_for_key(big_box)

## ENDI HUDDI SHU KODNI REKURSIYA USULIDA YOZAMIZ:
class Box:
    """Quti obyektini yaratish"""
    def __init__(self, items):
        self.items = items # Qutidagi elementlar.
        
    def make_a_pile_to_look_through(self):
        """Qutining ichidagi narsalarni olish"""
        return self.items # Ichki elementlar ro'yxatini qaytarish.
    
def look_for_key_recursive(items):
    """Berilgan elementlar ro'yxatini rekursiv tarzda tekshiradi. Agar 'KEY' topilsa, True qaytaradi, aks holda False"""
    for item in items:
        if isinstance(item, Box): # Agar element quti bo'lsa.
            if look_for_key_recursive(item.make_a_pile_to_look_through()):
                return True # Ichki qutida kalit topilgan.
        elif item == "KEY": # Agar element kalit bo'lsa.
            print("🔑 Key is found!")
            return True
    
    return False

def look_for_key(main_box):
    """Asosiy qutida kalitni rekursiv qidirish"""
    if not look_for_key_recursive(main_box.make_a_pile_to_look_through()):
        print("❌ Key not found")
        
## ✅ **Test qilish**
small_box = Box(["paper", "pen"]) # Kalit yo'q.
medium_box = Box(["notebook", small_box]) # Ichida kichik quti bor.
big_box = Box(["clothes", "shoes", medium_box, "KEY"]) # Kalit mavjud.
look_for_key(big_box)

## Bu ikkala kod ham bir xil vazifani bajaradi lekin REKURSIYA kodi anchagina ihcham va tushunarliroq bo'ladi.
    
## Yana bir misol orqali rekursiyani tushinishga harakat qilamiz.
# def sana(n): # REKRUSIV funksiya.
#     print(n) # Chaqirilayotgan qiymatni konsolga chiqaradi.
#     # if n <= 1: # Funksiyani to'xtash sharti, bu holatda agar berilgan qiymat 1dan kichik yoki teng bo'lsa degani bo'ldi.
#     #     return # Shart qanoatlantirilsa dastur ishlashdan to'htaydi. 
#     # else: # Aks holda.
#         sana(n - 1) # Qiymat 1dan kichik yoki teng bo'lguncha, qiymatdan 1 ayirib boramiz.

# sana(5) 


## AMALIYOT. Faktorial topish funksiyasini REKURSIYA orqali yozish.
# def factorial(n):
#     """REKRUSIV usulda faktorialni hisoblash"""
#     print(n, end=' ')
#     if n == 0 or n == 1: # Bazaviy holat 0! = 1 va 1! = 1.
#         return 1 # REKURSIYA ning to'xtash nuqtasi.
    
#     return n * factorial(n - 1) # REKURSIV chaqirish: n * (n - 1)! ni hisoblash.

# ## ✅ **Test qilish**
# num = 5 # Faktorialini hisoblash uchun son.
# print(f"-> {num}! = {factorial(num)}") # Natija: 5! = 120

## XULOSA.

# ## 📌 **Qachon rekursiyadan foydalanish ma'qul?**
# ## Rekursiya **takroriy** yoki **murakkab tuzilmalarga ega** bo‘lgan masalalarni soddalashtirish uchun ishlatiladi. Quyida **rekursiya ishlatilishi kerak bo‘lgan asosiy holatlar** keltirilgan:



# ## 🔹 **1️ Matematik hisob-kitoblarda (Faktorial, Fibonacci, Exponent)**
# ##**Rekursiya ishlatilishi uchun eng oddiy misollar – matematik funksiyalar**.

# ##✅ **Qayerda ishlatish mumkin?**  
# ##✔ Faktorial: `n! = n × (n-1)!`  
# ##✔ Fibonacci sonlari: `F(n) = F(n-1) + F(n-2)`  
# ##✔ Daraja hisoblash (Exponentiation): `a^n = a × a^(n-1)`

# ##**Misol: Fibonacci sonlari**
# ##```python
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(7))  # Natija: 13

# ##💡 **Nima uchun rekursiya ishlatildi?**  
# ##- Har bir son oldingi ikkita sonning yig‘indisiga bog‘liq.  
# ##- Oddiy iteratsion usul bilan yozish murakkabroq bo‘lishi mumkin.  



# ## 🔹 **2️⃣ Daraxt (Tree) va Grafik (Graph) tuzilmalarini qidirishda**
# ##**Daraxt va grafik tuzilmalar rekursiv tabiatga ega**, shuning uchun ularni rekursiya bilan oson ishlash mumkin.

# ##✅ **Qayerda ishlatish mumkin?**  
# ##✔ Fayl tizimlarini tekshirish  
# ##✔ Binarlashgan qidiruv daraxti (BST)  
# ##✔ Graf qidirish (DFS va BFS algoritmlari)

# ##**Misol: Rekursiv DFS (Depth First Search)**
# ##```python
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

#     def add_child(self, child):
#         self.children.append(child)

# def depth_first_search(node):
#     print(node.value)  # Tugunning qiymatini chiqarish
#     for child in node.children:
#         depth_first_search(child)  # Rekursiv chaqirish

# # Daraxt yaratamiz
# root = Node("A")
# child1 = Node("B")
# child2 = Node("C")
# child3 = Node("D")
# root.add_child(child1)
# root.add_child(child2)
# child1.add_child(child3)

# # DFS ishlatamiz
# ##depth_first_search(root)

# ##💡 **Nima uchun rekursiya ishlatildi?**  
# ##- Daraxt tuzilmalari tabiatan rekursiv bo‘lib, **har bir tugun o‘zining kichik tarmoqlariga ega**.  
# ##- Har bir tugunni o‘zining bolalariga rekursiv murojaat qilish orqali tekshiramiz.  



# ## 🔹 **3️⃣ Fayl tizimini yoki kataloglarni qidirishda**
# ## Kompyuter fayllari **daraxt** tuzilmasida saqlanadi, shuning uchun **rekursiv qidirish** yaxshi ishlaydi.

# ##✅ **Qayerda ishlatish mumkin?**  
# ##✔ Kataloglarni ichma-ich qidirish  
# ##✔ Fayllarni indeksatsiya qilish  
# ##✔ Kattaroq hajmdagi ma’lumotlarni topish  

# ## **Misol: Rekursiv fayl qidirish**

# import os

# def find_file(directory, filename):
#     for item in os.listdir(directory):
#         full_path = os.path.join(directory, item)
#         if os.path.isfile(full_path) and item == filename:
#             print(f"🔍 Fayl topildi: {full_path}")
#             return full_path
#         elif os.path.isdir(full_path):
#             find_file(full_path, filename)  # Rekursiv chaqirish

# # Test qilish
# # find_file("C:/Users/YourUsername/Documents", "target_file.txt")

# ##💡 **Nima uchun rekursiya ishlatildi?**  
# ##- Har bir katalog boshqa kataloglarni o‘z ichida saqlaydi.  
# ##- Har bir katalogga kirib, ichki fayllarni tekshirish kerak.  



# ## 🔹 **4️⃣ Qaytarish (Backtracking) algoritmlarida**
# ##Ba’zi algoritmlar muammoni hal qilish uchun **har bir imkoniyatni tekshirib chiqish** talab qiladi. 

# ##✅ **Qayerda ishlatish mumkin?**  
# ##✔ Sudoku yechish  
# ##✔ N-Queens muammosi  
# ##✔ Kombinatorik muammolar  

# ## **Misol: N-Queens muammosi (oddiy holatda)**

# def solve_n_queens(n, row=0, columns=[]):
#     if row == n:  
#         print(columns)  # Barcha joylashuvlarni chop etish
#         return
#     for col in range(n):
#         if col not in columns:  # Shu ustunda ilgari qirol bo‘lmasa
#             solve_n_queens(n, row + 1, columns + [col])

# solve_n_queens(4)  # 4 ta shoh uchun yechim

# ##💡 **Nima uchun rekursiya ishlatildi?**  
# ##- Har bir imkoniyat tekshiriladi.  
# ##- Har bir qatorda yangi joylashuvni sinab ko‘rib, keyingi qatorga o‘tamiz.  



# ## 🔹 **5️⃣ Dynamic Programming (DP) muammolarida**
# ##Ba’zi murakkab algoritmlarni rekursiya bilan soddalashtirish mumkin. 

# ##✅ **Qayerda ishlatish mumkin?**  
# ##✔ Fibonacci sonlarini optimallashtirish  
# ##✔ Eng uzun umumiy qatorni topish (Longest Common Subsequence)  
# ##✔ Eng arzon yo‘lni topish (Minimum Cost Path)  

# ## **Misol: Memorization bilan Fibonacci (Dynamic Programming)**

# from functools import lru_cache

# @lru_cache(None)
# def fibonacci(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(50))  # Katta sonlar uchun tezroq ishlaydi

# ##💡 **Nima uchun rekursiya ishlatildi?**  
# ##- Oddiy rekursiya **katta sonlar uchun sekin ishlaydi**, shuning uchun **memorization** bilan optimallashtirildi.  



# ## 🔹 **Rekursiyadan foydalanmaslik kerak bo‘lgan holatlar**
# ##❌ **Juda katta `n` qiymatlar uchun** – Rekursiya juda ko‘p chaqirilsa, `RecursionError` bo‘lishi mumkin.  
# ##❌ **Oddiy sikllar bilan hal qilsa bo‘ladigan masalalar** – Oddiy **for yoki while** bilan ishlovchi masalalar rekursiyasiz tezroq ishlaydi.  
# ##❌ **Ko‘p xotira ishlatiladigan jarayonlar** – Har bir rekursiv chaqiruv **stack memory** band qiladi.  

# ## **Misol: Fibonacci sikl yordamida tezroq ishlaydi**

# def fibonacci_iter(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# print(fibonacci_iter(50))  # Juda tez ishlaydi

# ##💡 **Nima uchun rekursiya ishlatilmagan?**  
# ##- **Stack Overflow bo‘lishining oldini oladi**  
# ##- **Kamroq xotira ishlatadi**  



# ### **🔥 Xulosa**
# ##| **Qayerda ishlatish kerak?** | **Rekursiya mosmi?** |
# ##|------------------------------|----------------------|
# ##| ✅ Matematik funksiyalar (Faktorial, Fibonacci) | **Ha** |
# ##| ✅ Daraxt va graf qidirish (DFS, BFS) | **Ha** |
# ##| ✅ Fayl tizimlarini qidirish | **Ha** |
# ##| ✅ Qaytarish (Backtracking) algoritmlari | **Ha** |
# ##| ✅ Dynamic Programming (Memorization) | **Ha** |
# ##| ❌ Juda katta `n` qiymatlar uchun | **Yo‘q** |
# ##| ❌ Oddiy sikllar bilan hal qilsa bo‘ladigan muammolar | **Yo‘q** |
# ##| ❌ Ko‘p xotira talab qiladigan muammolar | **Yo‘q** |



