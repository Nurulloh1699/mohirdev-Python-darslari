# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 08:30:01 2024

@author: DavrServis
"""
#9-dars IF-ELIF-ELSE (agar\aks holda,agar\yoki)
#15.10.2024.
#Muallif:Abdurashidov Nurulloh.



# Biz o'tkan darslarda if va else shart operatorlari bilan tanishtik va ular bilan ishlashni
# o'rgandik. Bu operatorlarni kamchilik tomoni ham bor yani ular faqat bitta shartni
# tekshiradi holos. Quyida buni ko'rib o'tamiz. 
son = -50 # Bizda son teng 50 ga.
if son > 0: # Agar son katta bo'lsa 0 dan.
    print("son musbat") # Unda bu son musbat.
else: # Aks holda.
    print("son manfiy") # Bu son manfiy.

# Endi biz misol ko'ramiz hayvonot bog'i misolida.
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     print("Sizga kirish bepul!") # Bu o'rinlarda biz qayta-qayta print() funksiyasidan
# # emas balki shu kodga analog qilib uni boshqachoroq qilishimiz mumkin.
# elif yosh <= 12:
#     print("Sizga kirish 5000 so'm!")
# elif yosh <= 18:
#     print("Sizga kirish 8000 so'm!")
# else:
#     print("Sizga kirish 10000 so'm!")
    
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     narh = 0 # Bu o'rinda biz print() funksiyasidan emas shunchaki yangi narh degan
# # o'zgaruvchi bilan ishimizni bitiryapmiz.
# elif yosh <= 12:
#     narh + 5000
# elif yosh <= 18:
#     narh + 8000
# else:
#     narh + 10000    
#     print(f"sizga kirish {narh} so'm!")
# Yuqoridagi usulning ham kamchiligi bor bu yerda agar birinchi shart to'g'ri kelsa qolgan
# shartlarni tekshirib o'tirmaydi dastur va birmuncha noqulay.

# Endi biz bir vaqtning ozida bir necha shartni tekshirishni ko'rib chiqamiz.
# Buning uchun bizda (or)yoki va and(va) operatorlari bor. Biz birinchisini ko'ramiz (or).
# kun = input("Bugun nima kun?>>> ") # Kunni kiritishni so'rayapmiz.
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba': # Ikkita shart beryapmiz bir 
# # vaqtning o'zida, agar ikkalasidan bittasi to'g'ri bo'lsa ham birinchi funksiya ishlaydi.
#     print("Bugun dam olish kuni!")
# else: # Aks holda.
#     print("Bugun ish kuni peshona ekan!") # Ikkinchi funksiya ishlaydi.

#Endi biz ikkinchi operatorni ko'ramiz, yani and(va) operatorini.
# Bu yerda nima amal bajariladi? Foydalanuvchidan so'raymiz ikkita ma'lumotni va u kiritgan
# ma'lumotlarga qarab davom etamiz.
# kun = input("Bugungi kunni kiriting: ") # 1-ma'lumot.
# harorat = float(input("Havo harorati nechi? ")) # 2-ma'lumot.

# if kun.lower() == 'yakshanba' and harorat >= 30: # and(va) operatorini or(yoki) operatoridan
# # farqi nomidan ham bilsa bo'ladi, bunda birinchida berilgan ikkala shart ham to'g'ri bo'lishi kerak.
#     print("Cho'milishga borsa bo'ladi!")
# elif kun.lower() == 'yakshanba' and harorat < 30:
#     print("Havo sovuqroq ekan uyda qolgan ma'qul!") # Kod to'liqroq ishlashi uchun else:
# # qo'shamiz
# else:
#     print("Adashma bugun ish kuning!") 

# Endi ko'radigan ko'dimiz or(yoki) va and(va) operatorlarini qo'shib yanayam ko'proq shartlarni
# tekshirib ko'ramiz.
# kun = input("Bugun nima kun? ")
# harorat = float(input("Bugun havo qanday? "))

# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat>=30:
#     print("Cho'milishga borsa bo'ladi!")
# elif kun.lower() == 'shanba' or kun.lower() == 'yakshanba' and harorat < 30:
#     print("Havo sovuq Cho'milishga borib bo'lmaydi!")
# else:
#     print("Adashma bugun sani ish kuning!")     
    
# Keling shu o'rinda mantiqiy(BOOLEAN) degan ma'lumotlar turi bilan ham tanishaylik.
# Buni biz oshxona misolida ko'ramiz.
# narh = 15000 # Mijoz ovqat sotib oldi.
# choy = 1 # Bu yerda 1 = (True)ga. 
# salat = 0 # Bu yerda 0 = (False)ga.

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
    
#     print(f"Jami {narh} so'm")
# Aytkanimizdek yuqoridagi kodda agar bitta shart bajarilsa boshqa shartlar tekshirilmaydi

# Kelin siz bilan bi vaqtnig o'zida koddagi hamma shartni tekshiradigan kod yozamiz.
# Buni ham oshxona misolida ko'ramiz.
# narh = 15000 # Mijoz ovqat sotib oldi.
# non = 1
# choy = 0
# kompot = 1
# salat = 0
# assorti = 1
# # Yuqorida biz kodning boshini yozib oldik endi qanday shartlar tekshirilishi va 
# # bajarilishi kerak bo'lsa shuni hal qilib olamiz.
# if choy:
#     print("Mijoz choy sotib oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non sotib oldi.")
#     narh = narh + 4000    
# if kompot:
#     print("Mijoz kompot sotib oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat sotib oldi.")
#     narh = narh + 8000
# if assorti:
#     print("Mijoz assorti sotib oldi.")
#     narh = narh + 15000    
# Yuqoridagi shartlarning har biri bir biridan mustaqil yani alohida.    
#print(f"Mijozdan umumiy {narh} so'm bo'ldi.")

# Keyingi tanishadigan operatorimiz (in (bormi)) operatori, bunda ma'lum bir matnni ro'yxat ichida
# bormi yo'qmi tekshiramiz.
# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa'] # Ovqatlar ro'yxati.
# ovqat = input("Nima ovqat yeysiz? ") # Mijozdan nima ovqat yeyishini so'rayapmiz.
# if ovqat.lower() in menu: # Mijoz tanlagan ovqat menu da bo'lsa.
#     print("buyurtmangiz qabul qilindi.") # Shu yozuv chiqadi.
# else: # Aks holda.
#     print("Kechirasiz bizda bunday ovqat yo'q.") # Shu yozuv chiqadi.
    
# Huddi shu kodni (not in (yo'qmi)) orqali yozsak ham bo'ladi.  
# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa'] # Ovqatlar ro'yxati.
# ovqat = input("Nima ovqat yeysiz? ") # Mijozdan nima ovqat yeyishini so'rayapmiz.
# if ovqat.lower() not in menu: # Mijoz tanlagan ovqat menu da bo'lmasa.
#     print("Kechirasiz bizda bunday ovqat yo'q.") # Shu yozuv chiqadi.
# else: # Aks holda.
#     print("buyurtmangiz qabul qilindi.") # Shu yozuv chiqadi.
    
# Ro'yxatlar bilan ishlaganda biz ikkita ro'yxatni bir-biriga solishtirishimiz ham mumkin.
# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# for taom in buyurtmalar: # Tsikl ochyapmiz yani buyurtmalar ichidagi har bir taom uchun.
#     if taom in menu: # menu ichidagi har bir taom uchun.
#         print(f"Menuda {taom} bor.") # Buyurtmalar asosida menuni tekshirib natija chiqadi.
#     else: # Aks holda.
#         print(f"Kechirasiz, menuda {taom} yoq.") # Menuda so'ralgan taom yo'qligini aniqlandi.
        
# Bir narsaga etibor berin yuqoridagi kodlarda biz qiymatlarni o'zimiz qo'lda yozdik.
# Dasturda esa aksincha bo'sh ro'yxat foydalanuvchi kiritadigan qiymatlar bilan
# to'ldirilish mumkin.

# Bazida ro'yxatlarni avval tekshirib olishga to'g'ri keladi. Buning uchun quyadi ishni qilamiz.
# buyurtmalar = []
# if buyurtmalar: # Agar buyurtmalar degan ro'yxatda.
#     print(f"Ro'yxatda {len(buyurtmalar)} ta taom bor.") # Ro'yxat tekshirilyapti.
# else:# Aks holda.
#     print("Ro'yxat bo'sh.") # Quyidagi kod konsolga chiqadi.
 
# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# if buyurtmalar: # Agar buyurtmalar degan ro'yxatda.
#     print(f"Ro'yxatda {len(buyurtmalar)} ta taom bor.") # Ro'yxat tekshirilyapti.
# else:# Aks holda.
#     print("Ro'yxat bo'sh.") # Quyidagi kod konsolga chiqadi.

# for taom in buyurtmalar: # Tsikl ochyapmiz yani buyurtmalar ichidagi har bir taom uchun.
#      if taom in menu: # menu ichidagi har bir taom uchun.
#          print(f"Menuda {taom} bor.") # Buyurtmalar asosida menuni tekshirib natija chiqadi.
#      else: # Aks holda.
#          print(f"Kechirasiz, menuda {taom} yoq.") # Menuda so'ralgan taom yo'qligini aniqlandi.   
         
# TOPSHIRIQLAR.
#1 Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa
# "Rahmat!", agar toq son kiritsa "Bu son juft emas!" degan xabarni chiqaring.
# son = int(input("Iltimos juft son kiriting: ")) # Foydalanuvchidan son kiritishini
# # so'radik va uni o'nlik songa otkazib oldik.
# if son / 2 == 0: # Kiritilgan son 2ga bo'linganda qoldiq qolmasligi tekshirilyapti.
#     print(f"{son} juft emas, juft son kiriting.") 
# else: 
#     print("Rahmat!")      
    
#2 Foydalanuvchidan yoshini so'rang, va muzeyga kirish uchun chipta narhini
# quyidagicha chiqaring:
    # Agar foydalanuvchi 4 yoshdan kichik yoki 60 yoshdan katta bo'lsa bepul.
    # Agar foydalanuvchi 18 yoshdan kichik bo'lsa 10000 so'm.
    # Agar foydalanuvchi 18 yoshdan katta bo'lsa 20000 so'm
# yosh = int(input("Iltimos yoshingizni kiriting: "))
# if yosh <= 4 or yosh >= 60:
#     print("Sizga kirish bepul!")    
# elif yosh <= 18:
#     print("Sizga kirish bileti 10000 so'm.")
# elif yosh >= 18:
#     print("Sizga kirish bileti 20000 so'm.")
    
#3 Foydalanuvchidan ikkita son kiritishini so'rang, sonlarni solishtiring va ularni 
# teng, katta yoki kichikligi haqida habarni chiqaring.
# son1 = float(input("Iltimos birinchi sonni kiriting: "))
# son2 = float(input("Iltimos ikkinchi sonni kiriting: "))

# if son1 == son2:
#     print(f"{son1} = {son2}")
# if son1 > son2:
#     print(f"{son1} > {son2}")
# if son1 < son2:
#     print(f"{son1} < {son2}")  
    
#4  mahsulotlar degan ro'yxat yarating va kamida 10ta turli mahsulotni kiriting. Yangi 
# savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5ta turli
# mahsulotni kiritishini so'rang. Savatdagi elementlarni, mahsulot ro'yxati bilan
# solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda ,
# "Mahsulot do'konimizda yo'q" degan xabarni chiqaring.
mahsulotlar = ['kartoshka', 'piyoz', 'sabzi', 'olma','shaftoli', 'anor', 'banan','guruch',
'makaron','o\'yinchoq']
savat =[]
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor.")
        else:
            print(f"Do'konimizda {mahsulot} yoq.")
    
    