# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:25:01 2024

@author: DavrServis
"""
# UMUMIY TAKRORLASH.
# 1-DARS BIRINCHI DASTURLAR.

# BIRINCHI DASTURLAR.
# print("hello world!")
# print(""" Salom
#      qlaysiz """)
# print("Yaxshi otga bir qamchi, \nYomon otga ming qamchi")
# print("Men \"Dell\" markali noutbook sotib oldim.")

# ARIFMETIK AMALLAR.
# print(26+5*7)
# print("Beshni beshga qo'shish uchun (+) dan foydalanamiz 5+5 =",5+5, "bo'ladi.")
# print("O'ndan uchni ayirish uchun(-) dan foydalanamiz va 10-3 =",10-3, "bo'ladi.")
# print("Yettiga yettini ko'paytirish uchun (*) dan foydalanamiz va 7*7 =",7*7, "bo'ladi.")
# print("To'rtni ikkiga bo'lganda o'nlik son ko'rinishida bo'lish uchun (/) dan foydalanamiz 4/2 =", 
# 4/2, "ga teng.")
# print("To'rtni ikkiga butun son ko'rinishida bo'lish uchun (//) ishlatiladi va 4//2 =", 
# 4//2, "ga teng bo'ladi.")
# print("To'qqizning kvadratini bilish uchun (**) dan foydalanamiz 9**2 =", 9**2, "ga teng.")
# print("Bo'linmaning qoldig'ini bilish uchun (%) dan foydalanamiz va 18%5 =", 18%5, "bo'ladi")

# IZOHLAR.
# Endi biz sizlar bilan izohlarga to'htalib o'tamiz ularni yozishda esa bizga (#) belgisi
# yordamga keladi.

# print("Assalomu Aleykum") # Bu kod konsolga chiqadi.
# print("Nurulloh") Bu kod esa konsolga chiqmaydi.

# AMALIYOT TOPSHIRIQLARI.
#1 - TOPSHIRIQ. Quyidagi matnni aynan shu ko'rinishda konsolga chiqaring.
# ("Nexia", "Tico", 'Damas' ko'rganlar qilar havas.) # Buning uchun quyidagicha kod yozamiz.
# print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas.")

#2 - TOPSHIRIQ. Quyidagi misollarni yechimini Pythonda chiqaring. Har bir misoldan avval misol
# matnini izoh ko'rinishida yozing. Javoblarni savol va yechim ko'rinishida chiqaring:
# 5 ning 4-darajasi 625 ko'rinishida.
# print("5ning 4-darajasi",5**4,"ga teng.")
# print("22ni 4ga bo'lganda qancha qoldiq qolishini aniqlaymiz 22%4 =", 22%4, "ga teng bo'ladi.")
# print("Tomonlari 125ga teng bo'lgan kvadratning yuzi va perimetrini topamiz.Yuza: 125*125 =", 125*125,
# "Perimetr: 4*125 =",4*125)
# print("Diametri 12ga teng bo'lgan doiraning yuzi (π=3.14)",3.14*(12/2)**2,"ga teng bo'ladi.")

#3 - TOPSHIRIQ. Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuasini toping
# (Pifagor teoremasidan foydalaning.)
# print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuasi teng bo'ladi:(6**2+7**2)**(1/2) =",
# (6**2+7**2)**(1/2), "ga teng bo'ladi")

# 1-DARS TUGADI.

# 2-DARS. O'zgaruvchilar va ma'lumot turlari.

# O'zgaruvchilar (veriable). Python dasturlash tilida o'zgaruvchilar yaratish juda oson va ularni istalgan vaqt chaqirib olishimiz
# juda oson. Quyida o'zgaruvchilar yaratishni ko'rib chiqamiz.
# ism = "Abdulloh"
# yosh = 25
# print(ism) 
# print(yosh)
# Biz bitta print bilan bir nechta o'zgaruvchilarni kiritish imkoniga egamiz. Quyida buni ko'rib chiqamiz.
# print(ism, yosh)

# O'zgaruvchilar bunday nomlanishiga sabab uni biz istalgan vaqt o'zgartirishimiz mumkin.
# ism = "Abdulloh"
# print(ism)
# ism = "Nurulloh"
# print(ism)
# O'zgaruvchilarni kiritishda ularni qanday talqin qilamiz, bunda ba'zi qoidalarga rioya qilishimiz talab etiladi.

# O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak

# O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas

# O'zgaruvchi nomida faqatgina lotin alifbosi harflari (A-z), raqamlar (0-9) va pastki chiziq (_) qatnashishi mumkin

# O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas

# O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (ism, ISM, va Ism uchta turli o'zgaruvchi)

# Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funksiyalar va maxsus kalit so'zlarning nomini berish mumkin emas.

# AMALIYOT TOPSHIRIQLARI.

#1 - "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring.
# matn = ("Hello World!")
# print(matn)

#2 - xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni
# ham konsolga chiqaring.
# xabar = ("Salom dunyo!")
# print(xabar)
# xabar = ("Seni sevaman!")
# print(xabar)

#3 - class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?)
# class = ("Hello World!") # Bu o'rinda xato chiqadi chunki class Pythonning ozining ichki komandasi hisoblanadi.

#4 - Quyidagi kodni bajaring:
# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radius", radius, "ga teng aylananing yuzi =", aylana_yuzi)

# 2 - DARS TUGADI.


