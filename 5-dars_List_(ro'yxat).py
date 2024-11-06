# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:20:15 2024

@author: DavrServis
"""

#5-dars List (ro'yxat).
#14.10.2024.
#Muallif:Abdurashidov Nurulloh.

# Pyhon dasturlash tilida list(ro'yxat) yaratish uchun ro'yxat nomi va [] orqali yaratamiz.
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
print(mevalar)

# Ro'yxatlarning ichida hohlagan qiymatlarni qo'llashimiz mumkin bo'ladi.
# Quyida sonlardan iborat ro'yxat tuzamiz.
narxlar = [2000, 7000, 42000, 3000, 27000, 16000, -25, 24.7]
print(narxlar)
# Yuqorida etibor bersangiz o'nlik son manfiy son va hokazo korinishda davom etaveradi.

# Biz aralash ro'yxatlar ham yaratishimiz mumkin.
sonlar = ['bir', 'ikki', 3, 4, 5]
print(sonlar) 

# Bundan tashqari biz mutlaqo bo'm bosh ro'yxat ham yaratishimiz mumkin.
ismlar = [] # bo'sh ro'yxat.
print(ismlar)
# Bu ro'yxatlar qayerda ishlaydi degan savolga javob tariqasida bu ro'yxatlar input()
# yordamida foydalanuvchi tomonidan kiritiladigan qiymatlar bilan to'ldirishimiz mumkin.

# Ro'yxatdagi istalgan qiymatni(elementni) chaqirib olib undan foydalanish imkoniyatiga
# egamiz. Har bir elementga biz tartib raqami(indeksi) bo'yicha murojat qilishimiz mumkin.
# Dasturlashda sanash(indeks) doim 0dan boshlanadi.Yani agar ro'yxatta elementlar 5ta
# bo'lsa indeks bo'yicha sanashta bu elementlar 4gacha indekslanadi.
print(mevalar[0]) # kabi

# Agar ro'yxatda elementlar soni ko'p bo'lsa va indeksi aniq bo'lmasayu bizga eng ohiridagi
# element kerak bo'lsa u holda [-1] bilan ham murojaat qilsak bo'ladi.
print(mevalar[-1])

# Ro'yxat ichidagi matnli qiymatlarga oldingingi darslarda ko'rilgan metodlarni ham
# qo'llashimiz mumkin.
print(mevalar[0].upper()) # va boshqa metodlarni ham qo'llashimiz mumkin.

# Shu asnoda raqamli qiymatlar bilan ham har hil amallar bajarsak bo'ladi.
print(narxlar[0] + narxlar[1]) # shu asnoda davom etaveradi.

# Endi ro'yxat elementlarini qiymatini o'zgartirishni ko'rib chiqamiz.
mevalar[0] = 'anor' # bu holatda o'zgartirmoqchi bo'lgan elementimizni indeksi bilan 
# murojat qilamiz
print(mevalar)

# Endi biz ro'yxatga oldingi qiymatlarini saqlab qolgan holda yangi qiymat
# qo'shishni o'rganamiz, buning uchun nizda .append() degan metod bor.
print(mevalar)
mevalar.append('tarvuz') # Bu holatda biz ro'yxatga 'tarvuz' degan qiymatni qo'shyapmiz.
print(mevalar) # Natijada tarvuz ro'yxat ohiriga qo'shildi. 
# .append() metodi doim ro'yxatning ohiriga element qo'shadi.
mevalar.append('olma')
print(mevalar)

# Ro'yxatning boshiga va yoki o'rtasiga element qo'shish uchun esa .insert() metodidan 
# foydalanamiz.
mevalar.insert(0, 'banan') # bu holatda birinchi qiymat qo'shiladigan joy(indeks)
# tanlanadi keyin qo'shiladigan qiymat beriladi. Hozirgi holatda element ro'yxatning
# boshiga qo'shildi.
print(mevalar)

# ESLATMA! Ro'yxat yaratyotkanda albatta ko'plik qo'shimchasini qo'shing (mevalar, cars),
# bu kelajakda o'zingiz uchun kerak bo'ladi.

# Endi ro'yxatdan ma'lum bir elementni ochirib tshlashni ko'rib chiqamiz.
cars = []
cars.append('Jentra')
cars.append('Onix')
cars.append('Malibu')
cars.append('Cobalt') # Ro'yxatni yaratib unga elementlar qo'shib oldik.
# Endi bo'lsa bu ro'yxatdan elementlarni o'chirishni ko'rib chiqamiz.
del cars[0] # Bu 1-usul
print(cars)
# Va yana ro'yxatga boshqa element qo'shishim kerak bo'lsa .insert() dan foydalanaman.
cars.insert(0,'Nexia 3')
print(cars)

# Deylik siz biror qiymatni o'chiqmoqchisizda lekin uni indeksini bilmaysiz bu holatda biz
# .remove() metodidan foydalanamiz.
cars.remove("Malibu") # Bu holatda biz ro'yxatdan "Malibu" qiymatini o'chirib tashlayapman.
print(cars)

# Deylik bizning ro'yxatimizda ikkita bir hil qiytmat bor bu holatda .remove() o'ziga 
# uchragan birinchi elementni o'chiradi ikkinchisi esa qoladi.
hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove('mushuk')
print(hayvonlar)

# Endi ro'yxatdan biror bir elementni .pop() metodi orqali sug'irib olishni
# ko'rib chiqamiz. Bunda ochirib
# tashlashdam farqli o'laroq elementni ro'yxat ichidan olib uni yana boshqa ro'yxat 
# ichiga joylashimiz mumkin bo'ladi.
bozorlik = ['yog\'', 'un', 'guruch', 'kartoshka', 'piyoz', 'go\'sht']
mahsulot = bozorlik.pop(1) # Biz 1-indeksdagi unni olib uni mahsulot deb nomlamgan 
# yangi ro'yxatga qo'shdim. Endi kichik dastur yozib ko'ramiz.
print("Men " + mahsulot + " sotib oldim")
print("Oladigan mahsulotla:", bozorlik)

# Agar biz .pop() metodidan foydalanganda unga hech qanday indeks bermasak, u holda u 
# avtomatik ravishda ro'yxatni ohiridagi elementni sug'urib oladi.
mahsulot2 = bozorlik.pop()
print(mahsulot2)

# TOPSHIRIQLAR
#1 ismlar dega ro'yxat yarating va kamida 3ta yaqing do'stingizni ismini kiriting.
ismlar = ['Abdurahmon', 'Hojiakbar', 'Akramjon', 'Muzaffar']

#2 Ro'yxatdagi har bir do'stingizga qisqa habar yozib konsolga chiqaring.
print(f"Salom {ismlar[0]} ishlaring yaxshimi." )
print(f"Do'stim {ismlar[-1]} bahtimga sog' bo'lgin.")
print(f"{ismlar[1]} bugun choyxona bormidi?")
print(f"To'yonani pulini faqat {ismlar[2]} bermadi.")

#3 sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang
# (musbat, manfiy, butun, o'nlik).
sonlar = [300000, 232000, 796000, -290000, 12335.7]

#4 Yuqoridagi ro'yxatdagi sonlar ustida turli hil amallar bajarib ko'ring.
# Ro'yxatdagi bazi sonlarni qiymatini o'zgartiring va bazilarini esa almashtiring.
print(sonlar[0] + sonlar[-1])
print(sonlar[2] / sonlar[1])
print(sonlar[-1] * sonlar[1])

print (sonlar.insert(-1, 350000))
print(sonlar.remove(-290000))

#5 t_shaxslar va z_shaxslar degam 2ta ro'yxat yarating va biriga o'zingiz eng ko'p 
# hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizning tirik bo'lgan 
# shaxslarning ismlarini yozing.
t_shaxslar = ['Muhammad SAV', 'Abu Bakr Siddiq', 'Umar ibn Hattob', 'Usmon ibn Afvon',
'Ali ibn AbuTolib']
z_shaxslar = ['Yorqinjon', 'Naziraxon', 'Nurulloh']
  
#6 Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), 
# quyidagi ko'rinishda chiqaring.

print(f"Men {t_shaxslar.pop(0)} va {z_shaxslar.pop(0)} ning suhbatiga guvoh bo'lishni istardim")

#7 friends nomli bo'sh ro'yxat tuzing va unga .append() metodi yordamida 5-6 mehmonga
# chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append('Abdurahmon')
friends.append('Hojiakbar')
friends.append('Akramjon')
friends.append('Muzaffar')
friends.append('Lazizbek')
friends.append('To\'rabek')
print(friends)

#8 Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi orqali 
# o'chrib tashlang'
friends.remove('Lazizbek')
friends.remove('To\'rabek')
print(friends)

#9 Ro'yxatning boshiga, ohiriga va o'rtasiga yangi ismlarni kiriting.
friends.insert(3, 'Asadbek')
friends.append('Lazizbek')
friends.insert(-1, 'Akbar Ali')
print(friends)

#10 Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append()
# metodlari yordamida mehmonga kelgan do'stlaringizni ismini friends ro'yxatidan
# sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(-1))
print("\nKelgan mehmonlar: ", mehmonlar)

















 





