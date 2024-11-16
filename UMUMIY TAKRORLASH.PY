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

# kocha="Bog'bon"

# mahalla="Sog'bon"

# tuman="Bodomzor" 

# viloyat="Samarqand"

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
# countries = ["o'zbekiston", 'qatar', 'rossiya', 'ispaniya']
# print("Countries ro'yxati ichida ", countries, "shu davlatlar bor.\n")

#2 - Ro'yxatning uzunligini konsolga chiqaring.
# print("Countries ro'yxatida: ", len(countries), "ta element bor\n")

#3 - sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring.
# print("Countries ro'yxatidagi elementlarnig tartiblangan holati: ", sorted(countries), "shunday bo'ladi\n")

#4 - sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring.
# print("Countries ro'yxatidagi elementlarnig teskari tartiblangan holati: ", sorted(countries, reverse=True),\
# "shunday bo'ladi\n")
    
#5 - Asl ro'yxatni qaytadan konsolga chiqaring.
# print("Countries ro'yxatining asl ko'rinishi: ", countries,"shu ko'rinishda.\n")

#6 - reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring.
# countries.reverse()
# print("Asl ro'yxatning teskari ko'rinishi: ", countries, "shu ko'rinishda.\n")

#7 - sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

#8 - 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
# j_sonlar = list(range(120,1200,2))
# print("120dan 1200gacha bo'lgan juft sonlar: ", j_sonlar, "dan iborat.\n")

#9 - Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring.
# print("j_sonlar ro'yxatidagi sonlar yeg'indisi: ", sum(j_sonlar), "ga teng.\n")

#10 - Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring.
# print("j_sonlar ro'yxatidagi eng katta va eng kichik son o'rtasidagi ayirma: ", max(j_sonlar) - min(j_sonlar), "ga teng.\n")

#11 - Ro'yxatdagi elementlar sonini hisoblang.
# print("j_sonlar ro'yxatidagi elementlar soni: ", len(j_sonlar), "taga teng.\n")

#12 - Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring.
# print(j_sonlar[0:21],"\n")
# print(j_sonlar[260:281],"\n")
# print(j_sonlar[520:541],"\n")

#13 - taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting.
# foods = ['osh', 'somsa', 'kabob', 'shirguruch', 'shorva']

#14 - nonushta degan yangi ro'yxatga taomlardan nusxa oling.
# nonushta = foods[:]

#15 - Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing.
# nonushta.remove('osh')
# nonushta.remove('kabob')
# nonushta.remove('shorva')
# nonushta.append('non va qaymoq')
# nonushta.append('m_kasha')


#16 - Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(foods,"\n")
# print(nonushta,"\n")

#17 - Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat
# berib ko'ring.
# nonushta = tuple(nonushta)
# nonushta[0] = 'osh'

# 6 - DARS TUGADI.

# 7 - DARS.
# FOR TSIKLI. 
# Dasturlash davomida kodimizning biror bir qismini bir necha marta takrorlash talab etilishi mumkin.
# Bunda bizga FOR operatori yordamga keladi. Bu operator yordamida biz kodlarimizni bir necha marta takrorlashimiz
# mumkin. Dasturlashda bu TSIKL (LOOP) deyiladi.

# Quyidagi misolni ko'ramiz.Bizda mehmonlar degan ro'yxat bor, har bir mehmonning ismini yangi qatordan
# chiqarmoqchimiz. Buning uchun quyidagi kodni yozamiz. 
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim'] # Oddiy ro'yxat.
# for mehmon in mehmonlar: # Mehmonlar ro'yxatidagi har bir mehmon uchun quyidagi kodni bajar deyapmiz.
#     print(mehmon) # Natija.
# Yuqoridagi tsikl toki mehmonlar ichidagi elementlar tugagunga qadar davom etadi.