# 3 - DARS: MATN (STRING).
# String matn Pythonda eng muhim ma'lumot turlaridan biri va ular ("") yoki ('') qo'shtirnoq yoki birtirnoq ichida yoziladi.
# ism = "Abdurashidov"
# avto = "Nexia"
# print(ism)
# print(avto)

# Pythonda matnlar Unicode jadvalidagi istalgan belgilardan iborat bo'lishi mumkin.
# matn = ('Men yangi 📱 oldim.')
# print(matn)

# MATNLARNI QO'SHISH. Matnlarni qo'shish uchun (+) dan foydalanamiz.
# ism = "Abdulloh"
# print("Mening ismim " + ism)

# ism = 'Ahad'
# familya = 'Qayum'
# print(ism + familya)

# Yuqoridagi misolda ikki matn bir-biriga yopishib qoldi bini oldini olish uchun o'rtada joy tashlashimiz kerak.
# print(ism + ' ' + familya) # ko'rinishida.

# F-STRING yordamida biz bir necha matnlarni bir biriga qo'shishimiz mumkin bo'ladi.
# mat1 = "Men seni sevaman!"
# mat2 = "Mavluda"
# print(f"{mat1} {mat2}")

# bu usul yordamida uzun matnlarni ham yozsak bo'ladi.
# fname = 'Bond'
# lname = 'James'
# matn = f"Salom mening ismim {fname}. {lname} {fname}!"
# print(matn)

# F-STRING yordamida nafaqat matnlarni balki balki turli ifodalarni ham ham jamlab yozishimiz mumkin bo'ladi. Bunda ifodalar va
# o'zgaruvchilar katta qavs {} ichida yoziladi.
# tyil = 1999
# print(f"Siz {tyil}-yilda tug'ulgansiz")
# print(f"Yoshingiz {2025 - tyil} da")

# MAXSUS BELGILAR. Maxsus belgilar yordamida matnga turli o'zgarishlar kiritish mumkin. Masalan, matnga bo'shliq qo'shish uchun (\t)
# belgisidan, yangi qatordan boshlash uchun (\n) belgisidan foydalanamiz.
# print("Hello World!")
# print("Hello \tWorld!") # matnlar orasida bo'sh joy tashlaydi.
# print("Hello \nWorld") # (\n) belgisidan keyin kelgan matn yangi qatordan boshlanadi.

# MATNLAR BILAN ISHLASH. Pythonda matnlar ustida amalga oshirish mumkin bo'lgan tayyor funksiyalar mavjud. Odatda, biror funksiya
# ma'lum bir obyektga (o'zgaruvchi, ma'lumot turiga) xos bo'lsa, bunday funksiyalar METODLAR deb ataladi.
# Metodlarni qo'llash uchun metod nomi matndan so'ng (.metod_nomi()) ko'rinishida yoziladi.
# Bularga misol: .upper() va lower() metodlari.

# .upper() metodi matndagi har bir harfni bosh harfga o'zgartiradi. 
# ism_sharif = "Abdurashidov Nurulloh"
# print(ism_sharif.upper())

# .lower() metodi matndagi har bir harfni kichik harfga o'zgartiradi.
# ism_sharif = "ABDURASHIDOV NURULLOH"
# print(ism_sharif.lower())

# .title( metodi matndagi har bir so'zni birinchi harfini katta harfga o'zgartiradi.
# ism_sharif = "abdurashidov nurulloh"
# print(ism_sharif.title())

# .capitalize() metodi matndagi birinchi so'zning birinchi harfini katta harfga o'zgartiradi.
# ism_sharif = "ABDURASHIDOV NURULLOH"
# print(ism_sharif.capitalize())

# Bizda navbatdagi metodlar .strip(), .rstrip() va .lstrip() metodlari bularning har biri o'ziga hos.

# .lstrip() metodi matn boshidagi bo'shliqni yani chap tomondagi.
# .rstrip() metodi matn ohiridagi bo'shliqni yani o'ng tomondagi.
# .strip() metodi esa matn boshi va oxiridagi bo'shliqlarni olib tashlaydi. Quyida buni misol asosida ko'ramiz.
# meva = "    meva    "
# print("Men " + meva.lstrip() + " ni yaxshi ko'raman.") # .lstrip()
# print("Men " + meva.rstrip() + " ni yaxshi ko'raman.") # .rstrip()
# print("Men " + meva.strip() + " ni yaxshi ko'raman.") # .strip()

# ESLATMA. Yuqoridagi metodlar o'zgaruvchi ichidagi asl matnni o'zgartirmaydi! O'zgartirilgan matnni saqlab qolish uchun uni
# o'zgaruvchiga qayta yuklash lozim bo'ladi: meva = meva.strip().
# meva = meva.strip()
# print(meva)

# .input() FOYDALANUVCHI BILAN MULOQOT.
# fOYDALANUVCHI BILAN MULOQOTGA KIRISHISH UCHUN BIZ .INPUT() FUNKSIYASINI ISHLATAMIZ.
# ism = input("Ismingiz nima? ") # Bu o'rinda foydalanuvchidan ma'lumot kiritishini so'rayapti.
# print("Assalomu Alekum, " + ism)

# Keling endi shu dasturni chiroyliroq ko'rinishda qilishga harakat qilib ko'ramiz.
# ism = input("Ismingiz nima? \n>>> ")
# print(f"Assalomu Alekum, {ism.title()}")

# AMALIYOT TOPSHIRIQLARI.
#1 - Quyidagi o'zgaruvchilarni yarating: 

kocha="Bog'bon"

mahalla="Sog'bon"

tuman="Bodomzor" 

viloyat="Samarqand"

