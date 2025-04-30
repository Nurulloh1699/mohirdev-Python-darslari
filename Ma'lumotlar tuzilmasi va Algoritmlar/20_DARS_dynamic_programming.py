# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 15:19:26 2025

@author: DavrServis
"""

## DYNAMIC PROGRAMMING.

## DYNAMIC PROGRAMMING - Bu muammoni BIR NECHTA MAYDA muammolarga bo'lib, ularga yechim topish orqali katta muammoga yechim topish usuli.

## MISOL sifatida o'tgan darsimizda ko'rgan THE KNAPSACK PROPLEM muammosini ko'ramiz:

## The Knapsack Problem:
    ## 1. Bizda M kilo sig'adigan qop bor.
    ## 2. Do'konda N ta element bor. Har bir elementning VAZNI va NARXI turlicha.
    ## 3. MUAMMO: Qopga sig'adigan eng qimmat elementlar kombinatsiyasini topish.
    
## Demak bu yerda o'g'ri do'konga qop bilan kirdi, uning qopiga deylik 4 kg narsa sig'adi. Endi do'konda quyidagilar bor.
    ## 1. Noutbuk - 3kg -> 2000$
    ## 2. MacPro  - 4kg -> 3000$
    ## 3. MacMini - 1kg -> 1500$
## Vazifa og'ri qopiga sig'adigan eng foyda keltiradigan narsalarni olib chiqib ketishdan iborat.

## Agar GREEDY algoritmidan foydalansak:
    ## Yechim tez lekin optimal bo'lmaydi. Ya'ni agar tezlikga etibor qaratsak, o'g'ri bir qarashda eng qimmat narsa bo'lgan MacPro ni oladi.

## Agar biz ENG OPTIMAL yechimni olmoqchi bo'lsak:
    ## OPTIMAL YECHIM: Barcha kombinatsiyalarni ko'rib chiqishimiz kerak bo'ladi. Bizda esa quyidagi kombinatsiyalar hosil bo'ladi:
        ## Noutbuk     MacPro     MacMini     JamiVazn     JamiNarx
        ## 0           0          0           0 kg         0$    ✅
        ## 0           0          1           1 kg         1500$ ✅
        ## 0           1          0           4 kg         3000$ ✅
        ## 0           1          1           5 kg         4500$ ❌
        ## 1           0          0           3 kg         2000$ ✅
        ## 1           0          1           4 kg         3500$ ✅ eng ko'p foyda keltirgani uchun eng to'g'ri javob shu ✅
        ## 1           1          0           7 kg         5000$ ❌
        ## 1           1          1           8 kg         6500$ ❌
## Bu yerda o'g'ri qanday yo'l tutsa qanday natijaga erishishsi mumkinligini ko'rishimiz mumkin. 


## Endi shu muammoni DYNAMIC programming bilang hal qilishga urinib ko'ramiz:
    ## OPTIMAL YECHIM: Dynamic programming. Muammoni bir nechta mayda muammolarga bo'lamiz.
    
## Avallida jadval yaratiladi:
    ##                          1kg     2kg     3kg     4kg      
    ## MacMini - 1kg, 1.5k$     1.5k$   1.5k$   1.5k$   1.5k$
    ## MacPro  - 4kg, 3k$       1.5k$   1.5k$   1.5k$   3k$
    ## Noutbuk - 3kg, 2k$       1.5k$   1.5k$   2k$     3.5k$
    
## Mummoni hal qilish uchun uni mayda muammolarga bo'lib olib hal qilamiz, ya'ni avalliga 1kg sumka uchun keyin 2kg sumka uchun va xokazo
## davom etamiz. Do'kondagi mahsulotlar uchun ham shunday avalliga do'konda faqat bitta mahsulot bor deb olinadi.

## DYNAMIC programmingninga avzalliklaridan biri agar bizda yana bitta mahsulot paydo bo'lsa hamma hisobkitobni boshidan boshlash talab
## qilinmaydi, shunchaki jadvalga yana bir mahsulot qo'shiladi holos.
    ##                          1kg     2kg     3kg     4kg      
    ## MacMini - 1kg, 1.5k$     1.5k$   1.5k$   1.5k$   1.5k$
    ## MacPro  - 4kg, 3k$       1.5k$   1.5k$   1.5k$   3k$
    ## Noutbuk - 3kg, 2k$       1.5k$   1.5k$   2k$     3.5k$
    ## Iphone  - 1kg, 2k$       2k$     3.5k$   3.5k    4k$
    
## Deylik yana bir mahsulot qo'shilsa 1kg lik Ipad 1000$ narx bilan. Bu holatda ham faqatgina jadvalimizning pastiga yana bitta qator
## qo'shishimiz kifoya bo'ladi.
    ##                          1kg     2kg     3kg     4kg      
    ## MacMini - 1kg, 1.5k$     1.5k$   1.5k$   1.5k$   1.5k$
    ## MacPro  - 4kg, 3k$       1.5k$   1.5k$   1.5k$   3k$
    ## Noutbuk - 3kg, 2k$       1.5k$   1.5k$   2k$     3.5k$
    ## Iphone  - 1kg, 2k$       2k$     3.5k$   3.5k$   4k$
    ## Ipad    - 1kg, 1k$       2k$     3.5k$   4.5k$   4.5k

## Ko'rib turganingizdek biz ortiqcha qiyinchiliksiz mahsulotlar soni o'zgarishini tahlil qilishimiz mumkin, ya'ni mahsulotlarning
## ko'payishi bizning dasturimizning amallar sonini keskin oshishiga sabab bo'la olmaydi. Bunga albatta biz bitta katta muammoni kichik 
## muammolarga bo'lib olganimiz sabab bo'lyapti. Albatta yangi mahsulotlar qo'shilishi bilan natijamiz o'zgaradi lekin amallar soni keskin
## oshib ketmaydi.
  
 
