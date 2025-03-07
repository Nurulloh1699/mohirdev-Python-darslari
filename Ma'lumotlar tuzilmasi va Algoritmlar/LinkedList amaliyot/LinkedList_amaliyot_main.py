# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 01:33:36 2025

@author: DavrServis
"""

class Node: # LINKED LISTS uchun kerak bo'ladigan birinchi obyektimiz ya'ni tugun.
    """Tugun (Node) obyekti"""
    def __init__(self, data): # Node obyektining konstruktori.
        self.data = data # Tugunning qiymati (data) ni saqlash.
        self.next = None # Keyingi tugunga havola, hozircha yo'q (None)
        
class LinkedList: # Bu sinf barcha tugunlarni bog'lovchi LINKED LISTS obyekti hisoblanadi.
    """Linked List obyekti"""
    def __init__(self): # LINKED LIST obyekti konstruktori.
        self.head = None   # Ro'yxat boshida hech qanday tugun yo'q, shuning uchun head = None.
        
    def printList(self):
        temp = self.head # Ro'yxat boshidan boshlaymiz.
        while temp: # Toki tugunlar mavjud ekan. 
            print(temp.data) # Tugun qiymatini konsolga chiqaramiz.
            temp = temp.next # Keyingi tugunga o'tamiz.
            
    def push(self, new_data):
        """List boshiga tugun qo'shish"""
        # Yangi node yaratamiz
        new_node = Node(new_data) # 
        # List boshinikeyingi o'ringa suramiz.
        new_node.next = self.head
        # Yangi node ni list boishiga qo'yamiz.
        self.head = new_node
        
    def insertAfter(self, prev_node, new_data):
        """Biror tugundan so'ng tugun qo'shish"""
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        # Yangi tugun qo'shamiz
        new_node= Node(new_data)
        # Yangi tugunni keyingi tugunga bog'laymiz
        new_node.next = prev_node.next
        # Avvalgi tugunni yangi tugunga bog'laymiz
        prev_node.next = new_node
        
    def append(self, new_data):
        """List oxiriga tugun qo'shish"""
        # Yangi tugun yaratamiz
        new_node = Node(new_data)
        # List bo'sh emasligini tekshiramiz.
        if self.head is None:
            # Bo'sh bo'lsa yangi tugun list boshiga qo'shiladi.
            self.head = new_node
            return
        # Aks holda List oxiriga boramiz.
        last = self.head # List boshidan boshlaymiz.
        while last.next: # List ohirigacha boramiz.
            last = last.next
        last.next = new_node # List ohiriga yangi tugunni bog'laymiz.
        
    def deleteNode(self, key):
        """Listdan qiymat o'chirish"""
        # List boshini topib olamiz
        temp = self.head
        # Birinchi tugunni tekshiramiz
        if(temp and temp.data == key):
            self.head = temp.next # Agar 'head' ni o'chirish kerak bo'lsa, uni keyingi tugunga almashtiramiz
            temp = None # Eski 'head'ni yo'q qilamiz.
            return
        # Aks holda keyingi tugunlarni qarab chiqamiz.
        while temp:
            if temp.data == key: # O'chirish kerak bo'lgan tugunni topsak, sikldan chiqamiz.
                break
            prev = temp # Oldingi tugunni saqlaymiz.
            temp = temp.next #Keyingi tugunga o'tamiz. 
        # Agar qiymat topilmasa.
        if temp == None:
            return
        # Tugunni Listdan o'chiramiz.
        prev.next = temp.next # Oldingi tugunni keyingi tugunga bog'laymiz.
        temp = None # O'chirilgan tugunni xotiradan tozalaymiz.
        
                            