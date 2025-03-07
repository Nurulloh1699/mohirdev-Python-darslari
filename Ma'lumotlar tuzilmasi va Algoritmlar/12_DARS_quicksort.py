# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 10:09:15 2025

@author: DavrServis
"""

## QUICKSORT.

## QUICKSORT - bu tartiblash algoritmi. Oldingi darslarda ko'rganimiz SELECTION SORT dan ko'ra boshqacharoq yondashilgani uchun, undan
## tezroq hisoblanadi.

## QUICKSORT avvalgi darslarda ko'rgan SELECTION SORT ga nisbatan bir necha barobar tezroq, DIVEDE and CONQUER usuli yordamida yaratilgan
## shu asosda ishlaydi.

## Tasavvur qilamiz biz biror ARRAY elementlarini tartibga keltirmoqchimiz.
## Birinchi qiladigan ishimiz TO'XTASH SHARTI (base case) topish.
## Toxtash sharti ikki hil bo'lishi mimkin:
    ## 1. Bo'sh ARRAY bo'lsa [ ].
    ## 2. ARRAY imiz faqat bir elementdan iborat bo'lsa [9].
## Yuqoridagi ikki holatda ARRAY tartiblangan deb hisoblaymiz.
## To'xtash sharti uchun oddiy funksiya yozamiz:
def quicksort(array):
    if len(array) < 2:
        return array
## Agar ARRAY 2ta elementdan iborat bo'lsa, tartiblash oson:
    ## Birinchi elementni 2 - element bilan solishtiramiz va talab qilinsa o'rnini almashtiramiz: [12, 10] -> [10, 12].
## Agar ARRAY elementlari 3ta elementdan iborat bo'lsachi? Misol uchun: [25, 20, 5].
## Bu holatda QUICKSORT quyidagicha ishlaydi:
    ## 1. Bizga bitta tayanch nuqtasi kerak bo'ladi. Ixtiyoriy element TAYANCH NUQTASI (PIVOT) qilib olamiz: [25✅, 20, 5].
    ## 2. Tayanch elementadan kichkina, elementlarni NUQTADAN chapga, katta elementlarni nuqtadan o'nga ajratamiz: [20, 5] + 25.
    ## ETIBOR BERING! DIVIDE and CONQUER metodi orqli bizni muammoyimiz kichrayib borishi kerak va biz shuni kuzatyapmiz.
    ## 3. Toki TO'XTASH SHARTIGA YETGUNGA QADAR chapdagi va o'ngdagi elementlar uchun yuqoridagi qadamlarni takrorlaymiz (REKURSIYA).
    ## Bizning holatda: [20✅, 5] -> [5] + 20. Endi [5] bitta o'zi qoldi va TO'XTASH SHARTI bajarildi, dastur to'xtaydi.
    ## Foydalanuvchiga  tartiblangan ARRAY qaytariladi: [5, 20, 25].
    
## Kattaroq ARRAY lar uchun ham huddi shu tartibda ishlaydi:
    ## 1. ARRAY qabul qilib olinadi: qsort[22, 25, 20, 5].
    ## 2. Tayanch nuqta tanlaymiz: [22✅, 25, 20, 5] -> qsort[20, 5] + 22 + qsort[25], 25 TO'XTASH SHARTIga to'g'ri keldi.
    ## 3. TO'XTASH SHARTI bajarilguncha yuqoridagi amallarni qaytaramiz: [20✅, 5] -> qsort[5] + 20, Natija: 5, 20 tartiblandi.
    ## 4. Yuqoridagi ajralibh qolgan elment ham TO'XTASH SHARTIni bajargani uchun: 25ni o'zini qaytaradi. Bu amallar CALL STACK bo'lib 
        ## ishlaydi, ya'ni TO'XTASH SHARTI qanoatlantirilmaguncha natija uzatmaydi, hamma elementlar o'z joyini egallagandan keyin esa 
        ## bixga natija qaytadi: [22✅, 25, 20, 5] -> qsort[20, 5] + 22 + qsort[25] = [20, 5, 22, 25]
                             ##  [20✅, 5] -> qsort[5] + 20 = [5, 20]
                             ##  [5, 20, 22, 25] -> shu asnoda hamma elementlar tartiblandi.

## QUICKSORT algoritmi tez ishlashi uchun tayanch elementini tasodifiy olgan afzal(doim ARRAY ning birinchi elementi olingan holda 
## SELECT SORT kabi BIG O qiymati O(n²) bo'lishi mumkin).
## Aslida esa QUICKSORT algoritmi uchun BIG O:  O(nlogn) -> O(n ko'paytirilgan logorifm n ga teng).  

## QUICKSORT ningfunksiyasi bilan tanishamiz:
from random import randrange # "randrange" funksiyasini "random" kurubxonasidan import qilamiz. Bu funksiya tasodifiy indekstanlash uchun
## ishlatiladi.
def qsort(array): # "qsort" funksiyasi "massiv"ni saralaydi. ARRAY kiruvchi massiv. 
    """
       Tezkor saralash (QUICK SORT) algoritmi rekursiya yordamida
       ARRAY: Saralanishi kerak bo'lgan ro'yxat (massiv)    
    """
    # if len(array) < 2: # TO'XTASH SHARTI. Agar massivda 2tadan kam element bo'lsa, u allaqachon saralangan hisoblanadi.
    #     return array # ARRAYni o'zini qaytaradi.
    # else: # Aks holda.
    #     privot = array.pop(randrange(len(array))) 
    #     ## "privot" elementini tanlash:    
    #         ## 1. "ranrange(len(array))" yordamida massivdan tasodifiy indeks tanlanadi.
    #         ## 2. "array.pop()" yordamida tanlangan indeksdagi element olib tashlanadi va "privot" o'zgaruvchisiga o'zlashtiriladi.
    #     ## "privot" - bu massivni kichik va katta qismlarga ajratishda foydalaniladigan element.
    #     kichik = [i for i in array if i <= privot]
    #     ## Kichik (chap) qismini yaratish:
    #             ## List comprehension usuli yordamida "array" elementlari orasidan "privot"dan kichik yoki teng bo'lgan element olinadi.
    #             ## Masalan, agar "privot = 10" va "array = [5, 8, 12, 22] bo'lsa.
    #                 ## kichik = [5, 8]
    #     katta = [i for i in array if i > privot]
    #     ## Katta (o'ng) qismini yaratish:
    #         ## "privot" dan katta bo'lgan elementlar tanlab olinadi.
    #         ## Masalan, agar "privot = 10" va "array = [5, 8, 12, 22]" bo'lsa.
    #             ## katta = [12, 22]
    #     return qsort(kichik) + [privot] + qsort(katta) 
    #     ## REKURSIYA yordamidakichik va katta qismlar yana "qsort" funksiyasiga yuboriladi.
    #     ## Birlashtirish:
    #         ## Avval saralangan kichik qism, keyin "privot" va oxirida saralangan katta qism qo'shiladi.
    #     ## Har bir REKURSIYA chaqiruvida massiv kattaligi kichrayib boradi va oxir-oqibat bazaviy holatga (TO'XTASH SHARTIga) yetadi.                          
                        
## AMALIYOT.
from random import randrange
def qsort(array):
    if len(array) < 2:
        return array
    else:
        # pivot = array.pop(0)
        pivot = array.pop(randrange(len(array)))
        kichik = [i for i in array if i <= pivot]
        katta = [i for i in array if i > pivot]
        print(f"{kichik} + [{pivot}] + {katta}")
        return qsort(kichik)  + [pivot] + qsort(katta)
    
if __name__ == '__main__':
    # array1 = [1, 5, 12, 0, -5, 66]
    # print(array1)
    # print(qsort(arra1))
    array2 = list(range(21))
    print(array2)
    print(qsort(array2))




## QUICKSORT algoritmini yanayam yaxshiroq tushunish uchun biz avval muammolarga yechim topishning o'ziga xos usuli bilan tanishamiz.
## Bu usul yuqorida ko'rganimiz DIVIDE and CONQUER yani BO'LIB TASHLAB, HUKMRONLIK QIL deb ataladi.

## DIVIDE and CONQUER metodi katta va murakkab muammolarga sodda yechim topish uchun ishlatiladi.

## Demak DIVIDE and CONQUER metodi, katta va murakkab muammolarga duch kelinganda ularni mayda muammolarga ajratib, ularga yechim topish
## orqali katta muammoni ham hal qilish demakdir.

## Misol uchun tasavvur qiling siz fermersiz va sizda 168m ga 68m lik yer maydoni bor, sizning vazifangiz maydonni bir nechta kvadratlarga
## bo'lishdan iborat. Kvadratlar imkon qadar katta bo'lishi kerak.

## 1. Maydonni teng ikkiga bo'lish (Bu holatda bo'lingan bo'laklar to'g'ri to'rtburchak shakliga kelib qoladi va bu xato).
## 2. Maydonni juda ko'p kvadratchalarga bo'lish. (Bu holatda bo'laklar hajmi juda kichik bo'lib ketadi).
## 3. Maydonni tavakkal bo'laklarga bo'lish (Bu holatda kvadratlarning hammasi ham bir xil bo'lmasligi mumkin).

## Shu tarzda biz qo'lda har hil metodlarni qo'llab chiqsak bu ko'p vaqt olishi mumkin.

## Bu holatda biz DIVIDE and CONQUER metodini esga olamiz. Bu holatda avval ko'rib o'tgan REKURSIYA ma'lumot tuzilmasi DIVIDE and CONQUERga
## misol bo'la oladi.

## REKURSIYA da bu masalani yechish uchun bizga kerak bo'ladi:
## 1. To'xtash sharti.
## 2. To'xtash shartiga yetib borgunga qadar bajariladigan amallar (rekursiyani takrorlash).

## Berilgan topshiriqni shartiga ko'ra eng katta va bir-biriga teng bo'lgan kvadratlarga bo'lish:
## 1. Mavjud 168x64 maydonni bo'lish uchun tomonlarni kichigini aniqlab, shu asosda maydonni bo'lamiz. Bizda 2ta 64x64 va 1ta  40x64 maydon 
## hosil bo'ldi, endi biz etiborimizni 1ta 40x64 maydonga qartamiz, chunki qolgan ikki maydon teng to'rtburchaklarga bo'lindi. Demak davom 
## etamiz.

## 2. Tomonlarni eng kichigini aniqlab, shu asosda kvadratga bo'lamiz. Bizda 1ta 40x40 va 40x24 maydon hosil bo'ldi yuqoridagi amallarni 
## takrorlaymiz. Oxirgi holatda bizda 8x8 teng to'rtburchaklar hosil bo'ldi va bu bizning masalamizga yechim bo'ladi.

## Yani 168x64 maydonni eng katta va teng to'rtburchaklarga bo'lishda, bizga eng optimal yechim 8x8 to'rtburchaklar ekan.

## Shubhalarga o'rin qolmasligi uchun matematik va geometrik jihatdan yondashuv kifoya. Chunki hosil bo'lgan eng katta kvadratlar 
## (64x64, 40x40, 40x24) tomonlarini ham 8 ga qoldiqsiz bo'lish mumkin. Bu aytib o'tganimiz eng kichik maydon orqali topgan yechimimiz 
## qolgan katta maydonlar uchun ham yechim bo'la oladi deganimiz YEVKLID algoritmi deb ataladi.

## Hozirgi qilgan amaliyotimiz EKUB ga to'g'ri keladi, ya'ni biz berilgan ikki tomon uchun Eng Katta Umumiy Bo'luvchini toptik holos.

## Etibor bergan bo'lsangiz, masalamizga yechim topish uchun biz har gal bir xil amaliyot bajardik va to'xtash shartigacha yetib bordik.
## To'xtash sharti esa bizning masalamizga yechim bo'ldi. 


## AMALIYOT.
## 2 sonning eng katta umumiy bo'luvchisiтш (EKUB) topuvchi funksiya yozish.

## Buning uchun quyidagi ikki usuldan foydalanish mumkin:

## Sonlarni ayirish usuli:

## Deylik bizga 45 va 27 sonlari berilgan, keling ularning EKUB topamiz.
# def ekub_ayirish(a, b): # Ikkita qiymat qabul qiladigan funksiya.
#     """Sonlarni ayirish usuli yordamida EKUB topish (REKURSIV usul)"""
#     if a == b:
#         return a # To'xtash sharti: Agar sonlar teng bo'lsa, ularning o'zlari berilgan sonlaning EKUBi bo'ladi.
#     elif a > b:
#         return ekub_ayirish(a - b, b) # Kattasida kichigini ayirish.
#     else:
#         return ekub_ayirish(a, b - a) # Kichigidan kattasini ayirish.
    
## **Test qilish**
# a, b = 45, 27
# print(f"Sonlarning ayirish usuli bilan EKUB ni topish: \n{a}, {b} = {ekub_ayirish(a, b)}")


## Sonlarni bo'lish va qoldiq olish usuli.

## Ikkita sondan kattasini kichigiga bo’lib qoldiq olamiz.

## Ularni o’rnini almashtiramiz.

## 1- va 2-qadamlarni sonlardan biri nol bo’lib qolguncha davom ettiramiz.

## Qolgan son shu ikki son uchun EKUB bo’ladi.

## 45 va 27 sonalri uchun EKUB hisoblaymiz:
# def ekub_bolish(a, b): 
#     """Sonlarni bo'lish usuli yordamida EKUB topish (REKRUSIV usul)"""
#     if b == 0:
#         return a # To'xtash sharti: Agar b = 0 bo'lsa, a qiymat EKUB bo'ladi.
#     else:
#         return ekub_ayirish(b, a % b) # Kattasini kichigiga bo'lib qoldiqni olish.
    
# ## **Test qilish**
# a, b = 55, 27
# print(f"Bo'lish va qoldiq olish usuli bilan EKUB ni topish: \n({a}, {b}) = {ekub_bolish(a, b)}")