# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:23:47 2025

@author: DavrServis
"""

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