# FOR TSIKLI QANDAY ISHLAYDI. Keling yana bir misolga etibor beraylik.
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']    
# for mehmon in mehmonlar: # Bu qator sikl sharti deyiladi va aynan shu qator kodni bir necha marta takrorlanishini
# # taminlaydi.
    # print(f"Hurmatli {mehmon}, ")
    # print("Sizni 20-mart kuni nahorgi oshga taklif qilamiz.")
    # print("Hurmat bilan, Palonchiyevlar oilasi.\n")
# Yuqoridagi 3ta qator sikl badani deyiladi va shart to'g'ri bo'lganda bajariladi.
# print("Dastur tugadi.\n") # Bu qator esa sikldan tashqarida va dasturga aloqasi yo'q.

# Quyidagi kod bilan yana bir misol ko'rgan bo'lamiz.
# cars = ['nexia', 'tico', 'damas'] # Oddiy ro'yxat.
# for car in cars: # FOR funksiyasi sharti.
#     print(car.title()) # Dastur tanasi.
# print("Ko'rganlar qilar havas!") # sikldan keyingi kod.
# # Agar 4-qatordagi kodni surmasak Python uni ham sikla ichida deb o'ylaydi va qayta qayta takrorlaydi.

# cars = ['nexia', 'tico', 'damas'] # Oddiy ro'yxat.
# for car in cars: # FOR funksiyasi sharti.
#     print(car.title()) # Dastur tanasi.
#     print("Ko'rganlar qilar havas!") # sikl ichidagi kod.

# FOR yordamida sonli ro'yxatlar bilan ishlash.
# Quyidagi misolni ko'zdan kechiramiz.
# sonlar = list(range(1,11)) # LIST va RANGE yordamida sonlar degan ro'yxat yaratib uning ichiga 1dan 11gacha sonlarni 
# # ro'yxatini yaratib olamiz.
# for son in sonlar: # FOR orqali sonlar ichidagi har bir son uchun.
#     print(f"{son} ning kvadrati {son**2} ga teng.") # Bu yerda har bir sonni kvadratini hisoblaydigan dastur yozyapmiz.
    
# FOR yordamida yangi ro'yxat ham shakllantirish mumkin. Quyidagi dasturda 1dan 10gacha sonlar ro'yxatini yaratib
# olyapmiz. Keyin esa sonlar kvadratini joylash uchun bo'sh ro'yxat yaratdik. FOR sikli ichida esa har bir sonning 
# kvadratini hisoblab, sonlar_kvadrati ro'yxatiga qo'shib boryapmiz.
# sonlar = list(range(1,11)) # Sonlar ro'yxatini shakllantirib olyapmiz.
# sonlar_kvadrati = [] # Bo'sh ro'yxat yaratib oldik va dastur davomida uni to'ldirib boramiz.
# for son in sonlar:# FOR sikli bilan har doimgiday sonlar ro'yxatidagi har bir son uchun:
#     sonlar_kvadrati.append(son**2) # Sonlar_kvadrati degan bo'sh ro'yxatimizni to'ldirishni boshladik. Har bir sonning
# # kvadratini hisoblab ularni sonlar_kvadrati ro'yxatimizga qo'shib ketamiz.
# print(sonlar) # Sonlarning alohida ro'yxatini chiqaramiz.
# print(sonlar_kvadrati) # Sonlar_kvadrati ro'yxatini alohida chiqaramiz.

# FOR va INPUT().
# FOR operatori va INPUT() funksiyasi yordamida foydalanuvchidan bir nechta qiymatlar qabul qilish va olingan
# qiymatlarni ro'yxatga joylash mumkin:
# dostlar = [] # Bo'sh ro'yxat yaratib olamiz.
# print("5ta eng yaqin dostingizni kim? ") # Foydalanuvchidan beshta eng yaqin do'stini so'raymiz. 
# for n in range(5): # range oraqli 5ta element yaratib olamiz va n ularning har biriga tenglab chiqamiz.
#     dostlar.append(input(f"{n+1}-ismini kiriting: ")) # dostlar ro'yxatiga .append() orqali input() ni qo'llagan holda 
# # foydalanuvchidan ro'yxatni to'ldirishini so'raymiz.
#     print(dostlar) # Va tayyor ro'yxatni konsolga chiqaramiz.
    
