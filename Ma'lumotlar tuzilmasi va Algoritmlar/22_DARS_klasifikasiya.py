# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 10:31:57 2025

@author: DavrServis
"""

## KLASIFIKASIYA va TAVSIYA tizimi.

## KLASIFIKASIYA K-nearest neighbor algorithm.

## KLASIFIKASIYA - bu belgilangan parametrlar orqali, berilgan elementni guruhga ajratish.

## K-Nearest Neighbors (KNN) algoritmi quyidagi sohalarda va vazifalarda keng qo‘llaniladi:

## Tasniflash (Classification)
    ## 1. Spam filtrlash – Elektron pochta xabarlarini spam yoki spam emas deb ajratish.
    ## 2. Tibbiy tashxis – Kasalliklarni tashxislash (masalan, o‘xshash simptomlarga ega bemorlarni guruhlash).
    ## 3. Yuzni aniqlash – Suratlarda inson yuzlarini aniqlash va tanib olish.

## Deylik bizda o'rik va dovcha (g'o'ra) bor va bizga yangi meva ko'rsatilyapti. Bizda mavjud mevalarga parametrlar belgilaymiz ularni
## ajrata olish uchun HAJMI va RANGI degan parametrlar belgilaymiz.

## Biz avval bu mevalarni ikkiga ajratib olamiz dovchalarni alohida va o'riklarni alohida.

## Birinchi yo'limiz yangi elementga eng yaqin bo'lgan 3ta (hohishga ko'ra 5ta, 7ta) qo'shnini topamiz va qaysilarga ko'proq yaqin bo'lsa 
## shu mevaga qo'shamiz bu K-nearest neighbor (K-ta eng yaqin qo'shnilar) algoritmi deyiladi.

    ## 4|
    ##  |
    ## 3|
    ##  |
    ## 2|
    ##  |
    ## 1|---------------->
    ##   1    2    3    4

## Demak bir tarafdan rangini hisoblaymiz va bir tomondan hajmiga baho beramiz.
    ## Y o'qi:
        ## 1. Yashil
        ## 2. Sariq
        ## 3. Sabzi rang
        ## 4. Qizg'ish
        
    ## X o'qi:
        ## 1. 5mm
        ## 2. 10mm
        ## 3. 15mm
        ## 4. 20mm
        
## Shu tariqa yangi qiymatni hajmi va rangiga qarab ikki guruhdan biriga ajratamiz. Natijani aniqlash uchun yangi element ikki nuqta
## o'rtasiga qo'yamiz va EVKLID formulasi orqali topamiz: 
import math  # Matematik hisob-kitoblar uchun kutubxona

def evklid_masofa(x1, y1, x2, y2):
    """Ikki nuqta orasidagi masofani hisoblash (Evklid masofasi)"""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 🔹 Misol uchun nuqtalar
x1, y1 = 3, 4
x2, y2 = 7, 1

# 🔹 Masofani hisoblash va chiqarish
masofa = evklid_masofa(x1, y1, x2, y2)
print(f"Ikkita nuqta orasidagi masofa: {masofa:.2f}")


## K-NN ASOSIDA TAVSIYA TIZIMI.

## Bu masalanu tushunish uchun misol sifatida biror bir saytni olamiz va shu sayt misolida ko'ramiz.
## Tasavvur qiling bizda KINOTUBE.UZ degan yoki boshqa biror nom bilan nomlangan kino, video sayti bor. Aytaylik bizda 1000ta foydalanuvchi 
## bor, endi bizga yana bir yangi foydalanuvchi qo'shildi. Endi bu foydalanuvchiga yoqadigan video yoki kinolarni taklif qilish uchun, u 
## qanday mazmundagi kino va videolarni ma'qul ko'rishini bilishimiz kerak.

## Bu holatda yangi foydalanuvchiga 10ta yoki 20ta kino, seriallarni ko'rsatib ulardan ma'qul ko'radiganlarini tanlash orqali unga nima 
## tavsiya qilishimizni bilishimiz mumkin.

## Bu holatda biroz boshqacharoq jadval tuzib olamiz.
    ##              Boqivoy     Oypopuk     Solijon     Masha(new_user)
    ## Triller      5           3           3           4   
    ## Komediya     4           5           4           5
    ## Drama        1           5           1           3 
    ## Jangari      4           2           5           1 
    ## Serial       0           3           1           2 

## Demak saytimizda bor kinolar janrlari va ularga yuqoridagi yangi userimizga sherik qilib olingan eski userlar.

## Yuqorida yangi userga taklif qilingan kinolardan yoqqanlarini tanlaganidan keyin biz unga qanday janrdagi kinolar yoqishini bilishimiz
## mumkin. Uni ham jadvalga kiritamiz va unga eng yaqin qiziqishlari eng yaqin userni topamiz va unga qarab yangi userimiz bosh ekraniga 
## mos janrdagi kinolarni videolarni tavsiya sifatida chiqaramiz 

## Bu holatda biz yana formula yozishimiz kerak bo'ladi. Yana EVKLID formulasidan foydalansak bo'ladi va endi biz old_users va new_user
## o'rtasidagi masofani hisoblaymiz.

## Bizda endi parametrlar soni biroz ko'proq bo'ladi holos qolgan hammasi oldingiday bo'ladi:
import math # Masofani hisoblash uchun math kutubxonasini import qilamiz.

## Foydalanuvchilarning janrlarga bo'lgan baholari.
users = {
    "Boqivoy":   [5, 4, 1, 4, 0], # Triller, Komediya, Drama, Jangari, Serial
    "Oypopuk":   [3, 5, 5, 2, 3], # Har bir user o'z baholarini bergan.
    "Solijon":   [3, 4, 1, 5, 1],
    "Masha":     [4, 5, 3, 1, 2] # Yangi user (Masha)  
    }

def euclidean_distance(user1, user2):
    """Ikki foydalanuvchi orasidagi Evklid masofasini hisoblaydi"""
    distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(user1, user2))) # EVKLID formulasi.
    return distance # Hisoblangan masofani qaytaradi.

## Yangi foydalanuvchi (Masha) ning reytingini olamiz.
target_user = users["Masha"]

## Eng yaqin userni topish
nearest_user = None # Eng yaqin userni saqlash uchun o'zgaruvchi.
min_distance = float("inf") # Boshlang'ich eng katta qiymat.

for user, ratings in users.items():
    if user == "Masha": # O'zini o'zi bilan solishtirmaymiz.
        continue
    
    distance = euclidean_distance(target_user, ratings) # Masofani hisoblaymiz.
    if distance < min_distance: # Agar yang imasofa kichikroq bo'lsa.
        min_distance = distance # Uni eng yaqin masofa sifatida belgilaymiz.
        nearest_user = user # Eng yaqin foydalanuvchini saqlaymiz.
        
## Natijani chiqaramiz.
print(f"Masha uchun eng yaqin foydalanuvchi: {nearest_user}")
print(f"Eng yaqin masofa: {min_distance: 2f}")