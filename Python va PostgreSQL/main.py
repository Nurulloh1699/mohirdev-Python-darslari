# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 11:52:11 2024

@author: DavrServis
"""

import psycopg2  # PostgreSQL bilan ishlash uchun kutubxona
from psycopg2 import OperationalError  # Xatoliklarni boshqarish uchun OperationalError klassi

# PostgreSQLga ulanish uchun konfiguratsiya
host = "localhost"  # Server manzili (mahalliy mashina uchun localhost ishlatiladi)
user = "postgres"  # PostgreSQL foydalanuvchisi nomi (standart nom)
password = "n1282754N"  # PostgreSQL foydalanuvchisi uchun parol
db_name = "postgres"  # Ma'lumotlar bazasi nomi (standart ma'lumotlar bazasi nomi)
port = "5433"  # PostgreSQL serverining ishlayotgan port raqami

# PostgreSQLga ulanish funksiyasi
def create_connection():
    try:
        # psycopg2 kutubxonasi orqali ulanishni o'rnatish
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=db_name,
            port=port
        )
        print("Ulanish muvaffaqiyatli!")  # Agar ulanish muvaffaqiyatli bo'lsa, xabar chiqariladi
        return connection  # Ulanish obyekti qaytariladi
    except OperationalError as e:
        print(f"Xato yuz berdi: {e}")  # Ulanish davomida xatolik bo'lsa, xabar chiqariladi
        return None  # Xatolik bo'lsa, None qaytariladi

# Oziq-ovqat mahsulotlari jadvalini yaratish funksiyasi
def create_table(connection):
    try:
        with connection.cursor() as cursor:  # Kursor obyekti yaratilib, unda SQL so'rovlar bajariladi
            cursor.execute("""
                DROP TABLE IF EXISTS food_items;  # Agar jadval mavjud bo'lsa, uni o'chiradi
                CREATE TABLE food_items (
                    id SERIAL PRIMARY KEY,  # Avtomatik raqamlanadigan asosiy kalit ustun
                    product_name VARCHAR(100),  # Mahsulot nomi uchun 100 ta belgigacha joy ajratiladi
                    price DECIMAL(10, 2),  # Mahsulot narxi, 10 raqamli, 2 kasrli qiymat
                    quantity DECIMAL(10, 2),  # Mahsulot miqdori (kasr yoki butun son)
                    unit VARCHAR(20)  # O'lchov birligi uchun joy (masalan, kg, litr)
                );
            """)
            connection.commit()  # O'zgarishlar ma'lumotlar bazasiga saqlanadi
            print("Jadval yaratildi yoki mavjud.")  # Jarayon muvaffaqiyatli bajarilganligini bildiradi
    except Exception as e:
        connection.rollback()  # Xatolik bo'lsa, o'zgarishlar bekor qilinadi
        print(f"Xato: {e}")  # Xatolik haqida xabar chiqariladi

# Oziq-ovqat mahsulotlarini bazaga qo'shish funksiyasi
def insert_food_items(connection, food_items):
    try:
        with connection.cursor() as cursor:  # Kursor obyekti bilan ishlash
            insert_query = """
                INSERT INTO food_items (product_name, price, quantity, unit)  # Ma'lumot qo'shish uchun so'rov
                VALUES (%s, %s, %s, %s);  # Parametrlar joyi
            """
            cursor.executemany(insert_query, food_items)  # Bir nechta yozuvni bir so'rovda qo'shish
            connection.commit()  # O'zgarishlar ma'lumotlar bazasiga saqlanadi
            print("Mahsulotlar bazaga qo'shildi.")  # Jarayon muvaffaqiyatli bajarilganligini bildiradi
    except Exception as e:
        connection.rollback()  # Xatolik bo'lsa, o'zgarishlar bekor qilinadi
        print(f"Xato: {e}")  # Xatolik haqida xabar chiqariladi

# Ma'lumotlar bazasidan oziq-ovqat mahsulotlarini olish funksiyasi
def get_all_food_items(connection):
    try:
        with connection.cursor() as cursor:  # Kursor obyekti bilan ishlash
            cursor.execute("SELECT * FROM food_items;")  # Barcha yozuvlarni tanlash uchun SQL so'rovi
            rows = cursor.fetchall()  # Natijalarni olish
            print("Oziq-ovqat mahsulotlari:")
            for row in rows:  # Har bir yozuvni chiqarish
                print(row)
    except Exception as e:
        print(f"Xato: {e}")  # Xatolik haqida xabar chiqariladi

# Asosiy dastur
if __name__ == "__main__":
    connection = create_connection()  # PostgreSQLga ulanishni o'rnatish
    if connection:  # Agar ulanish muvaffaqiyatli bo'lsa
        create_table(connection)  # Jadval yaratish funksiyasini chaqirish
        # Oziq-ovqat mahsulotlarining nomi, narxi (so'mda), miqdori va o'lchov birligi
        food_items = [
            ("Olma", 8000, 10, "kg"),  # Har bir mahsulotni o'z parametrlari bilan ro'yxatga qo'shish
            ("Banana", 12000, 15, "kg"),
            ("Sabzi", 3000, 20, "kg"),
            ("Pomidor", 7000, 5, "kg"),
            ("Piyoz", 5000, 8, "kg"),
            ("Salat", 4000, 6, "kg"),
            ("Brokoli", 15000, 3, "kg"),
            ("Qulupnay", 20000, 12, "kg"),
            ("Tovuq go'shti", 40000, 4, "kg"),
            ("Mol go'shti", 80000, 3.5, "kg"),
            ("Guruch", 18000, 5, "kg"),
            ("Makaron", 15000, 10, "kg"),
            ("Non", 3000, 100, "dona"),
            ("Sut", 7000, 50, "litr"),
            ("Tuxum", 10000, 150, "dona"),
            ("Pishloq", 50000, 8, "kg"),
            ("Qatiq", 6000, 25, "litr"),
            ("Sariyog'", 45000, 5, "kg"),
            ("Shakar", 18000, 10, "kg"),
            ("Tuz", 2000, 25, "kg")
        ]
        insert_food_items(connection, food_items)  # Mahsulotlarni jadvalga qo'shish
        get_all_food_items(connection)  # Jadvaldagi barcha yozuvlarni ko'rish
        connection.close()  # Ulanishni yopish
        print("PostgreSQL bilan bog'lanish yopildi.")  # Dasturni tugatish haqida xabar



