# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:03:35 2024

@author: DavrServis
"""

#13-dars NASTING. (Biron narsaning ichiga boshqa bir narsani saqlash.).
#29.10.2024.
#Muallif:Abdurashidov Nurulloh.

# NESTING. Biron narsaning ichiga boshqa bir narsani saqlash.

# car0 = {
#         "model" : "jentra",
#         "rang" : "qora",
#         "yil" : 2025,
#         "narh" : 18000,
#         "km" : 30,
#         "korobka" : "avtomat"
#         }
# car1 = {
#         "model" : "nexia 3",
#         "rang" : "oq",
#         "yil" : 2020,
#         "narh" : 10000,
#         "km" : 57000,
#         "korobka" : "mehanika"
#         }
# car2 = {
#         "model" : "cobalt",
#         "rang" : "stalnoy",
#         "yil" : 2023,
#         "narh" : 13000,
#         "km" : 100000,
#         "korobka" : "avtomat"
        # }
# Bu holatda har bir mashina haqidagi ma'lumotlarni chiqarish uchun birmincha qiyingarchilik duch 
# kelinyapti va buni oldini olish uchun boshqa usuldan foydalanib ko'ramiz.
# car = car0
# print(f"{car['model'] .title()} ,"
#       f"{car['rang'].capitalize()} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# Yani bu yerda bir yola uchta mashina haqidagi ma'lumotlarni chiqarish uchun uzun kod yozmasdan uni
# boshqa o'zgaruvchiga saqlab (for) funksiyasidan foydalanamiz.
# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()} ,"
#           f"{car['rang'].capitalize()} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")
    
# Yuqoridagi kodda hammasi ihcham va tushunarli holatda chiqti.
# print(cars)
# Lug'atlarni istalganini istalgan elementiga murojaat qilish imkoniyatiga ham egamiz.
# print(cars[0]['model']) # Masalan shu ko'rinishda.

# Yuqoridagi kodni yanayam tushunarliroq ko'rinishda chiqarish imkoniga egamiz buning uchun.
# print(f"{cars[2]['rang'].title()} "
      # f"{cars[2]['model']}") # Bu holatda so'ralgan ma'lumot yanayam tushunarliroq bo'lib chiqadi.

# Biz (for) tsikli yordamida lug'atlarni bitta bitta emas balki bitta tsikl bilan istalgancha lug'at
# yaratishimiz mumkin.
# malibus = [] # Yangi bo'sh ro'yxat.
# for n in range(10): # for tsikli yordamida n ga range(10) orqali 10ta qiymat berdik.
    # new_car = { # new_car degan lug'at yaratib unga qiymatlar berdik.
    #     "model" : "malibu",
    #     "rang" : None, # rangi noaniq.
    #     "yil" : 2025,
    #     "narh" : None,
    #     "km" : 0,
    #     "korobka" : "avto"
    #     }

    # malibus.append(new_car) # Bu kod orqali esa malibus degan bo'sh ro'yxatimizga new_car elementlarini 
# 10 marta qo'shtik va 10ta lug'at hosil qilib oldik.
# print(malibus)

# Quyida esa lug'at elementlarini qiymatini o'zgartirishga harakat qilamiz.
# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
#     print(malibus)
    
# for malibu in malibus[3:6]: # Bu yerda range() funksiyasining ishlashini ham unutmaymiz ohirgi son
# # hisoblanmaydi.
#     malibu['rang'] = 'qora'

# for malibu in malibus[6:]: # Bu yerda 6dan ohirgi son yani 10gacha bo'lgan qiymatlarni olib o'zgartiradi
#     malibu['rang'] = 'sariq'
#     malibu['korobka'] = 'mexanika'
    
# for malibu in malibus: # malibus ichidagi har bir malibu uchun.
#     print(malibu) 
    
# # Endi bu kodlarni biroz murakkablashtiramiz.
# for malibu in malibus: # Bu yerda qanday protsez ketyapti tuwuntiramiz. Malibusdagi har bir malibu 
#     if malibu['korobka'] == 'avto': # korobkasini tekshir va korobka avtomat(avto) bo'lsa
#         malibu['narh'] = 40000 # Narxini 40000
#     else: # Aks holda
#         malibu['narh'] = 35000 # Narxini 35000 qilgin
# for malibu in malibus:
#     print(malibu) # va ularni konsolga chiqar.
    
# LUG'AT ICHIDA RO'YXAT.
# Lug'at kalitlari odatda bitta elementni o'ziga biriktira oladi biz esa shuni ko'paytirishimiz
# mumkin. Bunda ro'yxat kaliti beriladi va kalit elementini ro'yxat ko'rinishida ifodalaymiz.
# dasturchilar = {
#     "ali" : ['java, python'],
#     "vali" :['sql', 'php'],
#     "shodi" :['c++', 'c#'],
#     "odil" :['html','css'],
#     "maryam" :['python','php']
#     }
# Endi bu ma'lumotlarni tushunarli va chiroyli ko'rinishda konsolga chiqarishga harakat qilamiz.
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end = '') # Bu yerda bu belgi qatorni davom ettirgin
# Degan manoni beradi.    
    # for til in tillar:
    #     print(til.upper())
        
# Endi biz lug'atlar ichida lug'at yaratishni ko'rib chiqamiz.
# hamkasblar = {
#     'ali':{'familyasi' : 'valiyev',
#          'tyil': 1992,
#          'malumot' : 'orta maxsus',
#          'tillar': ['css, html, js']
#          },
#     'vali':{'familyasi' : 'aliyev',
#          'tyil': 2002,
#          'malumot' : 'oliy',
#          'tillar': ['python, c++']
#          },
#     'shodi':{'familyasi' : 'qo\'ziev',
#          'tyil': 2000,
#          'malumot' : 'litseyni tugatgan',
#          'tillar': ['c++, c#']
#          }
#             }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title() } {info['familyasi'].title()} "
#       f"{info['tyil']}-yilda tug'ilgan, "
#       f"Malumoti: {info['malumot']}")
      
#     for til in info['tillar']:
#         print(til.upper()) 
     
# AMALIYOT TOPSHIRIQLARI.
#1 - Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxslar haqidagi ma'lumotlarni lug'at ko'rinishida
# saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
buxoriy = {
        "ism_sh" : "abu abdulloh muhammad ibn ismoil",
        "t_yil" : 810,
        "v_yil" : 870,
        "t_joyi" : "buxoro",
        
        }
qodiriy = {
        "ism_sh" : "abdulla qodiriy",
        "t_yil" : 1894,
        "v_yil" : 1938,
        "t_joyi" : "toshkent",
        
        }
vohidov = {
        "ism_sh" : "erkin vohidov",
        "t_yil" : 1936,
        "v_yil" : 2016,
        "t_joyi" : "farg'ona",
        
        }
navoiy = {
        "ism_sh" : "alisher navoiy",
        "t_yil" : 1441,
        "v_yil" : 1501,
        "t_joyi" : "xirot",
        }
shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs['ism_sh']
    tyil = shaxs['t_yil']
    tjoy = shaxs['t_joyi']
    vyil = shaxs['v_yil']
    print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
          f"{vyil-tyil} yil umr ko'rgan.")

# print(f"{shaxs0['ism_sh'].title()}, {shaxs0['t_joyi'].title()} shahrida, {shaxs0['t_yil']}-yilda tug'ilgan,\
# va {shaxs0['y_umri']} yoshida vafot etgan.")
# print(f"{shaxs1['ism_sh'].title()}, {shaxs1['t_joyi'].title()} shahrida, {shaxs1['t_yil']}-yilda tug'ilgan,\
# va {shaxs1['y_umri']} yoshida vafot etgan.")
# print(f"{shaxs2['ism_sh'].title()}, {shaxs2['t_joyi'].title()} shahrida, {shaxs2['t_yil']}-yilda tug'ilgan,\
# va {shaxs2['y_umri']} yoshida vafot etgan.") 
# print(f"{shaxs3['ism_sh'].title()}, {shaxs3['t_joyi'].title()} shahrida, {shaxs3['t_yil']}-yilda tug'ilgan,\
# va {shaxs3['y_umri']} yoshida vafot etgan.")      

#2 - Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida
# muallifning ismi va uning asarlarini konsolga chiqaring.
# buxoriy = {
#        "ism_sh" : "abu abdulloh muhammad ibn ismoil",
#        "t_yil" : "810",
#        "t_joyi" : "buxoro",
#        "y_umri" : "60",
#        "m_asarlari" : ["Al-jome' as-sahih, Al-adab al-mufrad, At-tarix al-kabir, At-tarix as-sag'ir"]
#        }
# qodiriy = {
#        "ism_sh" : "abdulla qodiriy",
#        "t_yil" : "1894",
#        "t_joyi" : "toshkent",
#        "y_umri" : "44",
#        "m_asarlari" : ["O'tkan kunlar, Mehrobdan chayon, Obid ketmon"]
#        }
# vohidov = {
#        "ism_sh" : "erkin vohidov",
#        "t_yil" : "1936",
#        "t_joyi" : "farg'ona",
#        "y_umri" : "80",
#        "m_asarlari" : ["Tong nafasi, Qo'shiqlarim sizga, O'zbegim, Qiziquvchan Matmusa"]
#        }
# navoiy = {
#        "ism_sh" : "alisher navoiy",
#        "t_yil" : "1441",
#        "t_joyi" : "xirot",
#        "y_umri" : "60",
#        "m_asarlari" : ["Xamsa, Lison ut-Tayr, Mahbub al-Qulub, Murojot"]
#        }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     ism = shaxs['ism_sh']
#     tyil = shaxs['t_yil']
#     tjoy = shaxs['t_joyi']
#     yumri = shaxs['y_umri']
#     asarlar = shaxs['m_asarlari'] 
#     print(f"{ism} ning mashxur asarlarii: ")
#     for asar in asarlar:
#         print(asar)

#3 - Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit,
# uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
kinolar = {
    'ali' : ["avatar, rossamaha, deadpool"],
    'vali' : ["ijtimoiy tarmoq, гадкий я"],
    'shodi': ["don, alibobo va 40 qaroqchi"],
    'avaz' : ["otkan kunlar, om shanti om"]
    }
for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()} ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)
        
#4 -  Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida
# saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.       
# davlatlar = {
#     'ozbekiston' : {
#         "dnomi" : "o'zbekiston",
#         "poytaxt" : "tohkent",
#         "aholisi" : 33000000,
#         "pbirligi" : "so'm",
#         "maydoni" : 448978 
#         },
#     'rossiya' : {
#         "dnomi" : "rossiya",
#         "poytaxt" : "moskva",
#         "aholisi" : 144000000,
#         "pbirligi" : "rubl",
#         "maydoni" : 17098246 
#         },
#     'aqsh' : {
#         "dnomi" : "aqsh",
#         "poytaxt" : "vashington",
#         "aholisi" : 327000000,
#         "pbirligi" : "dollar",
#         "maydoni" : 9631418 
#         },
#     'xitoy' : {
#         "dnomi" : "xitoy",
#         "poytaxt" : "pekin",
#         "aholisi" : 1200000000,
#         "pbirligi" : "yen",
#         "maydoni" : 9596962 
#         }
#     }     
# for davlat, info in davlatlar.items():
#     if davlat .lower() == 'aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydoni']}kv.km"
#           f"\nAholisi: {info['aholisi']}"
#           f"\nPul birligi {info['pbirligi']}"
              
#           )
    
#5 - Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida
# ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan
# xabarni chiqaring.
davlatlar = {
    'ozbekiston' : {
        "dnomi" : "o'zbekiston",
        "poytaxt" : "tohkent",
        "aholisi" : 33000000,
        "pbirligi" : "so'm",
        "maydoni" : 448978 
        },
    'rossiya' : {
        "dnomi" : "rossiya",
        "poytaxt" : "moskva",
        "aholisi" : 144000000,
        "pbirligi" : "rubl",
        "maydoni" : 17098246 
        },
    'aqsh' : {
        "dnomi" : "aqsh",
        "poytaxt" : "vashington",
        "aholisi" : 327000000,
        "pbirligi" : "dollar",
        "maydoni" : 9631418 
        },
    'xitoy' : {
        "dnomi" : "xitoy",
        "poytaxt" : "pekin",
        "aholisi" : 1200000000,
        "pbirligi" : "yen",
        "maydoni" : 9596962 
        }
    }     
davlat = input("Davlat nomini kiring: ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydoni']}kv.km"
          f"\nAholisi: {info['aholisi']}"
          f"\nPul birligi {info['pbirligi']}"
          )   
else:
        print("Bizda {davlat} haqida ma'lumot yo'q")
          