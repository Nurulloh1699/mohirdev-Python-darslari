# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 11:58:59 2025

@author: DavrServis
"""

## STACK - bu ingliz tilidan tarjima qilinganda qandaydur buyumlarni yoki fayllarni ustma-ust tahlanganini odatda STACK deb ataymiz.

## STACK - ishlash tartibi qisqacha, yangi mal'umotlar doim to'plamning ustiga qo'shiladi va yana ma'lumotlar bilan ishlamoqchi bo'lganimizda 
## to'plamning ustidagi ma'lumotlar bilan ishlay olamiz.

## STACK HUSUSIYATLARIGA TO'HTALADIGAN BO'LSAK:
## --- LIFO Ma'lumot to'plami.
## --- LIFO (Last In First Out) - Oxirgi kirgan birinchi chaqadi.
## --- Ma'lumotlar to'plam ustiga qo'shiladi va to'plam ustidan olinadi.


## Qayerlarda ishlatilishi mumkin:
## --- Email pochtani misol qilib olishimiz mumkin, ya'ni pochtaga eng ohirgi kelgan habar doim eng birinchi o'rinda turadi.
## --- Qong'iroqlar kitobchasi (Телефонная книга), bu holatda ham yuqorigidagidek vaziyat hosil bo'ladi. Sizga eng ohirgi qo'ng'iroq qilgan
## raqam doim birinchida turadi.
## --- Telefon habarnomalari ham shularning turiga mansub va yuqorigidagidek ishlaydi.


## STACK ustida bajarilishi mumkin bo'lgan amallar:
## 1. Push -> Element qo'shish.
## 2. Pop -> Elementni sug'urib olish. # Peek bilan farqi, biz Pop orqali eng yuqoridagi elementni sug'urib olib uning ustida turli amallar
## bajarishimiz mumkin.
## 3. isEmpty -> To'plam bo'sh ekanligini tekshirish.
## 4. isFull -> To'plam to'la ekanligini tekshirish. # Misol uchun: Agar bir STACK gimizga oldindan hajm berib qo'ygan bo'lsak, unga yana 
## element sig'adi yoki yo'q tekshirishimiz mumkin.
## 5. Peek -> Eng yuqoridagi element qiymatini ko'rish. # Pop bilan farqi, Peek orqali biz faqat eng yuqoridagi elementni ko'rishimiz mumkin
## bo'ladi holos.

## KELING ENDI MISOL KO'RAMIZ.
class Stack:
    """Stack (LIFO) ma'lumot tuzilmasi"""
    def __init__(self, max_size = None):
        """STACK yaratish 
        max_sie: STACK ning maksimal o'lchami (agar belgilansa) 
        """
        self.stack = [] # Elementlarni saqlash uchun bo'sh ro'yxat.
        self.max_sie = max_size # Maksimal hajm (ixtiyoriy)
        
    def push(self, item):
        """Yangi element qo'shish (ro'yxat boshiga)
           Agar to'la bo'lsa, xato habari chiqariladi
        """
        if self.isFull():
            print("❌ Stack to'la! Yangi element qo'shib bo'lmaydi.")
        else:
            self.stack.append(item) # Elementni ro'yxat ohiriga qo'shamiz (Stack boshiga).
            print(f"✅ Elemenrt '{item}' qo'shildi.")
            
    def pop(self):
        """Oxirgi elementni sug'urib olish va qaytarish
           Agar stack bo'sh bo'lsa, xato habari chiqariladi
        """
        if self.isEmpty():
            print("❌ Stack bo'sh! Element sug'urib bo'lmaydi")
            return None
        else:
            item = self.stack.pop() # Ro'yxat oxiridagi elementni o'chirib, qiymatni qaytaradi.
            print(f"✅ Element '{item}' sug'urib olindi.")
            return item
        
    def isEmpty(self):
        """Stack bo'sh ekanligini tekshirish
           Ro'yxat uzunligi 0 bo'lsa, True qaytaradi 
        """
        return len(self.stack) == 0
    
    def isFull(self):
        """Stack to'la ekanligini tekshirish (faqat max_size berilgan bo'lsa)
           Agar stack hajmi maksimal hajmga teng yoki katta bo'lsa, True qaytaradi     
        """
        if self.max_sie: # Agar maksimal o'lcham belgilangan bo'lsa.
            return len(self.stack) >= self.max_sie
        return False # Agar maksimal o'lcham belgilanmagan bo'lsa, doim False
    
    def peek(self):
        """Stackning boshidagi element qiymatini ko'rish
           Agar stack bo'sh bo'lsa, xato xabari chiqariladi         
        """
        if self.isEmpty():
            print("❌ Stack bo'sh! Element mabjud emas.")
            return None
        else:
            item = self.stack[-1] # Ro'yxat oxiridagi elementni ko'rsatadi (o'chirmaydi).
            print(f"👀 Eng yuqoridagi element: '{item}'")
            return item
        
    def size(self):
        """Stackdagi elementlar sonini qaytarish
           len() funksiyasi orqali ro'xat uzunligini olamiz
        """
        return len(self.stack)
    
    def __str__(self):
        """Stackning ko'rinishini matn ko'rinishida chiqarish
           Elementlar teskari tartibda (Stackning yuqorisi ro'yxat oxirida)
        """
        return "Stack: " + " -> ".join(map(str, reversed(self.stack))) + " (Top)"
    
## ✅ **Test qilish**
stack = Stack(max_size=5) # Maksimal hajmi 5ga teng Stack yaratamiz.

## Stackka element qo'shish.
stack.push("A") # Element "A" qo'shildi.
stack.push("B") # Element "B" qo'shildi.
stack.push("C") # Element "C" qo'shildi.
stack.push("D") # Element "D" qo'shildi.
stack.push("E") # Element "E" qo'shildi.

## Stack to'la bo'lgani uchun yana qo'shib ko'ramiz.
stack.push("F") # Stack to'la bo'lgani uchun xato xabari chiqadi.

## Stackdan element sug'urib olish.
stack.pop() # Eng yuqoridagi element "E" sug'urib olinadi.
stack.pop() # Eng yuqoridagi element "D" sug'urib olinadi.

## Stack boshidagi elementni ko'rish.
stack.peek() # Eng yuqoridagi element ("C") ko'rsatiladi (o'chirilmaydi).

## Stack to'liq yoki bo'sh ekanligini tekshirish.
print(f"🗂 Stack bo'shmi? {stack.isEmpty()}") # Stack bo'sh emas, False qaytadi.
print(f"🗂 Stack to'dimi? {stack.isFull()}") # Stack to'la emas, False qaytadi.

## Stackdagi barcha elementlarni ko'rish.
print(stack) # Stack holatini ko'rsatadi.
