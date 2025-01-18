# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:25:01 2024

@author: DavrServis
"""
# UMUMIY TAKRORLASH.
















# 31 - DARS.
# FAYLLAR.
# Faylni ochish va o'qish
# with open(r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\test.txt') as file:
#     pi = file.read()  # Fayl ichidagi barcha matnni o'qib, `pi` o'zgaruvchisiga saqlash

# Fayldan o'qilgan matnni konsolga chiqarish
# print(pi)

# Matn oxiridagi bo'sh joylar va yangi qator belgilarini olib tashlash
# pi = pi.rstrip()

# Matndagi barcha yangi qator (`\n`) belgilarini olib tashlash
# pi = pi.replace('\n', '')

# Matnni float turiga o'zgartirish
# pi = float(pi)

# Float qiymatni konsolga chiqarish
# print(pi)

# Endi boshqa fayl misolida ko'ramiz:
# filename = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\talabalar.txt'
# with open(filename) as file:  # `filename` o'zgaruvchisida ko'rsatilgan faylni ochadi
#     for line in file:  # Fayldagi har bir qatorni ketma-ket ko'rib chiqadi
#         print(line)  # Har bir qatorni ekranga chiqaradi

# Endi bu talabalarni ismlarini har birini bittadan obyekt sifatida saqlashni ko'rib chiqamiz:
# with open(filename) as file:  # `filename` o'zgaruvchisida ko'rsatilgan faylni ochadi
#     talabalar = file.readlines()  # Fayldagi barcha qatorlarni ro'yxat (list) sifatida o'qiydi

# O'qilgan qatorlar ro'yxatini konsolga chiqarish
# print(talabalar)  # `talabalar` ro'yxatini ekranga chiqaradi

# Keling endi talaba ma'lumotlari ohiridagi \n belgisini olib tashlashni ko'rib chiqamiz:
# talabalar = [talaba.rstrip() for talaba in talabalar]

# print(talabalar)

# Biz yuqorida faqat fayllarni o'qishni ko'rdik, endi ularga yozishni ko'rib chiqamiz.
# faylnomi = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\new_file.txt'
# ism = "Nurulloh"
# tyil = 1999
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism + '\n')
#     fayl.write(str(tyil) + '\n')
# print(faylnomi)
# Yuqoridagi usul orqali fayldagi eski ma'lumotlar o'chirilib ustidan yangi ma'lumotlar yoziladi, buni oldini olish uchun quyidagicha yo'l
# tutamiz:
# faylnomi = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\new_file.txt'

# with open(faylnomi, 'a') as fayl:
#     fayl.write("Anvarov" + "\n")
#     fayl.write("2004" + "\n")
    
# Biz matnlarni fayllarga saqladik, endi fayllarga lug'atlar va o'zgaruvchilar saqlashni ko'rib o'tamiz.
# import pickle # Bu usulda yaratilgan fayllar faqatgina Pythonning o'zida ochish mumkin bo'ladi boshqa hech qanday usul bilan ochib
# bo'lmaydi.

# talaba1 = {"ism":"Hasan", "familiya":"Husanov", "tyil":2003, "kurs":2}
# talaba2 = {"ism":"Alijon", "familiya":"Valiyev", "tyil":2004, "kurs":1}

# with open('info', 'wb') as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)
    
# Faylimizni tayorlab oldik keling endi uni o'qishga harakat qilamiz:
# import pickle

# with open('info', 'rb') as file:
#     talaba1 = pickle.load(file)
#     talaba1 = pickle.load(file)

# print(talaba1)
# print(talaba2)

# AMALIYOT TOPSHIRIQLARI:
#1 - Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching.
# import pickle  # pickle moduli import qilinmoqda, lekin hozircha bu kodda ishlatilmayapti

# Fayl manzilini belgilash
# filename = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\topshiriq1.txt'

# Faylni ochish va uning ichidagi qatorlarni o'qish
# with open(filename) as file:  # Faylni ochadi. "with" konstruktsiyasi faylni ishlatib bo'lgandan keyin yopishni ta'minlaydi.
#     for line in file:  # Fayldagi har bir qatorni ketma-ket ko'rib chiqadi
#         print(line)  # O'qilgan qatorni ekranga chiqaradi

#2 - Quyidagi pi_million_digits.txt faylini yuklab oling (faylda π  soni nuqtadan so'ng million xona aniqlik bilan yozilgan). 
# Sizning tug'ilgan kuningiz π soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz
# 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.
# import pickle
# pitop = r'C:\Users\DavrServis\Desktop\GitHUB\mohirdev-Python-darslari\Fayllar bilan ishlash\pi_million_digits.txt'
# with open(pitop) as file:
#     pi = file.read()
# pi = pi.rstrip()
# pi = pi.replace('\n', '')
# pi = pi.replace(' ', '')

# bdate = '16031999' or '03161999' or '19991603'
# # print(pi)
# print(bdate in pi)

# #4 - Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.
# pi = float(pi)
# print(pi)

# with open('pi','wb') as file:
#     pickle.dump(pi,file)

# 31 - DARS TUGADI.


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

# 33 - DARS.
# TRY-EXCEPT XATOLAR USTIDA ISHLASH.
# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2025-yosh}-yilda tug'ilgansiz!")
# Yoshingizni kiriting: 26
# Natija: Siz 1999-yilda tug'ilgansiz.

# Yoshingizni kiriting: 25.5
# ValueError: invalid literal for int() with base 10: '25.5'

# Endi shu holatlarni oldini olishni ko'rib chiqamiz. Buning uchun try-except funksiyasidan
# foydalanamiz: 
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)    
#     print(f"Siz {2025 - yosh}-yilda tug'ilgansiz.")
# except:
#     print("Siz butun son kiritmadingiz!")    
# Yoshingizni kiriting: 26.5
# Natija: Siz butun son kiritmadingiz!

# Yoshingizni kiriting: 26
# Natija: Siz 1999-yilda tug'ilgansiz.

# Agar yanayam to'g'riroq yozmoqchi bo'lsak bunday qilamiz:
# yosh = input("Yoshingizni kiritng: ")
# try:
#     yosh = int(yosh)
# except:
#     print("Siz butun son kiritmadingiz!")
# else:
#     print(f"Siz {2025-yosh}-yilda tug'ilgansiz.")
# Aytish kerakki yuqoridagi amallar bilan kod to'htab qolmaydi va agar kod davomiga biz ayrim
# qo'shimchalar yozsak o'shalar ham bajarilib keyin kodlar tugasa shunda dastur to'htaydi
# print("Dastur davom etyapti.")
# print("Dastur tugadi.")    
# Bunda ham natija o'zgarmaydi.

# except bilan biz turli xil xatolarni ushlashimiz mumkin. Yuqoridagi xolatga o'xshab har turli
# xatoga bir hil habar chiqavermaydi. Buni qanday amalga oshiramiz hozir ko'ramiz:

# ZeroDivisionError
# x, y = 5, 10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
    
# IndexError
# mevalar = ['olma', 'banan', 'gilos', 'shaftoli']
# try:
#     print(mevalar[5])
# except IndexError:
#     print("Xato index kiritdingiz ro'yxatda 4ta element bor xolos!")

# KeyError
# user = {"username" : "Nurulloh",
#         "status" : "Admin",
#         "email" : "nurik9.99@bk.ru",
#         "phone" : "998971234567"
#         }

# key = "tel"
# try:
#     print(f"Foydalanuvchi {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas.")

# Keling endi fayllar bilan ishlab ularda uchrashi mumkin bo'lgan xatolar bilan tanishamiz:
# filename = 'data.txt' # Bunday fayl mavjud emas.
# try: 
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"{filename} fayli mavjud emas.")
    
# Bir nechta fayllar bilan ishlab ko'ramiz:
# import json     
# talaba1 = "Abdurashidov Nurulloh"
# json_talaba1 = json.dumps(talaba1)
# talaba2 = "Abdurashidova Mavludaxon"
# json_talaba2 = json.dumps(talaba2)
# talaba4 = "Olim Olimov"
# json_talaba4 = json.dumps(talaba4)


# Json turidagi ma'lumotlarimizni faylga yuklaymiz:
# with open('json_talaba1', 'w') as f:
#      json.dump(talaba1, f) 
     
# with open('json_talaba2', 'w') as f:
#      json.dump(talaba2, f) 

# with open('json_talaba4', 'w') as f:
#      json.dump(talaba4, f) 
     
# files = ['json_talaba1', 'json_talaba2', 'json_talaba3', 'json_talaba4']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas!")
#     else:
#         print(talaba)      
# Shu tariqa biz fayllar bilan ishlashimiz mumkin.


# Biz faqat bitta EXCEPT emas, balki bir nechta EXCEPTlar yozishimiz ham mumkin:
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20 / n
# except ValueError:
#     print("Butun son kiritmadingiz!")
# except ZeroDivisionError:
#     print("0ga bo'lish mumkin emas.")
# else:
#     print(f"x = {x}")
    
# Aslida bizbunday kodlarni TRY-EXCEPT bilan emas WHILE sikli bilan yozsak ham bo'ladi ya'ni
# TRY-EXCEPT bizda jiddiyroq xatolar uchun desak, keling yuqoridagi kodlarni WHILE sikli orqali
# yozib ko'ramiz:
# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2025 - yosh}-yilda tug'ilgansiz!")

# Endi bu kodni WHILE sikliga tushiramiz:
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit(): # Bu yerda isdigit() metodi orqali kiritilgan qiymat raqamlardan iborat
    # yoki yo'qligini tekshiramiz.
#         yosh = int(yosh)
#         break
# print(f"Siz {2025 - yosh}-yilda tug'ilgansiz!")

# 33 - DARS TUGADI.

# 34 - DARS.
# FUNKSIYALARNI TEKSHIRISH.

# Bu dars orqali biz dasturimizni tekshirishni o'rganishni davom etamiz. Biz dasturimiz davomida
# turli hil finksiyalar va obyektlar yaratishimiz tabiiy va albatta o'z-o'zidan yozgan ko'dimizni 
# joyidayoq tekshirib ketishimiz kerak bo'ladi.

# Bu darsda biz qanday qilib bu tekshirishlarni avtomatlashtirishni o'rganamiz.

# Oddiy funksiyani tekshirishdan boshlaymiz:
# def get_full_name(ism, familiya):
#     return f"{ism} {familiya}".title()

# print(get_full_name('alijon', 'valiyev'))
# Natija: Alijon Valiyev
# Yuqoridagi kod ishladi va xatolarsiz

# Biz endi funksiyalarni UNITTEST orqali test qilishni boshlaymiz.
# Aslida quyida keltirilgan misollar alohida modullarda bajariladi lekin misol sifatida
# darsimizda yozib qo'yamiz.

# Deylik bu yerda xatolik bo'ldi va biz kutgan natija chiqmadi. Etibor bersangiz biz funksiyani 
# qo'lda tekshiryapmiz, lekin odatda Pythonda buni avtomatlashtirish mumkin va dastur o'zini-o'zi
# tekshiradigan qilib dastur yozishimiz mumkin.

# Bunday amalni amalga oshirish uchun Pythonda UNITTEST degan modul mavjud. Bu modul orqali biz 
# dasturimiz ustida bir nechta testlarni amalga oshirishimiz mumkin, agar bitta test amalga
# oshirsak, bu TEST CASE dev ataladi.

# Endi biz o'zimizga kerakli bo'lgan funksiyalarni alohida modulda saqlaymiz.

# name_test.py modulida yozilgan kodlar.
# import unittest # Bu qism ham standart shablon desak bo'ladi.
# from name import get_full_name # Bu qism test qilinayotkan obyektga qarab o'zgaradi.

# class NameTest(unittest.TestCase): # Test qilish uchun qo'llaniladigan standart shablon.
# Endi biz bu yerda etiboe beradigan narsamiz oddiy class ning ichida yozilgan metodlar funksiyani
# test qilish uchun yozilgani uchun ularni nomini boshiga test so'zini qo'shib ketamiz. Bu bizga 
# test dasturimizni bajarganimizda qo'l keladi va Python ham avval test so'zi bilan yozilgan 
# dasturlarni qidiradi va birma-bir bajarib chiqadi.
#     def test_toliq_ism(self): # To'liq ismni test qiluvchi metod.
#         name = get_full_name('nurulloh', 'abdurashidov') # Funksiyadan qiymat olyapmiz.
#         self.assertEqual(name, 'Nurulloh Abdurashidov') # Qiymat biz kiritgan qiymatga mos bo'lsa.
        
# unittest.main() # Tekshirish uchun yozilgan kod.
# Natija: Ran 1 test in 0.001s

        # OK
        
# Endi vaqt o'toshi bilan bizning funksiyamiz o'zgardi.
# def get_full_name(ism, otasi, familiya):  # Tartib: ism, otasi, familiya
#     return f"{ism} {otasi} {familiya}".title()

# print(get_full_name('alijon', 'olimovich', 'valiyev'))

# Test funksiyamizni o'zgartirganimiz yo'q. Agar endi tekshirsak quyidagicha javob olamiz:
# Natija: Ran 1 test in 0.002s

        # FAILED (errors=1)
# Ko'rib turganingizdek xato kelib chiqti.

# Nima qilishimiz mumkin? Bu xatoni to'g'irlash uchun biz full_name funksiyamizga o'zgartirish
# kiritamiz:
# def get_full_name(ism, familiya, otasi = ''):
#     if otasi:
#         return f"{ism} {otasi} {familiya}".title()
#     else:
#         return f"{ism} {otasi} {familiya}".title()
    
# Natija: Ran 1 test in 0.001s

        # OK

# Endi kodimiz yana testdan o'tdi.

# Bu holatda funksiyamiz qo'shimcha qiymat qo'shib qo'qganimiz uchun, testimizga ham qo'shimcha 
# qilishimiz kerak.
# def test_otasining_ismi(self):
#     name = get_full_name('nurulloh', 'abdurashidov', "yorqinjon o'g'li")
#     self.assertEqual(name, 'Nurulloh', 'Abdurashidov', "Yorqinjon o'g'li")
    
# Endi tekshirib ko'rsak.
# Natija: Ran 2 tests in 0.002s

        # FAILED (errors=1)
        
# Ikki marta test qilindi va bittasi xato deyapti.

# Xatoni to'g'irladik.
# Natija: Ran 2 tests in 0.003s

        # OK
# Endi hammasi joyida.

# Biz yuqorida matnlar bilan ishladik endi sonlar va raqamlar bilan ishlab ko'ramiz.
# def getArea(r, pi = 3.14159):
#     """Doiraning yuzini qaytaruvchi funksiya"""
#     return pi*(r**2)

# def getPerimeter(r, pi = 3.14159):
#     """Doiraning perometrini qaytaruvchi dastur"""
#     return 2 * pi * r
# Endi bu funksiyalarni test qilib ko'ramiz va buni yangi test moduli orqali qilamiz:
# import unittest
# from circle import getArea, getPerimeter

# class CircleTest(unittest.TestCase):
#     def test_area(self):
#         self.assertEqual(getArea(5), 78.53975)
#         self.assertEqual(getArea(10), 314.159)
        
# unittest.main()

# Aslida yuqorida matematik yechimlar uchun assertEqual tengligini ishlatishimiz noto'g'ri,
# chunki, nuqta verguligacha aniq natijalar olishimiz kam uchraydi va aynan shuning uchun 
# assertAlmostEquel tengligini ishlatganimiz maqsadga muvofiq bo'ladi Almost so'zining tarjimasi
# deyarli degan manoni beradi. Bu tenglik orqali butun son va undan keyin nuqta va nuqtadan 
# keyingi 7ta songacha tekshiradi agar hohlasak uzunlikni o'zimiz berishimiz ham mumkin.

# Shu tarzda endi biz Perimetrni ham tekshiramiz:

# Agar funksiya mantiqiy qiymat qaytarsa, bunday funksiyalarni assertTrue() va assertFalse() metodlari yordamida tekshirishimiz mumkin. 

# Quyidagi funksiyamiz kiritilgan son tub yoki yo'q ekanini tekshiradi:

# def tubSonmi(n):
#     if n==2 or n==3: return True
#     if n%2==0 or n<2: return False
#     for i in range(3, int(n**0.5)+1, 2):   # faqat toq sonlarni tekshiramiz
#         if n%i==0:
#             return False   
#     return True
# Funksiyani alohida tubSonmi.py fayliga saqlaymiz. Funksiyani tekshirish uchun tubSon_test.py dasturini yozamiz:

# import unittest
# from tubSonmi import tubSonmi

# class tubSonTest(unittest.TestCase):
#     def test_true(self):
#         self.assertTrue(tubSonmi(7))
#         self.assertTrue(tubSonmi(193))
#         self.assertTrue(tubSonmi(547))
#     def test_false(self):
#         self.assertFalse(tubSonmi(6))
#         self.assertFalse(tubSonmi(265))
#         self.assertFalse(tubSonmi(489))
        
# unittest.main()
# Test davomida tubSonmi() funksiyasini bir nechta tub (7, 193, 547) va tub bo'lmagan (6, 265, 489) sonlar bilan chaqirdik. Bunda assertTrue() metodi funksiyamiz haqiqatdan ham True qiymatini qaytarishini, assertFalse() metodi esa funksiyamiz False qiymat qaytarishini tekshiradi.

# TAQQOSLASH METODLARI
# TestCase klassi tarkibidagi boshqa taqqoslash metodlari ham mavjud:

# Metod
# Nimani taqqoslaydi?

# assertEqual(a, b) -> a == b

# assertNotEqual(a, b) -> a != b

# assertTrue(x) -> x ning qiymati True

# assertFalse(x) -> x ning qiymati False

# assertIs(a, b) -> a bu b

# assertIsNot(a, b) -> a bu b emas

# assertIsNone(x) -> x ning qiymati None

# assertIsNotNone(x) -> x ning qiymati None emas

# assertIn(a, b) -> a b ning ichida

# assertNotIn(a, b) -> a b ning ichida emas

# assertIsInstance(a, b) -> a b ning vorisi

# assertNotIsInstance(a, b) -> a b ning vorisi emas

# AMALIYOT TOPSHIRIQLARI:
#1 - Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya.
# def find_max(a, b, c):
#     return max(a, b, c)

# print(find_max(10, 20, 21))
# # Natija: 21

# # Test dasturi:
# class TestFindMax(unittest.TestCase):
#     def test_find_max(self):
#         self.assertEqual(find_max(10, 20, 15), 20)
#         self.assertEqual(find_max(5, 3, 8), 8)
#         self.assertEqual(find_max(-10, -5, -7), -5)


# unittest.main()

# #2 - Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta
# # harfga o'zgatiruvchi funksiya
# def capitalize_first_letters(strings):
#     capitalized_list = []
#     for string in strings:
#         capitalized_list.append(string.capitalize())
#     return capitalized_list
# texts = ['olma', 'shaftoli', 'banan']
# result = capitalize_first_letters(texts)
# print(result)
# # Natija: ['Olma', 'Shaftoli', 'Banan']

# # Test dasturi:
# class TestCapitalizeFirstLetters(unittest.TestCase):
#     def test_capitalize_first_letters(self):
#         self.assertEqual(capitalize_first_letters(['salom', 'dunyo']), ['Salom', 'Dunyo'])
#         self.assertEqual(capitalize_first_letters(['python', 'dasturlash']), ['Python', 'Dasturlash'])
#         self.assertEqual(capitalize_first_letters([]), [])


# unittest.main()

# #3 - Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya.
# def filter_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]   

# nums = [1,2,3,4,5,6,7,8,9]
# result = filter_even_numbers(nums)
# print(result)
# # Natija: [2, 4, 6, 8]

# # Test dasturi:
# class TestFilterEvenNumbers(unittest.TestCase):
#     def test_filter_even_numbers(self):
#         self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
#         self.assertEqual(filter_even_numbers([10, 11, 12, 13]), [10, 12])
#         self.assertEqual(filter_even_numbers([1, 3, 5]), [])
    
# unittest.main()

# #4 - Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) qaytaruvchi
# # funksiya yozing.
# import math
# def is_fibonachi(n):
#     def is_perfect_square(x):
#         s = int(math.sqrt(x))
#         return s * s == x
    
#     return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# print(is_fibonachi(21))
# # Natija: True

# # Test dasturi:
# import unittest

# class TestFibonachi(unittes.TestCase):
#     def test_is_fibonachi(self):
#         self.assertTrue(is_fibonachi(8))
#         self.assertTrue(is_fibonachi(13))
#         self.assertTrue(is_fibonachi(15))
    
# unittest.main()

# 34 - DARS TUGADI.

# 35 - DARS.
# KLASSLARNI TEKSHIRISH.

# Klasslarni tekshirish uchun avval oldingi darsda ko'rgan klasslarimizdan birini yaratib olamiz.
# class Car:
#     """(self, make, model, year, km = 0, price = None)"""
#     def __init__(self, make, model, year, km = 0, price = None):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price
#         self.__km = km
        
#     def set_price(self, price):
#         self.price = price
        
#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             raise ValueError("km manfiy bo'lishi mumkin emas")
            
#     def get_info(self):
#         info = f"{self.make.upper()} {self.model.title()}"
#         info += f"{self.year}-yil, {self.__km} km yurgan"
#         if self.price:
#             info += f" Narhi: {self.price}"
#         return info
    
#     def get_info(self):
#         info = f"{self.make.upper()} {self.model.title()}"
#         info += f"{self.year}-yil, {self.__km}km yurgan"
#         if self.price:
#             info += f" Narhi: {self.price}"
#         return info
    
#     def get_km(self):
#         return self.__km
# Endi bu klassimizni alohida modulga joylaymiz.

# QUYIDA BIZ DASTURIMIZNI CAR.PY MODULIDA SAQLAYMIZ:
# class Car:
#     """(self, make, model, year, km = 0, price = None)"""
#     def __init__(self, make, model, year, km = 0, price = None):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price
#         self.__km = km
        
#     def set_price(self, price):
#         self.price = price
        
#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             raise ValueError("km manfiy bo'lishi mumkin emas!")
            
#     def get_info(self):
#         info = f"{self.make.upper()} {self.model.title()}"
#         info += f"{self.year}-yil, {self.__km} km yurgan"
#         if self.price:
#             info += f" Narhi: {self.price}"
#         return info
    
#     def get_info(self):
#         info = f"{self.make.upper()} {self.model.title()}"
#         info += f"{self.year}-yil, {self.__km}km yurgan"
#         if self.price:
#             info += f" Narhi: {self.price}"
#         return info
    
#     def get_km(self):
#         return self.__km
    
# Endi bu klassimizni qo'lda tekshirib ko'ramiz:
# avto1 = Car("gm", "malibu", 2020)
# print(avto1.get_info())
# Mana oddiy holatda klassimizdagi get_info() metodini tekshirdik.

# Endi add_km() metodini ham tekshirib ko'ramiz:
# avto1.add_km(5000)
# Endi manfiy qiymat berib ko'ramiz:
# avto1.add_km(-500)
# Natija: ValueError: km manfiy bo'lishi mumkin emas!

# Keling endi har gal qo'lda tekshirishni oldini olish uchun test dastur yozamiz:


# QUYIDA BERILGAN TESTLAR CAR_TEST.PY MODULIDA SAQLANGAN BO'LADI. 
# import unittest
# from cars import Car

# class CarTest(unittest.TestCase):
#     """Car klassini tekshirish uchun test dastur!"""
#     def setUp(self):
#         make = 'GM'
#         model = 'Malibu'
#         year = 2020
#         self.price = 40000
#         self.km = 10000
#         self.avto1 = Car(make, model, year)
#         self.avto2 = Car(make, model, year, price = self.price)
        
#     def test_create(self):
#         # Qiymatlar mavjudligini ssertIsNotNone metodi orqali tekshiramiz:
#         self.assertIsNotNone(self.avto1.make)
#         self.assertIsNotNone(self.avto1.model)
#         self.assertIsNotNone(self.avto1.year)
#         # Qiymatlar mavjud emasligini assertIsNone metodi orqali tekshiramiz:
#         self.assertIsNone(self.avto1.price)
#         # Qiymat tengligini assertEqual metodi orqali tekshiramiz:
#         self.assertEqual(0, self.avto1.get_km())
#         # avto2 narhini tekshiramiz:
#         self.assertEqual(self.price, self.avto2.price)
        
# Test dasturimizni tekshirib ko'ramiz:
# unittest.main()
# Natija: Ran 1 test in 0.001s

        # OK

# Ba'zi holatlarda shoshganda masalan: model ga make ning qiymati biriktirilishi va yoki teskarisi bo'lgan holatlar bo'lishi mumkin. Bunday
# holatlarda hozirgi testimiz xato qaytarmaydi chunki biz faqat qiymat berilgan yoki yo'qligini tekshiryapmiz.
# Bunday holatlarda testga qo'shimcha qiymatni tekshirish uchun test qatorini qo'shib qo'yishimiz mumkin
        
# import unittest
# from cars import Car

# class CarTest(unittest.TestCase):
#     """Car klassini tekshirish uchun test dastur!"""
#     def setUp(self):
#         make = 'GM'
#         self.model = 'Malibu'
#         year = 2020
#         self.price = 40000
#         self.km = 10000
#         self.avto1 = Car(make, self.model, year)
#         self.avto2 = Car(make, self.model, year, price = self.price)
        
#     def test_create(self):
#         # Qiymatlar mavjudligini ssertIsNotNone metodi orqali tekshiramiz:
#         self.assertIsNotNone(self.avto1.make)
#         self.assertIsNotNone(self.avto1.model)
#         self.assertEqual(self.model, self.avto1.model)
#         self.assertIsNotNone(self.avto1.year)
#         # Qiymatlar mavjud emasligini assertIsNone metodi orqali tekshiramiz:
#         self.assertIsNone(self.avto1.price)
#         # Qiymat tengligini assertEqual metodi orqali tekshiramiz:
#         self.assertEqual(0, self.avto1.get_km())
#         # avto2 narhini tekshiramiz:
#         self.assertEqual(self.price, self.avto2.price) 
        
#     def test_set_price(self):
#         new_price = 45000
#         self.avto2.set_price(new_price)
#         self.assertEqual(new_price, self.avto2.price)
    
#     def test_add_km(self):
#         #1 Musbat qiymat berib ko'ramiz:
#         self.avto1.add_km(self.km)
#         self.assertEqual(self.km, self.avto1.get_km()) # Bu o'rinda biz yana bir narsani tekshirishimiz mumkin (kerak), yuqorida dasturchi 
# km qo'shishda + belgisini esdan chiqargan bo'lishi mumkin agar shunday bo'lsa bizning dastur xato ishlashi mumkin yani shunchaki ohirigi 
# berilgan km ga tenglab qo'yishi mumkin.
#         self.avto1.add_km(5000)
#         self.assertEqual(15000, self.avto1.get_km()) # + belgisi bo'lmagan holatda xato beradi yani km ni 5000 ga tenglab qo'ya qoladi.
#         #2 Manfiy qiymat berib ko'ramiz:
#         new_km = -5000
#         try:
#             self.avto1.add_km(new_km)
#         except ValueError as error:
#             self.assertEqual(type(error), ValueError)

# unittest.main()

# class Car:
#     """(self, make, model, year, km = 0, price = None)"""
#     def __init__(self, make, model, year, km = 0, price = None):
#         self.make = make
#         self.model = make # Shu qatordagi xato tufayli bu holatda biz xato natija oldik.
#         self.year = year
#         self.price = price
#         self.__km = km


# Yuqorida biz test_set_price(self) testini qo'shdik va bu orqali biz set_price degan metodimizni tekshiramiz bu metodimiz mashinaning
# narxini belgilaydi.

# Endi biz yuqorida add_km() metodi uchun test yozamiz bu biroz murakkabroq va bu o'rinda biz ikkita test yozishimiz kerak bo'ladi ya'ni
# bitta testimiz musbat qiymat berib va manfiy qimat berib tekshiramiz.


# ANALIYOT TOPSHIRIQLARI:
#1 - 30 - darsimizda Shaxs va Talaba klasslarini yaratgan edik. Shu ikki klassning xususiyatlari va metodlarini tekshiruvchi test dasturlar
# yozing.

# BU YERDA SHAXS KLASSI ASOSIY KODI KELTIRILGAN:
# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil

# TEST DASTURI:
# import unittest
# from shaxs import Shaxs  # Shaxs klassini import qilamiz

# class TestShaxs(unittest.TestCase):
#     """Shaxs klassining metodlarini test qilish uchun sinf."""
    
#     def setUp(self):
#         """Har bir testdan oldin bajariladigan metod."""
#         # Test uchun Shaxs obyektini yaratamiz
#         self.shaxs1 = Shaxs("Ali", "Valiyev", "AB1234567", 1990)
    
#     def test_get_info(self):
#         """get_info metodini test qilish."""
#         # Kutilgan natija
#         expected_info = "Ali Valiyev. Passport:AB1234567, 1990-yilda tug`ilgan"
#         # get_info metodi natijasini tekshiramiz
#         self.assertEqual(self.shaxs1.get_info(), expected_info)
#         # Izoh: get_info metodi to'g'ri natija qaytarsa, test muvaffaqiyatli o'tadi.
    
#     def test_get_age(self):
#         """get_age metodini test qilish."""
#         # 2025 yilda Shaxsning yoshini tekshiramiz
#         expected_age = 2025 - 1990  # 35 yosh
#         self.assertEqual(self.shaxs1.get_age(2025), expected_age)
#         # Izoh: get_age metodi kutilgan yoshni qaytarsa, test muvaffaqiyatli o'tadi.

# if __name__ == '__main__':
#     unittest.main()

# BU YERDA TALABA KLASSI ASOSIY KODI KELTIRILGAN:
# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil,idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
    
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    
# # TEST DASTURI:
# import unittest
# from shaxs import Shaxs  # Shaxs klassini import qilamiz
# from talaba import Talaba  # Talaba klassini import qilamiz

# class TestTalaba(unittest.TestCase):
#     """Talaba klassining metodlarini test qilish uchun sinf."""
    
#     def setUp(self):
#         """Har bir testdan oldin bajariladigan metod."""
#         # Test uchun Talaba obyektini yaratamiz
#         self.talaba1 = Talaba("Ali", "Valiyev", "AB1234567", 2000, "T123456")
    
#     def test_get_id(self):
#         """get_id metodini test qilish."""
#         # Kutilgan ID raqam
#         expected_id = "T123456"
#         # get_id metodi natijasini tekshiramiz
#         self.assertEqual(self.talaba1.get_id(), expected_id)
#         # Izoh: get_id metodi to'g'ri ID raqamni qaytarsa, test muvaffaqiyatli o'tadi.
    
#     def test_get_bosqich(self):
#         """get_bosqich metodini test qilish."""
#         # Kutilgan bosqich
#         expected_bosqich = 1
#         # get_bosqich metodi natijasini tekshiramiz
#         self.assertEqual(self.talaba1.get_bosqich(), expected_bosqich)
#         # Izoh: get_bosqich metodi to'g'ri bosqichni qaytarsa, test muvaffaqiyatli o'tadi.
    
#     def test_inheritance(self):
#         """Shaxs klassidan meros olishni test qilish."""
#         # Talaba obyektining Shaxs klassiga tegishli metodlarini tekshiramiz
#         self.assertEqual(self.talaba1.get_info(), "Ali Valiyev. Passport:AB1234567, 2000-yilda tug`ilgan")
#         # Izoh: get_info metodi Shaxs klassidan meros bo'lib o'tganini tasdiqlaydi.
#         self.assertEqual(self.talaba1.get_age(2025), 25)
#         # Izoh: get_age metodi Talaba obyektida ham to'g'ri ishlaydi.

# if __name__ == '__main__':
#     unittest.main()

#2 - Ikki klass uchun yagona test yoza olasizmi? (isInstance() funksiyasini eslang)
# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning asosiy ma'lumotlarini saqlash."""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         """Talabaning xususiyatlarini saqlash."""
#         super().__init__(ism, familiya, passport, tyil)  # Shaxs konstruktorini chaqirish
#         self.idraqam = idraqam
#         self.bosqich = 1
    
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich

