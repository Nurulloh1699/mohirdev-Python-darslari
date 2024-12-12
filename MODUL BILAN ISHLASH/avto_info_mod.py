# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:28:17 2024

@author: DavrServis
"""

def avto_info(kompaniya, model, rangi, korobka, year, narxi=None):
    avto = {
        'kompaniya': kompaniya,
        'model': model,
        'rang': rangi,
        'korobka': korobka,
        'yil': year,
        'narx': narxi
    }
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini
    beruvchi funksiya"""
    avtolar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting: ")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Mashina modeli: ")
        rangi = input("Mashinaning rangi: ")
        korobka = input("Mashinaning korobkasi: ")
        year = input("Ishlab chiqarilgan yili: ")
        narxi = input("Mashinaning narxi: ")
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, year, narxi))
        
        javob = input("Yana avtomobil qo'shasizmi? (h/y): ").lower()
        if javob != 'h':
            break
    return avtolar

def info_print(avto_info):
    """Avtomobillar haqida saqlangan ma'lumotlarni konsolga chiqaruvchi funksiya"""
    print(
        f"{avto_info['rang'].title()} "
        f"{avto_info['kompaniya'].upper()} "
        f"{avto_info['model'].upper()}, "
        f"{avto_info['korobka']} korobka, "
        f"{avto_info['yil']}-yil, "
        f"{avto_info['narx']}$"
    )
