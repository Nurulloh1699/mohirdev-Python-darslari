# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:46:45 2025

@author: DavrServis
"""

# Qanday qilib berilgan 100ta son ichidan tushirib qoldirilgan sonni topish mumkin.
import random # Random moduli import qilinib olinyapti.
n = 100 # n o'zgaruvchisiga 100 ni tenglab qo'yyapmiz.
numbers = list(range(1, n + 1)) # List va Range orqali ro'yxat shakllantirib olyapmiz.
x = numbers.pop(random.randint(1, n + 1)) # Pop va Random metodlari yordamida 100ta son ichidan 1 sonni sug'urib olyapmiz. 
print(x) # Sug'urib (tushurib qoldirilgan) olingan son konsolga chiqarilyapti

#1 - yechim (bu yechim unchalik ham optimal emas):
numbers2 = list(range(1, n + 1)) # Yana bir ro'yxat shakllantirilyapti va ro'yxat o'zini to'liqligini saqlab turibti.
print(sum(numbers2) - sum(numbers)) # Oddiy yechim taklif qilinyapti ikki ro'yxat ayirmasini hisoblash orqali yechim topilyapti.

#2 - yechim (nisbatan yaxshiroq bo'lgan yechim ):
for i in range(1, n): # Range orqali 1dan n gacha bo'lgan sonlar olinyapti.
    if i not in numbers: # Bu o'rinda i har bir songa tenglab chiqilyapti va agar i biror songa yetib borganda va u son mavjud bo'lmasa. 
        print(i) # Mavjud bo'lmagan sonni konsolga chiqaramiz.
        break # Dastr to'htaydi.
    
#3 - yechim (eng to'g'ri deb tasdiqlangan yechim)
summa = n * (n + 1) / 2 # Matematikada mavjud bo'lgan formula 1dan n gacha bo'lgan sonlarning yeg'indisini qaytaradi.
print(summa - sum(numbers)) # Ohirida ikki yeg'indini ayirish kifoya bo'ladi.