#2 - Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring: Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani,
# Samarqand viloyati
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati.")

#3 - Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# print("Qayerda yashaysiz? ")
# kocha = input("Ko'changizni kiriting: ")
# mahalla = input("Mahallangizni kiriting: ")
# tuman = input("Qaysi tumanda yashaysiz: ")
# viloyat = input("Viloyatingizni kiriting: ")
# print(f"Men {kocha.title()} ko'chasi, {mahalla.title()} mahallasi, {tuman.title()} tumani, {viloyat.title()} viloyatida yashayman.")

#4 - Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# print(f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati.")

#5 - Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang.
# manzil = f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati."
# print(manzil)

#6 - manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
# manzil = f"{kocha.title()} ko'chasi, \n{mahalla.upper()} mahallasi, \n{tuman.lower()} tumani, \n{viloyat.capitalize()} viloyati."
# print(manzil)

# 3 - DARS TUGADI.

# 4 - DARS: SONLAR.
# Pythonda sonlarning bir necha turlari bor,quyida ular bilan birma-bir tanishamiz.

# INTEGER (BUTUN SONLAR).
# a = 20 # Sonlar musbat
# b = -30 # manfiy
# c = 0 # 0ga teng bo'lishi mumkin.
# d = a+b
# print(d)

# KVADRAT YUZINI HISOBLAYMIZ.
# k_tomoni = 20 # Kvadrat tomonlari 20 ga teng ekan.
# k_yuzi = k_tomoni ** 2 # Yani bu yerda 2*2 dek gab k_tomonlarini darajaga oshirib qoyamiz va jvadrat yuzini olamiz.

#O'NLIK SONLAR.FLOATS (SUZUVCHI NUQTALI SONLAR).
# Bu sonlarni misol orqali tushunishga harakat qilamiz.
# pi = 3.14159 # O'nlik son (float).
# radius = 10 # Butun son. 
# diametr = 2 * radius # Aylana diametrini topish uchun radiusni 2ga ko'paytiramiz.
# print("Aylana uzunligu", pi * diametr, "ga teng.") # Bu qadam orqali biz aylana uzunligini toptik (pi * diametr) orqali.

# BUTUN SONDAN O'NLIK SONGA.
# Avval aytkanimizdek ikkita butun sonni bo'lish bizga doim natijada o'nlik son beradi(natija butun bo'lsa ham).
# a = -20 # Butun son.
# b = 10 # Butun son.
# c = a/b # Bo'lamiz.
# print(c) # Natija o'nlik son ko'rinishida chiqadi(-2.0).

# Shuningdek butun va o'nlik son o'rtasidagi har qanday arifmetik amallarning natijasi ham o'nlik son bo'ladi.
# a = 10 
# b = 2.0
# print(a+b) # Natija 12.0.
# print(a-b) # Natija 8.0.
# print(a*b) # Natija 20.0.
# print(a/b) # Natija 5.0. Shu ko'rinishda.

# UZUN SONLARNI KIRITISH. 
# Uzun sonlarni kiritishda (_) pastki chiziqdan foydalanishimiz mumkin. Python pstki chiziqni (_) son tarkibida
# inobatga olmasdan uzun sonligicha qabul qiladi, ammo bu bizga qulaylik yaratadi va sonlarni kiritishda tushunarliroq
# harakat qilishimizga yordam beradi.
# aholi_soni = 33_580_000
# print("O'zbekistonda aholi soni", aholi_soni, "dan ortiqroqni tashkil qiladi.") # Bu yerda son 33580000 ko'rinishida chiqadi.

# KONSTANTA.
# Aksar dasturlash tillarida o'zgarmas qiymat (KONNSTANTA) lar mavjud. Misol uchun (π = 3.14159) doimiy holatda.
# Pythonda konstanta tushunchasi yo'q va bunday o'zgarmas qiymatlar kiritish uchun bosh harflardan foydalanilari(PI).
# PI = 3.14159 # KONSTANTA.
# radius = 21.1   

# BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH.
# Birdaniga bir nechta o'zgaruvchiga qiymat berish uchun o'zgaruvchilar va ularga mos qiymatlar vergul (,) bilan
# ajratiladi: Quyida buni ko'rib chiqamiz.
# x, y, z = 12, 234, 254 # Shu ko'rinishda.
# print(x, y, z)

# Bu usulni istalgan turdagi o'zgaruvchiga qo'llashimiz mumkin.
# yosh, ism = 36, "Nurulloh"
# print("Meni ismim", ism, ", yoshim esa ", yosh, "da")

#O'ZGARUVCHILAR TURINI ALMASHTIRISH.
# ism = "Jobir"
# yosh = 30
# xabar = ism + ' ' + yosh + 'yoshda'
# print(xabar) # Bu yerda xatolik yuz beradi va bu xatolik shundan iboratki int tipidagi ma'lumotni str tipidagi
# ma'lumotga qo'shib bo'lmasligi haqida. Buni to'g'irlash uchun quyidagicha yo'l tutamiz.
# xabar = ism + ' ' + str(yosh) + 'yoshda' # Bu yerda yoshni str ga tenglab oldik.

#O'ZGARUVCHI TURINI TEKSHIRISH.
# O'zgaruvchilarni tekshirish bizga yuqoridagi singari xatolarni oldini olish imkonini beradi va bu dasturda
# o'zgaruvchilar soni ko'payib ketkanda ham ish beradi.
# ism = "Jobir"
# yosh = 36
# print(type(yosh)) # Bu yerda yosh ning tipini.
# print(type(ism)) # Bu yerda esa ism ning tipini aniqladik.

