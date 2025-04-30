# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 00:18:35 2025

@author: DavrServis
"""

## HASH TABLES.

## HASH FUNKSIYA - bu qidiruv algoritmlari ichida BIG O qiymati bo'yicha eng tezkorlaridan biri O(1).

## Hash Jadval (Hash Table) — bu ma'lumotlarni kalit-qiymat juftliklari shaklida saqlash uchun ishlatiladigan ma'lumotlar tuzilmasi.
## Hash jadvalda har bir kalit hash funksiya yordamida indeksga o'zgartiriladi va shu indeks bo'yicha qiymat saqlanadi.

## Boshlanishiga tasavvur qiling sizda ARRAYlar bor va bu ARRAYlar tartibli va tartibsiz. ARRAYdagi har bir elementning nomi bor va narxi bor.
## Endi oddiy savol, ushbu ro'yxatdan qidiruv amalaga oshirish uchun qancha vaqt ketadi. 
## Agar ro'yxat tartiblangan bo'lsa BINARY SEARCH ishlatish mumkin va qidirish vaqti O(log₂n) ga teng bo'ladi va element qancha ko'p bo'lsa
## qidiruv vaqti ham mos ravishda oshib boradi.
## Agar ro'yxat tartibsiz bo'lsa, siz BINARY SEARCH ishlata olmaysiz va LINEAR SEARCH dan foydalanasiz, qidiruv vaqti esa O(n) ga teng bo'ladi.

## O(log₂n) aslida kichkina vaqt lekin ma'lumotlar ham odatda kam bo'lmaydi.

## Tassavur qiling siz ro'yxatni yodlab olgansiz va sizdan ma'lumot so'ralganda siz aslo ma'lumot qidirmaysiz va shunchaki yodlangan narsani
## javob sifatida qaytarasiz. Agar buni BIG O da o'lchaydigan bo'lsak qancha vaqt ketadi? O(1).

## Hash jadvallar orqali biz aynan shu yodlab olishni dasturlashimiz mumkin. Dasturning maqsadi esa, dasturimiz biz ma'lumot so'raganimizda
## uni qidirib o'tirmasin yoddan javob bersin.

## HASH FUNKSIYA.
## Hash jadvallarni tuzishdan oldin biz HASH FUNKSIYA bilan tanishishimiz kerak. Bu matematik funksiya va bunda rasayam chuqurlashish shart
## emas 

## HASH FUNKSIYA ning vazifasi siz unga biron bir matn bersangiz anashu matnni takrorlanmas noyob sobga o'tkazib beradi. Bu biriktirilgan son
## boshqa matnlarda takrorlanmasligi kerak.

## HASH FUNKSIYA TURLARI.
## Yaxshi HESH FUNKSIYAni o'ziga yarasha belgilari bor.
    ## 1. Bir hil matn uchun bir hil son qaytaradi. Masalan, olma desak "olma" -> 5 soniga biriktirilishi mumkin. Bu misol holos aslida son 
    ## bundan ancha farq qiladi.
    ## 2. Har hil matn uchun har hil son qaytaradi. Har bir yangi matnga biriktirilgan son boshqalarida qaytarilmaydi.
    ## 3. HASH FUNKSIYA sizga kerakli oraliqdagi sonlarni qaytaradi.
    
## Amalda tushunish uchun esa HASH CONCULATION degan saytga kirib amalaiyot qilsak bo'ladi.


## AMALIYOT.
## HASH funksiyasi yaratish qoidalari:
    ## Deterministik — bu narsa yoki jarayonning oldindan aytib bo'ladigan va bir xil sharoitlarda har doim bir xil natija beradigan
    ## ekanligini anglatadi.
    
    ## Massiv (inglizcha: Array) — bu bir xil turdagi ma'lumotlarni bir joyda saqlash uchun ishlatiladigan ma'lumotlar tuzilmasi.
    ## Massivda bir nechta qiymatlar ketma-ket joylashtiriladi va har bir qiymatga indeks orqali murojaat qilish mumkin.


    ## 1. Deterministik: Har safar bir xil kalit uchun bir xil hash qiymatini qaytarishi kerak.
    ## 2. Tezkor: Hash qiymatini tez vva samarali hisoblashi kerak.
    ## 3. Har xil qiymatlar: Turli kalitlar uchun imkon qadar har xil hash qiymatlari berishi kerak.
    ## 4. Chegaralangan diapazon: Hash qiymati berilgan diapazonda bo'lishi kerak (masalan, massivning uzunligidan oshmasligi kerak).
    
## ODDIY HASH FUNKSIYA YARATISH: Telefon kontaktlari kitobi misolida ko'ramiz (Pythonda HASH funksiya lug'atlarga to'g'ri keladi).

## 📒 Kontaktlar kitobi (hash jadval) yaratish.
contacts = {} # {} - bu qavslar Pythonda lug'at yaratish uchun ishlatiladi, boshlanishiga u bo'sh bo'ladi.

# 📲 Kontaktlar kitobi uchun funksiya.
def add_contact(name, phone):
    """Kontakt qo'shish funksiyasi"""
    
    if name in contacts:
        print(f"❌ {name} allaqachon mavjud!")
    else:
        contacts[name] = phone
        print(f"✅ {name} muvoffaqiyatli qo'shildi!")
        