# dostlar = []
# print("Beshta eng yaqin do'stingiz kim? ")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-ismni kiriting: "))
# print(dostlar)

# AMALIYOT TOPSHIRIQLARI.
#1 - Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing.
# ismlar = ['abror', 'shodmon', 'bobur', 'dehqon', 'vali']
# for ism in ismlar:
#     print(f"Salom {ism.title()} ishlar yashiwimi.\n")
   
#2 - Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod 
# necha marta takrorlanganini yozing)
# ismlar = ['abror', 'shodmon', 'bobur', 'dehqon', 'vali']
# for ism in ismlar:
#     print(f"Salom {ism.title()} ishlar yashiwimi.\n")
# print(f"Kod {len(ismlar)} martaa takrorlandi.")

#3 - 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan
# konsolga chiqaring.
# t_sonlar = list(range(11,100,2))
# for son in t_sonlar:
#     print(f"{son}ning kubi {son**3}ga teng.")
    
#4 - Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling.
# Natijani konsolga chiqaring.
# kinolar = []
# print("Beshta eng yoqtirgan kinoingizni kiriting:")
# for  k in range(5):
#     kinolar.append(input(f"{k+1}-kinoni kiriting: "))
# print(f"Foydalanuvchi yoqtirgan kinolar ro'yxati: {kinolar}")

# kinolar = []
# print("Beshta eng yoqtirgan kinoingiz qaysi?")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kinoni kiriting!"))
# print(f"Foydalanuvchi kiritgan kinolar ro'yxati: {kinolar}")

#5 - Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan
# odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# soni = int(input("Bugun necha kishi bilan suhbat qurdingiz? ")) # INPUT orqali foydalanuvchidan nechta odam bilan 
# # suhbat qurganini aniqlaymiz va uni soni degan o'zgaruvchi yuklaymiz.
# ismlar = [] # Ismlar degan bo'sh ro'yxat yaratamiz.
# for n in range(soni): # FOR oraqli foydalanuvchi kiritgan son range o'zlashtirilishini taminlaymiz.
#     ismlar.append(input(f"{n+1}-suhbat qurgan odamingiz kim? ")) # Yuqoridagi foydalanuvchi kiritgan son aslida nechta
# # ism ro'qyxatga qo'shilishini aniqlaydi.
# print(ismlar) # Ro'yxatni konsolga chiqaramiz.

# soni = int(input("Bugun nechta odam bilan suhbat qurdingiz? "))
# ismlar = []
# for n in range(soni):
#     ismlar.append(input(f"{n+1}-ismni kiriting! ")) 
#     print(ismlar)
    
# 7 - DARS TUGADI.

# 8 - DARS.
# SHARTLAR VA TARMOQLANISH.
# TAQQOSLASH OPERATORLARI.
# Dastur tarmoqlanishi uchun, avvalo, biror shart bajarilishi kerak. Shart bajarilishini tekshirish uchun esa maxsus 
# taqqoslash operatorlari mavjud. Bu operatorlar yordamida biz o'zgaruvchilarning ma'lum qiymatga tengligini yoki,
# aksincha, teng emasligini yoxud ifodalarning natijasini berilgan qiymatdan katta yoki kichikligini va hokazo
# shartlarni tekshirib ko'rishimiz mumkin.
# Quyida Pythondagi taqqoslash operatorlarini ko'rib chiqamiz.

# == (Tenglik) a == b.
# != (Tengsizlik) a != b.
# < (Kichik) a < b.
# <= (Kichik yoki teng) a <= b.
# > (Katta) a > b.
# >= (Katta yoki teng) a >= b.

# Taqqoslash operatorlari mantiqiy qiymat qaytaradi (bool). Mantiqiy qiymatlar True (Shart bajarildi) yoki
# False (Shart bajarilmadi) bo'lishi mumkin.
# True ingliz tiladan (To'g'ri), False esa (Yolg'on) deb tarjima qilinadi. Quyida bir misol bilan buni mustaxkamlaymiz.
# a = 5
# b = 6
# print(a == b) # a teng(mi)? b ga. Natija False bo'ladi chunki teng emas.

