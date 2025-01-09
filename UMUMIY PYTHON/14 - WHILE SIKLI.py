# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 02:13:07 2025

@author: DavrServis
"""

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