# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 06:32:58 2024

@author: DavrServis
"""

#4-dars Sonlar.
#13.10.2024.
#Muallif:Abdurashidov Nurulloh.

# Sonning ildizini topish: son**(1/2) shu formulani iwlatamiz.

# O'zgaruvchilarni ichiga biz har hil qiymatlarni berishimiz mumkin sonlar ham shular
# jumlasidandir. Biz hohlasak butun son(int 12) yoki bo'lmasam o'nlik son(float 1.6) ko'rinishida.

a = 20
b = 5.5 # ERIBOR BERING! float turidagi sonlarning orasi (.) bilan ajratiladi (,) emas 
# Quyida biz bu o'zgaruvhilarni tipini tekshirishni ko'rib chiqamiz.
print(type(b))

# Qiymatni uzun son shaklida berayotkanimizda uni o'qish qulay bo'lishi uchun 
# pastki chiziqni (_) ishlatishimiz mumkin bo'ladi.
aholi_soni = 8_142_307_120 # ko'rinishida.
print("Yer yuzining aholi soni:", aholi_soni, "ga teng.")

# O'zgaruchiga bir nechta qiymat berishta ularni vrgul bilan (,) ajratib yozishimiz kifoya 
# qiladi.
x, y, z = 12, 23, 5.5
print(x, y, z)

# ETIBOR BERING! Bo'lish (/) va ko'paytirish(*)(agar qiymatlarning bittasi o'nlik son bo'lsa) 
# amallarida qaytariladigan javob o'nlik ko'rinishida bo'ladi.
# Buni bartaraf etish uchun esa ikkitali bo'lish (//) va ko'paytirishda (*)(ikkala qiymat)
# ham butun son bo'lishini taminlash kerak.
d = 20/5 
q = 20*5.5
print(d, q)

d = 20//5 
q = 20*5
print(d, q)

# CONSTANT qiymatlar (o'zgarmas qiymatlar) Pythonda bunday tushuncha yoq lekin agar 
# o'zgaruvchi katta harflar (PI, A) bilan berilsa bu CONSTANT qiymat deb kelishib olingan.

radius = 20
PI = 3.14159
diametr = 2*radius # odatda diametr 2*radiusga teng bo'ladi.
print("Aylana uzunlig =", PI*diametr) # Aylana uzunligini topish uchun esa PI ni deametrga
# ko'paytirish bilan topiladi.

# O'zharuvcgilarda string va int qiymatlarini (+) qo'shib bo'lmaydi.
ism = "Jobir"
yosh = 36 # Bu holatni bartaraf qilish uchun esa (str) funksiyasidan foydalanamiz.
#yosh = str(yosh) # Aslida esa bunday qilish xato bo'ladi chunki endi yoshning qiymati (str)
# ga o'tib qoldi va keyinchalik foydalanmoqchi bo'lsak bu xato ko'rsatishi mumkin
xabar = ism + ' ' + str(yosh) + ' yoshda'# Xatolarni oldini olish uchun esa shu qatorda 
# yosh ni str ga o'tkazamiz.
print(xabar)

# Foydalanuvchining tug'ilgan yilini topishga harakat qilamiz.
#t_yil = int(input("Tug'ilgan yilingizni kiriting: ")) # Foydalanuvchidan tug'ilgan yilini so'raymiz.
# Yuqoridagi kodda xato yuz bermasligi uchun int() funksiyasini esdan chiqarmaymiz.
#yosh = 2024 - t_yil # Joriy yildan foydalanuvchi tug'ilgan yilini ayiramiz.
#print("Siz", yosh, "yoshda ekansiz.")

# 3 hil funksiya bilan yaqindan tanishib chiqamiz int(), float() va str()
a = int("10") # qiymatni butun son ko'rinishida saqlaydi.
b = float("10") # qiymatno o'nlik son ko'rinishida saqlaydi.
temp = str("36.6") # qiymatni matn ko'rinishida saqlaydi.

# TOPSHIRIQLAR
#1 Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:
# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur tuzing.
#son = int(input("Istalgan soningizni kiriting: "))
#print(son,"sonining kvadrati", son**2, "ga teng")
#print(son,"sonining kubi", son**3, "ga teng")

#2 Foydalanuvchining yoshini so'rab uning tug'ilgan yili aniqlovchi dastur tuzing.
#yosh = int(input("Yoshingizni kiriting: "))
#print("Siz", 2024-yosh,"yilda tug'ilgansiz.")

#3 Foydalanuvchidan ikkita son so'rab uning (+)(-)(*)(/) topadigan dastur.
print("Istalgan ikkita soningizni kiriting:")
a = int(input("1-son >>> "))
b = int(input("2-son >>> "))
print("Yig'indisi", a+b)
print("Ayirmasi", a-b)
print("Ko'paytmasi", a*b)
print("Bo'linmasi", a/b)



