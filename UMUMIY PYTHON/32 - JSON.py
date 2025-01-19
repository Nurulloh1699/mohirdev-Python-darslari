# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:47:49 2025

@author: DavrServis
"""

# 32 - DARS.
# JSON.

# Boshlamishiga google maps bilan ishlab ko'ramiz.
# import json
# import googlemaps
# from apikey import APIKEY

# ## GoogleMaps
# gmaps = googlemaps.Client(key = APIKEY)

# data = gmaps.geocode('Oltiariq, Farg\'ona, Uzbekistan')

# # print(geocode_result)

# g = json.dumps(data[0], indent = 4, sort_keys = True)
# print(g)  

# import json
# x = 10
# x_json = json.dumps(x)
# print(x)
# print(x_json)

# y = 5.5
# y_json = json.dumps(y)
# print(y)
# print(y_json)

# JSON ni ishlatkanimizda yani ma'lumotlarni JSON ga olib o'tkanimizda, ma'lumotlar avval
# JavaScript so'ngra sting ga o'tkaziladi:
# m = True
# print(m)
# Natija: True
# m_json = json.dumps(m)
# print(m_json)
# Natija: true

# Yana bir misol ko'ramiz:
# sonlar = (1,2,3,4,5)
# print(sonlar)
# Natija: (1, 2, 3, 4, 5)
# sonlar_json = json.dumps(sonlar)
# print(sonlar_json)
# Natija: [1, 2, 3, 4, 5]

# Ko'rib turganingizdek bizdagi tuple ro'yxati to'rtburchak qavsli [] oddiy ro'yxatga o'zgarib
# qoldi. Buning sababi shundaki JavaScript da Pythondagi tuple ro'yxatlar maxsus ARRAY degan 
# ma'lumot turiga o'tkaziladi.

# Keling Pythondagi ma'lumot turlari JavaScript da qanday ma'lumot turiga o'zgarishini ko'ramiz:
    # dict -> Object
    # list -> Array 
    # tuple -> Array
    # str -> String
    # int -> Number
    # float -> Number
    # True -> true
    # False -> false
    # None -> null
# Demak ma'lumot turlari shu ko'rinishda o'zgarar ekan.

# Keling endi bu ma'lumot turlarini yana qaytadan Pythonga o'tkazamiz:
# print(json.loads(m_json))
# Yuqorida mantiqiy qiymat o'z holatiga qaytdi keling endi ro'yxatimizni ham o'z holiga
# qaytaramiz:
# print(json.loads(sonlar_json))

# Endi bu yerda ro'yxatimiz oddiy ro'yxatligicha qoldi buning sababi ro'yxatimiz JavaScriptga
# o'tkanidan keyin Array ma'lumot turiga o'tkazilgan edi. Python bu ma'lumot turini aniq turini 
# bilmagani uchun uni oddiy ro'yxat ko'rinishida qabul qildi.

# Bu holatda albatta sonlar_json string ko'rinishida saqlandi va biz uni elamentlarini
# ko'ramiz desak bunday qila olmaymiz:
# print(sonlar_json[0])
# Natija: [ 
# Yani bu str turiga mansub bo'lgani uchun ro'yxatning har bir elamentini alohida db yuritadi.

# Keling endi json ekranga chiqaradigan ma'lumotlarni chiroyliroq qilib chiqarsin shuni tashkil
# qilamiz:
# bemor = {
#     "ism" : "Alijon Valiyev",
#     "yoshi" : 30,
#     "oila" : True,
#     "farzandlar" : ("Axmad", "Bonu"),
#     "allergiya" : None,
#     "dorilar" : [
#         {"nomi": "Analgin", "miqdori" : 0.5},
#         {"nomi": "Panadol", "miqdori" : 1.2}
#         ]
#     }
# print(type(bemor))
# Natija: dict
#bemor_json = json.dumps(bemor)
#print(type(bemor_json))
# Natija: str
#print(bemor_json)

# bemor_json = json.dumps(bemor, indent = 4)
# print(bemor_json)

# Aytaylik biz bemor ichadigan dorilarini ko'rmoqchimiz:
# print(bemor.keys())
# print(bemor["dorilar"])

# Biz bu jsonlarni fayllarga saqlashimiz mumkin:
# with open('bemor.json', 'w') as f:
#     json.dump(bemor, f) 

# Endi biz bemor_json degan o'zgaruvchini toyorlaymiz va uni qayta oddiy o'zgaruvchi holatiga
# o'tkazamiz:
# bemor_json = json.dumps(bemor)
# print(type(bemor_json))

# Demak xulosa: json.dumps orqali biz o'zgaruvchini json ga o'tkazamiz json.loads orqali esa uni
# yana oddiy o'zgaruvchi holatiga qaytaramiz.

# Endi fayllarni qanday ochamiz shuni ko'rib chiqaylik:
# import json

# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)
# print(type(bemor))
# Endi uni qaytadan yana oddiy o'zgaruvchiga o'tkazamiz.
# bemor2 = json.loads(bemor_json)
# print(type(bemor2))

# AMALIYOT TOPSHIRIQLARI:
#1 - Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring:
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# import json
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_json = json.dumps(data)
# print(data_json)

#2 - Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring:
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)
# print(type(talaba))
# print(talaba["ism"])
# print(talaba["familiya"])

#3 - Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.
# with open('data.json', 'w') as d:
#     json.dump(data, d)
    
# with open('talaba.json', 'w') as t:
#     json.dump(talaba, t)
    
#4 - Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan.
# Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida
# konsolga chiqaring.
# import json  # JSON formatdagi fayllar bilan ishlash uchun json kutubxonasini yuklaymiz

# try:  
    # Xatolarni ushlash va ishlov berish uchun try-except blokidan foydalanamiz
    # with open('students.json', 'r') as s:  
        # 'students.json' faylini o'qish uchun ochamiz ('r' - read mode, faqat o'qish rejimi)
        # talabalar = json.load(s)  
        # JSON fayldan ma'lumotlarni yuklaymiz va Python ro'yxati yoki lug'atiga aylantiramiz

        # print(talabalar)  
        # Yuklangan ma'lumotlarni konsolga chiqaramiz
# except json.JSONDecodeError as e:  
    # Agar JSON fayl noto'g'ri formatda bo'lsa, bu xatoni ushlaydi
    # print("JSON formatida xatolik:", e)  
    # Xato haqida batafsil ma'lumotni konsolga chiqaramiz
# except FileNotFoundError:  
    # Agar fayl topilmasa (masalan, noto'g'ri nom berilgan bo'lsa), bu xatoni ushlaydi
    # print("Fayl topilmadi.")  
    # Fayl yo'qligi haqida xabar beramiz

# JSON ma'lumotlarini dictionary formatida saqlaymiz
# data = {
#     'student': [
#         {'id': '01', 'name': 'Tom', 'lastname': 'Price', 'year': 4, 'faculty': 'Engineering'},
#         {'id': '02', 'name': 'Nick', 'lastname': 'Thameson', 'year': 3, 'faculty': 'Computer Science'},
#         {'id': '03', 'name': 'John', 'lastname': 'Doe', 'year': 2, 'faculty': 'ICT'}
#     ]
# }

# Talabalar ro'yxatidan 'name' va 'lastname' ma'lumotlarini chiqaramiz
# for talaba in data['student']:  
    # Har bir talaba uchun data['student'] ro'yxatini takrorlaymiz
    # name = talaba['name']  
    # Talabaning ismini olish
    # lastname = talaba['lastname']  
    # Talabaning familiyasini olish
    
    # print(f"{name} {lastname}")  
    # Ism va familiyani formatlangan holda chiqarish.
    
#5 - Quyidagi bog'lamaga kirsangiz, Wikipediadagi Python dasturlash tili haqidagi maqolani JSON ko'rinishida ko'rishingiz mumkin. Brauzerda chiqqan ma'lumotni JSON ko'rinishida saqlang (brauzerda Ctrl+S tugmasini bosib). Faylni Pythonda oching va konsolga maqolaning sarlavhasi (title) va qisqa matnini (extract) chiqaring: https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python

# import json

# JSON faylni ochish va o'qish
# with open('python_wikipedia.json', 'r', encoding='utf-8') as f:
    # data = json.load(f)

# JSON ma'lumotlarini to'liq ko'rish
# print(json.dumps(data, indent=4, ensure_ascii=False))

# Identifikatorni JSON tarkibidan toping va shunga qarab kodni o'zgartiring
# page_id = list(data['query']['pages'].keys())[0]  # Birinchi identifikatorni avtomatik olish

# Sarlavha va qisqa matnni olish
# title = data['query']['pages'][page_id]['title']
# extract = data['query']['pages'][page_id]['extract']

# Natijani konsolga chiqarish
# print("Sarlavha:", title)
# print("Qisqa matn:", extract)
 

# 32 - DARS TUGADI.