# Eslatma! Ikkala klass uchun test dasturini keyinchalik yozamiz.

# 35 - DARS TUGADI.


# 36 - DARS.
# PYTHON STANDART KUTUBXONASI.

# Biz o'zimizni dasturimizda turli hil tayyor kutubxonalardan foydalanishimiz mumkin va bu bizga dasturimizda bir necha qulayliklar
# yaratishimiz mumkin.

# Birinchi tanishadigan kutubxonamiz datetime() kutubxonasi bo'ladi. Bu kutubxona orqali biz aniq vaqtni belgilash imkoniga ega bo'lamiz:
# import datetime as dt
# datetime()
# hozir = dt.datetime.now()
# print(hozir)
# Sanani ajratib olish:
# print(hozir.date())
# Vaqtni o'zini ajratib olish:
# print(hozir.time())
# Soatni o'zini ajratib olish:
# print(hozir.hour)
# Minutni o'zini ajratib olish:
# print(hozir.minute)
# Sekundlarni o'zini ajratib olish:
# print(hozir.second)

# datetime ni ichida yana bitta maxsus obyekt bor date deb ataladi va faqat sanani ko'rsatadi:
# date()
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")

# Endi masalan biz alohida sana yaratmoqchi bo'lsam nima qilaman:
# ertaga = dt.date(2025, 1, 16)
# print(f"Ertangi sana: {ertaga}")