# .INPUT() va SONLAR.
# Avvalgi bo'limda o'rganganimiz .input("") foydalanuvchidan qandaydir ma'lumot so'rash. Kelin foydalanuvchidan 
# tug'ilgan yilini so'ragan holda uni yoshini hisoblab ko'ramiz.
# tyil = input("Itimos tug'ilgan yilingizni kiriting: ") # Foydalanuvchini tug'ilgan yilini so'raymiz.
# yosh = 2024 - tyil # Joriy yildan ayiramiz tug'ilgan yilini yoshi kelib chiqadi bu teskarisiga ham ishlaydi yani 
# tug'ilgan yilini topish uchun ham.
# print(f"Siz {yosh}da ekansiz.") # Natijani chiqaramiz.Va bu yerda xatolik beradi. Uni tarjima qilsak int tipidan
# str tipidagi malumotni ayirib bo'lmaydi degan hulosa hosil bo'ladi. Gap shindaki .input() o'ziga kiritilgan har qanday
# qiymatni str ko'rinishida qabul qiladi.

# Bu kodni to'gri yozish uchun esa quyidagicha yo'l tutamiz.
# tyil = int(input("Iltimos tug'ilgan yilingizni kiriting: ")) # Foydalanuvchini tug'ilgan yilini so'raymiz, va uni int
# butun son korinishida saqlaymiz.
# yosh = 2024 - tyil # Joriy yildan tug'ilgan yilni ayiramiz.
# print(f"Sizning yoshingiz {str(yosh)} da ekan.") # Ntijani chiqarishta yoshni tipini str ga o'tkazamiz va tayyor.

# AMALIYOT TOPSHIRIQLARI.
#1 - Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur.
# son = float(input("Istalgan soningizni kiriting:"))
# print(f"Kiritilgan {son} sonining kvadrati = {son**2}.")
# print(f"Kiritilgan {son} sonining kubi = {son**3}.")

#2 - Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur.
# yosh = int(input("Yoshingiz nechchida? "))
# print(f"Siz {2024 - yosh}-yilda tug'ilgan ekansiz.")

#3 - Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va
# bo'linmasini chiqaruvchi dastur
# print("Istalgan ikki sonni kiriting!")
# bson = float(input("Birinchi sonni kiriting: "))
# ison = float(input("Ikkinchi sonni kiriting: "))
# print(bson + ison)
# print(bson - ison)
# print(bson * ison)
# print(bson / ison)

# 4 - DARS TUGADI.



# 5 - DARS.RO'YXATLAR.

# Bir vaqtning o'zida bitta o'zgaruvchi ichida birnechta elementlarni saqlash imkonini beruvchi ma'lumot turi
# RO'YXATLAR (LIST) deyiladi. Quyida bunga misollar ko'rib chiqamiz.
# mevalar = ['1','2','3','4','5'] # Ro'yxatlar bir vaqtda istalgancha element qabul qilish imkoniga ega.
# mevalar = ['olma','nok','banan','shaftoli','tarvuz', "o'rik"] # <- Oddiy ro'yxat.
# narxlar = [1000,2000,3000,4000,-1341,10.234] # <- Narxlar ro'yxati.
# sonlar = ['bir', 'ikki', 3, 4, 5] # <- Aralash ro'yxat.
# ismlar = [] # <- Bo'sh ro'yxat.
# print(mevalar) Bulardan istalgan ro'yxatni konsolga chiqarishimiz mumkin.

# RO'YXAT ELEMENTLARINING TARTIBLANISHI. 
# Biz ro'yxatlarga murojaat qilishda ularni o'z tartib raqami bilan chaqirishimiz mumkin. Dasturlash tillarida tartib
# Bo'yicha raqamlash yani indekslash 0 dan boshlanadi yani birinchi elementni chaqirish uchun r_nomi[0] deb murojaat
# qilamiz. Quyida bunga misollar ko'rib chiqamiz.
# print("Birinchi meva:", mevalar[0]) # Shu ko'rinishda.
# print("Birinchi meva:", mevalar[3]) # Bunda bizga 4-element chiqib keladi.
 
# Agar ro'yxat ichidagi elementlar matn(str) tipida bo'lsa unga biz har hil metodlarni qo'llashimiz mumkin.
# mevalar = ['olma','nok','banan','shaftoli','tarvuz', "o'rik"]
# print("Birinchi meva:", mevalar[0].title()) # Shu ko'rinishda.
# print("Birinchi meva:", mevalar[3].upper())

# # LIST ELEMENTLARI USTIDA ARIFMETIK AMALLAR.
# narxlar = [1000,2000,3000,4000,1341,10234]
# print(narxlar[1] + narxlar[2]) # Bunda ikkinchi va uchinchi narxlar o'zaro qo;shiladi.

# # Pythonda LIST ning eng ohirgielementiga -1 indeksi orqali murojaat qilishingiz mumkin, bu ro'yxatning aniq uzunligini
# # bilmagan hollarimizda asqotadi.
# sonlar = [1, 2, 3, 4, 5, 6, 123, 35634, -12312, 12.1231]
# print(sonlar[-1]) # Mana shu ko'rinishda.

# ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH.
# Dastur davomida listning tarkibi o'zgarishi, elementlar qo'shilishi, bazi elementlar o'chirilishi tabiiy hol shularni
# ko'rib chiqamiz.
# Ro'yxatdagi biror elememntning qiymatini o'zgartirish uchun kerakli elementga uning indeksi bo'yicha murojaat etamiz
# va yangi qiymat yuklaymiz. 
# QIYMAT O'ZGARTIRISH.
# narxlar = [1000,2000,3000,4000,10000,24000] # <- Narxlar ro'yxati.
# narxlar[2] = 32000 # 3-tartib raqamli elementga qiymat berdik.
# narxlar[0] = 7000 # 1-tartib raqamli elementga qiymat berdik.
# print(narxlar) # Natija.
# # Mavjud bo'lmagan indeksga qiymat yuklab yoki o'zgartirib bo'lmaydi.

# # QIYMAT QO'SHISH.
# # Qiymat qo'shishning ikkita usuli bor shularni ko'rib chiqamiz. .APPEND() METODI.
# mevalar = ['olma','nok','banan','shaftoli','tarvuz', "o'rik"] # <- Oddiy mevalar ro'yxat.
# mevalar.append('qovun') # Yangi element ('qovun') qo'shdik.
# print(mevalar) # Natija.

# .append metodi bo'sh ro'yxatni to'ldirish uchun juda qulay.
# Dastur boshida bo'sh ro'yxat yaratib dastur davomida uni to'ldirib boramiz.
# cars = [] # Bo'sh ro'yxat yaratib oldik.
# cars.append('jentra') # Ro'yxatga yangi ('jentra') element qo'shdik.
# cars.append('cobalt') # Ro'yxatga yangi ('cobalt') element qo'shdik.
# cars.append('nexia 3') # Ro'yxatga yangi ('nexia 3') element qo'shdik.
# print(cars) # Natija.

# .INSERT() metodi.
# .insert metodi orqali oqali ro'yxatning istalgan joyiga yangi element qo'shishimiz mumkin.
# Mwtod ichida yangi elementning indeksi va qiymati beriladi.
# cars =['cobalt', 'jentra', 'nexia 3'] # Ro'yxat yaratib oldik.
# print(cars) # Natija.
# cars.insert(0, 'malibu') # Yangi element qo'shamiz. 
# print(cars) # Natija.
# cars.insert(2, 'damas') # Yangi element qo'shamiz. 
# print(cars) # Natija.

# ELEMENTNI O'CHIRISH.
# Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki qiymatini bilishimiz lozim.
# Elementni indeks yordamida indeks yordamida olib tshlash uchun DEL operatoridan foydalanamiz.
# mevalar = ['olma','nok','banan','shaftoli','tarvuz', "o'rik"] # <- Oddiy mevalar ro'yxat.   
# del mevalar[1] # DEL operatori bilan elementni ('nok') indeksi bo'yicha olib tashladik.
# print(mevalar) # Natija.

# Elementlarni qiymati bo'yicha o'chirish uchun esa .REMOVE() metodidan foydalanamiz.
# Buning uchun qavs ichida olib tashlanishi kerak bo'lgan qiymatni yozamiz.
# mevalar = ['olma','nok','banan','shaftoli','tarvuz', "o'rik"] # <- Oddiy mevalar ro'yxat.
# mevalar.remove('shaftoli') # .REMOVE('shaftoli') metodi bilan elementni olib tashladik.
# print(mevalar) # Natija.

# # .REMOVE() metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chirib tashlaydi, yani agar ro'yxatda 2 va undan
# # ortiq bir xil element bo'lsa ularning faqat birinchisi o'chirib tashlanadi.
# pets = ["sigir", "qo'y", "mushuk", "it", "sigir", "buqa"] # <- oddiy uy hayvonlari ro'yxati.
# pets.remove("sigir") # .REMOVE("sigir") metodi bilan elementni olib tashladik. 
# print(pets) # Natijada ro'yxatda ikkita bir xil element bo'lgani uchunularning biri olib tashlandi.

# # ELEMENTNI SUG'URIB OLISH.
# # Bazida biror elementni butunlay ochirib tashlash emas balki uni sug'irib olib, foydalanish talab etiladi.
# # Buning uchun biz Pythonda .POP() metodidan foydalanamiz.
# bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"] # <- oddiy bozorlik ro'yxati.
# mahsulot = bozorlik.pop(3) # 4-elementni sug'urib olamiz va uni mahsulot degan o'zgaruvchiga yuklaymiz.
# print("Men " + mahsulot + " sotib oldim") # print() yordamida Natijani chiqaramiz.
# print("Olinmagan mahsulotlar:", bozorlik) 

# # Agar .POP() metodida indeks berilmasa, ro'yxatning ohirgi elementini sug'urib olinadi.
# numbers = [1,2,3,4,5] # <- oddiy raqamlar ro'yxati.
# print(numbers) # Natija.
# numbers.pop() # .pop() metodida indeks bermasdan ro'yxatning ohirgi elementini sug'urib olamiz. ETIBOR BERING! agar 
# # sug'urib olingan element yangi o'zgaruvchiga yuklanmasa shunchaki yo'q bo'lib qoladi.
# print(numbers) # Natija.

# # AMALIYOT TOPSHIRIQLARI.
# #1 - ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting.
# ismlar = ['abdurahmon', 'hojiakbar', 'erkinjon']
# print(ismlar)

# #2 - Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring.
# print(f"Salom {ismlar[0].title()}, bugun choyxonaga boramizmi?")
# print(f"Salom {ismlar[1].title()}, bugun choyxonaga boramizmi?")
# print(f"Salom {ismlar[2].title()}, bugun choyxonaga boramizmi?")