# Yana bitta boshqacharoq misol ko'ramiz.
# a = 5
# b = 6
# print(a == (b - 1))

# Matnlarni va sonlarni taqqoslash usullari.
# print('anvar' == 'Anvar ') # Matnlarni taqqoslash.
# print(10**2<2**10) # Sonlarni taqqoslash.

# Taqqoslash qanday bajarilishini tushunish uchun quyidagi mashqlarni bajarib ko'ramiz.
# ism = 'anvar' # O'zgaruvchiga yuklandi.
# print(ism != 'Ahad') # ism da bosh harfli 'Ahad' teng emas kichik harfli 'ahad' ga (True) javob qaytadi.
# print(ism.title() == 'Ahad') # Bu yerda endi title() metodidan foydalandik va endi mantiqiy qiymat (False) ga teng bo'ladi.

# num1 = [1,2,3] # <- 1 - ro'yxat.
# num2 = [1,2,4] # <- 2 - ro'yxat.

# print(num1 != num2) # Ikkita ikki ro'yxatni teng emasligini so'rayapmi va bu (True) javob qaytaradi.
# print(9**2 >= 7*9+18) # 9 ning kvadrati (81) katta yoki teng ifodadan, hisoblasak ifoda ham (81) ga teng bo'ladi.
# Kelib chiqadiki (True) qiymat qaytaradi.

#x = 10 # <- x ni 10ga tengalab olamiz va uni turli ifodalar oraqali turli ifodalarga tenglashga urunib ko'ramiz.
# print(x*x < x**2) # 10 ko'paytirilgan 10ga va bu ifoda kichikmi 10 ning kvadratidan. (False) degan javob qaytaradi.
# print(x*x >= float(f"{x**2}")) # Bu yerda ham huddi shunday ifoda boshqacharoq talqinda. (True) qiymat qaytaradi.

# IF-ELSE OPERATORI.
# Avvalgi bo'limda biz turli ifodalarni  taqqoslashni o'rgandik, keling, endi taqqoslashning natijasiga ko'ra
# tarmoqlanishini ham ko'zdan kechiraylik. Buning uchun dasturlash tillarida maxsus "if" operatori mavjud. "if" so'zi 
# ingliz tilidan "agar" deb tarjima qilinadi va ma'lum bir shart qanoatlantirilishiga qarab shu shartga bog'langan
# kod ham bajariladi.
# son = int(input("Istalgan son kiriting: ")) # Foydalanuvchidan istalgan son kiriting deb so'raymiz.
# if son > 0: # "if" operatori orqali kiritilgan sonnig 0dan katta ekanini tekshiramiz. Bu qatorni "agar son 0 dan katta
# bo'lsa" deb o'qish mumkin.
    # print(son, "musbat son") # Bu qator "if" operatorining badani hisoblanadi va faqatgina yuqoridagi shart to'g'ri
# (True) bo'lsa, bajariladi.

# Agar yuqorida biz misol uchun: -10 sonini kiritganimizda kod bajarilmasdi va hech narsa konsolga chiqmasdi.
# Keling endi buni tekshirishimiz uchun yangi "else" operatori bilan tanishamiz."else" so'zi ingliz tiladan "aks holda"
# debn tarjima qilinadi va "if" operatorida bajarilgan shart qanoatlantirilmasa, "else" operatoridan keyingi kod
# bajariladi.

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 7: # Agar yosh 7dan kichik yoki 7ga teng bo'lsa.
#     print("Sizga aftobus bepul!")
# else: # Aks holda.
    # print("Sizga chipta 7000")
    
# Shart "badani" shartdan biroz o'nggasurib yozilgan har bir qator if/else shartining badani hisoblanadi.

# BIR QATOR IF-ELSE
# Qisqa kodlar uchun shart va uning badanini 1 qatorga jamlab yozishimiz ham mumkin. Agar shartimiz faqat "if" dan
# iborat bo'lsa, uning badanini keyingi qatordan emas, ikki nuqtadan keyin yozish kifoya.
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh > 65: print("Siz COVID-19 havf guruhida ekansiz.")

