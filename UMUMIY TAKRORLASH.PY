# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:25:01 2024

@author: DavrServis
"""
# UMUMIY TAKRORLASH.

# 1-DARS
# BIRINCHI DASTURLAR.

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


# 3 - DARS.
# MATN (STRING).

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

# 4 - DARS.
# SONLAR.

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



# 5 - DARS.
# RO'YXATLAR.

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

# 10 - DARS. LUG'AT VA TO'PLAM.

# Lug'at bir obyektga bog'liq ma'lumotlarni kalit so'z va qiymat juftligi ko'rinishida saqalash imkonini beradi.
# Misol uchun, biz biror avtomobilga oid lug'at yaratishimiz va lug'atda shu avtomobilga tegishli barcha
# ma'lumotlarni saqlashimiz mumkin (avtomobilning nomi, rangi, yili, motori, narxi, va hokazo).

# Nima uchun bu ma'lumot turi lug'at deyilishini tushinish uchun oddiy lug'atga qaraylik. Odatda, lug'atdagi
# ma'lumotlar ikki qismdan iborat bo'ladi: KALIT SO'Z va IZOH (yoki TARJIMA). Xuddi oddiy lug'atlardagi kabi Python
# lug'atidagi ma'lumotlar ham ikki qismdan iborat bo'ladi: KALIT SO'Z va QIYMAT (ingliz tilida bu "KEY-VALUE PAIR"), 
# "KALIT-QIYMAT JUFTLIGI deyiladi."

# Dasturlashda ko'p ishlatiladigan atamalarni ingliz tilida yodlab qolish juda muhim! Bu sizga kelajakda yangi
# ma'lumotlar izlashda, xatolar ustida ishlashda, umuman ish faoliyatingizda ko'p asqatadi. Shuning uchun "veriable,
# integer, float, string, list, tuple, dictionary, function, loop, key, key, value" va boshqa atamalarning ma'nosini
# yaxshilab o'zlashtirib oling.

# Pythonda lug'at yaratish uchunkatta {jingalak} qavsdan foydalanamiz. Qavs ichida har bir element uchun kalit so'z
# va qiymat beramiz. Ularning orasi ikki nuqta (:) bilan, har bir element (juftlik) esa vergul (,) bilan ajratiladi.
# car = {'model':'ferrari', 'rang':'qizil'}
# print(car)  

# Yuqorida car degan lug'at yaratdik. Lug'atda 2ta element bor: mashinaning modeli (ferrari) va rangi (qixzil).
# Bu yerda 'model' va 'rang'kalit so'zlar, 'ferrari' va 'qizil' esa mos kelivchi kalit so'zlarning qiymatlaridir.

# Lug'at ichidagi kalitlar takrorlanmasligi kerak. Agar lug'at yaratishda kalit so'zlar takrorlans, ulardan faqat
# oxirgisining qiymati saqlanib qoladi. 
        
# LUG'AT BILAN ISHLASH.
# Lug'atdagi biror elementni ko'rish uchun unga kalit so'z orqali murojaat qilamiz.
# car = {'model':'ferrari', 'rang':'qizil'} # oddiy lug'at yaratib olamiz.
# print(car['model']) # konsolga mashina modeli ni chiqaramiz.
# # ferrari
# print(car['rang']) # konsolga mashina rangi ni chiqaramiz.
# # qizil

# Lug'atdagi qiymatlar son (int, float), matn (string), ro'yxat (list, tuple), hattoboshqa lug'at ham bo'lishi mumkin.
# talaba = {'ism_sh':'murod nazarov', 'yosh': 20, 't_yil': 2000}
# print(f"{talaba['ism_sh'].title()},{talaba['t_yil']}-yilda tug'ilgan,{talaba['yosh']} yoshda.") 
     
# Uzun lug'atlarni bir necha qatorga bo'lib yozishimiz mumkin. Bunda har bir element alohida qatordan yoziladi va
# qator oxirida vergul qo'yilib, yangi qatorga o'tiladi.
# car = {
#      "make":"GM",
#      "model":"Malibu",
#      "color":"Black",
#      "gear":"Automatic",
#      "year":"2020",
#      "price":"40000"
#      }  
# print(car)

# get() METODI.
# Yuqorida biz lug'at elementiga kalit so'z orqali murojaat etishni o'rgandik.
# print(car['model'])
# Malibu

# Bu usulni kamchiligi shundaki, agar lug'atda siz so'ragan kalit topilmasa, dastur KEYERROR xatoligi bilan to'htab
# qoladi.
# print(car['narx'])
# KeyError 'narx'

# Lug'atda 'narx' kalit so'zi bo'lmagani uchun yuqoridagi kod KEYERROR degan xatoni qaytardi.
# Hozir get() metodi yordamida lug'atga murojaat etish va mavjud bo'lmagan kalitning o'rniga biror xabar qaytarishni
# ko'rib chiqaylik.
# narx = car.get('narx', 'Bunday kalit mavjud emas!')

# Yuqoridagi lug'at nomidan so'ng .get() metodini yozdik, argumentlar sifatida kelit so'z ('narx') va kalit mavjud
# bo'lmaganida chiqadigan xabarni yozdik ('Bunday kalit mavjud emas').
# print(narx)

# Agar .get() metodida ikkinchi argumentni tashlab ketsangiz va siz so'ragan kalit mavjud bo'lmasa, .get() metodi
# NONE qiymatini qaytaradi.
# narx = car.get('narx')
# print(narx)
# None

# None, qiymat mavjud emas degan ma'noni beradi.

# YANGI JUFTLIK QO'SHISH.
# Lug'atda yangi element (kalit so'z va qiymatlar =) qo'shishimiz ham mumkin. Keling, yuqoridagi talaba nomli
# lug'atga yana 2ta yangi - kurs va fakultet nomli kalit so'zlar va qiymatlar qo'shamiz:
# talaba['kurs'] = 4
# talaba['fakultet'] = 'informatika'
# Lug'atni konsolga chiqarib ko'ramiz:
# print(talaba)

# BO'SH LUG'AT.
# Bazida dastur boshida bo'sh lug'at yaratib, dastur davomida lug'atga yangi ma'lumotlar kiritib borish talab
# qilinishi mumkin. Bunday holatda bo'sh lug'at quyidagicha yaratiladi:
# car = {}

# Dastur davomida esa lug'atga qiymatlar kiritilib borilishi mumkin:
# car['model'] = 'Mazda 6' # Bu usul orqali yangi bo'sh lug'atga elementlar qo'shamiz.
# car['color'] = 'Red'
# car['price'] = 40000
# print(f"{car['color']} {car['model']}, {car['price']}$")
# Lug'atda kalit so'zlar qanday ketma-ketlikda kiritilsa, shu tartib saqlanib qoladi.

# QIYMATNI O'ZGARTIRISH.
# Biror kalit so'zga tegishli qiymatni o'zgartirish esa quyidagicha amalga oshiriladi:
# car['price'] = 38000
# print(f"{car['color']} {car['model']}, {car['price']}$")

# KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH.
# Lug'atda elementlarning DEL operatori yordamida o'chiramiz:
# car = {'model':'Malibu', 'color':'Red', 'price': 40000} # Oddiy lug'at.
# print(car) # Konsolga chiqaramiz.
# del car['color'] # DEL yordamida 'color' elementini o'chirami bu holatda kalit so'z ham qiymat ham o'chib ketadi.
# print(car) # Natijani konsolga chiqaramiz.

# AMALIYOT TOPSHIRIQLARI.
#1 - otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot
# kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga
# chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# otam = {
#         'ism_sh':'Yorqinjon Maksimov',
#         't_yil': 1970,
#         'yoshi':54,
#         'millati':"o'zbek"
#         }
# onam = {
#         'ism_sh':'Naziraxon Maksimova',
#         't_yil': 1977,
#         'yoshi':47,
#         'millati':"o'zbek"
#         }
# akam = {
#         'ism_sh':'Mamatoji Abdurashidov',
#         't_yil': 1995,
#         'yoshi':29,
#         'millati':"o'zbek"
#         }
# ayolim = {
#         'ism_sh':'Mavludaxon Abdurashidova',
#         't_yil': 2003,
#         'yoshi':21,
#         'millati':"o'zbek"
#         }
# print(f"Mening dadam {otam['ism_sh']}, {otam['t_yil']}-yilda tug'ilgan va yoshi {otam['yoshi']}da millati {otam['millati']}.\n")
# print(f"Mening dadam {onam['ism_sh']}, {onam['t_yil']}-yilda tug'ilgan va yoshi {onam['yoshi']}da millati {onam['millati']}.\n")

#2 - Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# s_taomlar = {
#     'men':'shirguruch',
#     'ayolim':'sho\'rva',
#     'onam':'mastava',
#     'otam':'farqi yo\'q'
#     }
# print(f"Mening sevimli taomim {s_taomlar['men']},\n Ayolimning sevimli taomi {s_taomlar['ayolim']},\n\
#       Onamning sevimli taomlari {s_taomlar['onam']},\n Dadamga bo'lsa {s_taomlar['otam']}.")
      
#3 - Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
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

#4 - Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
# print("Lug'atimizda quyidagi elementlar bor (int, float, string, list, tuple, bool, dict, for, in, not in, if) \
# sizga qaysinisi haqida ma'lumot kerak?'\n")
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
# soz = input("Yuqoridagi lug'atdan istalgan malumot turini kiriting: ")
# print(python.get(soz, "Bunday ma'lumot turi yo'q!"))

#5 - Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
# print("Lug'atimizda quyidagi elementlar bor (int, float, string, list, tuple, bool, dict, for, in, not in, if) \
# sizga qaysinisi haqida ma'lumot kerak?'\n")
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


# soz = input("Yuqoridagi lug'atdan istalgan ma'lumot turini kiriting: ")
# tarjima = python.get(soz)
# if tarjima == None:
#     print("Lug'atimizda bunday so'z yo'q!")
# else:
#     print(f"Siz so'ragan {soz} soz'ining ma'nosi {tarjima}.")

# 10 - DARS TUGADI.

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

# 12 - DARS.
# TO'PLAMLAR.

# Pythonda to'plam (set) yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta elementlarmni saqlashda
# qo'llaniladi. 
# To'plam yaratish uchunha lug'atlardagi kabi katta (jingalak) qavsdan foydalanamiz.
# sonlar = {1,2,3}
# print(sonlar)

# ismlar ={"Alijon", "Valijon", "Boqijon"}
# print(ismlar)
# To'plam bir xil elementni saqlamaydi.

# sonlar = {1,2,2,3,4,5,1,1,9} # Bir hil sonlar ishtirok etkan to'plam.
# print(sonlar) # Natija esa butkul boshqacha bo'ladi.

# ETIBOR BERING! Yuqoridagi kodning 1 - qatorida biz 3, 4 va 5 qiymatlarini 2 martadan takrorlab yozganimizga
# qaramay, to'plam ichida bu sonlar bir martadan saqlandi, xolos.
# Bo'shto'plam yaratish uchun set() funksiyasidan foydalanamiz:
# a = set() # Bo'sh to'plam yaratildi.

# Ro'yxatdan farqli o'laroq, set ichidagi elementlar biror tartibda saqlanmaydi va ularga indeks orqali murojaat qilib
# bo'lmaydi.
# sonlar = {1,2,3,4,5,6} # Oddiy to'plam.
# print(sonlar[0]) # Yuqoridagi to'plamni 1 - elementini chaqirishga urunsak. Xatolik beradi.

# Avvalgi bo'limda ko'rganimizdek, to'plamlar biror ro'yxatdan qaytarilgan elementlarni o'chirib tashlash uchun
# juda qulay:
# mevalar = ['olma', 'anjir', 'olma', 'uzum', 'olma', 'uzum'] # Elementlar bir necha bor qaytarilgan ro'yxat. 
# mevalar = set(mevalar) # Mevalar ro'yxatimizni set() ga o'zgartirdik.
# print(mevalar) # Bu ro'yxatni set() orqali konsolga chiqarsak barcha qaytarilgan elementlardan faqat bittadan 
# element qoldi.

# Yuqoridagi misolda mevalar ro'yxatida olma va uzum bir necha bor takrorlangan edi, biz set() funksiyasi yordamida 
# ro'yxatni to'plamga o'zgartirdik va ortiqcha elementlardan xolos bo'ldik.
# Agar to'plamni yana ro'yxatga o'tkazish talab qilinsa, list() funksiyasiga murojaat qilamiz:
# mevalar = list(mevalar) # Qaytadan mevalar ro'yxatimizni asl holiga qaytaramiz.
# print(mevalar) # Natija.

# TO'PLAMGA ELEMENT QO'SHISH.
# To'plamga yagona element qo'shish uchun .add() metodidan, bir nechta element qo'shish uchun esa .update() 
# metodidan foydalanamiz.
# mevalar = {'anjir', 'olma', 'uzum'} # Oddiy to'plam yaratib olamiz.
# mevalar.add('banan') # Bittagina element qo'shamiz.
# print(mevalar) # Natijani chiqaramiz.

# mevalar.update(['anor', 'qovun']) # To'plamimizga bir nechta element qo'shamiz.
# print(mevalar) # Natijani ko'ramiz.

# .update() metodidan foydalanganda parametr sifatida ro'yxat yoki lug'at uzatishimiz mumkin.

# TO'PLAMDAN ELEMENT O'CHIRISH.
# To'plamdan element o'chirish uchun .discard() va .remove() metodlari mavjud.
# mevalar = {'olma', 'banan', 'anjir', 'olma', 'uzum', 'olma', 'uzum'} # Oddiy to'plam.
# mevalar.discard('anjir') # .discard() metodi orqali bitta elementni o'chiramiz.
# print(mevalar) # Natija.

# mevalar.remove('banan') # .remove() metodi orqali bitta elementni o'chiramiz.
# print(mevalar) # Natija

# Yuqoridagi ikki metod bir vazifani bajaradi, ularning o'rtasidagi farq shundaki, agar biz o'chirmoqchi bo'lgan
# element to'plamda mavjud bo'lmasa .remove() metodi xato qaytaradi, .discard() esa xato qaytarmaydi.
# sonlar = {1,2,3,4,5,6} # Sonlar to'plami.
# sonlar.remove(7) # Yo'q sonni kiritkanimiz uchun xato qaytaradi.

# sonlar = {1,2,3,4,5,6} # Sonlar to'plami.
# sonlar.discard(7) # Yuqoridagi natijadan farqli o'laroq bunda xato qaytarmaydi.

# To'plamdan element o'chirishning (sug'urib olishning) yana bir usuli .pop() metodidir. Lekin to'plam elementlari
# indeksi mavjid bo'lmagani sababli .pop() metodi to'plamdan tasodifiy elementni sug'urib oladi:
# sonlar = {1,2,3,4,5,6,7} # Oddiy to'plam.
# son = sonlar.pop() # .pop() metodi orqali to'plamimizdan tasodifiy raqamni o'chiramiz (Sug'urib olamiz).
# print(son) # Natija.

# TO'PLAMALAR USTIDA AMALLAR.
# To'plamalar matematikada ham keng qo'llanilgani uchun ularning ustida  o'ziga xos matematik amallar bajarish mumkin.
# Misol uchun, ikki to'plamni birlashtirish uchun | operatori yoki .union() metodidan foydalanamiz.
# A = {1,2,3,4} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# B = {3,4,5,6} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# C = A|B # Endi ularni | operatori yordamida birlashtiramiz.
# print(C) # Natijani ko'ramiz.

# A = {1,2,3,4} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# B = {3,4,5,6} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# D = A.union(B) # Endi ularni .union() metodi bilan birlashtiramiz.
# print(D) # Natija.

# Ikki to'plamning kesishmasini (bir xil elementlarini) topish uchun esa & operatori yoki .intersection() metodidan
# foydalanamiz:
# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# c = a&b # Endi ularni & operatori orqali ikki to'plamning bir xil elementlarini topamiz.
# print(c) # Natija.

# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# d = a.intersection(b) # .intersection() metodi yordamida ikki to'plamning bir xil elementlarini topamiz.
# print(d) # Natija.

# Ikki to'plam o'rtasidagi farqni topish uchun esa ayirish (-) operatori yoki .difference metodidan foydalanamiz.
# B to'plamning A to'plamdan farqi deganda (A-B) Ato'plamga kiruvchi, lekin B to'plamda yo'q elementlar tushuniladi.
# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# print(a-b) # Natija a-b yani aytib o'tkanimizday a da bor b da esa yo'q elementlar tushuniladi.

# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# print(b.difference(a)) # Natija, endi esa b da bor a da esa yoq elementlar chiqadi.

# To'plamlar o'rtasidagi simmetrik farqni topish uchun ^ operatori yoki .symmetric_difference() metodidan foydalanamiz.
# Simmetrik farq deb A va B to'plamga kiradigan, lekin bir vaqtda ikkalasiga kirmaydigan elementlar tushuniladi.
# Quyidagi misolda {3,4} elementlari ikkala to'plamda bo'lgani uchun simmetrik farqqa kirmaydi.
# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# c = a^b
# print(c)

# a = {1,2,3,4,5} # 1 - Oddiy raqamlar to'plamini yaratib olamiz.
# b = {3,4,5,6,7} # 2 - Oddiy raqamlar to'plamini yaratib olamiz.
# d = a.symmetric_difference(b)
# print(d)

# AMALIYOT TOPSHIRIQLARI.
#1 - uch xil ranglar saqlangan to'plam yarating.
# colors = {'sariq', 'qizil', 'qora'}
# print(colors)

#2 - To'plamga .add() va .update() metodlari yordamida ranglar qo'shing.
# colors.add('yashil')
# colors.update(['kumush', 'binafsha'])
# print(colors)

#3 - Quyidagi ikki to'plam uchun umumiy elementlarni ajratib olib, yangi to'plam yarating:
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# set3 = set1 & set2
# print(set3)

#4 - Yuqoridagi ikki to'plam orasidagi farqlarni konsolga chiqaring.
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# set3 = set1 - set2
# print(set3)
# set4 = set2 - set1
# print(set4)

#5 - Ikki to'plam orasidagi simmetrik farqni toping.
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# set3 = set1 ^ set2
# print(set3)

#6 - Sizdaquyidagi ro'yxat bor:
# bozorlik = ['choy', 'non', 'kortoshka', 'tuxum', 'sut']
# mahsulotlar = ['non', 'sut', 'tuxum', 'olma', 'un', 'tuz']
# bozorlik - siz sotib olishingiz kerak bo'lgan narsalar;
# mahsulotlar - do'kondagi mavjud mahsulotlar.

#7 - Sotib olishingiz kerak bo'lgan mahsulotlarning qay biri do'konda bor ekanini alohida ro'yxat (list) saqlang.
# obm = []
# for n in bozorlik:
#     if n in mahsulotlar:
#         obm.append(n)
# print(f"Do'konda bor mahsulotlar quyidagilar: {obm}")
        
#8 - Do'konda mavjud bo'lmagan mahsulotlar ro'yxatini yarating.
# dmbm = []
# for n in bozorlik:
#     if n not in mahsulotlar:
#         dmbm.append(n)
# print(f"Do'konda mavjud bo'lmagan mahsulotlar quyidagilar: {dmbm}")
 
#9 - Do'kon egasi siz so'ragan mahsulotlarni olib keldi. Mahsulotlar ro'yxatiga yangi mahsulotlarni qo'shing.
# mahsulotlar.append('choy')
# mahsulotlar.append('kortoshka')
# print(mahsulotlar)

# 12 - DARS TUGADI.

# 13 - DARS.
# NESTING.

# Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yo boshqa lug'atni yoki, aksincha, ro'yxat ichida
# lug'atni saqlash ham qo'l kelishi mumkin. Bu ingliz tilida NESTING deyiladi. Nesting Pythondagi foydali
# xususiyatlardan biridir. Kelin, bunga bir nechta misollarni ko'rib chiqamiz.

# LUG'ATLAR RO'YXATI.
# Biz avvalgi darsimizda talabarning ma'lumotlarni lug'at shaklida saqlashni ko'rgan edik. Shunday talabalardan yuzlab bo'lganda
# ularning har biriga alohida lug'at qilishimiz tabiiy, lekin bu lug'atlar bilan ishlash qiyinchilik tug'dirishi mumkin.
# Shunday holatda barcha lug'atlarni (talabalarni) bitta ro'yxatga joylab, ular ustida turli amallar bajarish mumkin.

# Quyidagi misolda 3ta alohida lug'atda 3ta avtomobil haqida ma'lumotlar saqlangan:
# car0 = {
#         'model':'jentra', 'rang':'qora',
#         'yil':2018, 'narx':13000,
#         'km':50000, 'korobka':'avtomat'
#         }
# car1 = {
#         'model':'cobalt', 'rang':'oq',
#         'yil':2020, 'narx':15000,
#         'km':62000, 'korobka':'avtomat'
#         }
# car2 = {
#         'model':'nexia3', 'rang':'qizil',
#         'yil':2021, 'narx':12500,
#         'km':5760, 'korobka':'mexanika'
#         }
# Agar biz har bir avtomobil haqida ma'lumot olmoqchi bo'lsak, har bir lug'atga alohida murojaat etishimiz talab qilinadi:
# car = car0
# print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narx']}$")
# car = car1
# print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narx']}$")
# car = car2
# print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narx']}$")

# Yuqoridagi natijani chiqarishning osonroq usuli barcha avtolarni bitta ro'yxarga joylab, for siklidan foydalanishdir:
# cars = [car0,car1,car2] # Lug'atlar ro'yxati.
# for car in cars:
#     print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}-yil, {car['narx']}$")
# Ishimiz birmuncha yengillashdi, kodimiz ham qisqardi.
# Natija esa bir xil.

# Ro'yxat ichidagi istalgan lug'atga indeks bo'yicha murojaat etishimiz ham mumkin (lug'at nomini yodlab qolish ham shart emas).
# print(cars[0])

# Biror lug'atdagi elementga murojaat qilish uchun esa quyidagi usuldan foydalanishimiz mumkin:
# print(cars[0] ['model'])

# print(f"{cars[2]['rang'].title()}"
#       f" {cars[2]['model'].title()}")

# for sikli orqali biz bo'sh lug'atlar ro'yxatini ham yaratib olishimiz mumkin:
# malibus = [] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik.
# for n in range(10): # Range orqali 10 element yaratib olamiz va n ni ularning har biriga tenglaymiz.
#     n = { # Har bir n ni lug'at shakliga keltirib olamiz.
#         'model':'malibu',
#         'rang':None,
#         'yil':2024,
#         'narx':None,
#         'km':0,
#         'korobka':'avto'
#                 } 
#     malibus.append(n) # Yuqoridagi lug'atni ro'yxatga qo'shamiz.
# # Yuqoridagi misolda biz 10ta Malibu mashinasidan iborat ro'yxat tuzdik. ETIBOR QILING, 'rang' kalitiga qiymat bermadik va None 
# # deb qoldirdik.
# # Endi ishlab chiqarish jarayonida mashinalarga turli ranglarni berishimiz mumkin. Misol uchun, birinchi 3ta mashinaga qizil rang
# # beramiz:
# for malibu in malibus[:3]: # Malibus ro'yxatidagi birinchi 3ta Malibu uchun:
#     malibu['rang'] = 'qizil' # Rngini qizil qilgin.
# # Keyingi 3tasiga qora:
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'

# # Oxirgi 4ta Malibuni rangini qora, korobkasini esa mexanika qilamiz:
# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['korobka'] = 'mexanika'
    
# # Kelin endi mashinalarni korobkasidan kelib chiqqan holda narx belgilaymiz:
# for malibu in malibus: # Malibus ro'yxatidagi har bir Malibu uchun:
#     if malibu['korobka'] == 'avto': # Agar korobkasi avtomat bo'lsa.
#         malibu['narx'] = 40000 # Narxi 40000$ bo'lsin.
#     else:
#         malibu['narx'] = 35000
# # Mashinalar ro'yxatini konsolga chiqaramiz.
# for malibu in malibus:# Malibus ro'yxatidagi har bir Malibu uchun:
#     print(malibu.values()) # Har bir Malibuni qiymatlarini konsolga chiqargin. Va biz shuncha yozgan kodlarimiz natijasini ko'ramiz.
    
# LUG'AT ICHIDA RO'YXAT.
# Bir kalitga bir nechta qiymatlar berish talab qilinganda qiymatlarni ro'yxat ko'rinishida yozish o'rinlidir. Misol uchun,
# bir tashkilotda bir nechta tashkilotda bir nechta dasturchilar ishlaydi va har bir dasturchi turli dasturlash tillarini biladi.
# Keling, dasturchilar lug'atini tuzamiz va har bir dasturchi haqidagi ma'lumotni konsolga chiqaramiz:
# dasturchilar = {
#     'ali':['python', 'c++'],
#     'vali':['html', 'css'],
#     'hasan':['php', 'sql'],
#     'husan':['python', 'php'],
#     'maryam':['c++', 'c#']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()}: ", end='')
#     for til in tillar:
#         print(f"{til.upper()} ", end='')

# print() funksiyasi har bir matndan so'ng yangi qator tashlaydi. Buning oldini olish uchun quyidagi usuldan foydalanish mumkin:
# print(string, end='') 

# LUG'AT ICHIDA LUG'AT.
# Bunday qilish tavsiya qilinmaydi, istisno holatlarda lug'at ichidagi qiymatlarni lug'at ko'rinishida ham saqlash mumkin.
# Misol uchun, ish joyingizdagi hamkasblaringiz haqidagi ma'lumotlarni saqlashda hamkasblaringizning ismi kalit, u haqidagi
# ma'lumotlar esa lug'at ko'rinishida berilishi mumkin.

# hamkasblar = {
#     'ali':{
#         'familya':'valiyev',
#         'tyil':1995,
#         'malumot':'oliy',
#         'tillar':['python','c++']
#         },
#     'vali':{
#         'familya':'aliyev',
#         'tyil':2000,
#         'malumot':'orta',
#         'tillar':['html','css']
#         },
#     'hasan':{
#         'familya':'husanov',
#         'tyil':1998,
#         'malumot':'oliy',
#         'tillar':['python','php']
#         }
#     }
# print(hamkasblar)

# # Hamkasblar to'g'risidagi ma'lumotlarni esa quyidagicha ko'rish mumkin:
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan.\n"
#           f"Malumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi: ")
#     for til in info['tillar']:
#         print(til.upper())
        
# Lug'at ichidagi lug'atlar bir xil tuzilishga ega bo'lgani ishingizni ancha yengillashtiradi, aks hold, kodingiz murakkablashib
# ketishi mumkin.

# AMALIYOT TOPSHIRIQLARI:
#1 - Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
# buxoriy = {
#         'ism':'Abu Abduloloh Muhammad ibn Ismoil',
#         'tyil':810,
#         'tjoy':'buxoro',
#         'vyil':870
#         }
# qodiriy = {
#         'ism':'Abdulla Qodiriy',
#         'tyil':1894,
#         'tjoy':'toshkent',
#         'vyil':1938
#         }
# vohidov = {
#         'ism':'Erkin Vohidov',
#         'tyil':1936,
#         'tjoy':'fargona',
#         'vyil':2016
#         }
# navoiy = {
#         'ism':'Alisher Navoiy',
#         'tyil':1441,
#         'tjoy':'xirot',
#         'vyil':1501
#         }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"\n{ism} {tyil}-yilda {tjoy.title()}da tug'ilgan, "
#           f"{vyil - tyil} yil umr ko'rgan."
#           )
#2 - Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va
# uning asarlarini konsolga chiqaring.
# buxoriy = {
#         'ism':'Abu Abduloloh Muhammad ibn Ismoil',
#         'tyil':810,
#         'tjoy':'buxoro',
#         'vyil':870,
#         'asarlari':['al-jome as-sahih', 'al-adab al-mufrad', 'at-tarix al-kabir', 'at-tarix as-sag\'ir']
#         }
# qodiriy = {
#         'ism':'Abdulla Qodiriy',
#         'tyil':1894,
#         'tjoy':'toshkent',
#         'vyil':1938,
#         'asarlari':['o\'tkan kunlar', 'mehrobdan chayon', 'obid ketmon']
#         }
# vohidov = {
#         'ism':'Erkin Vohidov',
#         'tyil':1936,
#         'tjoy':'fargona',
#         'vyil':2016,
#         'asarlari':['tong nafasi', 'qo\'shiqlarim sizga', 'o\'zbegim', 'qiziquvchan matmusa']
#         }
# navoiy = {
#         'ism':'Alisher Navoiy',
#         'tyil':1441,
#         'tjoy':'xirot',
#         'vyil':1501,
#         'asarlari':['xamsa', 'lison ut-tayr', 'mahbub al-qulub', 'munojot']
#         }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"\n{ism}ning sevimli asarlari quyidagilar:")
#     for asar in shaxs['asarlari']:
#         print(f"{asar.title()}")
        
#3 - Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli
# kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
# kinolar = {
#     'abdurahmon':['shapka', 'oltin devor', 'sevgi'],
#     'nurulloh':['king kong', 'omar va xanna', 'qasoskorlar'],
#     'mavluda':['shabnam', 'om shanti om', 'baxt']
#     }
# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino.title())
#4 - Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
# Har bir davlat haqida ma'lumotni konsolga chiqaring.
# davlatlar = {
#     'aqsh':{
#         'poytaxti':'vashington',
#         'axolisi': 327000000,
#         'maydoni': '9631418 kv.km',
#         'pul birligi':"dollar"
#         },
#     'rossiya':{
#         'poytaxti':'moskva',
#         'axolisi': 144000000,
#         'maydoni': '17098246 kv.km',
#         'pul birligi':"rubl"
#         },
#     "o'zbekiston":{
#         'poytaxti':'toshkent',
#         'axolisi': 33000000,
#         'maydoni': '448978 kv.km',
#         'pul birligi':"so'm"
#         }
#     }
# for davlat, info in davlatlar.items():
#     print(f"\n{davlat.title()}ning poytaxti {info['poytaxti'].title()}")
#     print(f"Axolisi: {info['axolisi']}")
#     print(f"Maydoni: {info['maydoni']}")
#     print(f"Pul birligi: {info['pul birligi']}")
    
#5 - Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot
# bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
# davlatlar = {
#     'aqsh':{
#         'poytaxti':'vashington',
#         'axolisi': 327000000,
#         'maydoni': '9631418 kv.km',
#         'pul birligi':"dollar"
#         },
#     'rossiya':{
#         'poytaxti':'moskva',
#         'axolisi': 144000000,
#         'maydoni': '17098246 kv.km',
#         'pul birligi':"rubl"
#         },
#     "o'zbekiston":{
#         'poytaxti':'toshkent',
#         'axolisi': 33000000,
#         'maydoni': '448978 kv.km',
#         'pul birligi':"so'm"
#         }
#     }
# print("Biz 3ta davlat haqidagi ma'lumotlarni jamlaganmiz: AQSH, ROSSIYA, O'ZBEKISTON")
# davlat = input("Iltimos davlat nomini kiriting: ").lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.upper()}ning poytaxti {info['poytaxti'].title()}")
#     print(f"Axolisi: {info['axolisi']}")
#     print(f"Maydoni: {info['maydoni']}")
#     print(f"Pul birligi: {info['pul birligi']}")
# else:
#     print(f"Bizda {davlat} haqida ma'lumot yo'q!")

# 13 - DARS TUGADI.

# 14 - DARS.
# WHILE SIKLI.

# Biz 3 - bobda for sikli yoerdamida kodning ma'lum qismini bir necha bor takrorlashni o'rgangan edik. Ushbu bobda esa while sikli
# bilan tanishamiz. Bu ikkisining o'rtasidagi farq shudaki, for siklining takrorlanishi biror ro'yxat (lug'at, to'plam) elementlari soniga
# bog'langan bo'lsa, WHILE siklining takrorlanishi biror shartning qanoatlanishiga bo'g'langan bo'ladi.

# WHILE so'zi ingliz tilidan "toki" deb tarjima qilinadi.

# WHILE QANDAY ISHLAYDI?
# WHILE sikli badanidagi kodning necha marta takrorlanishi biror shartga bog'langan bo'ladi. Tushunarli bo'lishi uchun qiyidagi misolni
# ko'zdan kechiramiz:
# son = 1 
# while son <= 5: # TOKI son 5dan kichik yoki teng ekan....
#     print(son, end=' ') # sonni konsolga chiqaramiz va 
#     son = son + 1 # songa 1ni qo'shamiz.
# Yuqoridagi dasturni tahli qilamiz:
#   1 - qatorda. Avval son degan o'zgaruvchi yaratdik va unga 1 qiymatini berdik.
#   2 - qatorda. "Toki son 5dan kichik yoki teng ekan" keyingi qatorda bajar dedik.
#   3 - qatorda. Sonni konsolga chiqardik.
#   4 - qatorda. Songa 1 qo'shdik.
# 4 - qatordan so'ng kod yana 2 - qatorga qaytadi va son <= 5 shartini tekshiradi, agar shart bajarilsa (True), 3 - 4 qatorlar
# takrorlanadi.
# 5 - qadamdan so'ng son = 5 bo'lganida while sikli to'htaydi.

# Pythonda += operatori bor. Bu operator o'ng tarafdagi qiymatni chap tarafdagi qiymatga qo'shadi. Misol uchun, son = son + 1
# ifodasini son += deb yozdik.

# WHILE va INPUT().
# WHILE sikli yordamida dasturni to'xtatish imkoniyatini foydalanuvchiga berishimiz mumkin.
# print("Kiritilgan sonning kvadratini hisoblovchi dastur. ")
# savol = "Istalgan soningizni kiriting"
# savol += ("Dasturni to'xtatish uchu 'exit' deb yozing!")
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
    
#     if qiymat != 'exit':
#         print(f"{qiymat} ning kvadrati {float(qiymat)**2} ga teng!")
# Yuqoridagi dastur toki foydalanuvchu 'EXIT' deb yozmaguniga qadar takrorlanaveradi.

# ISHORA - FLAG/
# Yuqoridagi misolda dasturni to'xtatish uchun yagona shartni tekshirdik (qiymat != 'exit). Katta dasturlarda bir shartni emas,
# bir nechta shartlarni tekshirish  va ulardan biri bajarilgan taqdirda dasturni to'xtatish talab qilinishi mumkin.
# Bunday holatlarda biror o'zgaruvchidan ishora (flag) sifatida foydalanishimiz mumkin. Agar dastur bajarilishi davomida dasturni
# to'xtatish shartlaridan biri bajarilganda ishora o'zgaruvchining qiymatini o'zgartiramiz va dastur o'z-o'zidan to'xtaydi.

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting " # Foydalanuvchiga habar.
# savol += ("To'xtatish uchun 'exit' deb yozing!") # Yuqoridagi habarga qo'shimcha (+=) ishorasi orqali qo'shilgan.
# ishora = 1 # Ishorani 1ga yani True gatenglab olamiz. 
# while ishora: # Toki ishora = True (1) ekan.
#     qiymat = input(savol) # Yangi qiymat degan o'zgaruvchi, va unga input orqali foydalanuvchiga yuzlanyapmiz.
#     if qiymat == 'exit': # Agar foydalanuvchi 'exit' deb yozadigan bo'lsa sodda qilib aytganda.
#         ishora = 0 # Ishorani 0ga yani False ga tenglagin (va bu holatda dasturdan chiqib ketiladi shartlar bajarilmaydi.)
#     else: # Aks holda 
#         print(f"{qiymat} ning kvadrati, {float(qiymat)**2} ga teng!") # Kiritilgan sonni kvadratini hisobla.

# BREAK OPERATORI.
# BREAK operatori yordamida sikl bajarilishini saikl badanidan to'xtatishimiz mumkin. Ya'ni sikl to'xtashi WHILE dan so'ng
# yozilgan shartga emas, sikl ichidagi boshqa shartga bog'lanishi mumkin:
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur!") # Foydalanuvchi uchun ma'lumot.
# savol = "Istalgan soningizni kiriting!" # Savol degan yangi o'zgaruvchiga foydalanuvchi qilishi mumkin bo'lgan ishni yozdik.
# savol += ("Dasturni to'xtatish uchun 'exit' deb yozing! ") # Dasturni tugatish uchun foydalanuvchi qilishi kerak bo'lgan amal.

# while True: # Abadiy sikl. # Siklni boshladik 
#     qiymat = input(savol) # Yangi qiymat degan o'zgaruvchiga yuqoridagi birlashtirilgan savolni yuklaymiz va input orqali
# # foydalanuvchiga taqdim qilamiz.
#     if qiymat == 'exit': # Agar qiymat 'exit' ga teklansa 
#         break # Dasturni to'htatish.
#     else: # Aks holda.
#         print("{qiymat} ning kvadrati, {float(qiymat)**2}") # Kiritilgan qiymatni kvadratini hisoblash uchun kod.
# print("Dastur tugadi!") # Foydalanuvchi tomonidan 'exit' deb yozilganda dastur tugagani haqidagi habar.

# BREAK operatori for siklini to'xtatish uchun ham ishlatiladi:
# sonlar = list(range(1,11)) # Range oraqli yangi list ro'yxat (1dan 10gacha) yaratib olamiz.
# for son in sonlar: # Sonlar ichidagi har bir son uchun.
#     if son == 5: # Agar son 5ga teng bo'lsa.
#         break # Dasturni to'htatkin.
#     print(f"{son} ning kvadrati {son**2}") # Yo'q bo'lsa shu kodni bajar.
    
# Sikl ichida bir nechta break operatorlari bo'lishi mumkin.
    
# CONTINUE OPERATORI.
# CONTINUE operatori esa, aksincha, ma'lum bir shart bajarilganda qadam tashlab o'tish uchun mo'ljallangan
# (operator qo'yilgan o'sha qadamni tashlab o'tib ketadi.)
# sonlar = list(range(1,11)) # 1dab 11gacha (11 kirmaydi) sonlar ro'yxati tuzdik.
# for son in sonlar: # sonlar ichidagi har bir son uchun.
#     if son == 5: # Agar son 5ga teng bo'lsa.
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")
    
# Natijaga e'tibor bering, son 5ga teng bo'lganda siklimiz 1 qadam tashlab o'tib ketdi va 5 ning kvadratini konsolga chiqarmadi:
    
# WHILE sikliga ham misol ko'ramiz, Quyidagi kod 0 dan 10gacha Bo'lgan juft sonlarni konsolga chiqaradi:
# son = 1 # Son ning birinchi qiymati 1ga teng.
# while son < 10: # While sikli orqali son 10dan kichik bo'lsa yani o'shanga qadar.
#     son += 1 # Bu kodda songa 1 qo'shib boramiz.
#     if son%2 != 0: # Agar son toq bo'lsa.
#         continue # Agar son toq bo'lsa uni tashlab o'tib ketkin.
#     else: # Aks holda (juft bo'lsa)
#         print(son, end=' ') # Uni konsolga chiqargin.
        
# Sikl ichida bir nechta continue operatorlari bo'lishi mumkin.

# ABADIY SIKL TUZOG'I.
# Sikllar bilan ishlashda abadiy sikl yaratib qo'yishdan ehtiyot bo'lishimiz kerak. Abadiysiklga turli mantiqiy xatolar sabab 
# bo'lishi mumkin: noto'g'ri shart, 'zgarmas qiymat, kodlar ketma-ketligida xatolik va hokazo.

# Dasturlaringiz abadiy siklga tushib qolganda dasturni to'htatish uchun konsolda (terminalda) Ctrl+C tugmalarini bosing.

# Keling ba'zi misollarni ko'ramiz. DIQQAT, Quyidagi kodni ehtiyotkorlik bilan bajaring.
# son = 0 
# while son < 10:
# #   son += 1 # ESDAN CHIQARILGAN QATOR.
#     if son%2 != 0:
#         continue
#     else:
#         print(son)
# Yuqoridagi kod abadiy davom etadi, sababi, biz sonning qiymatini o'zgartirishni unutdik.

# Yana bir misol ko'ramiz:
# son = 0 
# while son < 10:
#     if son%2 != 0:
#         continue
#     else:
#         print(son)
#    # son += 1 # Qatorlar ketma-ketligida xatoga yo'l qo'yildi.
# Yuqoridagi kod ham abadiy siklga misol bo'la oladi.

# son = 1 
# while son > 0: # Shart berishdagi xatolik tufayli abadiy siklga tushib qolinadi.
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)
# Yuqoridagi sikl ham abadiy davom etadi.

# AMALIYOT TOPSHIRIQLARI:
#1 - Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.
# print("Foydalanuvchidan yoqtirgan kitoblari haqida so'raydigan dastur.")
# savol = "Yoqtirgan kitoblariz bormi! Bo'lsa ular qaysilar: "
# savol += ("Dasturni to'htatish uchun esa 'stop' deb yozing! ")
# kitoblar = []
# ishora = 1
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         break
#     else:
#         print("Rahmat!")
        
#2 - Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha
# 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini
# chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# print("Foydalanuvchini yoshiga qarab chipta narxini chiqaruvchi dastur!") # Dastur haqida ma'lumot.
# savol = "Iltimos yoshingizni kiriting! " # Foydalanuvchi qilishi kerak bo'lgan amal haqida ma'lumot.
# while True: # while True teng.
#     qiymat = input(savol) # Yangi qiymat degan o'zgaruvchi input orqali foydalanuvchiga savol beryapti.
#     if qiymat == 'exit' or qiymat == 'stop': # Agar goydalanuvchi 'exit' yoki 'stop' deb yozadigan bo'lsa.
#         break # Dasturni tugatkin.
#     yosh = int(qiymat) # Yosh degan qiymatga foydalanuvchi kiritkan qiymatni integer (butun son)qilib yukladik.
#     if yosh <= 7: # Agar foydalanuvchini yoshi 7dan kichik bo'lsa.
#         narh = 2000 # Kirish narxi 2000.
#     elif 7 < yosh <= 18:
#         narh = 3000
#     elif 18 < yosh <= 65:
#         narh = 10000
#     else: # Aks holda.
#         narh = 0 # Kirish tekin.
#     if narh == 0: # Agar narh teng bo'lsa 0ga.
#         print("Sizga kirish bepul!") # Foydalanuvchiga chiquvchi habar.
#     else: # Aks holda.
#         print(f"Sizga kirish {narh} so'm!") # Shu habar chiqsin.
# print("Dastur tugadi foydalangangiz uchun rahmat!") # Dastur tugatilgan holatda shu habarni chiqar.

# Yuqoridagi dasturni boshqa usullarda ham (break, ishora yoki shart) yozib ko'ramiz.
# print("Foydalanuvchilarga muzeyga kirish narxini bellgilab beradigan dastur!")
# savol = "Iltimos yoshingizni kiritint! "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'stop':
#         ishora = False
#         break
#     yosh = int(qiymat)
#     if yosh <= 7:
#         narh = 2000
#     elif 7 < yosh <= 18:
#         narh = 3000
#     elif 18 < yosh <= 65:
#         narh = 10000
#     else: 
#         narh = 0
#     if narh == 0:
#         print("Sizga kirish bepul!")
#     else:
#         print(f"Sizga kirish {narh} so'm!")
# print("Dastur tugadi!")

#3 - Xatolarni to'g'irlang.
# print("Kiritilgan sonni ildizini qaytaruvchi dastur!")
# savol = "Musbat son kiriting: "
# savol += "(Dasturni tugatish uchun esa 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     # if qiyma < 0: # Shu ikki qatordagi xatolik dasturni to'g'ri ishlashiga halaqit beryapti.
#         # continue
#     if qiymat == 'exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz}ga teng")
# 14 - DARS TUGADI.

# 15 - DARS.
# WHILE, RO'YXATLAR VA LUG'ATLAR.
# Ro'yxatlar (lug'atlar) bilan ishlashda while siklining foydalari juda ko'p. Misol uchun, foydalanuvchidan bir nechta
# ma'lumotlarni qabul qilib olish, ro'yxatdan takrorlanuvchi qiymatlarni o'chirib tashslash yoki bir ro'yxatni ikkinchi
# ro'yxatga ko'chirishda while siklidan foydalanish mumkin.


# WHILE YORDAMIDA RO'YXATNI TO'LDIRISH.
# Quyidagi dasturga e'tibor bering, avval ismlar degan bo'sh ro'yxat yaratib oldik. Keyin esa while sikli yordamida
# foydalanuvchidan ro'yxatga ism qo'shishni so'rayapmiz. So'ngra foydalanuvchidan yana ism qo'shmoqchi yoki yo'q ekanini so'raymiz 
# va foydalanuvchining javobiga ko'ra yo sikl boshiga qaytamiz, yo siklni to'xtatamiz.
# ismlar = []
# print("Do'stlaringizni ro'yxatini tuzamiz!")
# n = 1
# while True:
#     savol = f"{n} - do'stingizni ismini kiriting: "
#     ism = input(savol).lower()
#     ismlar.append(ism)
#     javob = input("Yana is qo'shasizmi? (ha/yoq): ").lower()
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         break
# print("Ro'yxat tuzildi quyidagi ismlar bor!")
# for i in ismlar:
#     print(i.title())

# WHILE YORDAMIDA LUG'ATNI TO'LDIRISH.
# Yuqoridagi usul bilan while sikli yordamida lug'atlarni ham shakllantirishimiz ham mimkin. Quyidagi kodda ism bu kalit, yosh esa
# kalitga mos kelivchi qiyma. WHILE siklining davomiyligi esa ishira qiymatiga bog'liq.
# print("Do'stlaringizni yoshini saqlaymiz!") # Foydalanuvchiga ma'lumot.
# dostlar = {} # Bo'sh lug'at yaratib olamiz.
# n = 1 # n ga 1 qiymat beramiz. 
# ishora = True # Ishora ham qo'shib olamiz va True qiymat beramiz.
# while ishora: # WHILE sikli ishoraning qiymatiga qarab davom etadi. Yani u True bo'lsa ishlaydi va aksincha False bo'lsa to'htaydi.
#     ism = input("Do'stingizni ismini kiriting: ") # ism degan o'zgaruvchi. Keyinchalik undan kalit so'z sifatida foydalanamiz.
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ") # yosh degan o'zgaruvchi ism degan o'zgaruvchining qiymati bo'ladi.
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat. Lug'at elementlarini shakllantirib oldik.
    
#     javob = input("Yana ma'lumot qo'shasizmi: (ha/yo'q) ") # Foydalanuvchidan so'raymiz, yangi elementlar qo'shamizmi ha/yo'q
#     if javob == "yo'q": # Agar javob yo'q bo'lsa.
#         ishora = False # Ishora qiymati False ga o'zgaradi. Natijada dastur tugaydi.
    
# print("Do'stlaringiz haqidagi ma'lumotlar tayyor:")
# for ism, yosh in dostlar.items(): # for orqali lug'at elementlariga murojaat qilamiz.     
#     print(f"{ism.title()} {yosh} yoshda.") # Ularni chiroyli shaklda konsolga chiqaramiz.

# RO'YXAT ELEMENTLARINI O'CHIRISH.
# Avvalgi darslarimizning birida ro'yxat elementlarini o'chirish uchun .remove(qiymat) metodi bilan tanishgan edik.
# Esingizda bo'lsa, bu metod ro'yxatdan eng birinchi uchragan qiymatni o'chiradi. Agar ro'yxatimizda ma'lum bir qiymat
# bir necha bor takrorlangan bo'lsa, ularning barchasini o'chirish uchun WHILE siklidan foydalanishimiz mumkin:
# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'malibu', 'nexia'] # Oddiy ro'yxat faqat ichida bir xil elementlari bor.
# print(cars) # Konsolda ko'rishimiz mumkin.
# while 'nexia' in cars: # WHILE sikli orqali 'nexia' nomli elementlar ro'yxatda bor ekan degan manodagi sikl yozdik. 
#     cars.remove('nexia') # 'nexia' degan elementni o'chirgin.
# print(cars) # Natijani chiqaramiz.

# RO'TXATDAN RO'YXATGA ELEMENT KO'CHIRISH.
# Tassavur qiling, bizda ma'lum bir ro'yxat bor, biz ro'yxat bor, biz ro'yxatdagi har bir element ustida biror amalni bajarib, 
# uni birinchi ro'yxatdan ikkinchi ro'yxatga ko'chirib olmoqchimiz. Shunday halotlarda WHILE sukli juda qo'l keladi.

# Quyidagi misolni ko'raylik. Bizda talabalar ro'yxati bor. WHILE sikli, toki ro'yxatda talabalar bor ekan, aylanaveradi,
# Sikl ichida biz .pop() metodi yordamida talabaning ismini ro'yxatdan sug'urib oldik va foydalanuvchidan talabani baholashni
# so'radik. Talabaning ismi va bahosini lug'at elementi ko'rinishida saqlab qo'ydik (talaba - kalit, baho - qiymat).
# talabalar = ['hasan', 'husan', 'olim', 'botir'] # Oddiy talabar ro'yxatini yaratib oldik.
# for t in talabalar: # talabalar ro'yxatidagi har bir talaba uchun.
#     print(f"{t.title()}.", end=' ') # Uni konsolga chiqar.
# baholangan_talabalar = {} # Yangi bo'sh lug'at.
# while talabalar: # Toki talabalar ro'yxatida element borakan.
#     talaba = talabalar.pop() # Har bir talabani talabalar ichidan sug'urib olyapmiz.
#     baho = input(f"\n{talaba.title()}ning bahosini kiriting: ") # Foydalanuvchidan talabaga baho qo'yishini so'rayapmiz.
#     print(f"{talaba.title()} baholandi!") # Foydalanuvchi talabani baholasa shu talab baholandi degan habarni chiqaryapmiz.
#     baholangan_talabalar[talaba] = baho # Hosil bo'lgan ikkita o'zgaruvchini (talab va baho) baholangan_talabalar degan
# # o'zgaruvchiga lug'at ko'rinishida joylayapmiz.
# for talaba, baho in baholangan_talabalar.items(): # Hosil bo'lgan lug'atimizni elementlariga murojaat qilgan holda.
#     print(f"\n{talaba.title()}ning bahosi: {baho}!") # Ularni konsolga chiqaryapmiz.
    
# AMALIYOT TOPSHIRIQLARI.
#1 - Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# print("Foydalanuvchidan buyurtmalarni qabul qilib oluvchi dastur.")
# buyurtmalar = []
# n = 1
# while True:
#     buyurtma = input(f"{n} - buyurtmani kiriting: ")
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana biror nima buyurtma berasizmi? (ha/yo'q): ")
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         break
# print(f"Buyurtmalar qabul qilindi ular bilan tanishing:")
# for buyurtma in buyurtmalar:
#     print(f"{buyurtma.title()}")

#2 - e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir
# nechta elementlar (mahsulot va uning narhi) kiritishni so'rang. 
# print("e-bozor mahsulotlarini ro'yxatini tuzamiz!")
# mahsulotlar = {}
# n = 1
# while True:
#     mahsulot = input(f"{n} - mahsulotni kiritng: ")
#     narh = input(f"{mahsulot.title()}ni narhini kiriting: ")
#     print(f"{mahsulot} ro'yxatga qo'shildi!")
#     mahsulotlar[mahsulot] = narh
#     javob = input("Yana mahsulot kiritasizmi? (h/y): ")
#     if javob == 'h':
#         n += 1
#         continue
#     else:
#         break
    
# print("e-bozor mahsulotlari ro'yxati tuzildi:")
# for mahsulot, narh in mahsulotlar.items():
#     print(f"{mahsulot.title()}ning narhi - {narh} so'm!")
    
#3 - Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar
# bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring,
# aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# buyurtmalar = ["o'rik", "shaftoli", "olma"] # Foydalanuvchi kerakli mahsulotlar ro'yxati.
# mahsulotlar = { # Mahsulotlar ro'yxati (LUG'AT KO'RINISHIDA).
#     'olma': 20000,
#     'anjir': 40000,
#     'shaftoli': 37000,
#     'uzum': 50000,
#     'qovun': 12000,
#     'tarvuz': 7000,
#     }

# while buyurtmalar: # Toki buyurtmalar ichida element bor ekan 
#     buyurtma = buyurtmalar.pop() # Buyurtmalar ichidagi har bir buyurtmani sug'urib ol.
#     if buyurtma in mahsulotlar.keys(): # Sug'urib olingan buyurtma mahsulotlar lug'atining kalitlari ichida bo'lsa 
#         narh = mahsulotlar[buyurtma] # Xuddi shu mahsulotni qiymatini, yani narhini yangi NARH degan o'zgaruvchiga yuklagin.
#         print(f"{buyurtma.title} - {narh} so'm") # Natijani chiroyli va tushunarli ko'rinishda chiqaramiz.
#     else: # Aks holda.
#         print(f"Bizda {buyurtma} yo'q!") # Foydalanuvchiga bizda bunday mahsulot yo'qligi haqida ma'lumot beramiz.

# 15 - DARS TUGADI.

# 16 - DARS.
# XATOLAR BILAN ISHLASH.

# Har qanday dasturchi kod yozishda xatoga yo'l qo'yadi. Ko'p yozgan odam ko'p xato qiladi va bu tabiiy. Ba'zi xatolarimiz
# Python tomonidan dasturbajarilishidan avval aniqlanadi. Ba'zilari essa dastur bajarish jarayonida aniqlanib, dasturimiz
# to'xtab qoladi.

# Ushbu bobda dastavval dasturchilar ko'p yo'l qo'yadigan xatolar bilan tanishamiz. Keyin esa dastur bajarilishi davomida
# xatolik yuz berganda dastur to'xtab qolishining oldini olishni o'rganamiz.

# XATOLARNING TURLARI.
# SiyntaxError - SINTAKSIS XATOLIK.
# Biz bu xatolik turo nilan 2 - bobda tanishgan edik. SyntaxError eng ko'p uchraydigan xato bo'lib, odatda, dasturlash tili
# qoidalariga amal qilmaslik natijasida kelib chiqadi. Aksar dasturlash muhitlari bunday xatolikni dastur bajarilishidan oldin
# aniqlab, dasturchiga ishora beradi. Sintaksis xatolik bor dasturni Python bajarmaydi.
# print "Hello World!"
# SyntaxError: Missing parentheses in call to 'print'.
# Did you mean print("Hello World!")?

# Odatda, dasturlash mihiti xatoning turi bilan birga (SyntaxError) xato haqida qo'shimcha ma'lumot ham beradi:
# Missing parentheses in call to 'print'. Did you mean print("Hello World!")? shu ko'rinishda.

# Xatolar bilan ishlashda xatolik matnini sinchikovlik bilan o'qish va tahlil qilish juda muhim. Agar ingliz tilini bilmasangiz
# Google Translate yoki Yandex Tarjimon kabi onlayn xizmatlar yordamida xatolik matnini o'zingizga tushunarli (O'zbek yoki Rus)
# tilga tarjima qilib xatoni to'g'irlashingiz mumkin.

# EOL va EOF xatolik.
# EOL (End of Line - qator yakuni) xatoligi sintaksis xatoliklarning bir turi bo'lib, odatda, qator oxirida qo'shtirnoqni
# (bir tirnoq) yopish esdan chiqqanda yuzaga keladi.
# print("Hello World! 
# SyntaxError: Unterminated string literal (detectedat line 2752)


# EOF (End of function - funksitya yakuni) xatoligi esa funksiya oxirida qavsni yopish esdan chiqqanda yuzaga keladi.
# print("Hello World!"
# SyntaxError: '(' was never closed

# EOF xatoligining muammoli tarafi - Python aynan qaysi funksiya yopilmay qolganini ko'rsata olmaydi va dastur yakuniga
# ishora qiladi. Dasturingiz uzun bo'lsa, kodingizni sinchiklab ko'zdan kechirib chiqish talab etiladi.

# IndentationError - JOY TASHLASHDA XATOLIK.
# Python tilida vaziyatga qarab kodni qator boshidan joy tashlab yoki tashlamasdan yozish muhim ahamiyatga ega. Qator boshidan
# asossiz joy qoldirish IndentationError ga olib keladi.

# Quyidagi kodga e'tibor bering, qator boshida 1 dona bo'sh joy qolgani uchun dasturlash muhiti xatoni aniqlab, ╳ bilan belgilab
# qo'yadi.
# print("Hello World!") # Bu kod shunga misol.

# Ba'zi joylarda esa, aksincha, bo'sh joy tashlab yozish talab qilinadi. Masalan, for siklida yoki if-elif-else shartlarining
# ichida va hokazo.
# print("O'ngacha sanaymiz.")
# for n in range(11):
# print(n) # Bu qatorddagi xatolik bitta Tab yani 4ta harflik bo'sh joy tashlanmagan degani (IndentationError).

# Yana bir misol ko'ramiz:
# son = 50 
# if son >= 0:
#     print("Musbat son")
# else:
# print("Manfiy son") # Bu qarda ham xatolik qaytaradi yana print ni bir Tab surishni unutdik.

# QANDAY JOY TASHLASHIMIZ KERAK.
# Aslida, hech bo'lmaganda 1 harflik bo'sh joy qoldirish ham bizni IndentationError dan holos etadi. 

# ETIBOR BERING! Agar dastur boshidan beri bitta Tab dek joy tashlab kelgan bo'lsangiz ohirigacha shunday qiling va aksincha.

# RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK
# Run time error dastur bajarish jarayonida kelib chiqadi va dasturning ishlashini to'xtatadi. Sintaksis xatolikdan farqli ravishda 
# Python bunday xatolarni dasturni bajarishdan oldin aniqlay olmaydi. Bu xatoliklarning bir necha turi bor.
# Ulardan ba'zilari bilan tanishamiz:

# TypeError
# Biror funksiya yoki metodga noto'g'ri ma'lumot turini yuborish:
# son = input("Istalgan sonni kiriting: ")
# print(f"{son} ning kvadrati {son**2} ga teng.") 
# Yuqoridagi koddagi xatolik biz sonni butun son (int) yoki o'nlik son (float) ga o'tkazib olmaganimiz.

# NameError
# O'zgaruvchi funksiya, obyekt nomini noto'g'ri yozish natijasida kelib chiquvchi xatolik.
# Quyida bunga misol ko'ramiz.
# prit("Hello World!")
# Natijada xatolik beradi. Biz print funksiyasini yozishda xatolikka yo'l qo'ydik.

# Yana bir misol ko'ramiz:
# mevalar = ['olma', 'uzum', 'shaftoli', 'bexi']
# for meva in mvalar: # Xatolik shu qatorga to'g'ri keladi. mevalar degan o'zgaruvchini nomini yozishda xatoga yo'l qo'ydik.
#     print(meva)

# ValueError
# Funksiyaga noto'g'ri qiymatni yuborish natijasida xatolik.
# Quyida bunga misol ko'ramiz.
# son = int(input("Istalgan sonni kiriting: "))
# if son >= 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")
# Dasturni bajarishda xatolik yuz beradi qachon biz qiymat berishda adashsak. Masalan, biz 5.5 kiritdik, bu xato chunki yuqorida 
# biz son degan o'zgaruvchiga butun son deb (int) qiymatlaganmiz. Aytish mumkinki kodimiz universalroq bo'lishi uchun son ga
# o'nlik son deb (float) qiymat berishimiz kerak bo'ladi.

# IndexError
# Yangi dasturchilar yo'l qo'yadigan yan bir xato indeks xatolikdir. Ya'ni ro'yxat elementlariga murojaat etishda ineksini
# noto'g'ri kiritish (ro'yxatda mavjud bo'lmagan elementga murojaat qilish):
# Quyida bunga misol ko'ramiz:
# mevalar = ['olma', 'anor', 'uzum']
# print(mevalar[3]) # Xatolik shundan iboratki oldingi darslarimizda biz aytib o'tkanimizdek dasturlashda indekslash 0dan boshlanadi.
# Shu qoidaga asosan bizning ro'yxatimizda elementlar faqat 2gacha indekslangan shu sababli IndexError xatosi kelib chiqyapti.

# ZeroDivisionError
# Dastur jarayonida 0ga bo'lish natijasida yuzaga keladigan xatolik.
# x, y = 50, 50
# z = 250/(x-y) # x-y=0
# Yuqoridagi misolda qavsning ichidan 0 degan javob chiqadi va 0ga bo'lib bo'lmasligini inobatga olgan holda xato qayd etiladi.

# MANTIQIY XATOLAR.
# Mantiqiy xatolar - dasturchi tomonidan dastur algoritmini yozishda yo'l qo'yilgan xatolar. Bunday xatolar dastur bajarilishiga
# to'sqinlik qilmasa-da, dastur to'g'ri ishlashiga xalaqit qiladi va kutilgan natijani bermaydi.

# Mantiqiy xatolar eng ko'p uchraydigan va aniqlash qiyin bo'lgan xatolar hisoblanadi. Aksar holatlarda Python mantiqiy xatolarni
# aniqlamaydi va dastur bajarilaveradi (lekin kutilgan natija chiqmaydi). Bunday xatolarni oldini olish uchun dasturimizning har
#  bir  qadamida chiqayotgan natijalarni tekshirib borish kerak. Katta dasturlar o'nlab, balki yuzlab funksiyalardan iborat bo'ladi, 
# agar mantiqiy xatolar vaqtida topilmasa, minglab qator kodlarni ko'zdan kechirib chiqish talab qilinishi mumkin.

# Mantiqiy xatolar turli ko'rinishda bo'lishi mumkin, masalan, sonlar bilan ishlashda:
# radius = 5
# pi = 4.14
# aylana_yuzi = pi * radius ** 2
# print(aylana_yuzi)
# Kod bajariladi, natija ham chiqadi. Lekin natija xato. Nima uchun? Sababi, biz π = 4.14 deb xato yozib ketdik
# (to'g'ri qiymat: π = 3.14).

# Avval aytkanimizdek, mantiqiy xatolarning oldini olish uchun dasturimizning har bir qadamida chiqayotgan natijalarni
# tahlil qilib borish muhim. Sodda dasturlar qo'lda bajariladi, murakkabroq funksiyalar uchun esa maxsus test dasturlar yoziladi.
# Test dasturlar yozish haqida kelgusi boblarda alohida gaplashamiz. Hozir esa qo'lda tekshirishni ko'raylik:
# son = float(input("Istalgan son kiriting: ")) # 4 ni kiritamiz va 2 degan javobni olamiz.
# ildiz = son**1/2
# print(f"{son}ning ildizi {ildiz} ga teng.")
# Dasturimiz biz kutgan natijani berdi. Lekin yaxshi dasturchi bitta test bilan chegaralanmaydi. Dasturni qayta bajaramiz:
# son = float(input("Istalgan son kiriting: ")) # 9 ni kiritamiz va 4.5 degan javobni olamiz.
# ildiz = son**1/2
# print(f"{son}ning ildizi {ildiz} ga teng.")   
# Mana endi natija xato, 9 sonining ildizi 4.5 bo'lib chiqti. Kodni tahlil qilamiz: 2 - qatorda ildizni hisoblashda 1/2 qavs ichida
# yozilmagani xatolikka olib kelyapti. Natijada foydalanuvchi kiritgan son avval 1 - darajaga oshirildi va undan keyin 2ga bo'lindi.
# Kodni to'g'irlaymiz va dasturni 3-4 marta turli qiymatlar berib bajarib ko'ramiz:
# son = float(input("Istalgan son kiriting: ")) # 9 ni kiritamiz va 3 degan javobni olamiz.
# ildiz = son**(1/2)
# print(f"{son}ning ildizi {ildiz} ga teng.")

# Ba'zida noo'rin bo'sh joy qoldirish (yoki qoldirmaslik) ham mantiqiy xatoga olib kelishi mumkin:
# mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi")
# Yuqorida "Dastur tugadi" matni bir marta, dastur tugaganidan so'ng chiqishi kerak edi. Lekin o'ngga surilib qolgani uchun bir
# necha marta qaytarildi.
 
# Bundan boshqa ham mantiqiy xatoliklar juda ko'p uchraydi. Mantiqiy xatoliklar mutlaqo topilmasdan ham qolib ketishi va dastur
# bozorga chiqqanidan keyin aniqlanishi tabiiy hol. Shuning uchun ham aksar dasturlar tez-tez yangilanib turadi.

# Dasturlash jarayonida bundan boshqa xatolilklar ham ko'p uchraydi. Biz ulardan ba'zilari bilan tanishdik, xolos. Keyingi bo'limda
# Runtime xatoliklar  dastur davomida aniqlash va dastur to'xtab qolishining oldini olishni o'rganamiz.

# AMALIYOT TOPSHIRIQLARI.
#Quyidagi dasturlarda bir nechta xatolar bor ularni to'g'irlang:

#1
# son = float(input("Juft son kiriting: ")
# if son%2==0:
#     print("Bu son juft emas.') # shu qatorda xatolik bor (qo'shtirnoq va birtirnoq bilan bog'liq)
# else:
#     print("Rahmat!"))    

#2
# yosh = (input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18 # Xatolik shu qatorda elif sharti berkitilmagan ohirida ikkita nuqta qo'yilmagan.
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")

#3
# x = float(input("Birinchi sonni kiriting: ") # Shu qatorda qavs yopilmagan.
# y = float(input("Ikkinchi sonni kiriting: ") # Shu qatorda qavs yopilmagan.
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}") # shu qatorda xatolik bor (qo'shtirnoq va birtirnoq bilan bog'liq)
# else # Shu qatorda xatolik bor else funksiyasi yopilmagan.
#     print(f"{x}>{y}")

#4
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun' # shu qatorda xatolik bor ro'yxatning qavslari yopilmagan.

# # shu qatorga savat degan bo'sh ro'yxat qo'shishimiz kerak edi.

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat # shu qatorda xatolik bor for funksiyasi yopilmagan.
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")     

#5
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               # 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: ')) # shu qatorda xatolik bor f-string ichidagi matnni qo'shtirnoqqa
# # olish kerak edi yoki (') belgisi oldidan (\) belgisini qo'yish kerak edi.

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahslot) # shu qatorda xatolik bor (mahslot) bo'lib qolgan (mahsulot) bo'lishi kerak edi.
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas: # if deb shart berishta hamxatolik bor to'g'ri variantni quyirog'da keltirdim.
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda mavjud.")

#6
# users = ['alisher1983','aziza','yasina' 'umar'] # Shu qatorda ('yasina'(,) 'umar') belgisining tashlab ketilishi mantiqiy xatoga
# # sabab bo'ladi. 

# login = input("Yangi login tanlang:' ) # Yuqorida ko'rgan xatoligimiz qo'shtirnoq bilan bog'liq. Bu qatordagi yana bir xato 
# # .lower() metodi qo'shilmagan

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")

#7
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n): # Agar shu qatordagi ifodaga son % n == 0 ga deb qo'yilsa to'g'ri boladi.
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
        

# 16 - DARS TUGADI.

# 17 - DARS.
# EXCEPTIONS.

# Avvalgi bo'limda "Run time error" xatoliklari bilan tanishdik. Bunday xatolar dastur bajarish jarayonida kelib chiqadi va
# dasturning ishlashini to'xtatadi. Sintaksis xatolikdan farqli ravishda, Python bunday xatolarni dasturni bajarishdan avval
# aniqlay olmaydi. Ushbu darsimizda mana shunday xatoliklarni jilovlashni o'rganamiz. Maqsadimiz - xatolik yuz berganda dastur
# to'xtab qolishining oldini olish. Gap shundaki, dastur davomida xato yuz berganda Python maxsus EXCEPTION (istisno) obyektini 
# yaratadi. Agar bu obyekt "tutib" olinmasa, dastur bajarilishdan to'xtaydi.

# TRY-EXCEPT.
# Istisno obyektlarni tutib olish uchun Pythonda maxsus TRY-EXCEPT operatorlari bor. Bu operatorlar quyidagicha ishlaydi.
# TRY operatori badanida bajarish kerak bo'lgan kod yoziladi, EXCEPT operatori badanida esa xatolik sodir bo'lganda bajarilishi
# kerak bo'lgan kod yoziladi. Ya'ni dasturimiz to'xtab qolmasdan bajarilaveradi.

# Tushunarli bo'lishi uchun quyidagi misolni ko'ramiz:
# yosh = input("Iltimos yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2024-yosh} yilda tug'ilgansiz!")

# Yuqoridagi dasturning 1-qatorida biz foydalanuvchidan yoshini kiritishni so'radik. Navbatdagi qatorda esa foydalanuvchi kiritgan
# qiymatni int() funksiyasi yordamida butun songa o'tkazyapmiz. Agar foydalanuvchi kiritganda butun emas, o'nlik son kiritsa bu
# ValueError xatoligiga olib keladi va dastur bajarilishdan to'xtaydi:

# Yoshingizni kiriting: 32.5
# ValueError: invalid literal for int() with base 10: '32.5'

# Mana shunday xatoliklarning oldini olish uchun xato yuz berishi mumkin bo'lgan qatorlarni TRY-EXCEPT bloki yordamida yozamiz.
# Bunda Try bloki ichida bevosita xato keltirib chiqarishi mumkin bo'lgan kodni, EXCEPT bloki ichida esa xatolik yuz berganda 
# bajarilishi kerak bo'lgan buyruqni yozamiz.

# Tushunarli bo'lishi uchun yuqoridagi dasturni yangidan yoxamiz:
# yosh = input("Iltimos yoshingini kiriting: ")
# try: # Kod to'g'ri ishlaganda bajariladigan soha.
#     yosh = int(yosh) 
#     print(f"Siz {2024-yosh} yilda tug'ilgansiz!")
# except: # Kodda xatolik bo'lganda bajariladigan soha.
#     print("Butun son kiritmadingiz!")
# print("Dastur tugadi!")

# Bu yerda ham dastavval foydalanuvchi yoshini so'radik. int() funksiyasini esa TRY badani ichida yozdik, agar foydalanuvchi
# to'g'ri qiymat kiritgan bo'lsa, kodimiz foydalanuvchining tug'ilgan yilini hisoblab ko'rsatadi, EXCEPT (istisno) yuz berganda 
# esa "Butun son kiritmadingiz" xabarini konsolga chiqaradi. Lekin dastur bajarilishdan to'xtamaydi va TRY-EXCEPT blokidan keyingi 
# qatorlar ham bakarilaveradi (print(Dastur tugadi!)).

# Dasturni tekshiramiz. Boshlanishiga to'g'ri qiymat kiritaylik:
# Iltimos yoshingini kiriting: 25
# Siz 1999 yilda tug'ilgansiz!
# Dastur tugadi!

# Yana bir bor, lekin bu safar o'nlik son kiritamiz:
# Iltimos yoshingini kiriting: 32.5
# Butun son kiritmadingiz!
# Dastur tugadi!   

# TRY-EXCEPT operatorining afzalliklaridan biri - foydalanuvchiga Python ko'rsatadigan tushunarsiz xatolar o'rniga o'zimiz istagan,
# tushunarliroq matnni ko'rsatish imkonini beradi. Shuningdek, kompleks tizimlarda arzimagan xatoni deb dasturimiz to'xtab
# qolishining oldini oladi.

# TRY-EXCEPT-ELSE.
# Yuqoridagi kodimizda vi TRY moduli ichida xato qaytarishi mumkin bo'lgan ifodani ham (yosh = int(yosh)), xato qaytarmaganda
# bajarilishi kerak bo'lgan ifodani ham (print(f"Siz {2024-yosh} yilda tug'ilgansiz!")) deb birdan yozib ketyapmiz. Aslida bunday
# qilishimiz to'g'ri emas. 

# To'g'ri usuli - avval xatoga tekshirish va xato yuz bermaganda bajariladigan ifodani alohida, ELSE blokida yozish:
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
except:
    print("Butun son kiritmadingiz!")
else:
    print(f"Siz {2024-yosh} yilda tug'ilgansiz!")
    