#3 - sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
# sonlar = [1, 2, 3, 4, 5, 6, 123, 35634, -12312, 12.1231]

# #4 - Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning
# # qiymatini o'zgartiring, ba'zilarini esa almashtiring.
# print(sonlar[0] + sonlar[3])
# print(sonlar[5] - sonlar[2])
# sonlar[0] = 9032
# son = sonlar.pop(7)
# print(sonlar)
# print(son)

#5 - t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy
# shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# t_shaxslar = []
# z_shaxslar = []
# t_shaxslar.append("Imom Buxoriy")
# t_shaxslar.append("Alisher Navoiy")
# t_shaxslar.append("Abu Bakir Siddiq")
# print(t_shaxslar)

# z_shaxslar.append("Rasul Kxusherbayev")
# z_shaxslar.append("Shavkat Mirziyoyev")
# z_shaxslar.append("Bill Gates")
# print(z_shaxslar)


#6 - Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan,\nva zamonaviy shaxslardan {z_shaxslar.pop(0)} lar, \nbilan uchrashgan bo'lardim")

#7 - friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan
# do'stlaringizni kiriting. 
# friends = []
# friends.append('abdurahmon')
# friends.append('hojiakbar')
# friends.append('erkinjon')
# friends.append('lazizbek')
# friends.append('akramjon')
# print(friends)

# #8 - Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
# friends.remove('lazizbek')
# friends.remove('akramjon')
# print(friends)
# #9 - Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# friends.insert(0, 'asadbek')
# friends.insert(2, 'akbar ali')
# friends.insert(-1, 'muzaffar')
# print(friends)

# #10 - Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan
# # do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# mehmonlar = []
# dostlar = ['abdurahmon', 'hojiakbar', 'erkinjon', 'lazizbek', 'akramjon']
# mehmonlar.append(dostlar.pop(1))
# mehmonlar.append(dostlar.pop(0))
# mehmonlar.append(dostlar.pop(-1))
# print(f"Mening tug'ilgan kunimga kelgan mehmonlar: {mehmonlar[0].title()}, {mehmonlar[1].title()}, {mehmonlar[2].title()}")

# 5 - DARS TUGADI.

# 6 - DARS.

# RO'YXATLAR BILAN ISHLASH.
# Bazi holatlarda ro'yxat elementlarini alifbo ketma-ketligida tartiblash talab qilinishi mumkin. Buning uchun maxsus 
# .sort() metodidan foydalanamiz. 
# cars = ['damas', 'jiguli', 'matiz', 'tico', 'nexia'] # <- oddiy ro'yxat.
# cars.sort() # Alifbo ketma-ketligida tartiblaymiz.
# print(cars) # Natija.

# Tartiblashda bosh harf kichik harfdan oldin kelishini etiborga oling. Agar ro'yxatdagi so'zlarning bosh harfi katta
# kichik aralash yozilgan bo'lsa ularni bir tartibga keltirib olish maqsadga muvofiq.
# moshinalar = ['damas', 'jiguli', 'matiz', 'GM', 'tico', 'nexia'] # Bu ro'yxatda endi bosh harfli so'zlar ham bor.
# moshinalar.sort() # Tartiblaymiz.
# print(moshinalar) # Natija.
# Bu holatda endi 'GM' eng birinchiga chiqib qoladi buni oldini olish uchun ro'yxatni bir hil ko'rinishga keltirib olish
# lozim.

# RO'YXATNI TESKARI TARTIBLASH.
# moshinalar = ['damas', 'jiguli', 'matiz', 'gm', 'tico', 'nexia'] # Oddiy ro'yxat.
# moshinalar.sort(reverse=True) # Ro'yxatni teskari tartiblaymiz.
# print(moshinalar) # Natija.

# RO'YXATNING ESKI HOLATIGA TEGMAGAN HOLDA TARTIBLASH.
# guests = ['Bahodir', 'Rahmatjon', 'Anvar', 'Farrux', 'Hasan', 'Husan', 'Shodmon'] # Oddiy ro'yxat.
# print(".sorted() qaytargan natijadagi ro'yxat: ", sorted(guests), "\n") # .sorted yordamida tartiblangan ro'yxat.
# print(".sorted() funksiyasi yordamida teskari tartiblangan ro'yxat: ", sorted(guests, reverse=True), "\n") # .sorted()
# yoedamida teskari tartiblangan ro'yxat.
# print("Asl holatdagi ro'yxat: ", guests, "\n") # Asl ro'yxat.

# Yuqoridagi ikki usul orqali sonlarni ham tartiblashimiz mumkin.
# ages = [21, 24, 45, 25, 79, 1] # <- Oddiy tartibsiz ro'yxat.
# print(ages) # Asl ro'yxat.
# print(sorted(ages)) # Tartiblangan.
# print(sorted(ages, reverse=True)) # Teskari tartiblangan.

# RO'YXATLARNI AYLANTIRISH.
# Buning uchun bizga .reverse() metodidan foydalanamiz.
# fruits = ['pear', 'apple', 'apricot', 'watermelon', 'lemon'] # Oddiy ro'yxat.
# fruits.sort() # Alifbo bo'yicha tartiblangan.
# print(fruits) # Natija.
# fruits.reverse() # Teskari tartiblangan.
# print(fruits) # Natija.

# RO'YXARNING UZUNLIGINI TOPISH YANI UNING ICHIDAGI ELEMENTLAR SONINI ANIQLASH.
# Buning uchun bizga len() funksiyasi kerak bo'ladi.
# fruits = ['pear', 'apple', 'apricot', 'watermelon', 'lemon'] # Oddiy ro'yxat.
# print(fruits) # Ro'yxat elementlari.
# print("FRUITS ro'yxatidagi elementlar soni: ", len(fruits)) # Elementlar soni.