# Deylik kodimizda "if-else" birgalikda qatnashsa, "if" ning badani undan oldin, "else" ning badani esa keyin yoziladi:
# x, y = 50, 29 # x = 50, y = 29
# print("x < y") if x < y else print("x > y") # Shu ko'rinishta.

# MATNLARNI SOLISHTIRISH.
# Matnlarni solishtirish bu yana bir muhim jihatlardan biri, buni biz birorbir satda yangi akkaunt ochyotgan odam
# misolida ko'rishimiz mumkin.
# Matnlarni solishtirishdan avval ularni lower metodidan foydalangan holda bir hil ko'rinishga olib kelib olish
# maqsadga muvofiq bo'ladi.
#ism = 'Ali' # O'zgaruvchi misolida ko'ramiz.
#ism.lower() == 'ali' # Bu yerda biz bor o'zgaruvchini oldin bir ko'rinishga keltirib olyapmiz va endi natija (True).

# AMALIYOT TOPSHIRIQLARI.
#1 - Quyidagi dasturlarni Pythonda bajarib ko'ring.
#1
# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

#2        
# javob = float(input("12x6 nechiga teng? "))
# if javob != 72:
#     print("Javobingiz xato!")        
# else:
#     print("Siz to'g'ri javob berdingiz.")

#3
# yosh = int(input("Yoshingiz nechida? "))
# if yosh >= 18:
#     print("Xush kelibsiz!")
# else:
#     print("Sizga kirish mumkin emas!")

#4
# yil = int(input("Tug'ilgan yilingizni kiriting: ")) # Foydalanuvchidan tug'ilgan yilini so'raymiz.
# if 2024 - yil < 18: # Agar joriy yoldan foydalanuvchi tug'ilgan yilini ayirilganda hosil bo'qlgan qiymat 18dan kichik
# # bo'lsa.
#     print(f"Yoshingiz {2021-yil}da ekan.") # Bu yerda foydalanuvchi kiritkan yilga qarab uning yoshi aniqlanadi.
#     print("Kirishingiz mumkin emas.") # Shart bajarilsa shu habar chiqadi.
# else: # Aks holda.
#     print(f"Yoshingiz {2024-yil}da, Xus kelibsiz!") # Bu habar chiqariladi.

#5
# login = input("Yangi login kiriting: ")
# if len(login) <= 5: # login uzunligini tekshiramiz.
#     print("Login 5ta harfdan ko'proq bo'lishi shart!")
# else:
#     print("Login qabul qilindi.")


#2 - Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi
# harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling. 
# cars =  ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())
        
#3 - Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.   
# cars =  ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())
        
#4 - Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini
# ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga
# chiqaring.
# login = input("Yangi login kiriting: ")
# if login.lower() == 'admin':
#     print(f"Xush kelibsiz, {login.title()}. \nFoydalanuvhcilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Salom {login}, Xush kelibsiz!")

#5 - Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan
# yozuvni konsolga chiqaring.
# print("Iltimos ikkita son kiriting!") 
# son1 = int(input("Birinchi sonni kiriting: ")) 
# son2 = int(input("Ikkinchi sonni kiriting: ")) 
# if son1 == son2: 
#     print(f"{son1} va {son2} sonlari bir-biriga teng.") 
# else: 
#     print(f"{son1} va {son2} sonlari bir-biriga teng emas.")
     
#6 - Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat
# bo'lsa "Musbat son" degan xabarni chiqaring. 
# son = int(input("Istalgan son kiriting: "))
# if son < 0:
#     print(f"{son} soni manfiy")
# else:
#     print(f"{son} soni musbat")
    
#7 - Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
# son = float(input("Istalgan musbat son kiriting: "))
# if son < 0:
#     print("Musbat son kiriting!")
# else:
#     print(f"{son} ning ildizi {son**0.5}")

# 8 - DARS TUGADI.

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
a = True
b = False

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
    
#6 - Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan
# sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
son = float(input("Iltimos butun son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi!")