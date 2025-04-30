# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:36:36 2025

@author: DavrServis
"""

from LinkedList_amaliyot_main import Node, LinkedList

## llist - Linked List yaratamiz.
llist = LinkedList()

## Uchta node (tugun) yaratamiz.
llist.head = Node('Seshanba')
tuesday = Node('Chorshanba')
wednesday = Node('Payshanba')
# print(llist.head.data)

## Tugunlarni bog'laymiz.
llist.head.next = tuesday
tuesday.next = wednesday
# print(llist.head.data)
# print(llist.head.next)
# print(llist.head.next.data)
# print(llist.head.next.next.data)

# # LinkedList ni funksiya yordamida konsolga chiqaramiz.
# llist.printList()

## List boshiga yangi tugun qo'shamiz.
llist.push('Dushanba')
# llist.printList()

## List o'rtasiga element qo'shamiz.
llist.insertAfter(llist.head.next, 2)
# llist.printList()

## List oxiriga tugun qo'shamiz.
llist.append('Juma')
llist.append('Shanba')
llist.printList()

## Ro'yxatimizdan element o'chiramiz.
llist.deleteNode(2)
llist.printList()