# Endi biz time ni ko'rib chiqamiz yani yaxlit soat:
# time()
# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozirgi soat: {vaqtHozir}")
# vaqtKeyin = dt.time(23, 45, 30)
# print(f"Keyingi vaqt: {vaqtKeyin}")

# Sanalar orasidagi farqni qanday topamiz? Buning uchun oddiy - airuv amalidan foydalanamiz:
# bugun = dt.date.today()
# ramazon = dt.date(2025, 2, 20)
# farq = ramazon - bugun
# print(farq)
# Agar etibor bersak, natija obyekt ko'rinishida hosil bo'ldi va buni yahlitlash uchun biz quyidagicha yo'l tutamiz:
# farq.days # kunni yahlitlab oldik.
# print(f"Ramazonga {farq.days} kun qoldi!")

# Soatlar orasidagi farqni ko'ramiz:
# hozir = dt.datetime.now()
# futbol = dt.datetime(2025, 1, 16, 23, 45, 00)
# farq = futbol - hozir
# print(farq)
# sekundlar = farq.seconds
# print(sekundlar)
# Sekundlardan minutlarni hisoblashimiz mumkin:
# minutlar = int(sekundlar/60)
# print(minutlar)
# Soatlar ham shu tartibda topiladi.
# soatlar = int(minutlar/60)
# print(soatlar)

