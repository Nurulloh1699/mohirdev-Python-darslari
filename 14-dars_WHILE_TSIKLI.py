# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:01:59 2024

@author: DavrServis
"""

#14-dars WHILE TSIKLI
#31.10.2024.
#Muallif:Abdurashidov Nurulloh.

#.INPUT() funksiyasiga misol ko'ramiz.
# ism = input("Ismingiz nima? ") # Foydalanuvchidan ismini so'raymiz.
# savol = "Salom {ism.title()}, yoshingiz nechida? " # Foydalanuvchini ismini va uning ismi orqali uning yoshini
# # so'raydigan matnni kiritib olamiz.
# yosh = input(savol) # Yuqoridagi matnni yosh degan o'zgaruvchiga yuklaymiz.
# yosh = int(yosh) # Foydalanuvchi kiritgan yoshni integer butun qilib saqlaymiz.
# height = input("Bo'yingiz necha metr? ") # Foydalanuvchiga yangittan murojaat qilamiz va bo'y o'lchamini so'raymiz.
# height = float(height) # Kiritilgan malumotni float (o'nlik songa olib o'tamiz)

# WHILE (TOKI) TSIKLINI KO'RIB CHIQAMIZ.
# Endi biz while tsikli orqali oddiy dastur tuzib ko'ramiz.
# son = 1 # Sonning qiymatini biz 1 gha tenglab oldik.
# while son <= 5: # WHILE (TOKI) tsikli orqali shart beryapmiz toki son 5dan katta yoki 5ga teng bo'lmaguncha.
#     print(son, end= ' ') # Yuqoridagi shartga muvofiq shart bajarilsa son konsolga chiqarilsin.
#     son += 1 # yoki son = son + 1 ikki kod ham bir hil natija qaytaradi.
# print("Son qiymati 5 dan oshdi va dastur tugadi.") # Yuqoridagi shartga muvofiq son agar 5ga tenglashsa yoki oshsa
# dastur tugaydi.


# # WHILE va INPUT() yordamida kiritilgan sonning kvadratini hisoblovchi dastur yozamiz.
# print("Foydalanuvchi kiritgan sonning kvadratini hisoblovchi dastur.\n") # Dastur nima vazifa bajarishi haqida ma'lumot.
# savol = "Istalgan son kiriting: " # Savol deb nomlangan o'zgaruvchiga matn yukladik va bu matn foydalanuvchiga nima
# # qilsh kerakligini aytamiz. 
# savol += "(Dasturni to'xtatish uchun esa 'exit' deb yozing!) \n >>> " # Bu matnni yuqoridagi savolga qo'shish orqali
# # foydalanuvchi dasturni qaysi yo'l bilan tugatishi mumkinligi haqida ma'lumot beryapmiz.
# qiymat = '' # Bo'sh qiymatga kelajakda u str (matn) qabul qilishini aniqlashtirib ketyapmiz.
# while qiymat != 'exit': # Toki qiymat 'exit' ga teng bo'lmas ekan quyidagi kod bajariladi.
#     qiymat = input(savol) # qiymatga input orqali savolni yuklash bilan foydalanuvchi qilishi mumkin bo'lgan ishlarni 
# # tushunarli qilib konsolga chiqaryapmiz.    
#     if qiymat != 'exit': # Agar qiymat 'exit' ga teng bo'lsa.
#         print(f"Siz kiritgan {qiymat} sonining kvadrati {(float(qiymat) ** 2)} ga teng. \n") # Foydalanuvchi kiritgan
# # sonni kvadratini hisobla degan kod.
# print("Siz 'exit' deb yozdingiz va shu sababli dastur tugadi.") # Foydalanuvchi uchun ma'lumot.   

# Endi yuqoridagi kod shartini boshqa yo'l bilan tekshirish yo'lini ko'rib chiqamiz.

# # ISHORA O'ZGARUVCHI ni ko'rib chiqamiz. Buning uchun yuqoridagi kodni boshqacharoq qilib yozamiz.
# print("Foydalanuvchi kiritgan sonning kvadratini hisoblovchi dastur.\n") # Dastur nima vazifa bajarishi haqida ma'lumot.
# savol = "Istalgan son kiriting: " # Savol deb nomlangan o'zgaruvchiga matn yukladik va bu matn foydalanuvchiga nima
# # qilsh kerakligini aytamiz. 
# savol += "(Dasturni to'xtatish uchun esa 'exit' deb yozing!) \n >>> " # Bu matnni yuqoridagi savolga qo'shish orqali
# # foydalanuvchi dasturni qaysi yo'l bilan tugatishi mumkinligi haqida ma'lumot beryapmiz.
# ishora = True # Shu yerda mana biz ishora yaratib unga True qiymatini berdik.
# while ishora: # Toki ishora True ekan quyidagi shart bajarilsin.
#     qiymat = input(savol) # Qiymatga yuqoridagi savollarni yuklab olamiz.
#     if qiymat == 'exit': # Agar shart teng bo'lsa 'exit' ga
#             ishora = False # Ishora False bo'lsin va tabiiyki dastur tugatilsin.
#     else: # Aks holda, quyidagi shart bajarilsin.
#         print(f"Siz kiritgan {qiymat} sonining kvadrati {(float(qiymat) ** 2)} ga teng. \n") # Foydalanuvchi kiritgan 
# # sonni kvadratini hisoblaymiz.
# print("Siz 'exit' deb yozdingiz va shu sababli dastur tugadi.") # Foydalanuvchi uchun ma'lumot. 

# BREAK. Endi biz dasturni to'xtatishni boshqa usulini ko'rib chiqamiz. Yana yuqoridagi koddan foydalanamiz.
# print("Foydalanuvchi kiritgan sonning kvadratini hisoblovchi dastur.\n") # Dastur nima vazifa bajarishi haqida ma'lumot.
# savol = "Istalgan son kiriting: " # Savol deb nomlangan o'zgaruvchiga matn yukladik va bu matn foydalanuvchiga nima
# # qilsh kerakligini aytamiz. 
# savol += "(Dasturni to'xtatish uchun esa 'exit' deb yozing!) \n >>> " # Bu matnni yuqoridagi savolga qo'shish orqali
# # foydalanuvchi dasturni qaysi yo'l bilan tugatishi mumkinligi haqida ma'lumot beryapmiz.
# while True: # Bu endi abadiy tsikl bo'ldi va to'xtamay qaytarilaveradi.
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # Tsiklni to'xtatish.
#     else: # Aks holda, quyidagi shart bajarilsin.
#         print(f"Siz kiritgan {qiymat} sonining kvadrati {(float(qiymat) ** 2)} ga teng. \n") # Foydalanuvchi kiritgan 
# # sonni kvadratini hisoblaymiz.
# print("Siz 'exit' deb yozdingiz va shu sababli dastur tugadi.") # Foydalanuvchi uchun ma'lumot. 

# BREAK ni yana bir misol orqali ko'rib chiqamiz.
# sonlar = list(range(1,11)) # Bu yerda list (ro'yxat) yaratib oldik va unga 1dan 11gacha bu holatda 11ning o'zi bu
# # ro'yxatga kirmaydi.
# for son in sonlar:# Bu yerda son degan o'zgaruvchini sonlardagi har bir songa tenglab chiqyapmiz yani sonlar ichidagi
# # har bir son uchun. 
#     if son == 5: # Bu yerda shart beryapmiz, agar son 5ga teng bo'lsa u holda.
#         break # Dasturni to'htatgin, yani bizda sonlarimiz ko'proq edi lekin bu yerda BREAK bo'lganu uchun dastur shu 
# # yerda to'htaydi.
#     print(f"{son} ning kvadrati {son**2} ga teng") # Dastur to'htagunga qadar olingan sonlarni kvadratini chiqaradi.
    
# # CONTINUE. Endi BREAK dan farqli o'laroq boshqacharoq vazifani o'tab beradigan CONTINUE komandasi bilan tanishamiz.
# # Ayni yuqoridagi kod misolida buni ko'rib chiqamiz.
# sonlar = list(range(1,11)) # Bu yerda list (ro'yxat) yaratib oldik va unga 1dan 11gacha bu holatda 11ning o'zi bu
# # ro'yxatga kirmaydi.
# for son in sonlar:# Bu yerda son degan o'zgaruvchini sonlardagi har bir songa tenglab chiqyapmiz yani sonlar ichidagi
# # har bir son uchun. 
#     if son == 5: # Bu yerda shart beryapmiz, agar son 5ga teng bo'lsa u holda.
#         continue # Bu yerda CONTINUE komandasi berilgan shartni ko'rib chiqib dasturning boshiga qaytadi va shartda
# # ko'rsatilgan (bizning holatimizda) elementni tashlab keyingi qadamga o'tib ketadi.
#     print(f"{son} ning kvadrati {son**2} ga teng") # Dastur to'htagunga qadar olingan sonlarni kvadratini chiqaradi.
    
    
# WHILE ichida CONTINUE. Quyidagi misol asnosida ko'rib chiqamiz.
# son = 0 # Sonni 0 gatenglab olyapmiz.
# while son <= 10:# WHILE tsiklini boshlayapmiz, buholatda son kichik yoki teng bo'lmaguncha 10ga. Yani birma-bir ko'rib 
# # chiqqin deyapmiz.
#     son += 1 # Songa har safar 
#     if son%2 != 0: # Sonni ikkiga bo'lgandagi qoldiq 0ga teng bo'lmasa juft sonlar chiqadi yoki aksincha (==) teng
# #bo'lsa toq sonlar chiqadi.
#         continue # Shartga muvofiq har bir son tekshiriladi va shartga to'g'ri kelmaganlari duch kelsa dasturning boshiga 
# # qaytadi shartga to'g'ri kelmagan elementni tashlab ketkan holda dastur ishlashda davom etadi.
#     else: # Aks holda.
#         print(son) # Son konsolga chiqariladi.
        
# ABADIY TSIKLLARNI KO'RIB CHIQAMIZ. Quyidagi kodlar misolida abadiy tsikillarga misollarni ko'rib chiqamiz.
# Bazi qatorlar unutib qoldirilganda:
# son = 0
# while son <= 10:
#     # son += 1 # Manashu qatorni yo'qligi bizni abadiy tsikilga tuwurib qo'ydi.
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)

# Komandalar ketma- ketligi buzilganda:       
# son = 0
# while son <= 10:
#     # son += 1 # Manashu qatorni yo'qligi bizni abadiy tsikilga tuwurib qo'ydi.
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)
#     son += 1 # Bu yerda esa komandalar ketmaketligida xato bo'ldi va abadiy tsikilga tuwib qoldik.

# Shart (tsikl aslida qanday ishlashini tushunmay) no'tog'ri berilganda:
# son = 1
# while son > 0: # Birinchi va ikkinchi qatorda shart yozishda xato qilingani bizni abadiy tsiklga tuwurib qo'ydi.
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)

# AMALIYOT TOPSHIRIQLARI.
#1 - Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan
# dasturni to'xtating.
# savol = ("Sevimli kitoblaringizni kiriting!\n")
# savol += ("Barchakitoblarni kiritib bo'lganingizdan keyin 'exit' deb yozing.\n")
# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat')

#2 - Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm,
# 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini
# so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin
# (ikkita shartni ham tekshiring).
# savol = "Yoshingizni kiriting: " # Foydalanuvchidan savol so'ralyapti.

# while True: # While ni True ga tenglab oldik.
#     qiymat = input(savol) # Foydalanuvchidan qiymat so'rash asnosida qiymatga yuqoridagi savolni yuklaymiz.
#     if qiymat == 'exit' or qiymat == 'quit': # Ikkita shart beramiz.
#         break # Yuqoridagi shart bajarilsa dastur to'htasin. Aks holda davom etsin.
#     yosh = int(qiymat) # Foydalanuvchi kiritgan qiymatni yosh ga va yoshni int butun songa o'tkazib olamiz.
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18: # yosh 7dan katta yoki 7ga teng bo'lsa va 18dan kichik bo'lsa.
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0: # Yuqoridagi shartlarni tekshirgan holda foydalanuvchiga navbatdagi habarni chiqarishini kodda yozamiz.
#         print("Sizga chipta bepul") # Bu holatda yosh agar 65dan yuqori bo'lsa narh 0 bo'lib qaytadi va shu holda
# # yuqoridagi habar chiqadi.
#     else: # Aks holda quyidagi habar chiqadi.
#         print(f"Chipta {narh} so'm")
# savol = "Yoshingiz nechida? "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 5000
#     elif 18 <= yosh < 65:
#         narh = 10000
#     else: 
#         narh = 0
    
#     if narh == 0:
#         print("Sizga kirish bepul!")
#     else:
#         print("Sizga kirish", narh, "so'm.")

#3 - Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda.
# Xatolarni to'g'rilay olasizmi?
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol) 
    qiymat = int(qiymat) # Xato shu qatorda edi (qator unutib qoldirilgan.)
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")