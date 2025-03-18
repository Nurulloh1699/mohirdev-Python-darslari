# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 13:07:31 2025

@author: DavrServis
"""

## REGRESSIYA MUAMMOSI. K-nearest neighbor algorithm.

## Biz o'tgan darsimizda KINOTUBE.UZ saytimizga kirgan yangi foydalanuvchi uchun mavjud foydalanuvchilarning qiziqishlari orqali, ya'ni ularni
## solishtirgan holda o'sha yangi foydalanuvchimizga ham tavsiyalar berishni ko'rgan edik.

## KELING ENDI SAVOLNI BOSHQACHASIGA QO'YAMIZ.

## Deylik bizning platformada yangi kino (TITANIK 2) chiqdi va biz shu kinoni new_user (Masha) ga sota olamizmi va bu kinoni new_user o'zi qanday
## baholaydi shuni bilmoqchimiz.

## BUNI BILISH UCHUN QANDAY AMALLAR BAJARAMIZ KO'RAMIZ:
    ## 1. Boshlanishiga new_userga eng yaqin odamlarni ajratib olamiz (ya'ni key = 4). Ularga ism berib olamiz.
    ## 2. Bu ajratib olgan user larimiz bizni eski user larimizdan va biz ularni TITANIK 2 filmiga qanday baho berganini ko'ramiz:
        ## 1. Oypopuk - 4.5 ball
        ## 2. Jon     - 4 ball
        ## 3. Linda   - 5 ball
        ## 4. Tanya   - 3.9 bqall
        ## 5. Masha   - ?
    ## 3. Bizning oldimizdagi muammo new_user (Masha) ushbu kinoga qancha ball beradi.
    ## 4. Demak bizning birinchi ishimiz oddiy manashu 4 ta eng yaqin odamni olib ularning ballarini o'rtachasini hisoblaymiz. 
        ## Masha = (4.5 + 4 + 5 + 3.9) / 4 = 4.35  Demak new_user ga yangi kinomizga qo'yadigan bahosi katta ehtimol bilan 4.35 ball bo'ladi. 

## Buni bilish nimaga kerak?
## Tasavvur qiling siz katta elektron do'kon egasisiz va sizning do'koningizga har kuni yuzlab yangi tovarlar qo'shiladi va sizda 1000 lab
## foydalanuvchilar bor. Endi siz ularning qiziqishlariga qarab ularga mahsulot taklif qilishingiz kerak bo'ladi. Ya'ni kimgadir APPLE yoqadi,
## kimdir SAMSUNG ishlatadi va yana kimdir kiyim-kechak qidiryapti. Bu holatda siz REGRESSIYA degan algoritm borligini bilsangiz har bir 
## foydalanuvchiga nimalarni tavsiya qilgan ma'qulligini aniqroq bilishingiz mumkin.


## REGRESSIYA GA YANA BIR MISOL KO'RAMIZ:
    
## Deylik siz somsa pishirasiz yoki somsa biznesingiz bor va sizning oldingizda turgan savol har kuni nechta somsa pishirish kerak?
## Ya'ni sizda somsalar ortib qolmasin va yetmay ham qolmasin. Demak siz shunday bir optimal sonni topishingiz kerakki, siz har kuni, har
## kunlik talabga mos somsalarni pishirishingiz kerak.

## Qiladigan ishimiz:
    ## 1. Parametrlarni topish (REGRESSIYA miz to'g'ri ishlashi uchun parametrlarni to'g'ri berishimiz judayam muhim). Har bir masala uchun 
    ## parametr belgilashda shu sohani ichiga kirish talab qilinadi (universal parametrlar yo'q).
        ## 1. Ob-havo (1 - yomon, 5 - zo'r) Havo yaxshi bo'lsa bizda ko'proq mijoz bo'ladi va yomon bo'lsa kamroq misolida.
        ## 2. Ish-kuni ((0) yoki hafta ohiri bo'lsa (1)) Ish kunlari uncha savdo bo'lmaydi dam olish kunlari har xil yeg'inlar hisobiga
        ## (tog'oralarga olishadi) savdo hajmi ortadi.
        ## 3. To'ylar mavsumi (0 va 1) To'ylar bo'lgan holatda (tog'oralarga va hokazolarga) ko'proq savdo bo'ladi.
    ## Yuqoridagi 1 va 0 ha yoki yo'q vazifasini bajaradi.
    
    ## Tasavvur qilamiz bir bir qancha statistika yeg'ganmiz.
    ## MAVJUD STATISTIKA:
        ## A. (5, 1, 0) = 300 somsa (Bu yerdagi raqamlar yuqorida berilgan parametrlardan olingan 5 - ob-havo yaxshi, 1-hafta oxiri kabi).
        ## B. (3, 1, 1) = 225 somsa
        ## C. (1, 1, 0) = 75 somsa
        ## D. (4, 0, 1) = 200 somsa
        ## E. (4, 0, 0) = 150 somsa
        ## F. (2, 0, 0) = 50 somsa
        

    ## Vazifamiz berilgan parametrlarga asosan bugun qancha somsa pishirilishi kerakligini hisoblash. Deylik bugun havo yaxshi, hafta oxiri
    ## va to'y mavsumi emas (4, 1, 0).
    
    ## Biz masofalarni hisoblashni ko'rganmiz. Bu holatda ham biz mavjud A, B, C, D..... nuqtalarga yangi nuqta kelyapti va biz bularni 
    ## hisoblashimiz kerak:
        ## A. 1 <-
        ## B. 2 <-
        ## C. 9
        ## D. 2 <-
        ## E. 1 <-
        ## F. 5 
    ## Biz key ni 4 deb olamiz va eng yaqin 4ta nuqtani topamiz. Bu nuqtalarda sotilgan somsalarni qo'shamiz va 4ga bo'lamiz bizda
    ## pishirilishi kerak bo'lgan somsalar miqdori kelib chiqadi.
    ## Bugun = (300 + 225 + 200 + 150) / 4 = 218.75 
    
## Demak bugungi holatga ko'ra biz 218 - 220 somsa pishirganimiz ma'qul ekan.

## ENDI SHU HOLATNI DASTURINI KO'RAMIZ.
import numpy as np
from scipy.spatial import distance

def knn_samsa_prediction(data, new_point, k = 4):
    distances = []
    
    ## Masafolarni hisoblash (Evklid masofasi).
    for point, samsa_count in data:
        dist = distance.euclidean(point, new_point) # Yangi nuqta bilan mavjud nuqtalar orasidagi masofani hisoblash.
        distances.append((dist, samsa_count)) # Masofani va unga mos somsa sonini saqlash.
    
    ## Masofalar bo'yicha saralash (eng yaqin nuqtalarni topish uchun).
    distances.sort()
    
    ## Eng yaqin K ta qo'shnining somsalar sonini hisoblash.
    nearest_neghbors = distances[:k] # Eng yaqin K ta qo'shnini tanlash.
    predicted_samsa = np.mean([count for _, count in nearest_neghbors]) # Ularning o'rtacha somsa miqdorini hisoblash.
    
    return round(predicted_samsa) # Natijani yaxlitlab qaytarish.

## Mavjud statistika (ob-havo, ish-kuni, to'y mavsumi va unga mos somsa miqdori).
data = [
        ((5, 1, 0), 300), # Havo juda yaxshi, hafta oxiri, to'y yo'q -> 300ta somsa sotildi.
        ((3, 1, 1), 225), # Havo o'rtacha, hafta oxiri, to'y bor -> 225ta somsa sotildi.
        ((1, 1, 0), 75), # Havo yomon, hafta oxiri, to'y yo'q -> 75ta somsa sotildi.
        ((4, 0, 1), 200), # Havo yaxshi, ish kuni, to'y bor -> 200ta somsa sotildi.
        ((4, 0, 0), 150), # Havo yaxshi, ish kuni, to'y yo'q -> 150ta somsa sotildi.
        ((2, 0, 0), 50) # Havo yomon, ish kuni, to'y yo'q -> 50ta somsa sotildi.
        ]

## Bugungi shartlar: Havo yaxshi (4), Hafta oxiri (1), To'y mavsumi emas (0).
new_point = (4, 1, 0)

## Optimal somsa sonini hisoblash.
predicted_samsa = knn_samsa_prediction(data, new_point)
print(f"Bugun {predicted_samsa}ta somsa pishirish kerak.")    


## XULOSA QILADIGAN BO'LSAK:
    ## 1. K-NN algoritmini klassifikasiya va regressiya uchun qo'llash mumkin.
    ## 2. K-NN to'g'ri ishlashi uchun paramaetrlarni to'g'ri tanlash o'ta muhim
        ## Bu ham alohida muammo va universal yechim yo'q.
    ## 3. Masofani hisoblash uchun boshqa, aniqroq formulalar bor (masalan kosinus o'xshashlik - cosine similarity (ikkita vektor
    ## o'rtasidagi burchakni hisoblaydi)).
    
