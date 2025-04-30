# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 22:59:43 2025

@author: DavrServis
"""

## GRAPH (GRAF) - bu TUGUNLAR (NODES) va ularning bog'lovchi QIRRALAR (EDGES) dan iborat ma'lumotlar tuzilmasi. GRAF yordamida obyektlar 
## o'rtasidagi bog'alanishlarni ko'rsatish mumkin bo'ladi.

## QAYERLARDA QO'LLASH MUMKIN.
    ## 1. Navigatsiyada (Google Maps, Waze, Yandex Maps). Bu holatda siz bir manzildan ikkinchi manzilga borish uchun ishlatishingiz mumkin.
    ## Xaritalarda siz istagan manzilga borish uchun bir nechta yo'llarni chizib beradi va siz o'zingizga qulayini tanlaysiz.
    ## 2. Aloqa tarmoqlari. Bu holatda siz bir joydan ikkinchi joyga qo'ng'iroq qilayotkaningizda sizni eng yaqin aloqa tarmoqlari orqali 
    ## bog'lash kerak bo'ladi.
    ## 3. IP routing. Bu holatda bitta serverdan yakuniy foydalanuvchiga biror bir ma'lumotni yuborganda bu ma'lumot bir nechta yo'llar 
    ## orqali borishi mumkin.
    ## 4. Ijtimoiy tarmoqlarda siz taniydigan odamlarni topishda. Bu holatda ham ma'lumotlar graflarda saqlanadi.
    ## 5. Robot/Dron uchun yo'l topishda. Bu holatda ham dronlar bir nuqtadan ikkinchi nuqtaga uchgan vaziyatda parvoz marshrutini chizadi.
    

## Endi shu GRAF lar orqali qanday qilib ma'lumotlar qidirish mumkin. Buning uchun bizga BREADTH-FIRST SEARCH yordamga keladi va bu qidirish 
## algoritmi aynan GRAF lar bilan ishlaydi.

## Yuqoridagi algoritmni ishlatish orqali biz ikkita savolga javob olamiz:
    ## 1. A va B node orasida yo'l bormi?
    ## 2. A dan B ga eng yaqin yo'l qaysi?


## Misol orqali tushunishga harakat qilamiz.
## Siz ijtimoiy tarmoqdasiz va sini bir qancha do'stlaringiz qamrab olgan va shu do'stlardan qaysi biridur sizni mashxur odam bilan bog'lay 
## oladi. 

## Vazifamiz, siz mashxur odam bilan aloqa o'rnata olasizmi va qaysi do'stingiz orqali buni amalga oshirishingizni topish.

## Demak ishni boshlaymiz, boshlanishiga eng yaqin do'stlarimizni aniqlab olamiz (Ali, Vali va Tohir).
## Endi mahsxur odamni Elon Musk deb olamiz.
## Endi birinchi bo'lib do'stlarni tekshiramiz ular orasida bizga kerakli odam bormi (tabiiyki yo'q).
## Do'stlarimizni birma-bir tekshirib chiqamiz ular ichida bizga kerakli odam yo'q. Shu o'rinda BREADTH-FIRST SEARCH algorimi ishlashini
## tushinishimiz kerak.
## Ya'ni agar do'stlarimiz orasida bizga kerakli odam bo'lmasa, ularning do'stlarini ham ro'yxatga qo'shamiz.
## Bizda tahminan [Ali, Vali, Tohir, Olim, Aziza, Botir, Ziyoda, Elon Musk, Mohir] ko'rinishidagi ro'yxat hosil bo'ldi ro'yxatni tekshirsak
## Elon Musk ro'yxatda mavjud, demak biz birinchi savolimizga javob oldik. Siz va Elon Muskni o'rtasida aloqa o'rnatsa bo'lar ekan.
## Ikkinchi qiladigan ishimiz, bu amalni nechta qadam orqali amalaga oshirishimiz mumkin. Bu savolga ham javob aslida tayyor, ya'ni biz 
## birinchi do'stlarimizni orasidan qidirdik va keyin do'stlarimizni do'stlarini tekshirdik, xulosa 2 qadam bilan biz buni amalga oshirdik.

## Shu o'rinda savol tug'ulishi mumkin yuqoridagi ro'yxatni yani avval do'stlarimiz va keyin do'stlarimizni do'stlari ro'yxatini qanday
## tuzdik.
## Demak bizda ro'yxat mavjud edi va biz bu ro'yxatni tepadan tekshirib tushdik va pastiga yangi ma'lumotlarni qo'shdik bu esa QUEUE deb 
## ataladi.

## Yuqorida ko'rganimiz bu yo'naltirilgan GRAF (directed graph) deyiladi. Chunki bu ro'yxatdagi elementlarda bog'lanishlar bir taraflama bo'ladi. Ya'ni
## mendan meni yaqin do'stlarimga yo'nalish bor lekin qaytish yo'q, bu huddi obuna bo'lishga o'xshaydi. Men ularga obuna bo'lganmanu, ular
## menga obuna bo'lishmagan.

## Bizda yana yo'naltirilmagan GRAF lar ham bo'ladi (undirected graph). Pythonda GRAF larni DICTIONARY (lug'at, hash jadvali) yordamida 
## yaratish mumkin.

## Yuqorida ko'rib o'tgan GRAF imizni ko'rinishini quyidagicha tasvirlasak bo'ladi.


## PYTHONDA GRAF YARATISH.
## graph = {} # Bo'sh graph.
## graph['siz'] = ['ali', 'vali', 'tohir'] # Bu yerda sizga bog'langan qo'shnilar. Bu holatda qo'shnilar ham bir taraflama bo'ladi.
## graph['ali'] = ['aziza', 'olim'] # Bu holatda ham ALI ga AZIZA va OLIM qo'shni lekin OLIM va AZIZA ga ALI qo'shni bo'la olmayddi.
## graph['vali'] = ['botir', 'ziyoda']
## graph['tohir'] = ['elon musk', 'mohir']
## graph['olim'] = [] # OLIM ning qo'shnilari yo'qligi uchun ro'yxat bo'sh qoldi.
## graph['aziza'] = []
## graph['botir'] = []
## graph['ziyoda'] = ['aziza']
## graph['elon musk'] = []
## graph['mohir] = []

## BEVOSITA PYTHONDA ESA BU KOD QUYIDAGICHA BO'LADI:
# graph = {'siz':['ali', 'vali', 'tohir'],
#          'ali':['aziza', 'olim'],
#          'vali':['botir', 'ziyoda'],
#          'tohir':['elon musk', 'mohir'],
#          'olim':[],
#          'azia':[],
#          'botir':[],
#          'ziyoda':['aziza'],
#          'elon musk':[],
#          'mohir':[]
#     }

## TO'LIQ KODNI YOZISHNI BOSHLAYMIZ.
from collections import deque # deque - ikki tomonlama navbat (queue) yaratishi mumkin.

def search(start_node, target = 'elon musk'):
    """
    GRAF yordamida 'target' (elon musk) nomli shaxsni qidiruvchi funksiya.
    start node - qidiruvni boshlash kerak bo'lgan tugun (node).
    target - qidirilayotgan shaxs (standart 'elon musk').
    """
    
    search_queue = deque() # Qidiruv uchun navbat yaratamiz.
    search_queue += graph[start_node] # Bosglang'ich tugunning barcha qo'shnilarini navbatga qo'shamiz.
    searched = set() # Qidiruvdan o'tgan (tekshirilgan) odamlarni saqlash uchun to'plam (set)
    
    ## Navbat bo'sh bo'lmaguncha qidirishni davom ettiramiz.
    while search_queue:
        person = search_queue.popleft() # Navbatdagi birinchi elementni olamiz.
        if person not in searched: # Agar bu odam ilgari tekshirilmagan bo'lsa.  
            if person  == target: # Agar bu odam qidirilayotgan shaxs bo'lsa.
                print(f"{target}ni topdik!") # Qidiruv muvoffaqiyatli!
                # print (searched).
                return True # Funksiyani tugatamiz va True qaytaramiz.
            else: # Aks holda.
                search_queue += graph[person] # Odamning qo'shnilarini navbatga qo'shamiz.
                searched.add(person) # Ushbu odamni esa tekshirilganlar ro'yxatiga qo'shamiz.
    return False # Agar navbat tugasa va topilmasa, False qaytaramiz.

if __name__ == '__main__': 
    graph = {'siz':['ali', 'vali', 'tohir'],
             'ali':['aziza', 'olim'],
             'vali':['botir', 'ziyoda'],
             'tohir':['elon musk', 'mohir'],
             'olim':[],
             'aziza':[],
             'botir':[],
             'ziyoda':['aziza'],
             'elon musk':[],
             'mohir':[]
        }
    print(search('siz', 'elon musk'))