# RANGE() FUNKSIYASI.
# RANGE() funksiyasi oraqli biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. 
# sonlar = list(range(0,10)) # Bu o'rinda yaratilgan sonlar ketma-ketligini list orqali ro'yxatga yuklab oldik.
# print(sonlar) # Aytib o'tish kerakki range() funksiyasi belgilangan sonlar ketma-ketligini yaratar ekan ohirgi sonni 
# qiymatini olmaydi yani bizning holatda 10 sonini olmaydi.

# RANGE() orqali biz qadamniham berishimiz mumkin. Quyida buni misollar bilan ko'rib chiqamiz.
# juft_sonlar = list(range(0,20,2)) # 0dan 20gacha 2 qadam bilan. (juft sonlar)
# toq_sonlar = list(range(1,20,2)) # 1dan 20gacha 2 qadam bilan. (toq sonlar)
# print(juft_sonlar) # 0dan 20 gacha bo'lgan juft sonlar ro'yxati aytkanimizdek 20 sonining o'zi bu ro'yxatga kirmaydi.
# print(toq_sonlar) # 0dan 20 gacha bo'lgan toq sonlar ro'yxati, agar shu yerda biz 20 o'rniga 21 kiritib toq sonlarni 
# so'raganimizda toq sonlar ro'yxatiga kira olmas edi yuqoridagi qoidaga muvofiq.

# Agar sonlar ketma ketligi 0dan boshlansa, range() funksiyasida ikkinchi argumentni ko'rsatish kifoya. 
# a = list(range(0,10))
# b = list(range(10))
# print(a)
# print(b)
# Yuqoridagi kodning natijasi bir hil bo'laveradi.

# SONLI RO'YXATLAR USTIDA SODDA AMALLAR.
# Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham amalga oshirishimiz mumkin. Masalan, ro'yxatdagi eng katta
# sonni topish max() funksiyasidan, eng kichigini topish uchun min() funksiyasidan va sonlarning yeg'indisini topish
# sum() funksiyasidan foydalanamiz.
# narxlar = [12000, 25000, 240000, 12300000, 5000, 97000] # Oddiy ro'yxat.
# print("NARXLAR ro'yxatidagi eng kichin son: ", min(narxlar), "\n") # Eng kichigini topish.
# print("NARXLAR ro'yxatidagi eng katta son: ", max(narxlar), "\n") # Eng kattasini topish.
# print("NARXLAR ro'yxatining sonlar yeg'indisi: ", sum(narxlar), "\n") # Umumiy yeg'indisini topish.

# Yuqoridagi kodni boshqacha ko'rinishda yozsak ham bo'ladi.
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)

# print("Eng arzon narx: ", arzon, \
#       "\nEng qimmat narx: ", qimmat, \
#           "\nJami narxlar yeg'indisi: ", jami)
# Shu o'rinda aytib o'tish kerakki kodingiz rasayam uzun bo'lib ketsa kodni (\) shu belgi orqali qatorni bir-necha
# qatorlarga bo'lishingixz mumkin.

# RO'YXATNI KESISH. 
# Bazida ro'yxatnimng ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin. 
# Deylik, biz quyidagi cars degan ro'yxatdan birinchi 3ta elementni ajratib olmoqchimiz, buning uchun boshlang'ich va
# ohirgi indekslarni beramiz: 
# cars = ['damas','niva', 'jiguli', 'matiz', 'tico', 'nexia'] # <- oddiy ro'yxat.
# my_cars = cars[0:3] # 0dan boshlab uchta elementni ajratib olamiz.
# print(my_cars) # Natija.
# Pythonda ro'yxatni kesishda 2-ko'rsatilgan indeksdan bitta avval to'xtaydi. Yuqoridagi misolda ham 0, 1, 2-elementlar
# ajratib olindi range() funksiyasi bolan bir hil ishlaydi.


# Yuqoridagi usul bilan ro'yxatni istalgan joyidan bo'lishimiz mumkin:
# print(cars[2:5]) # Natijada 2-indeksdan 5-ineksgacha bo'lgan elementlar kesib olinadi.

# Agar boshlang'ich indeksni bermasangiz, Python avtotmatik ravishda 0-indeksdan boshlab kesadi. Agar 2-indeksni
# kiritmasangiz, ro'yxatning ohirigacha kesadi:
# print(cars[:4]) # Ro'yxatning boshidan 4ta elementni ajratish.
# print(cars[3:]) # 3-elementdan ro'yxat ohirigacha kesish.

# RO'YXATDAN NUSXA OLISH.
# Dastur davomida biror ro'yxatdan nusxa olish talab qulinishi mumkin. Buning uchun tenglik (=) belgisidan foydalansak bo'ladm?
# Quyidagi misolga etibor bering:
# sonlar1 = [1, 2, 3, 4, 5] # Sonlar degan ro'yxat yaratamiz.
# sonlar2 = sonlar1 # Sonlar2 degan ro'yxatni sonlar1ga tenglaymiz.
# sonlar2.append(6) # Sonlar2 degan ro'yxatimizga 6 sinini qo'shamiz.
# sonlar2.append(7) # Sonlar2 degan ro'yxatimizga 7 sinini qo'shamiz.
# print("Bu sonlar1 ro'yxati: ", sonlar1)
# print("Bu sonlar2 ro'yxati: ", sonlar2)
# Bunda natija biz kutkandek chiqmaydi chunki sonlar2 = sonlar1 deb yozgan komandamiz yangi ro'yxat yaratish o'rniga 
# ikkala o'zgaruvchini ham xotirasidagi bitta ro'yxatga bog'lab (yo'naltirib) qo'ydi. Yani bitta ro'yxat ikkita
# nomga ega bo'lib qoldi. 