# Bu date kutubxonasi edi:
    
# Endi math kutubxonasi bilan tanishamiz:
# import math

# PI  = math.pi
# print(f"PI ning qiymati: {PI}")
# E = math.e
# print(f"e ning qiymati: {E}") 

# Trigonometriyaga oid funksiyalar:
# math.sin(math.pi/2)
# math.cos(0)
# math.tan(PI)

# Radianlar va burchaklar o'rtasida konvertatsiya
# print(math.degrees(math.pi/2)) # Radian qiymat berilgan burchak qiymatni qaytaradi.
# print(math.radians(90)) # Burchak qiymat bersak radiandagi qiymatlarni qaytaradi.

# Logorifmik funksiyalar:
# Natural logorifm.
# math.log(5)
# 10 asosli logarifm.
# math.log(100)

# Sonlarni yaxlitlash:
# x = 4.6
# print(math.ceil(x)) # Yuqoriga yaxlitlash.
# print(math.floor(x)) # Pastka tomon yaxlitlash.
# round funksiyasi sonni eng yaqin butun songa yaxlitlaydi.
# print(round(x))

# Kvadrat ildiz:
# x = 81
# math.sqrt(x)

# Darajaga oshirish:
# math.pow(x, 3) # x ning kubi.
# math.pow(x, 5) # x ning 5-darajasi.
# math.pow(x, 1/3) # x dan kub ildiz


