# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 11:17:59 2025

@author: DavrServis
"""

## DIJKSTRA ALGORITMI.

## Biz avvalgi darsda GRAF orqali ikkita nuqta o'rtasidagi eng qisqa yo'lni (ENG KAM TUGUNLAR ORQALI O'TILADIGAN YO'L) topishni ko'rdik.
## Endi biz bu holatda faqat tugunlar bilan emas, yo'l misolida olib tugundan tugunga qadar ketadigan vaqtni qo'shadigan bo'lsak (VAZNLI GRAF)
## natijamiz o'zgarib ketishi mumkin.

## DIJKSTRA algoritmi bizga VAZNLI GRAF larda "eng arzon" yo'lni topish uchun ishlatiladi.
## Arzon deganda biz ikki tugun orasidagi vaznlarning yeg'indisini tushunamiz.
    ## Bu vaznlar:
        ## 1. masofa
        ## 2. narx
        ## 3. vaqt
        ## 4. vazn
        ## 5. va o'lchash mumkin bo'lgan boshqa narsalar bo'lishi mumkin.

## ALGORITM QANDAY ISHLAYDI.
    ## 1. Boshlang'ich tugundan borish mumkin bo'lgan  "eng arzon" tugunni topamiz.
    ## 2. Eng arzon tugun qo'shnilarni "narxini" topamiz.
    ## 3. Yuqoridagi qadamlarni barcha tugunlar uchun takrorlaymiz.
    ## 4. Yakuniy yo'lni topamiz.
    
## OT        T         N        

## A   ->    B    ->   2
## A   ->    C    ->   6
## B   ->    C    ->   3
## B   ->    D    ->   4
## C   ->    D    ->   5
## C   ->    E    ->   6
## D   ->    F    ->   5
## E   ->    F    ->   0

## Yuqorida biz bajariladigan ishlarni ko'rib chiqyapmiz. Bu holatda A tugundan ikkita tugunga borish imkoni bor B va C, biz eng arzon yo'lni 
## tanlaymiz (B(2)). Oldimizda yana ikkita yo'l D va C, yana eng arzonini tanlaymiz (C(3)) va shu tariqa davom etamiz toki F ga yetib 
## borgunga qadar. Yakunda biz boshlang'ich (A -> B -> C -> D -> F (15)) natijani olamiz va bizda foydalanilmagan bitta tugun bor (E). Endi
## siklni teskarisiga qaytarib vaznni yanayam kamaytiramiz (F -> E -> C -> B -> A (11)) va yakuniy natijani olamiz.

## Agar vaznlar orasida MANFIY vazn bo'lsachi, bilib qo'yishimiz kerak DIJKSTRA algoritmi MANFIY vaznlar bilan ishlamaydi.

## Biz ikki hil GRAF lar bor deb atdik YO'NALTIRILGAN va YO'NALTIRILMAGAN. Farqi nimada? YO'NALTIRILGAN GRAF lar faqat bir yo'nalishli
## bo'ladi va aksincha YO'NALTIRILMAGAN GRAF lar esa ikki yo'nalishli sodda qilib aytganda bordi keldi mavjud bo'ladi.

## YO'NALTIRILMAGAN GRAF larning yana bir nomi CYCLIC GRAPH (aylanma graf). Misol uchun biz 1-tugundan 2-tugunga o'tamiz va 2-tugundan
## 3-tugunga o'tishimiz mumkin yoki ortga 1-tugunga qaytishimiz mumkin bo'ladi.

## Ana endi DIJKSTRA algoritmi CYCLIC GRAPH lar bilan ishlamaydi, algoritm faqat ACYCLIC GRAPH lar bilan ishlaydi. 


## Oldin ko'rgan BREADTH-FIRST va bugungi DIJKSTRA algoritmini solishtiramiz:

## BREADTH-FIRST algoritmi:
    ## 1. Bosh tugundan oxirgi tugungacha barcha tugunlarni ko'rib chiqadi.
    ## 2. Faqatgina vaznsiz (bir hil vaznli) graflar bilan ishlaydi.
    ## 3. Natija: "Eng qisqa" yo'l.
    ## BIG O: O(N+E). # Tugunlar va yo'llar soniga bog'liq.
    
## DIJKSTRA algoritmi:
    ## 1. Har qadamda eng arzon tugunga o'tadi.
    ## 2. Musbat vaznli va vaznsiz graflar bilan ishlaydi.
    ## 3. Natija: "Eng arzon" yo'l.
    ## BIG O: O(N+E(LogN)). # Bazi manbaalarda Node (tugun) so'zining o'rniga Vertices so'zi ham ishlatiladi shu sababli BIG O o'zgarishi 
    ## mumkin O(V+E(LogN)).

## Manfiy vaznli algoritmlar bilan ishlash talab qilinsa, BELLMAN-FORD algoritmidan foydalanish mumkin.


## AMALIYOT:
import heapq  # Minimal ustunlikli navbat (priority queue) uchun kerak

def dijkstra(graph, start, goal):
    """
    Dijkstra algoritmi yordamida 'start' tugundan 'goal' tugungacha eng qisqa yo'lni topish.
    graph - og'irlikli graf (kalitlar - tugunlar, qiymatlar - qo'shnilar va yo'l og'irliklari).
    start - boshlang'ich tugun.
    goal - maqsad tuguni.
    """
    
    ## 📏 Barcha tugunlarga masofa "infinity" qilib belgilanadi, boshlang'ich tugunga 0. 
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    ## 📍 Har bir tugun uchun eng qisqa yo'lni tiklash uchun ota tygynni saqlash.
    previous_nodes = {node: None for node in graph}
    
    ## 📦 Minimal ustunlikli navbat (masofa va tugun juftligi). Boshlang'ich tugun masofa 0 bilan.
    priority_queue = [(0, start)]
    
    while priority_queue:
        ## 🔽 Navbatdan eng kichik masofali tugunni olamiz.
        current_distance, current_node = heapq.heappop(priority_queue)
        
        ## 🎯 Maqsad tugunga yetib kelsak, qidiruvni to'xtatamiz.
        if current_node == goal:
            print(f"\nMaqsad tugun '{goal}' ga eng qisqa yo'l topildi!")
            break
        
        ## 🔁 Hozirgi tugunning barcha qo'shnilarini ko'rib chiqamiz.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  # Yangi masofani hisoblash.
                
            ## Agar yangi masofa avvalgidan qisqa bo'lsa, yangilaymiz.
            if distance < distances[neighbor]:
                distances[neighbor] = distance # Masofani yangilaymiz.
                previous_nodes[neighbor] = current_node  # Qo'shni tugunning "ota tugunini" belgilaymiz.
                heapq.heappush(priority_queue, (distance, neighbor)) # Yangi masofa bilan navbatga qo'shamiz.
                
    ## 🚦 Eng qisqa yo'lni tiklash (A -> ... -> F).
    path = []
    current = goal
    
    while current is not None:
        path.append(current) # Yo'lni oxiridan boshlang'ich tugunga qarab tiklaymiz.
        current = previous_nodes[current] # Ota tugunga o'tamiz.
    
    path = path[::-1]  # Yo'lni teskari tartibda yozamiz.
    
    ## 🛣️ Natijani ko'rsatish.
    if path[0] == start:
        print(f"Eng qisqa yo'l: {' -> '.join(path)}") # Yo'lni ko'rinishda chiqaramiz.
        print(f"Umumiy masofa: {distances[goal]}") # Maqsad tugunga bo'lgan eng qisqa masofani ko'rsatamiz.
    else:
        print(f"'{start}' dan '{goal}' ga yo'l topilmadi!") # Agar yo'l topilmasa xabar chiqariladi.
    
    return path, distances[goal] # Yo'l va masofani natija sifatida qaytaramiz.

## ✅ Test qilish uchun og'irlikli graf yaratamiz.
graph = {
    "A": {"B": 5, "C": 2}, # A tugunidan B ga 5 masofa, C ga 2 masofa.
    "B": {"D": 4, "E": 2}, # B tugunidan D ga 4 masofa, E ga 2 masofa.
    "C": {"B": 8, "E": 7}, # C tugunidan B ga 8 masofa, E ga 7 masofa.
    "D": {"F": 3}, # D tugundan F ga 3 masofa.
    "E": {"D": 6, "F": 1}, # E tugunidan D ga 6 masofa, F ga 1 masofa.
    "F": {} # F tugunida boshqa qo'shnilar yo'q.
}

## 🛣️ "A" tugunidan "F" tuguniga eng qisqa yo'lni topamiz.
dijkstra(graph, "A", "F")


    
                
    