# Endi biz aslida qanday yo'l tutishimiz kerak edi shuni ko'rib chiqamiz.
# sonlar1 = [1, 2, 3, 4, 5] # Sonlar degan ro'yxat yaratamiz.
# sonlar2 = sonlar1[:] # Bu o'rinda endi haqiqatdan ham nusxa oldik.
# sonlar2.append(6) # Sonlar2 degan ro'yxatimizga 6 sinini qo'shamiz.
# sonlar2.append(7) # Sonlar2 degan ro'yxatimizga 7 sinini qo'shamiz.
# print("Bu sonlar1 ro'yxati: ", sonlar1)
# print("Bu sonlar2 ro'yxati: ", sonlar2)
# Nusxa olish shu ko'rinishda amalga oshiriladi.

# TUPLES - O'ZGARMAS RO'YXATLAR.
# Dastur davomida o'zgarmas ro;yxatlar tuzish talab qilinishi mumkin. Pythonda bunday ro'yxatlar TUPLES deb yuriladi.
# TUPLE ichidagi qiymatlar bir marta beriladi dasturning boshida, so'ngra o'zgartirib bo'lmaydi. TUPLE elon qilishda
# listdan farqli o'laroq [] kvadarat qavslardan emas balki oddiy qavslar () ishlatiladi.

# tomonlar = (20, 30, 55.2)
# print(tomonlar)
# TUPLE elementlariga xuddi ro'yxat elementlariga murojaat etilgani kabi indeks bilan murojaat qilinadi.

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# Keling TUPLE ichidagi biror elementni o'zgartirib ko'ramiz.
# toys[3] = 'dragon' # Bu holatda albatta xatolik beradi chunki aytkanimizday o'zgarmas ro'yxatga faqat dastur boshida 
# o'zgartirish kirita olamiz keyinchalik (qo'shish, o'zgartirish, olib tashlash) o'zgartira olmaymiz.

# Mobodo bizdan TUPLE ni o'zgartirish talab qilinsa u holda avval TUPLE ni LIST ga o'zgartirishimiz kerak bo'ladi.
# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard') # TUPLE yaratib oldik.
# toys = list(toys) # TUPLE ni oddiy LIST ga o'tkazamiz.
# Endi o'zgarishlar kiritishimiz mumkin.
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'myQueen'
# Ro'yxatni qaytadan o'zgarmas ro'yxatga o'tkazamiz.
# toys = tuple(toys) # Shu ko'rinishda.
# print(toys) # Ko'rib turganingizday hammasi joyida.

# AMALIY TOPSHIRIQLAR.
#1 - O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
countries = ["o'zbekiston", 'qatar', 'rossiya', 'ispaniya']
print("Countries ro'yxati ichida ", countries, "shu davlatlar bor.\n")

#2 - Ro'yxatning uzunligini konsolga chiqaring.
print("Countries ro'yxatida: ", len(countries), "ta element bor\n")

#3 - sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring.
print("Countries ro'yxatidagi elementlarnig tartiblangan holati: ", sorted(countries), "shunday bo'ladi\n")

#4 - sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring.
print("Countries ro'yxatidagi elementlarnig teskari tartiblangan holati: ", sorted(countries, reverse=True),\
"shunday bo'ladi\n")
    
#5 - Asl ro'yxatni qaytadan konsolga chiqaring.
print("Countries ro'yxatining asl ko'rinishi: ", countries,"shu ko'rinishda.\n")

#6 - reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring.
countries.reverse()
print("Asl ro'yxatning teskari ko'rinishi: ", countries, "shu ko'rinishda.\n")

#7 - sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)

#8 - 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
j_sonlar = list(range(120,1200,2))
print("120dan 1200gacha bo'lgan juft sonlar: ", j_sonlar, "dan iborat.\n")

#9 - Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring.
print("j_sonlar ro'yxatidagi sonlar yeg'indisi: ", sum(j_sonlar), "ga teng.\n")

#10 - Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring.
print("j_sonlar ro'yxatidagi eng katta va eng kichik son o'rtasidagi ayirma: ", max(j_sonlar) - min(j_sonlar), "ga teng.\n")

#11 - Ro'yxatdagi elementlar sonini hisoblang.
print("j_sonlar ro'yxatidagi elementlar soni: ", len(j_sonlar), "taga teng.\n")

#12 - Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring.
print(j_sonlar[0:21],"\n")
print(j_sonlar[260:281],"\n")
print(j_sonlar[520:541],"\n")

#13 - taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting.
foods = ['osh', 'somsa', 'kabob', 'shirguruch', 'shorva']

#14 - nonushta degan yangi ro'yxatga taomlardan nusxa oling.
nonushta = foods[:]

#15 - Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing.
nonushta.remove('osh')
nonushta.remove('kabob')
nonushta.remove('shorva')
nonushta.append('non va qaymoq')
nonushta.append('m_kasha')


#16 - Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(foods,"\n")
print(nonushta,"\n")

#17 - Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat
# berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = 'osh'

# 6 - DARS TUGADI.

# 7 - DARS.






 