# Endigi foydali modul pprint moduli va bu modul bilan biz uzundan-uzun matnlarni chiroyli qilib chiqarish uchun foydalanamiz.
# from pprint import pprint
# import json

# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)
    
# print(bemor) # Oddiy print
# pprint(bemor) # PPrint

# import requests
# r = requests.get('https://api.github.com')

# print(r.json())
# pprint(r.json())

# Navbatdagi modul RegEx (RegularExpressions) bu moduldan odatda andozalar ya'ni matnlarni izlash uchun andoza yaratish uchun ishlatiladi.
# import re 
# from word_list import words
# word1 = "темир"
# word2 = "томир"
# word3 = "тулпор"

# andoza = "^т...p$" # Bu o'rinda biz andoza uchun shartlar berdik desak bo'ladi ya'ni bosh harf т va ohirgi harf р bo'lsin deganday.

# print(re.match(andoza, word1)) 
# print(re.match(andoza, word2))
# print(re.match(andoza, word3)) 

# matches = []

# Bu o'rinda tayyoe andozalar olish uchun iHateRegex saytiga kirilsa bu yerda tayyor andozalar olish mumkin.
# Quyida biz bir nechtasini ko'rib chiqamiz:
    
# Tasavvur qiling biz ma'lum bir matning ichidan bizning andozamizga mos matnni sug'urib olmoqchimiz:
# import re
# matn = "Bugungi kun juda qiziqarli o‘tdi, lekin hali ham koʻp ish qilish kerak. Agar qo‘shimcha ma'lumot kerak boʻlsa, menga yozing:\
#     info.random123@gmail.com. \
# Yana bir muhim voqea haqida xabar berishni unutibman. Biz har kuni bir narsa o‘rganamiz, to‘g‘rimi? Bog‘lanish uchun:\
#     contact_me456@outlook.com."

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza, matn)
# print(email)


