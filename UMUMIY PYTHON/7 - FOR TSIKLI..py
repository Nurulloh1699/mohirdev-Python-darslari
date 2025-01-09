# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:25:48 2025

@author: DavrServis
"""

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