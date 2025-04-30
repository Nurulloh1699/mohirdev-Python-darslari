# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 13:42:40 2025

@author: DavrServis
"""

## GREEDY ALGORITMLAR - OCHKO'Z ALGORITMLAR.

## Ba'zi muammolar hech qanday algoritmga tushmaydi, shunday holatlarda ochko'z algoritmlar yordamga keladi va har qadamda optimal yechimni
## tanlash asosida ishlaydi. Aytish mumkinki GREEDY algoritmi ha doim ham to'g'ri yechimni bermaydi, lekin muammo boshqa hech qaysi
## algoritmga tushmaganda va muammoni hal qilish ko'p vaqt olgan biz GREEDY algoritmiga murojaat qilamiz.

## QUYIDAGI MUAMMONI KO'RAMIZ.
    ## Bizda sinfxona va quytidagi darslar jadvali bor:
        ## 1. Matematika: 9:00 - 10:00
        ## 2. Fizika: 9:30 - 10:30
        ## 3. Adabiyot: 10:00 - 11:00
        ## 4. Informatika: 10:30 - 11:30
        ## 5. Tarix: 11:00 - 12:00
    ## Berilgan sinfda o'tish mumkin bo'lgan darslar ro'yxatini tuzing.
## YECHIM:
    ## 1. Eng erta tugaydigan darsni tanlaymiz va ro'yxatga qo'shamiz.
    ## 2. Ro'yxat oxiridagi darsdan keyin boshlanadigan eng erta darsni tanlaymiz va ro'yxatga qo'shamiz.
    ## 3. Jadvaldagi darslar tugagunicha 2-qadamni takrorlayveramiz.
## JAVOB:
    ## 1. Matematika: 9:00 - 10:00
    ## 2. Adabiyot: 10:00 - 11:00
    ## 3. Tarix: 11:00 - 12:00
    
## Aytishimiz mumkin bu juda oson masala deb, lekin aslida universitetlarda, darslar ko'p va auditoriyalar oz bo'lgan hollarda siz optimal 
## yechim topishiz uchun ko'p vaqt ketishi mumkin va aksincha GREEDY algoritmidan foydalanilsa masalaga oson yechim topiladi.

## GREEDY algoritmi bilan uchrab turadigan yana bir muammo:
    ## The Knapsack Problem (To'rvaxalta muammosi) - bu har hil sohada va turli ko'rinishda uchrashi mumkin. Quyida ularga misol keltiramiz.

## 1. Tasavvur qiling siz o'g'risiz va sizda 20kg nnarsa sig'adigan torva xalta bor. Siz uyga kirdingiz va qarshingizda:
        ## 1. Televizor - 1000$ lekin 18kg.
        ## 2. Noutbuk - 900$ lekin 3kg.
        ## 3. Mikravalnovka - 150$ lekin 5kg.
## Siz tezroq qaror qabul qilishingiz kerak (hisoblashga vaqt yo'q).

## 2. Tasavvur qiling siz duradgorsiz va sizda taxta bo'lagi bor (DVP/DSP). Siz undan eng kam keraksiz bo'lak (otxod) chiqargan xolda
## foydalanishiz kerak. Sizga GREEDY algoritmi yaxshi yechimlar taklif qilishi mumkin.

## 3. Har doim ham to'g'ri ishlamasligiga misol sifatida o'tgan darsda yechim topgan GRAF, ya'ni A nuqtadan B nuqtaga qanday qilib eng tez
## borish mumkinligini topgan edik. Buni GREEDY bilan ko'rsak u bizga o'zi tog'ri deb bilgan eng optimal yechimni beradi (12 minut).
## Lekin biz DIJKSTRA algoritmi bilan bundan ham tezroq yetib kelish mumkinligini ko'rgandik (11 - minut), ya'ni GREEDY eng optimal yechimni 
## beradi lekin har doim ham to'g'ri emas. Lekin judayam xato yechimni ham bermaydi, ustun jihati esa GREEDY juda tez ishlaydi.

## XULOSA:
    ## 1. Ochkoz algoritmlar har doim ham eng to'g'ri yechimni bermaydi.
    ## 2. Lekin amalga oshirish (dasturlash) tomonlama juda oson.
    ## 3. Agar to'g'ri yechimni topish juda ko'p vaqt (resurs) talab qilsa qoniqarli yechimni topish uchun GREEDY algoritmlarni tanlang.
    
## Mana shunday GREEDY algoritmi yordamida yechim topiladigan muammolardan biri THE SET-COVERING PROBLEM (to'plamni yopish muammosi). 

## Shu muammoni bitta ko'rinishini ko'rib chiqamiz
    ## 1. Tasavvur qiling, siz yangi uyali aloqa kompaniyasi uchun shahar bo'ylab  antenalar o'rnatib chiqishingiz kerak.
    ## 2. Sizga antenna o'rnatish uchun 4ta binoga ruhsat tegdi.
    ## 3. Har bir binoga qo'yilgan antenna faqatgina sanoqli hududlarni qamrab oladi.
    ## 4. Muammo barcha hududlarni qamraydigan eng kam antennalar (binolarni) toping.
    
## YECHIM: The Set-Covering Problem.
    ## 1. Binolarning mavjud kombinatsiyalarini quramiz (n ta bino uchun 2ⁿ kombinatsiya mavjud).
    ## 2. Kombinatsiyalar orasidan barcha hududlarni qanran oladiganlarini topamiz.
    ## 3. Ularning ichidan eng kam bino bor to'plamni tanlaymiz.
## BINOLAR: A, B, C, D binolar va 1, 2, 3, 4, 5, 6 hududlar bor.
    ## A = [1, 3, 4]
    ## B = [2, 4, 5]
    ## C = [1, 2, 6]
    ## D = [2, 5, 6]
    
## KOMBINATSIYALAR:
    # 1. **(A)** → [1, 3, 4]  
    # 2. **(B)** → [2, 4, 5]  
    # 3. **(C)** → [1, 2, 6]  
    # 4. **(D)** → [2, 5, 6]  
    # 5. **(A, B)** → [1, 2, 3, 4, 5]  
    # 6. **(A, C)** → [1, 2, 3, 4, 6]  
    # 7. **(A, D)** → [1, 2, 3, 4, 5, 6] # To'g'ri variant. ✅  
    # 8. **(B, C)** → [1, 2, 4, 5, 6]  
    # 9. **(B, D)** → [2, 4, 5, 6]  
    # 10. **(C, D)** → [1, 2, 5, 6]  
    # 11. **(A, B, C)** → [1, 2, 3, 4, 5, 6] # To'g'ri variant. ❌
    # 12. **(A, B, D)** → [1, 2, 3, 4, 5, 6] # To'g'ri variant. ❌
    # 13. **(A, C, D)** → [1, 2, 3, 4, 5, 6] # To'g'ri variant. ❌
    # 14. **(B, C, D)** → [1, 2, 4, 5, 6]  
    # 15. **(A, B, C, D)** → [1, 2, 3, 4, 5, 6] # To'g'ri variant. ❌  

## Ko'rib turganingizdek bizda mos variantlar 5ta, shart bo'yicha to'g'risi esa 1ta (A, D) ekan.

## Endi bu masalaga yechim topish uchun nechta amal talab qilinganini ko'ramiz (n binolar soni):
    ## n    set-covering O(2ⁿ)    GREEDY O(n²)     FARQ    
    
    ## 4    O(16)                 O(16)            1 BARAVAR 
    ## 10   O(1024)               O(100)           10 BARAVAR (GREEDY ning SET-COVERING ga nisbatan tezligi)
    ## 30   O(1,073,741,824)      O(900)           1,193,046 BARAVAR (GREEDY ning SET-COVERING ga nisbatan tezligi)
    
    

## AMALIYOT.

## Deylik bizda 30 ta hudud va bu hududlarni qamrab olish uchun 15 ta bino bor (Mos ravishda har bir binoning qamrovi har xil va har bir
## bino har xil hududlarni qamrab oladi (5 tadan ko'p va 2 tadan kam bo'lmagan holatda)). Bizning vazifamiz barcha hududlarni qamrab
## oluvchi  binolarning eng kam kombinatsiyaligini topishdan iborat.

## Misol uchun:
    ## Set-covering (barcha variantlarni ko'rib chiqadigan) algoritm uchun - 2**15 = 32768 -> O(2ⁿ)
    ## GREEDY algoritmi - 
    
## DASTUR KODI.
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint as print

## 📥 Ma'lumotlarni fayldan o'qiymiz.
with open('binolar.dat', 'rb') as file: # WITH fayli avtomatik yopadi, OPEN orqali biz belgilangan faylni ochamiz (RB rejimida), AS file.
    binolar = pickle.load(file) # pickle.load(file) - file ichidan pickle orqali saqlangan binolar ma'lumotlarini yuklaydi.
    hududlar = pickle.load(file) # pickle.load(file) - fayldan hududlar ma'lumotlarini yuklaydi.
    
print("Binolar va ularning qamrov hududlari:")
print(binolar)

## 📌 GREEDY algoritmi boshlanishi:
yakuniy_binolar = set() # Yakuniy tanlangan binolar to'plami.

## Barcha hududlar kamida bitta bino tomonidan qamrab olinganligini tekshiramiz.
qamrab_olingan_hududlar = set()
for bino_qamrovi in binolar.values():
    qamrab_olingan_hududlar |= bino_qamrovi # Barcha binolar qamrovini qo'shib boramiz
    
## 🛑 Agar barcha hududlar qoplanmagan bo'lsa, xatolik chiqadi.
if qamrab_olingan_hududlar != hududlar:
    print("❌ Xatolik: Ba'zi hududlar hech qaysi bino tomonidan qamrab olinmagan!")
    print(f"Qamrab olinmagan hududlar: {hududlar - qamrab_olingan_hududlar}")
else:
    print("✅ Barcha binolar kamida bitta bino tomonidan qamrab olingan.")
    
    ## 🔁 Algoritm har bir qadamni bosqichma-bosqich bajaradi.
    while hududlar:
        print("\n--- Yangi iteratsiya ---")
        best_bino = None # Hozircha eng yaxshi bino yo'q.
        qamralgan_hududlar = set() # Eng yaxshi bino qancha hudud qoplayotganini saqlash.
        
        print("🔍 Har bir bino qamrovi tahlil qilinmoqda...")
        for bino, bino_qamrovi in binolar.items():
            qamrov = hududlar & bino_qamrovi # Hozircha bina qancha yangi hududni qamrab oladi?
            print(f" {bino}: Qamrab olingan hududlar {qamrov}")
            
            ## 🔝 Eng ko'p yangi hududni qoplaydigan binoni tanlash.
            if len(qamrov) > len(qamralgan_hududlar):
                best_bino = bino
                qamralgan_hududlar = qamrov
                print(f" ✅ Hozircha eng yaxshi bino {best_bino}, Qamrab olgan hududlari {qamralgan_hududlar}")
                
        ## 🚨 Agar hech qanday bino tanlanmasa, algoritm to'htaydi.
        if best_bino is None:
            print("❌ Xatolik: Hududlarni to'liq qamrab olish imkonsiz!")
            print(f"Qamrab olinmagan hududlar: {hududlar}")
            break
        
        ## ✅ Eng yaxshi binoni tanlab, uning qamrab olgan hududlarni olib tashlaymiz.
        hududlar -= qamralgan_hududlar
        yakuniy_binolar.add(best_bino)
        
        print(f"🏢 Tanolamngan bino: {best_bino}")
        print(f"📉 Qolgan qoplanmagan hududlar: {hududlar}")
        print(f"✅ Hozirgacha tanlangan binolar: {yakuniy_binolar}")
        
    ## 🏁 Yakuniy natijani chiqarish.
    print("\n🎯 Yakuniy natija: Minimal binolar to'plami:")
    print(yakuniy_binolar)
    
    ## 📊 **Jadval shaklida natijalarni chiqarish**
    df = pd.DataFrame([(bino, binolar[bino]) for bino in yakuniy_binolar], columns=["Tanlangan bino", "Qamrab olingan hududlar"])
    print(df)
    
## Dastur to'laqonli ishlashi uchun, dastur faylida binolar_fixed.dat fayli ham bo'lishi kerak.


## Demak mana shunday murakkab muammolarni hal qilish va qoniqarli natija olish uchun GREEDY algoritmidan foydalansak bo'ladi.

## Bunday muammolarni o'zining nomi bor va ular, NP-COMPLETE PROBLEMS (NP-MUAMMOLAR) deyiladi.


## BIZ YANA BIR MISOL KO'RAMIZ.
## TRAVELING SALESPERSON PROBLEM (MUSOFIR MUAMMOSI).

## Savdogar ish bila safarga chiqdi va safar davomida 5ta manzilga kirib o'tishi kerak.
## MUAMMO: 5ta manzilga eng kam vaqt (yoki masofa) sarflab kirib o'tish yo'lini topish.

## AGAR MASALANI ODDIY YO'L BILAN YECHMOQCHI BO'LSAK.
## Boshlanishiga 5ta emas balki 3ta manzil bilan ishlab ko'ramiz va bu manzillar uchun 6 xil kombinatsiya tuzishimiz mumkin.
## Agar manzillar soni 4ta bo'lib qolsa demak kombinatsiyalar soni ham o'zgaradi (24), ya'ni bu yerda biz FAKTORIAL bo'yicha hisoblaymiz.
## Demak agar bizda 5ta nuqta bo'lsa kombinatsiyalar soni yana o'zgaradi (120) va biz bu kombinatsiyalar ichidan bizga eng mosini olamiz.

## Demak TRAVELING SALESPERSON uchun BIG O: O(n!) ga teng bo'ladi ekan.

## AGAR MASALANI GREEDY ALGORITMI BILAN YECHSAK.
## Bu holatda biz oddiygina eng mavjud variantlardan eng yaqini tanlangan holda tezdagina natijani olamiz. Albatta bu eng optimal yechim
## bo'lmasligi mumkin, optimalga yaqinroq holda bo'ladi.


## NP-MUAMMO BELGILARI.
## Siz yozgan algoritm misolida ko'ramiz:
    ## 1. Algoritmingiz kichik sonlar uchun tez, katta sonlar uchun juda sekin ishlaydigan muammolar.
    ## 2. "X ning barcha kombinatsiyalari sonini toping" mazmunida boshlanadigan muammolar.
    ## 3. Asosiy yechimni topish uchun barcha yechimlarni ko'rib chiqish talab etiladigan muammolar.
    ## 4. Ketma-ketliklarni qarab chiqish talab qilinadigan muammolar (MUSOFIR MUAMMOSI).
    ## 5. Barcha to'plamlarni ko'rib chiqish talab qilinadigan muammolar (ALOQA OPERATORLARI MUAMMOSI).
    ## 6. Set-covering yoki musofir muammosiga tushadigan barcha muammolar.
## Yuqoridagi belgilar uchraydigan masalalarga optimal yechim topish uchun ko'p vaqtingizni ketkazib o'tirmasdan OCHKO'Z ALGORITMLARDAN
## foydalangan to'g'ri bo'ladi (OPROKSIMATSIYA).

## OPROKSIMATSIYA - To'g'ri yechimni emas, balki to'g'ri yechimga eng yaqin yechimni topish.    







           
    
    
    

 


    
    
    


  
    