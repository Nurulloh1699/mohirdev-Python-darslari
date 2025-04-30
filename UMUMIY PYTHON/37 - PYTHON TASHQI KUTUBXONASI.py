# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:04:43 2025

@author: DavrServis
"""

# 37 - DARS.
# PYTHON TASHQI KUTUBXONASI.

# Tashqi kutubxona deganda boshqa dasturchilar tomonidan yozilgan tayyor funksiyalar, modullar va paketlarni yeg'indisi. Biz bu dasturlarni
# o'zimizni kompyuterimizga o'rnatib olib, o'zimizni loyihalarimizda foydalanishimiz mumkin.

# Tashqi kutubxonalarning eng kattasi PyPi.org sahifasi hisoblanadi.

# Endi biz modullar bilan birma-bir tanishib o'tamiz:
    
# Googletranslate dan foydalanamiz buning uchun bu modulni o'rnatamiz (pip install googletrans==3.1.0a0).
# from googletrans import Translator
# tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt). Bu yerda biz klassdan obyekt yaratib oldik.

# matn_uz = "Python - dunyodagi eng mashxur dasturlash tili!"

# # Istalgan matnni ingliz tiliga tarjima qilish uchun translate metodini chaqiramiz:
# tarjima = tarjimon.translate(matn_uz, dest = 'ru') # Translate metodida matnni o'zini berib boshqa parametrlarni bermasak ingliz tiliga tarjima qiladi.


# # Original matn:
# print(tarjima.origin) # Tarjima degan obyektimizning ichida origin degan hususiyatimiz bor va unda bizning matnimiz saqlanadi.

# # Tarjima:
# print(tarjima.text)

# # Original matn tili:
# print(tarjima.src.title())

# Natija: Python - dunyodagi eng mashxur dasturlash tili!
        # Python is the most popular programming language in the world!
        # Uz

# Biz bu matnni boshqa tillarga ham tarjima qilishimiz mumkin buning uchun yuqorida translete metodini ichida yana bir argument dest='ru'
# deb yozishimiz kereak bo'ladi.

# Natija: Python - dunyodagi eng mashxur dasturlash tili!
        # Python — самый популярный язык программирования в мире!
        # Uz
        
# # Shu yo'sinda biz boshqa matnlarni ham tarjima qilishimiz mumkin bo'ladi:
# matn_en = "Tashkent is the capital of Uzbekistan"
# tarjima_uz = tarjimon.translate(matn_en, dest = 'uz')
# print(tarjima_uz.text)       
# # Natija: Toshkent Oʻzbekistonning poytaxti

# Misol uchun biz soddagina dastur yozishimiz mumkin:
# msg = "Tarjima uchun so'z kiriting(chiqib ketish uchun 'q' deb yozing): "
# while True:
#     text = input(msg)
#     if text == "q":
#         break
#     else:
#         tarjima = tarjimon.translate(text, src = 'uz', dest = 'en')
#         print(tarjima.text)
        
        
# Ketingi modulimiz REQUESTS moduli buni o'rnatish uchun konsolda pip install requests deb yozishimiz kifoya.
# Modulning doydasiga kelsak, odatda internet sahifalarni chaqirib olishda ishlatiladi:
# import requests
# from pprint import pprint

# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
# pprint(r.text)

# Natijada biz kun.uz sahifasini to'liq yuklab olamiz html va css kodlari va albatta yangililar matnlari ham bular ichida bo'ladi.


# REQUESTS modulidan asosan API lar bilan ishlashda ishlatiladi.
# API nima degani? API bu onlaynda qandaydur tayyor hizmatlar bor, biz bu hizmatlarga tegishli ravishda murojaat qilganimizda u sahifa yoki
# hizmat bizga qandaydur foydali ma'lumot qaytaradi. Albatta bu holatda ishlab biz ko'plab ajoyib dasturlar yaratishimiz mumkin bo'ladi:
    
# Keling buni misolda ko'ramiz:
# restcountries API
# import requests # HTTP so'rovlarini yuborish uchun 'requests kutubxonasini import qilish.

# # Izlanayotgan mamlakat nomi:
# country = "Uzbekistan"

# # API so'rovi uchun URL manzili:
# url = f"https://restcountries.com/v3.1/name/{country}" # Mamlakat haqida ma'lumot olish uchun API manzili.

# # So'rov yuborish:
# r = requests.get(url) # API manziliga GET so'rovini yuborish va javobni 'r' o'zgaruvchisiga saqlash.

# try:
#     r_json = r.json() # Javobni JSON formatda o'qish. Agar muvoffaqyatsiz bo'lsa, xato yuzaga keladi.
    
#     # Javob ro'yxat ekanligini va bo'sh emasligini tekshirish.
#     if isinstance(r_json, list) and len(r_json) > 0:
#         # Agar ro'yxat bo'lsa, birinchi elementning 'capital' maydonini olishga harakat qilamiz.
#         # 'capital' maydoni mavjud bo'lmasa, ['No capital'] ni qaytarami. Keyin ro'yxatning birinchi elementini tanlaymiz.
#         capital = r_json[0].get('capital', ['No capital'])[0]
#         print("Capital: ", capital) # Aniqlangan poytaxtni chop etish.
#     else:
#         # Agar ro'yxat bo'sh bo'lsa, ma'lumot topilmaganini habar berish.
#         print("No data found for the given country.")
# except ValueError as e: # Agar JSON decodingda xato yuz bersa, bu xato ushlanadi.
#     print("Error decoding JSON:", e)
# except (KeyError, IndexError) as e: # Agar 'KeyError' yoki 'IndexError' yuz bersa, bu xato ushlanadi.
#     print("Error processing data:", e)
    
# Biz r_json buyrug'i orqali berilgan davlat haqida to'liq ma'lumotlarni ko'rishimiz mumkin.


# Endi yana bir sodda dastur yozib ko'ramiz (har safar ishga tushirilganda yangi tavsiya beradigan dastur):
# import requests
# import googletrans

# url = "https://api.adviceslip.com/advice"
# r = requests.get(url)
# advice = r.json()['slip']['advice']
# print(advice)

# translator = googletrans.Translator()
# tarjima = translator.translate(advice, dest = 'uz')
# print(tarjima.text)


# Endi biz BeautifulSoup modulini ko'rib chiqamiz. Bu modul odatda REQUESTS moduli bilan ishlatiladi va bu modul orqali biz veb sahifani
# ichidan aynan o'zimizga kerak bo'lgan ma'lumotlarni sug'urib olishimiz mumkin. Ya'ni biz yuqorida kun.uz saytini ko'rganimizda,
# html kodlar har-xil tushunarsiz narsalar ko'p chiqti va biz bu holatni bartaraf etgan holda BeautifulSoup moduli orqali o'zimizga 
# kerak matnlarni ajratib olishimiz mumkin.

# import requests
# from bs4 import BeautifulSoup

# sahifa  = "https://kun.uz/news/main"
# r = requests.get(sahifa)
# # pprint(r.text)

# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.prettify())
# news = soup.find_all(class_="news-title")
# print(news[0].text)

# import requests
# from bs4 import BeautifulSoup

# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)

# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title")

# if len(news) > 0:
#     print(news[0].text.strip())  # Birinchi yangilikni chop etish
# else:
#     print("Yangiliklar topilmadi. Sahifa tuzilmasini tekshiring.")

# from selenium import webdriver
# from bs4 import BeautifulSoup

# driver = webdriver.Chrome()  # ChromeDriver o'rnatilgan bo'lishi kerak
# driver.get("https://kun.uz/news/main")

# soup = BeautifulSoup(driver.page_source, 'html.parser')
# news = soup.find_all(class_="news-title")

# if len(news) > 0:
#     print(news[0].text.strip())
# else:
#     print("Yangiliklar topilmadi. Sahifa tuzilmasini tekshiring.")

# driver.quit()


# WordCloud moduli:
    
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ChromeDriver yo'lini kiriting
driver_path = "path/to/chromedriver"  # ChromeDriver-ning to'liq yo'lini kiriting
service = Service(driver_path)  # ChromeDriver servisini yaratish

url = "https://kun.uz/news/main"

# Selenium orqali sahifani yuklash
driver = webdriver.Chrome(service=service)
driver.get(url)

# Sahifadan HTML ma'lumotlarini olish
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Yangiliklar sarlavhalarini olish
news = soup.find_all(class_="news-title")  # Yangiliklar uchun class nomi

# Yangiliklar matnini olish
headlines = [item.text.strip() for item in news if item.text.strip()]

if headlines:
    print("Yangiliklar:")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")

    # Yangiliklarni bitta matnga birlashtirish
    text = " ".join(headlines)

    # So‘zlar bulutini yaratish
    wordcloud = WordCloud(
        width=800, height=400,
        background_color='white',
        colormap='viridis'
    ).generate(text)

    # So‘zlar bulutini ko‘rsatish
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Yangiliklar So‘zlar Buluti", fontsize=16)
    plt.show()

else:
    print("Yangiliklar topilmadi.")

# Brauzerni yopish
driver.quit()

# Shunga o'xshash bir qancha foydali modullar bor ular bilan ish faoliyatingiz davomida ko'p to'qnash kelasiz.