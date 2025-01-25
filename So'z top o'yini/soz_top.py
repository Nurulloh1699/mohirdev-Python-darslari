# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 21:12:18 2025

@author: DavrServis
"""

        
        
import random
from uzwords import words

# Tasodifiy so'z tanlash
def get_word():
    word = random.choice(words)  # So'zlarni tanlash uchun random.choice() dan foydalanamiz.
    while "_" in word or ' ' in word:  # "_" yoki bo'sh joy mavjudligini tekshiramiz.
        word = random.choice(words)
    return word.upper()  # So'zni katta harflarda qaytaramiz.

# Foydalanuvchi tanlagan harflar asosida so'zni ko'rsatish
def display(user_letters, word):
    display_letter = ""  # Boshlang'ich natija.
    for letter in word:  # So'zdagi har bir harfni tekshiramiz.
        if letter in user_letters:  # Agar harf foydalanuvchi kiritgan harflarda bo'lsa:
            display_letter += letter  # Natijaga harfni qo'shamiz.
        else:
            display_letter += "-"  # Aks holda "-" qo'shamiz.
    return display_letter

# O'yinni boshlash
def play_soz():
    word = get_word()  # Tasodifiy so'zni tanlaymiz.
    word_letters = set(word)  # So'zdagi harflarni o'z ichiga olgan to'plam.
    user_letters = ''  # Foydalanuvchi kiritgan harflar.
    print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi?")

    while len(word_letters) > 0:  # So'zning barcha harflari topilmaguncha davom etadi.
        print(display(user_letters, word))  # Hozirgi holatni ko'rsatamiz.
        
        if len(user_letters) > 0:  # Agar foydalanuvchi harflar kiritgan bo'lsa:
            print(f"Shu paytgacha kiritgan harflaringiz: {user_letters}")
        
        letter = input("Harf kiriting: ").upper()  # Harfni katta harfga o'zgartiramiz.
        
        if letter in user_letters:  # Agar harf oldin kiritilgan bo'lsa:
            print("Bu harfni oldin kiritgansiz! Boshqa harf kiriting.")
            continue
        elif letter in word:  # Agar harf to'g'ri bo'lsa:
            word_letters.remove(letter)  # To'plamdan harfni olib tashlaymiz.
            print(f"{letter} harfi to'g'ri ekan.")
        else:  # Agar harf noto'g'ri bo'lsa:
            print("Bunday harf yo'q!")
        
        user_letters += letter  # Foydalanuvchi harflariga qo'shamiz.
    
    # O'yin tugagach:
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urinishda topdingiz!")

# O'yinni ishga tushirish
play_soz()
    