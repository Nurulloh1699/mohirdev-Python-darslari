# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:19:28 2024

@author: DavrServis
"""

#7-dars FOR LOOP (TSIKL).
#15.10.2024. 8:20 da boshlandi.
#Muallif:Abdurashidov Nurulloh.

# Biz kod yozishda bitta kodni bir necha marta bajarish talab etilganda (tsikl) ga 
# murojat qilamiz.
  #mehmonlar = ['Ali','Vali', 'Hasan', 'Husan', 'Abror']
# shu orinda biz agar har bir elementga habar jo'natish talab etilsa nima qilamiz?
# Har biriga alohida kod yozsak ham bo'ladi lekin nega unday qilishimiz kerak ozi?
  #print("Salom",mehmonlar[0])
  #print("Salom",mehmonlar[1])
  #print("Salom",mehmonlar[2])

# Biz bu vaziyatda (tsikl) dan foydalansak bo'ladi.
  #for mehmon in mehmonlar: # Bu yerda (tsikl) ga shart beryapmiz va uni yangi o'zgaruvchiga 
# yuklayapmiz.
    #print("Salom", mehmon) # Bu (tsikl) tanasi deb ataladi va bu yerda nima vazifa bajarilish
# kerakligi yoziladi. (tsikl) tanasida odatda bo'sh joy (otsup) tashlanadi va bu zarur.    

# Bu yerda biz yangi (tsikl) yaratyapmiz.
  #mehmonlar = ['Ali','Vali', 'Hasan', 'Husan', 'Abror']
  #for mehmon in mehmonlar:
    #print(f"Hurmatli {mehmon}, sizni 8-noyabr kuni nahorgi oshga taklif qilamiz.")
    #print("Hurmat va ehtirom bilan, Palonchiyevlar oilasi.\n")
    
# Endi biz (tsikl) orqali sonlar bilan ishlashni ko'rib chiqamiz.
  #sonlar = list(range(1,11)) # Ro'yxat tashkil qilib oldik.
  #for son in sonlar: # (tsikl) ga shart berdik.
#    print(f"{son} ning kvadrati {son**2} ga teng") # (tsikl) bajarishi kerak bo'lgan topshiriq.

# (tsikl) da bo'sh ro'yxat bilan ishlashni ko'rib chiqamiz.
  #sonlar = list(range(11)) # Sonlardan iborat ro'yxat yaratib oldik.
  #sonlar_kvadrati = [] # Bo'sh ro'yxat ham yaratib oldik.
  #for son in sonlar:# sonlar ro'yxatidagi har bir son uchun.
    #sonlar_kvadrati.append(son**2) #.append() metodi yordamida sonlar_kvadrati nomli bo'sh
# ro'yxatimizga sonlar ro'yxatidagi har bir sonning kvadratini jamlayapmiz.
  #print(sonlar)
  #print(sonlar_kvadrati)

  #dostlar = [] # Bo'sh ro'yxat keyinchalik foydalanuvchi uchun.
  #print("5ta eng yaqin do'stingizni ismini kiriting!") # Foydalanuvchiga ishora.
  #for n in range(5): # range() funksiyasi yordamida 5 qiymatni shakllantirib olyapmiz.
    #dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting! ")) # Foydalanuvhcidan
# qiymat kiritishini so'raymiz.
  #print("Sizning eng yaqin do'stlaringiz", dostlar, "lardan iborat ekan.") # Natijani
# ro'yxat korinishida konsolga chiqaramiz.

# TOPSHIRIQLAR
#1 Kamida 5ta elementdan iborat ro'yxat tuzing va ro'yxatdagi har bir ismga takrorlanuvchi
# habar yozing.
mehmonlar = ['Ali','Vali', 'Hasan', 'Husan', 'Abror']
for odam in mehmonlar:
    print(f"Salom qalesan, {odam}\n")    
    
#2 Yuqoridagi (tsikl) tugagandan keyin "Kod n martta takrorlandi" degan habarni chiqaring.
# (n o'rniga kod necha martta takrorlanganini yozing.)
print(f"Kod {len(odam)} martta takrorlandi.") 

#3 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatni har bir elementining
# kubini yangi qatordan konsolga chiqaring.
  #t_sonlar = list(range(11,100,2))
  #print(t_sonlar)
  #for kub in t_sonlar:
    #print(f"{kub} soning kubi {kub**3}ga teng")
    
#4 Foydalanuvchi 5ta eng sevimli kinolarini kiritishini so'rang, va kinolar degan ro'yxatga
# saqlab oling. Natijani konsolga chiqaring.
  #kinola = []
  #print("5ta eng yoqtirgan kinolaringizni kiriting!")
  #for r in range(5):
    #kinola.append(input(f"{r+1}-kino nomini kiriting! "))
  #print("Siz yoqtirgan kinolar", kinola, "lardan iborat ekan.")    

#5 Foydalanuvchida bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va 
# har bir suhbatlashgan odamining ismini birma bir so'rab ro'yxatga yozing. Ro'yxatni
# konsolga chiqaring.

#n_people = int(input("Bugun nechta odam bilan suhbatlashdingiz?>>> "))
#suhbat = []
#for n in range(n_people):
#    suhbat.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi? "))
#print(suhbat)


  
n_people = int(input("Bugun nechta odam bilan suhbat qildingiz? >>>")) # Foydalanuvchidan
# bugun nechta odam bilan suhbat qurganini sonini so'rayapmiz.
ismlar = [] # Bo'sh ro'yxat yaratib oldim keyinchalik uni foydalanuvchi to'ldirishi ucun.
for n in range(n_people): # for orqali n ga range funksiyasi bilan foydalanuvchi 
# suhbatlashgan odamlar sonini berdik.
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: ")) # ismlarga qo'shyapmiz 
# (n+1) orqali yani foydalanuvchi 5 sonini kiritsa dastur 0-indeksdan 4-indeksgacha oladi,
# bunda (n+1) foydalanuvchiga chiqadigan malumotni tushunarliroq qilgani kerak.    
print(ismlar) # Ro'yxatni konsolga chiqaryapmiz.

