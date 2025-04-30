# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:56:11 2025

@author: DavrServis
"""

class Node:
    """LinkedList uchun tugun (Node)"""
    def __init__(self, task):
        self.task = task # Tugunning ma'lumoti (vazifasi).
        self.next = None # Keyingi tugunga ishora (Hozircha yo'q).
        
class LinkedList:
    """LinkedList orqali kunlik reja"""
    def __init__(self):
        self.head = None # Bog'langan ro'yxat boshini bo'sh qilib yaratamiz.
        
    def printPlan(self):
        """Kunlik rejani konsolga chiqarish"""
        temp = self.head # List boshidan boshlaymiz.
        if not temp: # Agar ro'yxat bo'sh bo'lsa.
            print("Reja bo'sh!") # Xabar chiqaramiz.
            return
        print("📅 Kunlik reja:") # Ro'yxat sarlavhasi.
        while temp: # Oxirigacha barcha tugunlarni ekranga chiqaramiz.
            print(f"✅ {temp.task}") # Vazifani chiqarish.
            temp = temp.next # Keyingi tugunga o'tish.
            
    def addTask(self, task):
        """Kunlik rajaga yangi vazifa qo'shish (boshiga)"""
        new_node = Node(task) # Yangi tugun yaratamiz.
        new_node.next = self.head # Yangi tugunni eski 'head' tugunga bog'laymiz.
        self.head = new_node # Yangi tugunni 'head' sifatida belgilaymiz.
        
    def appendTask(self, task):
        """Kunlik reja oxiriga vazifa qo'shish"""
        new_node = Node(task) # Yangi tugun yaratamiz.
        if not self.head: # Agar list bo'sh bo'lsa.
            self.head = new_node # Yangi tugunni bosh tugun qilib qo'yamiz.
            return
        last = self.head # Ro'yxat boshidan boshlaymiz.
        while last.next: # Ohirgi tugunga yetkuncha harakat qilamiz.
            last = last.next
        last.next = new_node # Oxirgi tugunni yangi tugunga bog'laymiz.
        
    def insertAfterTask(self, prev_task, task):
        """Berilgan vazifadan keyin yangi vazifa qo'shish"""
        temp = self.head # Ro'yxat boshidan boshlaymiz.
        while temp: # Oxirigacha aylanamiz.
            if temp.task == prev_task: # Agar kerakli tugunni topsak.
                new_node = Node(task) # Yangi tugunni yaratamiz.
                new_node.next = temp.next # Yangi tugunni avalgi tugunning keyingi tuguniga bog'laymiz.
                temp.next = new_node # Avvalgi tugunni yangi tugunga bog'laymiz.
                return
            temp = temp.next # Keyingi tugunga o'tish.
        print(f"⚠ '{prev_task}' topilmadi!") # Agar tugun topilmasa, habar chiqaramiz.
    
    def deleteTask(self, task):
        """Kunlik reja ichidan vazifani o'chirish"""
        temp = self.head # Ro'yxat boshidan boshlaymiz.
        
        # Agar boshidagi tugunni o'chirish kerak bo'lsa.
        if temp and temp.task == task:
            self.head = temp.next # 'head' ni keyingi tugunga almashtiramiz.
            temp = None # Eski tugunni xotiradan o'chiramiz.
            return
        
        prev = None # Oldingi tugunni saqlash uchun o'zgaruvchi.
        while temp and temp.task != task: # Tugun topilmaguncha davom etamiz.
            prev = temp # Oldingi tugunni saqlab qolamiz.
            temp = temp.next # Keyingi tugunga o'tish.
            
        if temp is None: # Agar tugun topilmasa.
            print(f"⚠ '{task}' topilmadi") # Xabar chiqaramiz.
            return
        
        prev.next = temp.next # Oldingi tugunni o'chirilayotgan tugunning keyingi tuguniga bog'laymiz.
        temp = None # Tugunni xotiradan o'chiramiz.
        

## ✅ **Foydalanish**
plan = LinkedList() # LinkedList obyektini yaratamiz.

# Kunlik rejaga vazifalar qo'shamiz.
plan.appendTask("Ertalab sport bilan shug'ullanish") # Oxiriga qo'shish.
plan.appendTask("Nonushta qilish") # Oxiriga qo'shish.
plan.appendTask("Dars tayorlash") # Oxiriga qo'shish.
plan.appendTask("Ish yoki o'qishga borish") # Oxiriga qo'shish.

## O'rtaga vazifa qo'shish.
plan.insertAfterTask("Nonushta qilish", "Kitob o'qish") # "Nonushta qilish" tugunidan keyin qo'shish.

## Boshiga vazifa qo'shish.
plan.addTask("Tongi meditatsiya") # Ro'yxat boshiga qo'shish.

## Kunlik rejani konsolga chiqarish.
plan.printPlan() # Barcha tugunlarni konsolga chiqarish.

## Vazifani o'chirish.
plan.deleteTask("Dars tayorlash") # "Dars tayorlash" tugunini o'chirish.

# Yangilangan rejani chiqarish.
print("\n📝 Yangilangan reja:")
plan.printPlan() # Vazifalar tahrir qilingandan keyin ro'yxatni konsolga chiqarish.
