# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 02:07:32 2025

@author: DavrServis
"""

# 11- DARS.
# LUG'AT ELEMENTLARI BILAN ISHLASH.

# Avvalgi bo'limda lug'at elementlariga kalit so'z orqali murojaat qilishni o'rgandik. Lug'atlar katta yoki kichik
# bo'lishi mumkin. Ba'zida lug'atdagi barcha kalitlarni yoki qiymatlarni bilmasligimiz mumkin. Bunday holatda qanday
# yo'l tutamiz. 

# Ushbu darsimizda lug'at elementlarini turli usullar yordamida chaqirishni o'rganamiz.

# .ITEMS() METODI.
# Ushbu metod orqali lug'at ichidagi barcha kalit-qiymat juftliklarni ko'rishimiz mumkin.
# talaba = {
#     'ism':'Nurulloh',
#     'familya':'Abdurashidov',
#     't_yil':1999,
#     'yosh':25,
#     'holati':'talaba'
#     } # Oddiy talaba ma'lumotlari lug'ati.
# print(talaba.items()) # Natijani chiqarish.

# Bu metodni to'g'ridan to'g'ri emas, for sikli yordamida chiqarish orqali lug'atdagi barcha elementlarni tushunarliroq
# shaklda ko'rishimiz mumkin.
# talaba = {
#     'ism':'Nurulloh',
#     'familya':'Abdurashidov',
#     't_yil':1999,
#     'yosh':25,
#     'holati':'talaba'
#     } # Oddiy lug'at.
# for kalit, qiymat in talaba.items(): # for orqali lug'at elementlarini tushunarli qilib chiqaramiz.
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}\n")
    
# Yuqoridagi dasturda talaba lug'atidagi har bir kalit va qiymat juftligini konsolga cgiqardik.
# ETIBOR BERING! for siklida biz bir emas, ikkita o'zgaruvchi yaratib oldik (kalit va qiymat).
# Bu usul lug'atlardagima'lumotlarni chiroyli ko'rinishda chiqarish uchun juda qulay.

# Bunda yana bir misol ko'ramiz:
# phones = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     } # Oddiy lug'at yaratib oldik.
# for k, q in phones.items(): # For sikli orqali bu safar qisqartmalardan foydalandik (k, q). 
#     print(f"{k.title()}ning telefoni {q.title()}.") # Natijani chiroyli qilib konsolga chiqarishga harakat qilamiz.
    
# .KEYS() METODI.
# Agar lug'atdagi kalit so'zlarni topish talab qilinsa, .keys() metodidan foydalanamiz:
# mahsulotlar = {
#     'olma': 15000,
#     'nok': 30000,
#     'uzum': 17000,
#     'shaftoli': 50000,
#     'anjir': 10000
#     } # Do'kondagi mahsulotlar ro'yxati.
# print(mahsulotlar.keys()) # Mahsulotlar lug'atidagi kalit so'zlar ro'yxatini chiqaramiz.

# Yuqoridagi kodda ham for siklidan foydalanishimiz mumkin.
# mahsulotlar = {
#     'olma': 15000,
#     'nok': 30000,
#     'uzum': 17000,
#     'shaftoli': 50000,
#     'anjir': 10000
#     }
# print("Do'kondagi mahsulotlar:") # Bizrinchi foydalanuvchiga koddan nima kutish mumkinligini bildiramiz.
# for mahsulot in mahsulotlar.keys(): # for sikli orqali yangi o'zgaruvchi yaratib uni mahsulotlar ichidagi kalit
# # so'zlarning har biriga tenglab olamiz.
#     print(mahsulot.title()) # Natija chiroyli chiqishi uchun .title() metodidan foydalanamiz.
# ETIBOR BERING! Yuqoridagi kodimizda for siklida .keys()metodini ishlatmasak ham, xuddi shu natija chiqadi.

# RO'YXAT VA LUG'AT.
# FOR sikli va IF sharti yordamida lug'atdagi biror qiymatlarni alohida chiqarishimiz mumkin:
# bozorlik = ['anor', 'uzum', 'non', 'baliq'] # Bozorlik ro'yxati.
# for m in mahsulotlar: # For orqali yangi m degan o'zgaruvchini yuqoridagi mahsulotlar lug'atidagi har bir elementga
# # tenglab chiqyapmiz.
#     if m in bozorlik: # Agar mahsulotlar ichidagi har bir elementga tenglangan m bozorlik ichida ham bo'lsa.
#         print(f"{m.title()} {mahsulotlar[m]} so'm.") # Unikonsolga shu tariqa chiqargin.

# Yuqoridagi kodga ETIBOR BERING! Biz avval bozorlik degan ro'yxat yaratdik (uyga bozorlik qilyapmiz), keyin esa
# mahsulotlar lug'atidagi har bir mahsulotni bizdagi bozorlik ro'yxati bilan solishtirdik. Agar mahsulot bizning
# bozorlik ro'yxatimizda bo'lsa, uning narxini konsolga chiqardik.

# Quyidagi misolda esa, aksincha, bozorlik ro'yxatidagi har bir elementni do'kondagi mahsulotlar bilan solishtiramiz
# va mahsulot do'konda yo'q bo'lsa, do'konga murojaat qildiramiz:
# for buyum in bozorlik: # Yangi buyum degan o'zgaruvchini bozorlik ro'yxatimiz ichidagi elementlarga tenglab olamiz.
    # if buyum not in mahsulotlar: # Agar buyum magazindagi mahsulotlar ichida bo'lmasa.
        # print(f" Kechirasiz bizda {buyum} yo'q.") # Magaiznchi bizga aytadigan gapini konsolga chiqaramiz.

# LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH.
# Avval aytkanimizdek, lug'at elementlari biz kiritgan tartibda saqlanadi. Agar elementlarini alifbo tartibida
# chiqarish talab qilinsa, sorted() funksiyasidan foydalanamiz:
# print("Do'konimizdagi mahsulotlar:") # Yuqorida yaratilgan lug'atimiz elementlarini tariblab chiqarishga harakat
# # qilamiz.
# for mahsulot in sorted(mahsulotlar): # Mahsulotni sorted orqali mahsulotlarni har bir elementiga tenglab olamiz.
#     print(mahsulot.title()) # Natijaga title() ni qo'shib chiroyli ko'rinishda chiqaramiz.
    
# .VALUES() METODI.
# Yuqorida biz .KEY() metodi yordamida lug'atdagi elementlarning kalitlarini ko'rishni o'rgandik. Agar element 
# qiymatlarini topish talab qilinsa, .VALUES() metodidan foydalanamiz. Quyida misol orqali buni ko'ramiz.
# phones = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     } # Oddiy lug'at tuzib olamiz.
# print(phones.values()) # Endi lug'atdagi elementlarni emas, balki qiymatlarni o'zini chiqaramiz.

# Quyidagi kodni ham bajarib ko'ramiz:
# print("Foydalanuvchilarni telefonlari:") # Foydalanuvchiga yo'nalish beramiz dasturdan nima kutishini bilsin.
# for tel in phones.values(): # Tel degan o'zgaruvchini phones ichidagi har bir qiymatga tenglaymiz (value).
#     print(tel.title()) # Natijani chiqaramiz. (faqat values lar chiqadi.).
    
# Yuqoridagi usul bilan qiymatlarni chaqirganimizda lug'atdagi barcha qiymatlar chiqib keladi. Agar biror qiymat
# ko'p marta qaytarilsa,konsolga ham ko'p marta chiqadi.

# Quyidagi misolni ko'ramiz: 
# phones = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'maryam':'galaxy s9',
#     'hamida':'huawei p30',
#     'tohir':'iphone x',
#     'hamdam':'iphone x'
    # } # Foydalanuvchilar haqida ma'lumotlarni o'zida jamlagan oddiy lug'at
# print("Foydalanuvchilarning telefonlari:") # Foydalanuvchiga yo'nalish.
# for tel in phones.values(): # Tel ni har bir qiymatga tenglaymiz. 
#     print(tel.title()) # Natijani olamiz.
    
# SET() FUNKSIYASI.
# Yuqoridagi natijaga etibor beradigan bo'lsak, bir nechta foydalanuvchilar  iphone x va galaxy s9 telefonidan 
# foydalanar ekanva bu modellar qayta-qayta konsolga chiqadi.
# Buning oldini olish uchun SET() funksiyasidan foydalanamiz. Bufunksiya to'plam yaratish uchun ishlatiladi.
# print("Foydalanuvchilar telefonlari:") # Foydalanuvchiga yo'nalish beramiz.
# for tel in set(phones.values()): # Tel ni yangi funksiya (set()) orqali phones qiymatlarini har biriga tenglab
# # olamiz. O'z navbatida SET() barcha bir hil qiymatlarni faqat bittadan nusxasini olib qoladi.
#     print(tel) # Natijani chiqaramiz.

# AMALIYOT TOPSHIRIQLARI.
#1 - Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va
# qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.     
# python = {
#     'int':'Butun son',
#     'float':'O\'nlik son',
#     'string':'Matn',
#     'list':'Ro\'yxat',
#     'tuple':'O\'zgarmas ro\'yxat',
#     'bool':'Mantiqiy ma\'lumot turi',
#     'dict':'Lug\'at',
#     'for':'Uchun',
#     'in':'Ichida',
#     'not in':'Ichida emas',
#     'if':'Agar'
#     }    
# for kalit, qiymat in sorted(python.items()):
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}\n")

#2 - Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni
# alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
# countrys = {
#     "ozbekiston":"toshkent",
#     "rossiya":"moskva",
#     "aqsh":"vashington",
#     "germaniya":"berlin",
#     "ispaniya":"madrid"
#     } 
# print("Davlatlar ro'yxati:")
# for country in sorted(countrys.keys()):
#     if country == 'aqsh':
#         print(country.upper())
#     else:
#         print(country.title())
        
# print("\nDavlat poytaxtlari ro'yxati:")
# for capital in sorted(countrys.values()):
#     print(capital.title())
    
#3 - Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
# print("Istalgan 5ta davlatingizni poytaxtini bilishingiz mumkin:(AQSH, Germaniya, Ispaniya, O'zbekiston, Rossiya)")
# countrys = {
#     "ozbekiston":"toshkent",
#     "rossiya":"moskva",
#     "aqsh":"vashington",
#     "germaniya":"berlin",
#     "ispaniya":"madrid"
#     } 
# print("Biz 5ta davlat poytaxtlari haqida ma'lumotlarni jamlaganmiz: UZB, RUS, AQSH, GER, ISP")
# country = input('\nQaysi davlatning poytaxtini bilishni istaysiz? ').lower()
# capital = countrys.get(country)
# if capital == None:
#     print(f"Kechirasiz, bizda {country.title()} haqida ma'lumot yo'q!")
# else:
#     if country == 'aqsh':
#         print(f"{country.upper()} ning poytaxti {capital.title()}")
#     else:
#         print(f"{country.title()} ning poytaxti {capital.title()}")
 
#4 - Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat
# buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa
# narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000,
#         'chuchvara':25000,
#         'mastava': 20000,
#         'manti': 28000
#         }
# print("Marhamat, buyurtma berishingiz mumkin!")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1} - buyurtmani kiritng: ").lower())
    
# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} bor, narxi {menu[buyurtma]} so'm.")
#     else:
#         print(f"Afsuski, bizda {buyurtma} yo'q!")
    
# 11 - DARS TUGADI.