# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 02:04:49 2025

@author: DavrServis
"""

# 9 - DARS.
# BIR NECHTA SHARTLARNI TEKSHIRISH.

# "if" yordamida biz faqatgina bitta shartni tekshira olamiz va uning natijasiga ko'ra (True/False) dasturimiz ma'lum bir
# amalni bajaradi. Agar dastur davomida bir nechta shartlarni tekshirish talab qilinsa, if-elif,else ketma-ketligidan
# foydalanamiz.

# ELIF-ELSE va IF so'zlarining jamlanmasi bo'lib, "aks holda, agar" deb tarjima qilinadi.
# "if" bilan boshlangan ketma-ketlik bir nechta "elif" lardan iborat bo'lishi mumkin.
# son = int(input("Istalgan sonni kiriting: "))
# if son > 0:
#     print("Kiritilgan son musbat!")
# elif son < 0:
#     print("Kiritilgan son manfiy!")
# else:
#     print("Kiritilgan son 0 ga teng!")
    
# IF-ELIF-ELSE juftligida birma bir shartlar tekshiriladi va agar shartlardan birortasi bajarilsa qolganlari tashlab
# yuboriladi, yani ularni tekshirib o'tirmaydi.

# Navbatdagi misol taabirida buni yanada tushunishga harakat qilamiz.
# yosh = int(input("Yoshingizni kiriting: ")) # Foydalanuvchidan yoshini kiritishni so'raymiz.
# if yosh <= 5: # Agar yosh kichik yoki teng bo'lsa 5ga.
#     print("Sizga kirish tekin!") # Shu kod bajarilsin.
# elif yosh <= 18: # Agar yosh kichik yoki teng bo'lsa 18ga.
#     print("Sizga kirish 5000so'm!") # Shu kod bajarilsin.
# elif yosh <= 65: # Agar yosh kichik yoki teng bo'lsa 65ga.
#     print("Sizga kirish 12000so'm!") # Shu kod bajarilsin.
# else: # Aks holda.
#     print("Yoshi ulug'larimizga ham kirish bepul!") # Shu kod bajarilsin.
    
# IF-ELIF-ELSE ketma-ketligida shartlarni tartibi juda muhim. Agar yuqoridagi ko'dimizda biz dastavval foydalanuvchi
# 12dan kichikligini tekshiradigan bo'lsak, dasturimiz biz kutgan natijani bermaydi.
# yosh = int(input("Yoshingizni kiriting: ")) # Foydalanuvchidan yoshini kiritishni so'raymiz.
# if yosh <= 18: # Agar yosh kichik yoki teng bo'lsa 5ga.
#     print("Sizga kirish 5000so'm!") # Shu kod bajarilsin.
# elif yosh <= 7: # Agar yosh kichik yoki teng bo'lsa 18ga.
#     print("Sizga kirish tekin!") # Shu kod bajarilsin.
# elif yosh <= 65: # Agar yosh kichik yoki teng bo'lsa 65ga.
#     print("Sizga kirish 12000so'm!") # Shu kod bajarilsin.
# else: # Aks holda.
#     print("Yoshi ulug'larimizga ham kirish bepul!") # Shu kod bajarilsin.    
# Yuqoridagi kod aytkanimizdek biz kutkan natijani bermaydi.

# Kod yozishda yaxshi amaliyotlardan biri kodlarni qisqa yozish va buyruqlarni qayta-qayta takrorlamaslikdir. Bu
# kelajakda kodni o'zgartirishda ham juda qo'l keladi.
# Avvalgi dasturda ham print() funksiyasini bir necha marta takrorlamaslik uchun kodimizni quyidagicha o'zgartiramiz.
# yosh = int(input("Iltimos yosjingizni kiriting: "))
# if yosh <= 7:
#     price = 2000
# elif yosh <= 12:
#     price = 5000
# elif yosh <= 18:
#     price = 8000
# else:
#     price = 12000
# print(f"Sizga kirish {price} so'm!")
# Yuqoridagi kodda bitta print() funksiyasi orqali kodni bajardik. Bu kelajakda kodimizni o'zgartirishimizni ham
# osonlashtiradi

# Deylik hayvonot bog'i yoshi 65dan yuqori insonlarga chegirma e'lon qildi, Bu kodga o'zgartirish kiritsak kifoya.
# yosh = int(input("Iltimos yosjingizni kiriting: "))
# if yosh <= 7:
#     price = 2000
# elif yosh <= 12:
#     price = 5000
# elif yosh <= 18:
#     price = 8000
# elif yosh <= 65:
#     price = 12000
# else:
#     price = 8000
# print(f"Sizga kirish {price} so'm!")

# IF-ELIF-ELSE zanjirirda else qismi majburiy emas:
# yosh = int(input("Iltimos yosjingizni kiriting: "))
# if yosh <= 7:
#     price = 2000
# elif yosh <= 12:
#     price = 5000
# elif yosh <= 18:
#     price = 8000
# elif yosh <= 65:
#     price = 12000
# elif yosh > 65:
#     price = 8000
# print(f"Sizga kirish {price} so'm!")    
# Yuqoridagi kodda biz baribir bir xil natija olaveramiz.

# AND va OR operatorlari.
# Yuqoridagi misollarda IF yoki ELIF dan so'ng biz faqatgina bitta shartni tekshirdik. Agar bir vaqtnint o'zida
# bir nechta shartlarni tekshirish talab qilinsa, buning uchun maxsus AND va OR operatorlari mavjud.

# OR operatori.
# OR ingliz tilidan "yoki" deb tarjima qilinadi va ikki va undan ko'p shartlardan BIRINI bajarilishini tekshirishda
# ishlatiladi. Demak, dasturning biror qismi bajarilishi uchun bir nechta shartlardan biriniQng to'g'ri (True)
# bo'lishi kifoya bo'lsa OR operatoridan foydalanamiz.
# kun = input("Bugun haftaning qaysi kuni? ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni!")
# else:
#     print("Bugun ish kuni!")
# Yuqoridagi kodga qaraylik , foydalanuvchidan hafta kunini so'raymiz, agar kun shanba yokiyakshanba bo'lsa, bugun
# da olish kuni degan xabarnichiqaramiz, aks holda, bugun ish kuni degan xabarni chiqaramiz.
# Aytib o'tish kerakki yuqoridagi kodda ikki shartdan biri bajarilsa kifoya natija (True) qiymat qaytaradi.

# Yana ham tushunarli bo'lishi uchun quyidagi ko'dlarni bajarib ko'ramiz:
# print(True or False)
# print(True or True)
# print(False or False)

# AND operatori.
# AND ingliz tilidan "va" deb tarjima qilinadi va ikki va undan ko'p shartlarning BARCHASINI bajarilishini
# tekshirishda ishlatiladi. AND operatori bilan yozilgan shartlarning BARCHASI bajarilgandagina TRUE qiymati qaytadi,
# shartlardan biri bajarilmay qolsa ham, FALSE qiymati qaytadi.
# Quyidagi misolni ko'ramiz.
# kun = input("Bugun qaysi kun? ")
# harorat = float(input("Havoharorati qanday? "))
# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print("Chomilishga borsa bo'ladi!")
# else:
#     print("Cho'milishga bormagan ma'qul.")
# Yuqoridagi kodning 3-qatordagi AND operatori kun.lower() == 'yakshanba' va harorat >= 30 shartlarining IKKISI HAM 
# bajarilgandagina TRUE qiymatini qaytaradi, aks holda, qiymat FALSE bo'ladi.

# BIR NECHTA SHARTLARNI KETMA-KET YOZISH.
# Shartlarni yozishda bir nechta AND va OR operatorlarini aralashtirib ham yozish mumkin.
# yosh = int(input("Iltimos yoshingizni kiriting!"))
# kun = input("Bugun qaysi kun? ")
# if (yosh < 7 or yosh > 65) and kun == 'chorshanba':
#     print("Bugun siz uchun mezeyga kirish bepul!")
# else:
#     print("Sizga kirish 5000so'm.")
    
# BOOLEAN MA'LUMOTLAR TURI.
# Yuqorida taqqoslash operatorlari yordamida turli ifodalarni solishtirishda TRUE yoki FALSE qiymatlari qaytishini
# ko'rdik. Bu qiymatlar BOOLEAN (mantiqiy) qiymatlar deb ataladi va dasturlashda juda keng qo'llaniladi.
# BOOLEAN ma'lumot turini ham huddi son yoki matn kabi o'zgaruvchilarda saqlash mumkin.
# a = True
# b = False

# Buni quyida yana misol orqali ko'rib chiqamiz.
# narx = 15000 # Mijoz 15000 so'mga taom oldi.
# choy = True # Mijoz choy ham oldi.
# salat = False # Mijoz salat olmadi.
# if choy and salat: # Agar mijoz choy va salat olgan bo'lsa.
#     narx = narx + 1000 # Narxga 10000 so'm qo'shamiz.
# elif choy or salat: # Agar mijoz choy yoki salat olgan bo'lsa.
#     narx = narx + 5000 # Narxga 5000 so'm qo'shamiz.
# print(f"Jami {narx} so'm.") # Yakuniy narxni chiqaramiz.
# ETIBOR BERING!!! choy va salat BOOLEAN(mantiqiy) qiymatlar bo'lgani uchun IF va ELIF shartlarida biz choy == True
# salat == True deb yozib o'tirishimiz shart emas.
# Yuqoridagi misolda choy = True (choy oldi) va salat = False (salat olmadi) bo'lgani uchun yakuniy
# narx + 500 = 20000 chiqdi.

# PYTHONDA True va False qiymatlari o'rniga 1 va 0 sonlarini ham ishlatish mumkin.

# SHARTLARNI KETMA-KET TEKSHIRISH.
# IF-ELIF-ELSE zanjirining kamchiliklaridan biri - shartlardan biri bajarilishi bilan qolgan shartlar tekshirilmaydi. 
# Shuning uchun shartlarni ketma-ket tekshirish uchun har bir shartni alohida IF bilan ajratish talab qilinadi.
# Avvalgi bo'limda ko'rgan misolni kengaytiraylik:
# narx = 15000 # Mijoz 15000 so'mga taom oldi. Qolgan qo'shimchalarni olganmi yo'qmi tekshiramiz.
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 0

# if choy: # Agar choy olsa (True yoki False bo'lishiga qarab.).
#     print("Mijoz choy oldi.")
#     narx = narx + 3000

# if salat: # Agar salat olsa (True yoki False bo'lishiga qarab.) 
#     print("Mijoz salat oldi")
#     narx = narx + 5000
    
# if non: # Agar non olsa (True yoki False bo'lishiga qarab.)
#     print("Mijoz non oldi.")
#     narx = narx + 4000

# if kompot: # Agar kompot olsa (True yoki False bo'lishiga qarab.)
#     print("Mijoz kompot oldi.")
#     narx = narx + 7000

# if assorti: # Agar assorti olsa (True yoki False bo'lishiga qarab.)
#     print("Mijoz assorti oldi.")
#     narx = narx + 10000 
    
# print(f"Jami {narx} summa!")
# Yuqoridagi dasturda har bir IF alohida tekshiriladi, avvalgi yoki keyingi IF ga bog'liq emas.

# RO'YXAT TARKIBINI TEKSHIRISH.
# IN operatori.
# IN operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishimiz mumkin.
# Quyidagi dasturlar misolida buni ko'rib chiqamiz.
# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa'] # Ro'yxatimizda quyidagi taomlar bor.
# print('manti' in menyu) # Menyuda 'manti' bormi? 
# Natija: False.

# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa'] # Ro'yxatimizda quyidagi taomlar bor.
# print('osh' in menyu) # Menyuda 'osh' bormi? 
# Natija: True.

# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa'] # Ro'yxatimizda quyidagi taomlar bor.
# ovqat = input("Nima ovqat yeysiz?>>> ")
# if ovqat.lower() in menyu:
#     print("Buyurtmangiz qabul qilindi.")
# else:
#     print("Afsuski, bizda bunday taom yo'q.")

# NOT IN operatori.
# NOT IN operatori yordamida esa biror element ro'yxatda yo'qligini tekshirishimiz mumkin.
# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa'] # Ro'yxatimizda quyidagi taomlar bor.
# print('manti' not in menyu) # Menyuda 'manti' yo'qmi?    
# Natija True, chunki haqiqatdan ham 'manti' ro'yxatimizda yo'q. 

# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa'] # Ro'yxatimizda quyidagi taomlar bor.
# print('osh' not in menyu) # Menyuda 'osh' yo'qmi?    
# Natija False, chunki 'osh' aslida ro'yxatimizda bor.

# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa'] # Ro'yxatimizda quyidagi taomlar bor.
# ovqat = input('Nima ovqat yeysiz? ') # Foydalanuvchidan nima ovqat yeyishini so'raymiz.
# if ovqat.lower() not in menyu:
#     print(f"Afsuski, {ovqat} bizda yo'q.")
# else:
#     print("Buyurtma qabul qilindi.")
# Yuqoridagi dasturda chiqariladigan xabarlar o'rni almashadi shartga qarab.

# NOT operatorini boshqa shartlar oldidan ham qo'yishimiz mumkin.Misol uchun, not a == 5 ifodasi a != 5 ifodasi bilan
# bir hil natija qaytaradi.
# a = 6 # a ni 6 ga tenglab oldik.
# print(a != 5) # Endi so'raymiz a teng emasmi 5ga (True)
# print(a == 5) # Endi so'raymiz a tengmi 5ga (False)
# print(not False) # False emas demak, (True) 
# print(not True) # True emas demak, (False)

# IKKI RO'YXATNI SOLISHTIRISH.
# Ikki ro'yxatni tarkibini tekshirish uchun FOR sikli va yuqoridagi IN operatoridan foydalanamiz:
# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa'] # Ro'yxatimizda quyidagi taomlar bor.
# buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menyu:
#         print(f"{taom} bor.")
#     else:
#         print(f"{taom} yo'q.")
        
# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa'] # Ro'yxatimizda quyidagi taomlar bor.
# buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom not in menyu:
#         print(f"Kechirasiz, bizda {taom} yo'q")
#     else:
#         print(f"Menyuda {taom} bor.")

# RO'YXAT BO'SH EMASLIGINI TEKSHIRISH.
# Albatta biz yuqoridagi kodda foydalanuvchi buyurtma qildi deb tasavvur qilyapmiz. Lekin foydalanuvchidan bo'sh
# ro'yxat kelsa-chi? Demak, FOR siklini bajarishdan oldin ro'yxat emasligiga amin bo'lishimiz kerak. Buning uchun
# ro'yxat uzunligini tekshirib ko'ramiz. Agar ro'yxat uzunligi 0ga teng bo'lsa, bu bo'sh ro'yxatdir.
# list1 = [1,2,3] # list1 degan o'zgaruvchiga ro'yxat orqali 3ta elementni yukladik.
# print(len(list1) > 0) # lis1 ni uzunligini tekshiryapmiz uni 0 dan katta degan ifoda orqali. (True)

# list2 = [] # Bo'sh ro'yxat.
# print(len(list2) > 0) # Ro'yxat uzunligi 0dan katta bo'lmagani uchun yani u bo'sh. (False)

# Lekin Pythonda ro'yxat bo'sh yoki bo'sh emasligini tekshirishning bundan ham oson yo'li bor. Buning uchun IF
# operatoridan so'ng ro'yxat nomini yozish kifoya. Agar ro'yxatda bir dona element bo'lsa ham, bu ifoda TRUE
# qiymatini, aks holda, FALSE qiymatini qaytaradi.
# list1 = [1,2,3] # Ro'yxatga 3ta element qo'shdik.
# if list1: # Bu ifoda TRUE qaytaradi, sababi, list1 bo'sh emas.
#     print(f"Ro'ytxatda {len(list1)} ta elementlar bor") # Yuqoridagi ifoda natijasini chiqarish uchun print().
    
# Yuqoridagi usuldan foydalanib avvalgi bo'limda ko'rgan dasturga o'zgartirish kiritamiz: 
# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa'] # Ro'yxatimizda quyidagi taomlar bor.
# buyurtmalar = ["osh", "somsa", "manti", "shashlik"] # Buyurtma qilingan taomlar.

# if buyurtmalar: # Yani buyurtmalar ro'yxati bo'sh bo'lmasa (ichida element bo'lsa)
#     for taom in buyurtmalar: # buyurtmalar ro'yxatidagi har bir taom uchun. 
#         if taom in menyu: # Agar taom menyu da bo'lsa.
#             print(f"Menyuda {taom} bor.") # Shu xabarni konsolga chiqargin.
#         else: # Aks holda.
#             print(f"Kechirasiz, menyuda {taom} yo'q.") # Shu xabarni konsolga chiqargin.
# else: # Aks holda bu eng yuqoridagi IF ga.
#     print("Savat bo'sh!") # Shu xabarni konsolga chiqargin.
    
# AMALIYOT TOPSHIRIQLARI.
#1 - Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son
# kiritsa "Bu son juft emas" degan xabarni chiqaring.           
# son = int(input("Iltimos juft son kiriting! ")) # Foydalanuvchidan juft son kiritishini so'raymiz.
# if son % 2 == 0: # Agar kiritilgan sonni 2 ga bo'lingandagi qoldiq 0 ga teng bo'lsa demak son juft. (True)
#     print("Rahmat!") # Shu xabar konsolga chiqadi.
# else: # Aks holda.
#     print("Siz kiritgan son juft emas.") # Shu xabar konsolga chiqadi.

#2 - Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul

# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm

# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm     

# yosh = int(input("Iltimos yoshingizni kiriting! "))
# if yosh < 4 or yosh > 60:
#     price = 'bepul'

# elif yosh <= 18:
#     price = 10000
    
# elif yosh > 18 and yosh < 60:
#     price = 20000
    
# print(f"Sizga kirish {price}")

#3 - Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi
# haqida xabarni chiqaring.
# print("Iltimos ikkita son kiriting!")
# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))

# if son1 > son2:
#     print(f"{son1} > {son2}")
    
# elif son1 < son2:
#     print("{son1} < {son2}")
    
# else:
#     print(f"{son1}, {son2} bu ikki son teng.")
    
#4 - mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat
# yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar
# ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda,
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ["olma","banan","sut","non","tuxum","shakar","guruch","yog'","choy","shokolad"]
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni qo'shing: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} do'konimizda bor.")
#     else:
#         print(f"Afsuski, {mahsulot} do'konimizda yo'q")
        
#5 - foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni
# so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz,
# foydalanuvchi!" xabarini chiqaring.
# users = ['anvar', 'kamol', 'abu', 'hoji', 'asad']
# login = input("Iltimos, yangi login tanlang!: ")

# if login in users:
#     print("Afsuski, bu login band.")
# else:
#     print("Xush kelibsiz!")
    
#6 - Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 dan 10 gacha bo'lgan
# sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
# son = float(input("Istalgan butun son kiriting: "))
# for n in range(2,11):
#      if not (son%n):
#          print(f"{son} soni {n} ga qoldiqsiz bo'linadi!")

# 9 - DARS TUGADI.