# Endi parol uchun andoza tayorlaymiz:
# andoza = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
# msg = "Yangi parol kiriting"
# msg += "(kamida 8ta belgidan iborat, kamida 1ta Lotin bosh harf, 1ta kichik harf, "
# msg += "1ta son va 1ta maxsus belgi bo'lishi kerak): "

# while True:
#     password = input(msg)
#     if re.match(andoza, password):
#         print("Maxfiy so'z qabul qilindi!")
#         break
#     else: 
#         print("Maxfiy so'z talabga javob bermadi!")


# AMALIYOT TOPSHIRIQLARI:
#1 - Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring:
from datetime import datetime, timedelta # Sana va vaqt bilan ishlash uchun kerakli kutubxonalarni import qilib olamiz.

# Bugungi sana:
bugungu_sana = datetime.now() # Hozirgi vaqtni olib, bugungi_sana o'zgaruvchisiga saqlaymiz.
# 2 haftalik farq bilan 10ta sana:
for i in range(10): # 10ta iteratsiya uchun siklni ishga tushiramiz.
    yangi_sana = bugungu_sana + timedelta(weeks = 2 * i)
    print(yangi_sana.strftime('%Y-%m-%d')) # Yangi sana 'YYYY-MM-DD' formatida konsolga chiqadi.

