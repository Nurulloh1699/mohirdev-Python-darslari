# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 14:34:12 2025

@author: DavrServis
"""

## LONGEST COMMON SUBSTRING (Xato so'zni to'g'irlash muammosi).

## Bunga misol tariqasida telefonda xabar yozayotkanimizda biror so'zni xato yozsak to'g'irlashni taklif qilishi mumkin masalan:
    ## bula ❌
    ## bola?
    ## balo?
    
## Demak yuqoridagi holatda BULA deb xato so'z yozganimizda, GOOGLE yoki boshqa bir platformada balki siz buni nazarda tutgandursiz deb ikkita
## (BOLA? BALO?) va ba'zida undan ham ko'proq so'z taklif qilishi mumikin. 

## Demak bu darsda aynan shu funksiya qanday dasturlangani haqida tushuncha ega bo'lamiz.

## Avvaliga biz bu masalani hal qilish usullari bilan tanishib chiqishimiz kerak bo'ladi:
    ## 1. Muammoni qanday maydalaymiz?
    ## 2. Jadvalning qiymatlari nima bo'ladi?
    ## 3. Jadvalning ustun va qatorlarida nimalar yoziladi?
    
## Endi keling oldingiday jadval tuzib olamiz:
    ##       B     U     L     A
    ## B     1     0     0     0
    ## O     0     0     0     0
    ## L     0     0     1     0
    ## A     0     0     0     2
    
## Bu yerda nima bo'ldi hozir tahlil qilamiz:
    ## 1. Biz ikki dastlabki ikki harfni solishtiramiz va bir biriga mos kelsa 1, aks holda 0 yozamiz.
    ## 2. Shu tariqa hamma harflarni solishtirib chiqamiz.
    ## 3. Ohirgi ikkita harflar bir-biriga mos, bu holatda etibor beradigan narsamiz, yuqorida 1 raqamini yozamiz va pastka 1 yozishdan
    ## oldin uning bir qator yuqoridagi dioganalda turgan raqamni ko'ramiz u yerda ham 1 raqami turgani uchun yakundagi natijaga uni ham
    ## qo'shamiz.Yakunda esa 2 raqamini olamiz.
    
    ## Etibor bering agar hamma harflar bir-biriga mos kelsa
    
## Endi keling BOLA so'zini bizda bor ikkinchi so'z BALO bilan solishtirib qaysi so'z ko'proq mos kelishini bilib olamiz.
     ##       B     A     L     O
     ## B     1     0     0     0
     ## O     0     0     0     1
     ## L     0     0     1     0
     ## A     0     0     0     0
     
## Ikkita so'zdan qaysi biri ko'proq mos kelishini solishtirmoq chi bo'lsak nimaga etibor beramiz:
    ## Albatta, asosiy jihat yakundagi raqam (birinchi so'zda 2 va ikkinchi so'zda 1\0).

## 2 raqami bu yerda, ikkita harf ketma-ket bir biriga mos kelganini bildiradi.


## ENDI, ENG MUHIM SAVOLLARDAN BERI. O'ZI BU FORMULA TO'G'RIMI?

## Tasavvur qilamiz bizda yana bir so'z bor TOLA va bu so'z bilan natijamiz qanday bo'ladi?
    ##       B     U     L     A
    ## T     1     0     0     0
    ## O     0     0     0     0
    ## L     0     0     1     0
    ## A     0     0     0     2

## Endi bu yerda biz ikkilanib qolishimiz tabiiy chunki ikki holatda ham yakuniy natija 2 ga teng bo'lyapti. Formulamiz yuqorida to'g'ri
## kelgan B harfini hisobga olmayapti. Demak bu formula unchalik ham to'g'ri emas ekan. Kyingi formulamizda biz nechta harflar mos kelganini
## ham hisoblashimiz kerak bo'ladi va shunda biz o'zimiz kutkan natijani olishimiz mumkin bo'ladi.


## ENDI KELING MUAMMOYIMIZGA YANGI YECHIM O'YLAB TOPAMIZ:
    ##       B     U     L     A
    ## B     1     1     1     1
    ## O     1     1     1     1
    ## L     1     1     2     2
    ## A     1     1     2     3

## Demak formulani tahlil qilamiz:
## 1. Birinchidagi ikkita harf (B) mos bo'lgani uchun boshlang'ich qiymatimiz 1 ga teng bo'ladi.
## 2. Nega ikkinchi holatda ham 1 ni oldik? Bu holatda bundan oldingi qatorga etibor bergan holda maksimum qiymatni (1) olyapmiz.
## 3. Shu tariqa bir xil harflar juftligi to'g'ri kelmaguncha davom etamiz.
## 4. Bir xil harflar to'g'ri kelganda esa maksimum qiymatga yana dioganaldagi raqam qiymati ham qo'shiladi.
## 5. Shu tariqa ohirgi ikkita harfning bir xilligi uchun, yakundagi natija 3 ni tashkil qiladi.

## Ishonch hosil qilish uchun qolgan so'zlarni (BALO) ham formulaga solib ko'ramiz:
    ##       B     A     L     O
    ## B     1     1     1     1
    ## O     1     1     1     2
    ## L     1     1     2     2
    ## A     1     1     2     2
    
## Yuqoridagi formulaga solamiz va 2ta o'xshash harf borligini ko'ryapmiz (yuqoridagi so'z eng to'g'ri varyant ekaniga ishonch hosil qildik).

## Keyingi so'z (TOLA) bilan solishtiramiz:
    ##       B     U     L     A
    ## T     0     0     0     0
    ## O     0     0     0     0
    ## L     0     0     1     1
    ## A     0     0     1     2
    
## Bu holatdan keyin formulamiz to'g'ri ekanligiga yanayam ishonch hosil qilyapmiz.

## Natija: Eng mos so'zni aniqladik.


## DYNAMIC PROGRAMMING HAQIDA XULOSA YASAYDIGAN BO'LSAK:
    ## 1. Dynamic Programming chegaralangan vaqt (resurs) bilan optimal yechim topish imkonini beradi. Demak vaqtimiz yoki resursimiz
    ## chegaralangan bo'lsa DP dan foydalanar ekanmiz.
    ## 2. DP muammoni mayda muammolarga bo'lish orqali yechim qidiradi. Bu holatda mayda muammolar bir-biridan mustaqil bo'lishi shart!
    ## 3. DP jadval tuzishdan boshlanadi.
        ## 1. Jadval har bir katagi alohida muammo bo'ladi.
        ## 2. Katakdagi qiymatlar siz optimizatsiya qilmoqchi bo'lgan qiymat bo'ladi (narx, masofa, vaqt)
        
## Dynamic Programming yechimni tez beradi, ya'ni biz optimal yechimga tez kelishimiz mumkin.
## Lekin bu yerda bitta muammo bor!!! Barcha muammolarga tushadigan yagona formula yo'q. Demak har-xil muammolar uchun yechim ustida 
## baribir bosh qotirishga to'g'ri keladi. Aytib o'tish kerakki, kerakli yechim topilganidan keyin natijani juda tez olish mumkin bo'ladi.


## QAYERLARDA ISHLATILADI???
    ## 1. DNK solishtirishda (odamlar, hayvonlar, kasalliklar).
    ## 2. Imloviy xatolarni to'g'irlaydigan dasturlarda. Biz ko'rgan formulamiz Levenshtein masofasi deb ataladi.
    ## 3. Fayllar, web sahifalar, rasm va hujjatlarni solishtirishda.
    ## 4. Matn muharrirlarida.
    ## 5. Yana minglab muammolarda qo'llash mumkin, sharti masalani mayda masalachalarga bo'la olsangiz kifoya.
    

## KICHIK AMALIYOT.
def levenshtein_distance(s1, s2):
    """Levenshtein masofasini hisoblaydi (Ikki so'z o'rtasidagi minimanl tahrir masofasi)"""
    m, n = len(s1), len(s2) # s1 va s2 uzunliklarini olamiz.
    
    ## DP jadvalini (matritsasini) yaratamiz. (m+1) x (n+1) o'lchamda.
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    ## Jadalning 1 - ustun va 1 - qatorini to'ldiramiz (bo'sh string bilan taqqoslash uchun).
    for i in range(m + 1):
        dp[i][0] = i # O'chirish amallari soni.
    for j in range(n + 1):
        dp [0][j] = j # Qo'shish amallari soni.
    
    ## Jadvalni to'ldirish uchun 2ta sikl ishlatamiz.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1 # Agar harflar bir xil bo'lsa, cost 0, aks holda 1.
            ## 3ta amal orqali minimal masofani tanlaymiz:
                ## 1. O'chirish (dp[i - 1][j] +1).
                ## 2. Qo'shish (dp[i][j - 1] + 1).
                ## 3. Alamashtirish (dp[i - 1][j - 1] + cost)
            dp[i][j] = min(dp[i - 1][j] + 1, # O'chirish.
                           dp[i][j - 1] + 1, # Qo'shish.
                           dp[i - 1][j - 1] + cost) # Almashtirish.
    
    return dp[m][n] # Oxirgi katakda minimal tahrir masofasi bor.

def find_closed_word(word, word_list):
    """Berilgan so'zga eng yaqin so'zni topish"""
    closest_word = None # Eng yaqin so'zni saqlash uchun o'zgaruvchi.
    min_distance = float('inf') # Minimal masofa uchun boshlang'ich katta qiymat.
    
    for w in word_list : # Har bir so'zni tekshirib chiqamiz.
        distance = levenshtein_distance(word, w) # Levenshtein masofasini hisoblaymiz.
        if distance < min_distance: # Agar yangi masofa avvalgidan kichik bo'lsa:
            min_distance = distance # Yangi minimal masofani saqlaymiz.
            closest_word = w # Eng yaqin so'zni yangilaymiz.
            
    return closest_word, min_distance # Eng yaqin so'z va masofani qaytaramiz.

## So'zlar ro'yxati (mavjud lug'at).
dictionary = ["apple", "banana", "grape", "pineapple", "orange", "aple", "apples"]

## Foydalanuvchidan so'z olish.
user_word = input("Sozni kiriting: ").strip().lower() # Foydalanuvchi kiritgan so'zni kichik harfga o'tkazamiz.

## Eng yaqin so'zni topish.
closest_word, distance = find_closed_word(user_word, dictionary)

## Natijani chiqarish.
print(f"Eng yaqin so'z: {closest_word} (masofa: {distance})")
    