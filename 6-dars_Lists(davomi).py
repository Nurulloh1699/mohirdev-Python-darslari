# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:39:49 2024

@author: DavrServis
"""

#6-dars Lists.
#14.10.2024.
#Muallif:Abdurashidov Nurulloh.

# Ro'yxatlarni .sort() metodi orqali alifbo ketma ketligida tartiblash.
cars = ['general motors', 'audi', 'mercedes benz', 'bmw', 'tesla']
  #cars.sort()
  #print(cars) 
# ETIBOR BERING! Katta va kichik harflar ketma ketlikka tasir qiladi yani birinchi bo'lib 
# katta harfdan boshlangan so'zlar keladi.
  #cars.append('Volvo')
  #print(cars)
  #cars.sort()
  #print(cars) # shu ko'rinishda.

# Endi ro'yxatimizni .sort(reverse=True) argumenti orqali teskari tartibda tahlashga
# harakat qilib ko'ramiz.
  #cars.sort(reverse=True) # Ro'yxatimizni teskari tahla deb buyruq berdik.
  #print(cars) # Natija.

# Bazida bizga ro'yxatning asl holatiga tegmagan holda uni tartiblash topshirig'i
# ham berilishi mumkin. Buning uchun biz sorted() funksiyasidan foydalanamiz.
  #print(sorted(cars))
# Huddi shu ro'yxatni asl holiga tegmagan holda uni teskari tahlashimiz ham mumkin.
# Buning uchun sorted( ,reverse=True) ni ishlatamiz
  #print(sorted(cars,reverse=True))
 
# Shu kodlarimizni endi sonli ro'yxatlarga nisbatan ham ishlatishimiz mumkin.
sonlar = [12,45,72,89,-4,-17.3,7.1]
  #print(sorted(sonlar)) # bunda sonlarning asl ketma ketligi o'zgargani yo'q.
 
# Asl ketma ketlikni o'zgartirish uchun esa yana o'sha .sort() metodiga murojat qilamiz.
  #sonlar.sort() 
  #print(sonlar)
# Teskari tahlash ham ayni o'sha ko'rinishda bo'ladi.
  #sonlar.sort(reverse=True)
  #print(sonlar) 

# Ro'yxatlarni tartiblamay turib ham uni aylantirib qo'yish imkoniga egamiz yani tartibini
# boshtan oyoqqa emas, balki oyoqdan boshga qilib. Bunda bizga .reverse() metodi yordamga keladi.
  #print(cars)
  #cars.reverse()
  #print(cars)

# Endi ro'yxatni uzunligini ko'rishga harakat qilamiz buning uchun bizga len() funksiyasi
# yordamga keladi.
  #print(len(cars))
  #print(len(sonlar)) # shu asnoda qo'llaniladi.

# Endi range() funksiyasini ko'rib chiqamiz. Bunda range() bizga ma'lum bir oraliqdagi sonlarni 
# qaytaradi yani yeg'adi va biz ularni bir yola ro'yxatga saqlash imkoniga ham egamiz.
  #numbers = list(range(0,21)) # bunda bizga numbers degan ro'yxatimizga range() funksiyasi 
# 0 dan 20 gacha bo'lgan sonlarni jamlab beradi yani ohirgi 21 degan raqamimiz kirmaydi.
  #print(numbers)
  
# range() funksiyasidan foydalanganda biz qadamni ham berishimiz mumkin.
  #toq_sonlar = list(range(1,20,2)) # 1 dan 20 gacha 2 qadam bilan yani faqat toq sonlar.
  #print(toq_sonlar) # Natijani ko'rishingiz mumkin.

  #juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan yani faqat juft sonlar
  #print(juft_sonlar)

# Qadamni biz har hil berishimiz mumkin yani hohlaganimizday.
  #sanash = list(range(0,101,10))
  #print(sanash) 
  
# min(), max() va sum() funksiyasi orqali ro'yxatni ichidan minimal qiymat va
# maksimal qiymatni topish va ro'yxat qiymatlarining yeg'indisini ham topishimiz mumkin.
  #narhlar = [13200, 11000, 9600, 15000, 7500, 6800]
  #arzon = min(narhlar) # narhlar ro'yxatidan eng arzonini topyapti.
  #qimmat = max(narhlar) # narhlar ro'yxatidan eng qimmatini topyapti.
  #summa = sum(narhlar) # narhlar ro'yxatini jami qiymatlar yeg'indisini topyapti.
  #print("Eng arzon narx", arzon, "eng qimmat narx", qimmat, "va jami summa teng", summa,"ga.")
  
  
# Ro'yxatlarni kesishni ko'rib chiqamiz. Bunda bizga ikki nuqta [:], yani indeks yoziladigan
# qavslar ichini vergul [,] bilan emas balki ikki nuqta [:] bilan bo'lamiz.
# ETIBOR BERING! bu yo'l ham huddi range() funksiyasidek ishlaydi.
 
# Ro'yxatni kesishni o'rganamiz 
  #cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'chevrolet', 'lada']
  #my_cars = cars[0:3] # my_cars ro'yxatiga cars ro'yxatidagi elamentlardan kesib olyapmiz.
  #print(my_cars) # Yuqoridagi holatda 0 dan 2 gacha bo'lgan qiymatlarni oldi va
# 3 qiymat o'z o'zidan qolib ketti.
# ETIBOR BERING! Agar biz kesib olishda indekslarni to'liq bermasak yani [:3] birinchi indeksni
# bermadikda ikkinchi indeksda 3 qo'ydik bu holatda birinchi indeksga avtomatik 0 chi
# indek beriladi va ro'yxatni kesib oladi va teskarisi [1:] birinchisi berilib ikkinchi
# indeks berilmadi bu holatda avtomatik ravishda 1 dan ohirigacha bo'lgan qiymatlarni oladi.

# Ro'yxatlardan nusxa olishni o'rganamiz.
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'chevrolet', 'lada']  
  #my_cars = cars
  #print(cars)
  #print(my_cars)

  #my_cars.remove('volvo')
  #my_cars[0] = 'lacetti'
  #print(my_cars)
  #print(cars)
# Yuqoridagi harakatlarimiz bilan biz ro'yxatdan nusxa olmadik balki bitta ro'yxatga
# ikkita nom berib qo'ydik shuning uchun ham biriga kiritilgan o'zgarish ikkinchisiga 
# ham tasir qilyapti.Buni bartaraf etish uchun endi biz metoddan foydalanishimiz kerak
# va bu maxsus metod [:] boshiga ham ohiriga ham hech qanday belgi yoki element qo'ymaymiz.
  #my_cars = cars[:]
  #print(cars)
  #print(my_cars)
  #my_cars.append('lexus')
  #my_cars.remove('chevrolet')
  #print(cars)
  #print(my_cars)
# Yuqoridagi harakatlarimiz bilan biz nusxa olish usulini to'g'ri bajardik va boshqa 
# ro'yxatlarga zarar yetkazmadik.

# TUPLE Ro'yxatlar yani o'zgarmas ro'yxatlar. Bu ro'yxat () oddiy qavslar bilan tashkil 
# qilinadi. 
toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
  #print(toys[0])
  #print(toys[-1])
  #print(toys[2:5])
# Ushbu amallarni bajarishda muammo yoq, lekin agar bu ro'yxatga o'zgartirish kiritmoqchi 
# bo'lsak bunda xato kelib chiqadi va biz bu ro'yxatni o'zgartira olmaymiz.
  #toys[3] = 'dragon'
  #print(toys) # Mana bu yerda xatolik chiqadi yani bu ro'yxatni o'zgartirib bo'lmaydi
# degan ma'noda.
  #toys.append("dragon")
  #print(toys) # Bu holatda ham xatolik chiqadi.
  
# Deylik biz majburmiz va bu ro'yxatga o'zgartirish kiritish zarur bu holda nima qilamiz.
# Albatta yechim bor, buning uchun avval TUPLE ro'yxatni oddiy LIST ga oz'gartirishimiz
# kerak bo'ladi.
toys = list(toys)
print(type(toys)) # Ro'yxatimiz oddiy LIST ro'yxatga o'zgardi va biz endi bemalol u bilan
# ishlashimiz mumkin bo'ladi.
toys.append('dragon')
toys.remove('bear')
toys[1] = 'mcqueen'
print(toys) # Mana endi bemalol ro'yxatni o'zgartirib oldik endi uni yana qaytadan TUPLE
# ro'yxatga o'tkazib qo'yamiz.

toys = tuple(toys)
print(type(toys)) # shu ko'rinishda.

# TOPSHIRIQLAR.
#1 O'zingizga ma'lum davlatlar ro'yxatini tuzing va uni konsolga chiqaring.
  #davlatlar = ["O'zbekiston", "Rossiya", "Amerika", "Falastin", "Portugaliya"]
  #print(davlatlar)

#2 Ro'yxatni uzunligini konsolga chiqaring.
  #print(len(davlatlar))

#3 .sorted funksiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring.
  #print(sorted(davlatlar))

#4 .sorted yordamida ro'yxatni teskari tartibda konsolga chiqaring.
  #print(sorted(davlatlar, reverse=True))

#5 Asl ro'yxatni qaytadan konsolga chiqarin.
  #print(davlatlar)

#6 .reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring.
  #davlatlar.reverse()
  #print(davlatlar)

#7 .sort() metodi yordamida ro'yxatni avval alifbo bo'yicha keyin esa alifboga teskari 
# tartibda konsolga chiqaring.
  #davlatlar.sort()
  #print(davlatlar)
  #davlatlar.sort(reverse=True)
  #print(davlatlar)

#8 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
  #juft_sonlar = list(range(120,1200,2))
  #print(juft_sonlar)

#9 Ro'yxatdagi sonlar yeg'indisini hisoblang va konsolga chiqaring.
  #yigindi = sum(juft_sonlar)
  #print(yigindi)

#10 Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani konsolga chiqaring.
  #kichik = min(juft_sonlar)
  #katta = max(juft_sonlar)
  #print("Ro'yxatdagi eng katta sondan", katta, "ro'yxatdagi eng kichik son", kichik,
  #"ayrilganda natija", katta-kichik, "ga teng bo'ladi.")

#11 Ro'yxatdagi elementlar sonini hisoblang.
  #print("juf_sonlar ro'yxatidagi elementlar soni",(len(juft_sonlar)),"taga teng.")

#12 Ro'yxatni boshidan, ohiridan va o'rtasidan 20ta elementni konsolga chiqaring.
  #print(juft_sonlar[0:21])
  #print(juft_sonlar[260:281])
  #print(juft_sonlar[519:540])

#13 taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting.
taomlar = ['Osh', 'Sho\'rva', 'Shirguruch', 'Non va Choy', 'Kabob']

#14 nonushta degan ro'yxatga taomlardan nusxa oling.
nonushta = taomlar[:]
print(nonushta, taomlar)

#15 Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va yana
# 2ta taom qo'shing.
nonushta.remove('Osh')
nonushta.remove('Sho\'rva')
nonushta.remove('Kabob')
print(nonushta)
print(taomlar)
nonushta.append('Ikkita tuxum')
nonushta.append('Qaymoq')

#16 Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring. 
print(nonushta)
print(taomlar)

#17 Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring  va nonushta[0] = 
# "qaymoq va non" deb qiymat berib ko'ring.

nonushta = tuple(nonushta)
print(type(nonushta))
nonushta[0] = "qaymoq va non"
print(nonushta) # Bu yerda xato beradi chinki biz ro'yxatni TUPLE ga o'zgartirdik.

   