# Natija: 2025-01-16
        # 2025-01-30
        # 2025-02-13
        # 2025-02-27
        # 2025-03-13
        # 2025-03-27
        # 2025-04-10
        # 2025-04-24
        # 2025-05-08
        # 2025-05-22
    
#2 - Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring:
from datetime import datetime # Sana va vaqt bilan ishlash uchun 'datatime' kutubxonasini yuklab olamiz.
# Ramazon va Qurbon hayiti sanalari:
ramazon_hayiti = datetime(2025, 3, 31) # Ramazon hayitining sanasi: 2025 - yil 31 - mart.
qurbon_hayiti = datetime(2025, 6, 28) # Qurbon hayitining sanasi: 2025 - yil 28 - iyun.

# Bugungi sana:
bugun = datetime.now() # Hozirgi vaqt va sanani 'datetime.now' funksiyasi orqali bugun o'zgaruvchisiga yuklaymiz.

# Kunning farqini hisoblash:
ramazon_kunlari_qoldi = (ramazon_hayiti - bugun).days # Ramazon hayitigacha qolgan kunlar.
qurbon_kunlari_qoldi = (qurbon_hayiti - bugun).days # Qurbon hayitigacha qolgan kunlar.

# Natijani konsolga chiqarish:
if ramazon_kunlari_qoldi >= 0: # Agar Ramazon hayitigacha qolgan kunlar 0 yoki undan katta bo'lsa.
    print(f"Ramazon hayitigacha {ramazon_kunlari_qoldi} kun qoldi!") # Konsolga qolgan kunlar chiqadi.
else: # Aks holda (hayit o'tib ketkan bo'lsa)
    print("Ramazon hayiti o'tib ketkan!") # Ramazon hayiti o'tib ketkanligi haqidagi xabar konsolga chiqarilsin.
    
if qurbon_kunlari_qoldi >= 0:
    print(f"Qurbon hayitigacha {qurbon_kunlari_qoldi} kun qoldi!")
else:
    print("Qurbon hayiti o'tib ketkan!")

# Natija: Ramazon hayitigacha 73 kun qoldi!
        # Qurbon hayitigacha 162 kun qoldi!
        
#3 - Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing
from datetime import datetime
def hisobla_tugilgan_kun(tugilgan_sana):
    """Tug'ilgan kundan boshlab bugungi sanagacha qancha yil, oy va kun o'tganini hisoblaydi.
    
    Args:
        tug'ilgan_sana (datetime): Tug'ilgan sana (datetime formatida).
        
    Returns:
        tuple: (yillar, oylar, kunlar)
    """
    bugun = datetime.now() # Hozirgi vaqt va sanani olamiz.
    yil_farq = bugun.year - tugilgan_sana.year # Yillar farqini hisoblaymiz.
    oy_farq = bugun.month - tugilgan_sana.month # Oylardagi farqni hisoblaymiz.
    kun_farq = bugun.day - tugilgan_sana.day # Kunlar farqini hisoblaymiz.
    
    # Agar oylarda yoki kunlarda manfiy qiymat bo'lsa, tegishli tuzatish kiritamiz:
    if kun_farq < 0:
        oy_farq -= 1
        oldingi_oy_kunlari = (bugun.replace(day = 1) - timedelta(days = 1)).day
        kun_farq += oldingi_oy_kunlari
        
    if oy_farq < 0:
        yil_farq -= 1
        oy_farq += 12
        
    return yil_farq, oy_farq, kun_farq

# Tug'ilgan sana:
tugilgan_sana = datetime(1999, 3, 16)

# Hisoblash:
yil, oy, kun = hisobla_tugilgan_kun(tugilgan_sana)

# Natijani chiqarish:
print(f"Siz tug'ilganingizdan boshlab {yil} yil, {oy} oy, {kun} kun o'tdi!")

# 36 - DARS TUGADI.


# 37 - DARS.
# PYTHON TASHQI KUTUBXONASI.






#  - DARS.
# LOYIHALAR. 
# "SON TOPISH" VA "SO'Z TOPISH" O'YINLARI.

# Ushbu bobda biz ikkita yangi o'yin ustida ishlaymiz. Dasturni yaratish jarayonida avval o'rgangan bilimlarimizni amalda qo'llaymiz.
# Shuningdek, yangi loyiha boshlashda muhim bo'lgan algoritm tushunchasi bilan tanishamiz.

# "SON TOPISH" O'YINI.
# Birinchi dasturimiz sodda "SON TOPISH" o'yini bo'ladi. Bu o'yin quyidagicha o'ynaladi.
#     1. Kompyuter biror berilgan oraliqda (masalan, 1dan 10gacha) son o'ylaydi.
#     2. Foydalanuvchi kompyuter o'ylagan sonni topishga urinadi va biror qiymat taxmin qilib kiritadi.
#     3. Agar taxmin to'g'ri bo'lsa, o'yin tugaydi, agar xato bo'lsa kompyuter foydalanuvchi taxmin qilgan son o'ylangan sondan katta yoki
# kichkligini aytadi va yangi son taxmin qilishni so'raydi.
#     4. Dastur shu zaylda foydalanuvchi to'g'ri sonni topguniga qadar davom etadi.


