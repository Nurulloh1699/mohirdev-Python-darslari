# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 11:52:23 2025

@author: DavrServis
"""

## YAKUNIY DARS.

## Bu darsda kurs davomida ko'rilmagan, lekin ko'rib chiqishga tavsiya etiladigan ba'zi bir algoritmlar va ma'lumotlar tuzilmalariga 
## to'htalib o'tamiz.

## 1 - KO'RADIGAN MA'LUMOTLAR TUZILMASI BU TREE.

## Kurs boshida ARRAY ma'lumotlar tuzilmasi bilan tanishgan edik.
    ## AFZALLIGI: Binary Search yordamida tez qidirish.
    ## KAMCHILIGI: Har ma'lumot qo'shgandan so'ng ARRAY ni tartiblash (sorting).
    
## MUAMMO: Ma'lumotlarni tartiblangan holda qo'shish mumkinmi?
## Yechim: Binary Search Tree ma'lumotlar tuzilmasi.

## Binary Search Tree qanday ishlashini ko'ramiz:
    ## Deylik bizda ro'yxat bor. Bu ro'yxatda TOHIR degan element bor va biz yangi MOHIR degan o'zgaruvchi qo'shmoqchimiz.
    ## Bilamizki M harfi T harfidan oldin keladi, demak yangi elementimiz ro'yxatda birinchida bo'lishi kerak.
    ## Shu tarzda davom etadi, ya'ni yangi qo'shilgan element avtomatik ravishda alifbo tartibida tartiblanadi va ro'yxatimizda o'z joyini
    ## egallaydi.

## Qidirish osonligi:
    ## Ro'yxatimiz tartiblangan bo'lganligi uchun qidirish ham birmuncha tez bo'ladi ya'ni ortiqcha vat olmaydi.
    ## Binary Search da odatda element qo'shish qiyinroq (ya'ni yangi element qo'shish uchun mavjud elementlarni birma-bir surib chiqishimiz
    ## kerak edi).
    ## Binary Search Tree esa bunday emas huddi qidirish kabi qo'shish ham ko'p vaqt olmaydi.
    

## BINARY SEARCH TREE TURLARI:
    ## Boshqa (tree) shajara turlari.
        ## 1. Red-black tree (o'zini muvozanatga keltiradi).
        ## 2. B-tree (ma'lumotlar bazasida ishlatiladi).
        ## 3. Heap.
        ## 4. Splay tree.



## 2 - KO'RADIGAN MA'LUMOTLAR TUZILMASI BU INVERTED INDEXES.

## Tasavvur qiling bizda 3ta internet sahifasi bor va ular quyidagi ma'lumotlarni o'zida saqlaydi:
    ## Mohir.dev
        ## 1. Python.
        ## 2. JavaScript.
        ## 3. Data Science.
        ## 4. HTML.
        
    ## Sariq.dev
        ## 1. Python.
        ## 2. Django.
        ## 3. Sql.
        ## 4. Data Science.
        
    ## Mayoq.uz
        ## 1. JavaScript.
        ## 2. HTML.
        ## 3. Bootstrap.
        ## 4. Css.
        
## Demak bular har bir sahifaga tegishli bo'lgan kalit so'zlar. Endi tasavvur qiling siz Google ni toki Yandex ni ochtingizda Python degan 
## so'rovni beryapsiz. So'rovingizga javoban brauzer sizga minglab natijalarni qaytaradi. Aynan shuni qidirish algoritmlari INVERTED INDEXES
## ma'lumotlar tuzilmasi yordamida qiladi.

## Keling buni qanday ishlashini ko'ramiz:
    ## Avvaliga bu so'zlarning har biri uchun hash jadvalini yaratamiz.
        ## KALIT            QIYMAT
        ## python           mohir.dev, sariq.dev
        ## javascript       mohir.dev, mayoq.uz
        ## data science     mohir.dev, sariq.dev
        ## html             mohir.dev, mayoq.uz
        ## django           sariq.dev
        ## sql              sariq.dev
        ## bootstrap        mayoq.uz
        ## css              mayoq.uz
        
## Hash jadval bu doim ikki qismdan iborat jadval kalit (kalitlar takrorlanmas bo'lishi kerak) va unga mos keluvchi so'zlar.
## Kyinchalik qidiruv maydoniga PYTHON db yozganimizda MOHIR.DEV va SARIQ.DEV platformasi natija sifatida qaytariladi.



## 3 - KO'RADIGAN ALGORITMIMIZ FURYE ALMASHTIRISHLARI ALGORITMI (FURYE TRANSFORMS).

## Qayerlarda ishlatiladi?
    ## 1. Signallarga ishlov berish uchun ishlatiladi.
    ## 2. Audioni alohida chastotalarga ajratish.
    ## 3. Rasmlarga ishlov berish.
    ## 4. Jarayonlarni bashorat qilish.
    ## 5. Turli sensorlar (yorug'lik sensorlari, video sensorlar).
    ## 6. DNK tahlili va hokazo.



## 4 - KO'RADIGAN ALGORITMIMIZ PARALLEL ALGORITMLAR.

## Bu algoritmlar qachon kerak? Mana bugungi kunda biz judayam katta ma'lumotlarga ishlov berishga to'g'ri kelyapti. Misol uchun, sizda
## terabaytlab rasmlar bo'lishi mumkin yoki terabaytlab tekstlar bo'lishi mumkin, juda katta ma'lumotlar bor. Misol uchun, deylik serverda
## millionlab foydalanuvchilar haqida ma'lumotlar saqlanadi. Bu ma'lumotlarga ishlov berishni siz eski usullar bilan qilaman desangiz bu
## judayam ko'p vaqt oladi. Shuning uchun zamonaviy kompyuterlarni qarasangiz, ularda bir necha yadroli protsessorlar bo'ladi. Bir nechta
## yadroli protsessorlarni maqsadi, bitta katta vazifani bir nechta mayda vazifalarga bo'lib ularni parallel bajarishdan iborat.

## Lekin aytib o'tish kerak bu paralellikni yaratish oson emas ya'ni dasturingiz bir vaqtning o'zida bir nechta qismi ishlashini 
## taminlash kerak bu esa oson emas.

## Afzallik va kamchiliklarini ko'rib chiqamiz:
    ## 1. Ulkan ma'lumotlarga ishlov berishni tezlashtirish usuli.
    ## 2. Zamonaviy kompyuterlarda bir necha yadroli prosessorlar o'rnatilgan.
    ## 3. Katta vazifani bir nechta mayda vazifalarga bo'lib parallel bajarish natijaga tezroq olib keladi.
    ## 4. Lekin parallel algoritmlar yaratish oson emas:
        ## 1. Jarayonlar bir-biriga bog'liq bo'lishi mumkin (ya'ni bir jarayonning natijasi ikkinchi jarayon uchun kerak bo'lishi). 
        ## 2. Parallel bajarilgan vazifalarni jamlash vaqt oladi.
        ## 3. Jarayonlarni muvozanat qilish qiyinligi (1- jarayon ozroq vaqt olib keyingi jarayon ko'proq vaqt olishi mumkinligi).
        


## 5 - KO'RADIGAN ALGORITMIMIZ BLOOM FILTERS.

## BLOOM FILTERS Nimalagini tushinish uchun quyidagi misolga etibor qaratamiz.
    ## * Google kuniga millionlab saytlarni indeksasiya qiladi.
    ## * Har kuni yana millionlar yangi sahifalar (video/rasm/post) yaratiladi.
    ## * Bitta sahifani qayta indeksasiya qilmaslik uchun indeksasiya qilingan saytlar ro'yxatini saqlab borish kerak.
    ## * Oson yo'li indeksasiya qilingan saytlarni hash jadvali ko'rinishida saqlash.
        ## * Hash jadvalidan o'qish vaqti O(1) ga teng.
        ## * MUAMMO: Milliardlab saytlar haqidagi jadvallarni saqlash uchun terrabaytlab joy kerak.
        ## * YECHIM: Bloom filter.
        
## BLOOM FILTER - bu ehtimoliy (probabilistic) ma'lumotlar tuzilmasi.
## Hash jadvali o'rniga Bloom filyerga sayt manzilini berish va bu sayt indeksasiya qilinganligi ehtimollini bilish mumkin.
    ## MISOL: 87% ehtimollik bilan indeksasiya qilingan.
## Bloom filterlar 100% aniqlik bermaydi, lekin juda kam joy egallaydi.



## 6 - KO'RADIGAN ALGORITMIMIZ HyperLogLog deb ataladi (BLOOM FILTERga o'xshab ketadi).

## HyperLogLog nimaligini tushunish uchun quyidagi misolni ko'ramiz:
    ## Amazon e-bozori foydalanuvchi ko'rgan (izlagan) mahsulotlar ro'yxatini saqlab borishi kerak (bunga yana TikTok, YouTube va boshqa
## video platformalarini ham misol qilish mumkin).
    ## Millionlab foydalanuvchilar milliardlab mahsulotlar qidiradi (video platformalar misolida ko'radigan bo'lsak foydalanuvchilarning
## ko'radi va layk bosadi).
    ## Har bir foydalanuvchi haqida bu ma'lumotlarni saqlab borish (logging) xotirada juda katta joy talab qiladi.
    ## YECHIM: HyperLogLog.
    ## Bu yechim ham BLOOM FILTER ka'bi ehtimollar nazariyasiga asoslangan va tahminiy yechim qaytaradi.
    
## HyperLogLog - bu foydalanuvchilar haqida ma'lumotlarni yeg'ib ularni yoqtiradigan narsalarini tahlil qilib, shunga qarab ushbu
## foydalanuvchiga yoqishi mumkin bo'lgan ma'lumotlarni qaytaradi.



## 7 - KO'RADIGAN ALGORITMIMIZ SECURE HASH ALGORITHM (SHA).

## Biz darslarimizni boshida hash jadvallar haqida gaplashgan edik hash jadvallar nima qiladi, hash jadvallar kalit so'zni biror bir
## indeksga o'zgartiradi.
## Agar siz jadvalda BANANA degan so'zni saqlamoqchi bo'lsangiz, bu so'zni raqamga o'zgartiradi va endi BANANA so'zi ro'yxatdagi 
## 0 - indeksga joylashtiriladi. Hash jadvallarining afzalligi, hash jadvallaridan qidirish juda tez sodir bo'ladi O(1).

## SECURE HASH ALGORITHM (SHA) algoritmi ham hash jadvallar asosida ishlaydi.
## Ammo hesh jadvallardan farqli ravishda (hesh da biz matnni songa o'zgartirgan edik) bitta matnni boshqa matnga o'zgartiramiz.
## Buning afzalligi shundaki bu o'zgartirilgan matnlar boshqa so'zning o'zgartirilgan matnlarida qaytarilmaydi.

## Misolda ko'radigan bo'lsak deylik siz internetdan katta fayl yuklayapsiz va orada internet ulanishida nosozlik sodir bo'ldi va
## yuklanayotgan faylga ziyon yetgan bo'lishi mumkin (kamchilik bilan yuklangan va hokazo) shuni tekshirish uchun bunday katta fayllar
## uchun SHA hash qiymati yaratilgan bo'ladi. 
## Demak siz o'zingizni kompyuteringizda ham uchbu hash qiymatni mos ravishda yaratasiz (deylik saytdagi qiymat SHA256 da yaratilgan) 
## va tekshirib olishingiz mumkin.

## Ikkinchi misolda, deylik siz google da ro'yxatdan o'tgansiz va parol qo'ygansiz ("abc123").
## Google da sizning parolingiz hash qiymat sifatida saqlanadi, ya'ni xakkerlar google bazasini buzib kirgan holatda ham, ular sizni
## parolingizni olisha olmaydi (hash qiymatni olishadi holos uni esa qayta parol holatiga keltirib bo'lmaydi).

## Yana bir ishlatilish sohasini ko'radigan bo'lsak bu mualliflik huquqini himoya qilish.
    ## ISHLATILISHI: Mualliflik huquqini himoya qilish.
    ## Kuchli hash funksiya (SHA256) o'xshash matnlar uchun ham mutlaqo tasodifiy hash qiymatlari qaytaradi.
        ## dog -> cd6357 
        ## dot -> e392da # bu holatda ko'rib turganingizdek holat qayd etiladi.
    ## Lekin ba'zida bizga o'xshash narsalarni solishtirish talab qilinadi.
    ## Bunday holatda Simbash (similar hash) funksiyasi yordam beradi, ya'ni o'xshash matnlar uchun o'xshash hash qiymatlar yaratadi.
        ## YouTube - yuklangan videolarni solishtirish uchun. Deylik YouTube ga video yuklasangiz, YouTube ning ozida mavjud kinolar uchun 
## hash qiymatlar bor. Ana endi siz video yuklaganingizda, sizning videoingiz uchun ham hash qiymat yaratiladi. Yaratilgan hash qiymatni
## YouTube bazasida mavjud hash qiymatlar bilan solishtiriladi va agar bu yaratilgan qiymat bazada mavjud bo'lsa, siz mumkin bo'lmagan 
## video yukladingiz.
        ## Truli platformalar o'g'rilangan kitob/dasturlar yuklanganini tekshirish uchun. Bu holatda agar siz biror saytdan kitob yuklab
## olsangizu va bu kitobning muallifi bo'lsa, endi siz bu kitobni biror saytga yuklamoqchi bo'lsangiz va bu sayt kuchli sayt bo'ladigan
## bo'lsa (YouTube, PlayMarket va hokazo) bu saytlar bu kitoblarning asl hash qiymatlarini o'zida saqlaydi va bu kitobni yuklashingizga
## yo'l qo'ymaydi. 



## 8 - KO'RADIGAN ALGORITMIMIZ DIFFIE-HELMAN ALGORITMI.

## Tasavvur qiling siz biror kishiga kalit so'z bilan SHIFRLANGAN xabar yubordingiz.
## Bu odam xabarni ochishi uchun KALIT SO'ZNI bilishi kerak.
## Kalit so'zni QANDAY QILIB YUBORASIZ?
## YECHIM: Diffie-Helman algoritmi(Assimetrik shifrlash).
## Bu algoritmda foydalanuvchida  2ta kalit bo'ladi: Ochiq va maxfiy.
## Ochiq kalitdan istalgan odam foydalanishi va xabarlarni shifrlashi mumkin.
## Lekin xabarni qayta ochish uchun maxfiy kalitni bilish shart bo'ladi.
## Demak ochiq kalit ommaviy, yopiq kalit esa maxfiyligicha sizda turadi.
## Ommaviy kalit bilan faqat shifrlash mumkin lekin ommaviy kalit bilan faylni ochib bo'lmaydi.

## Bu odatda PUBLIC KEY CRYPTOGRAPHY (ochiq kalit kriptografiyasi) deb ataladi. RSA algoritmi bu yo'nalishda ko'p qo'llaniladigan
## algoritmlardan biri.



## 9 - KO'RADIGAN ALGORITMIMIZ LINEAR PROGRAMMING DEB ATALADI.

## Chegaralangan resurslar bilan maksimal natijaga erishish algoritmlari. Ya'ni bu yerda bir nechta algoritmlar bor (bitta emas).

## MISOL:
    ## Duradgor rom yasash uchun 3m³ daraxt va 1L lak ishlatadi.
    ## Eshik uchun 5m³ daraxt va 2L lak ishlatadi.
    ## Har bir romdan 20$, eshikdan 35$ foyda oladi.
    ## Savol: 40m³ daraxt va 10L lak bilan maksimum qancha daromad olish mumkin?

## Yuqoridagi kabi muammolar SIMPLEX LINER algoritmlari yordamida yechiladi.

        
        
        

        