def search_contact(name):
    """Kontakt qidirish funksiyasi"""
    
    if name in contacts:
        print(f"🔍 {name}: {contacts[name]}")
    else:
        print(f"❌ {name} topilmadi!")
        
def update_contact(name, phone):
    """Kontaktni yangilash funksiyasi"""
    
    if name in contacts:
        contacts[name] = phone
        print(f"♻️ {name} muvoffaqiyatli yangilandi!")
    else:
        print(f" {name} topilmadi!")

def delete_contact(name):
    """Kontaklarni o'chirish funksiyasi"""

    if name in contacts:
        del contacts[name]
        print(f"🗑️ {name} muvoffaqiyatli o'chirildi!")
    else:
        print(f"❌ {name} topilmadi!")
        
def display_contacts():
    """Barcha kontaktlar ko'rsatish funksiyasi"""
    
    if contacts:
        print(f"📇 Kontaktlar ro'yxati:")
        for name, phone in contacts.items():
            print(f"👤 {name}: 📞 {phone}")
        else:
            print("❗ Kontaktlar ro'yxati bo'sh!")
            
## Foydalanuvchi uchun menyu.
def contact_menu():
    while True:
        print("\n📱 Kontaktlar kitobi:")
        print("1. Kontakt qo'shish.")
        print("2. Kontakt qidirish.")
        print("3. Kontakt yangilash.")
        print("4. Kontakt o'chirish.")
        print("5. Barcha kontaktlarni ko'rish.")
        print("0. Chiqish.")
        
        choice = input("Kerakli amalni tanlang: ")
        
        if choice == "1":
            name = input("Ismni kiriting: ")
            phone = input("Telefon raqamini kiriting: ")
            add_contact(name, phone)
            
        elif choice == "2":
            name = input("Qidirilayotgan ismni kiriting: ")
            search_contact(name)
            
        elif choice == "3":
            name = input("Yngilangan ismni kiriting: ")
            phone = input("Yangi telefon raqamini kiriting: ")
            update_contact(name, phone)
            
        elif choice == "4":
            name = input("O'chiriladigan ismni kiriting: ")
            delete_contact(name)
            
        elif choice == "5":
            display_contacts()
            
        elif choice == "0":
            print("✅ Dasturdan chiqildi!")
            break
        
        else:
            print("❌ Noto'g'ri buyruq! Qaytadan urunib ko'ring.")
            
## 🚀 Dasturni ishga tushirish.
contact_menu()