# ALGORITM.
# Dasturlashning muhim qismi to'g'ri reja qilish va dasturni mayda qadamlarga bo'lib olishdir. Bu Algoritm deyiladi. Xuddi ovqat
# pishirishda retsepdan foydalangandek, dastur yozishda ham Algoritmdan foydalanamiz.

# Yuqoridagi o'yin qoidasini ham bir nechta sodda qadamlarga bo'lib olamiz:
#     1. Kompyuter ma'lum oraliqda son "o'ylaydi": Albatta, kompyuter o'ylashga qodir emas, shuning uchun biz berilgan oraliqda biror 
# tasodifiy sonni qaytarishimiz kifoya (random funksiyasi orqali).
#     2. Foydalanuvchi taxmin qilgan sonni qabul qilib olish (input() orqali bo'ladi).
#     3. Taxmin va tasodifiy sonlarni taqqoslash ("==" sonlarni teng ekanini tekshiramiz).
#     4. Taqqoslash natijasiga ko'ra ("if-else" juftligidan foydalanamiz va natijaga qarab ikki hil yo'l tutamiz (a - b)).
#     a. O'yinni to'xtatish;
#     b. Foydalanuvchiga ishora berish va qayta taxmin qilishni so'rash va yuqoridagi 3 - 4 qadamlarni takrorlash ("while" sikli).
    
# Sodda algoritm tayyor, endi bevosita dastur yozishga kirishsak ham bo'ladi.

# DASTUR.
# Boshlanishiga dastur uchun kompyuterimizda alohida papka yaratamiz va dasturga oid fayllarni (modullarni) shu papkada saqlab boramiz.
# Dastur yozishda asosiy dasturimiz main.py qo'shimcha modullarni esa shu modul ichidagi funksiyaga oid so'zlar bilan nomlash to'g'ri
# bo'ladi.

# Biz ham boshlanishiga sonTop.py faylini yaratamiz va fayl ichiga yuqoridagi algoritm asosida sontop(x) funksiyasini yozamiz.
# Bu funksiyamiz argument sifatida kompyuter o'ylashi kerak bo'lgan sonlar oralig'inining yuqori chegarasini qabul qiladi (0dan x gacha)
# va biz bu parametrga standart 10 qiymatini berib qo'yamiz (ya'ni foydalanuvchi aniq oraliqni ko'rtsatmasa, kompyuter 0 dan 10 gacha
# son "o'ylaydi").

# Funksiyaichida birinchi qiladigan ishimiz - tasodifiy son "o'ylash". Buning uchun random modulidagi randint funksiyasidan foydalanamiz.
# Demak, dastur boshida random modulini import qilishni ham esdan chiqarmaslik kerak: 
# import random 
# def son_top(x = 10):
#     tasodifiy_son = random.randint(1, x) 

# Navbat foydalanuvchidan qiymatlar qabul qilishga. Keling, bundan kompyuter aynan qaysi oraliqda sono'ylaganini ham aytaylik.
    # print(f"Men 1dan {x} gacha son o'yladim. Topa olasizmi?")

# Ana endi bevosita input() funksiyasi yordamida foydalanuvchi kiritgan sonni qabul qilamiz va bu sonni tasodifiy son bilan solishtiramiz.

# Algoritmga ko'ra, biz foydalanuvchining taxminiga qarab turli amallarni bajarishimiz kerak:
    # 1. Agar taxmin tasodifiy sondan kichik bo'lsa, "Kattaroq son ayting";
    # 2. Agar taxmin tasodifiy sondan katta bo'lsa, "Kichikroq son ayting";
    # 3. Agar taxmin to'g'ri bo'lsa, "Yutdingiz!" deb aytishimiz kerak.
    
# O'yin foydalanuvchi yutguniga qadar davom etishi uchun kodimizni while sikli ichiga olamiz.

# Marhamat funksiya tayyor.
# import random 

# def son_top(x=10):
#     tasodifiy_son = random.randint(1, x) 
#     print(f"Men 1dan {x} gacha son o'yladim. Topa olasizmi?")
    
#     while True:
#         taxmin = int(input(">>> "))
#         if taxmin < tasodifiy_son:
#             print("O'ylagan sonim bundan kattaroq!")
#         elif taxmin > tasodifiy_son:
#             print("O'ylagan sonim bundan kichikroq!")
#         else: 
#             print("Topdingiz!")
#             break

# Biz funksiyani alohida modulda saqladik, keling main.py faylini yaratamiz-da, yuqoridagi modul va funksiyani import qilamiz:
# from son_top import son_top
# son_top()

# Faylimiz tarkibi qisqagina bo'ldi. main.py faylini bajaramiz
# Natija: Men 1dan 10 gacha son o'yladim. Topa olasizmi?
# 5
# O'ylagan sonim bundan kattaroq!
# 6
# O'ylagan sonim bundan kattaroq!
# 10
# Topdingiz!
        

# pyWebiO
# Avvalgi bobda pywebiomoduli bilan tanishgan edik, keling, ushbu modul yordamida dasturimizni brauzerda ishlaydigan qilamiz.

# Boshlanishiga modul ichidan input va put_text funksiyalarini chaqirib olamiz. input() funksiyasi bevosita qiymat qabul qilish uchun,
# put_text() esa foydalanuvchiga matn ko'rsatish uchun ishlatiladi.

# Avvalgi dasturda "Men 1 dan 10 gacha son o'yladim. Topa olasizmi?>>>" matnini ikkiga bo'lgan edik, bu safar ikkalasini ham input()
# funksiyasiga joylaymiz. Konsolga chiqarilayotgan matnlarni esa brauzerga chiqarish uchun kodimizdagi print funksiyasini put_text() bilan
# almashtiramiz:
# from pywebio.input import input
# from pywebio.output import put_text
# import random
# def sontop(x = 10):
#     tasodifiy_son = random.randint(1, x)
#     while True:
#     taxmin = int(input(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi? >>> "))
#     if taxmin < tasodifiy_son:
#         put_text("Kattaroq son ayting!")
#     elif taxmin > tasodifiy_son:
#         put_text("Kichikroq son ayting!")
#     else:
#         put_text("Yutdingiz!")
#         break
