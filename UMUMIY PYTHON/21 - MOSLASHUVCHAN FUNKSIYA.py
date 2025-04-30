# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:37:02 2025

@author: DavrServis
"""

# 21 - DARS.
# MOSLASHUVCHAN FUNKSIYA (*args, **kwargs).
# Agar funksiyangiz bir nechta argument qabul qilishi kerak bo'lsa-yu, lekin siz argumentlar sonini aniq bilmasangiz, Pythonda
# istalgancha qiymat qabul qiluvchi funksiya yaratish imkoniyati bor.


# *args USULI.
# Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa va parametrlar yagona qiymatlar ko'rinishida uzatilsa, funksiya 
# yaratishda argumentdan avval yulduzcha qo'yiladi (*arguments).

# Quyidagi misolni ko'raylik. summa() nomli funksiyamiz istalgancha sonlarni qabul qilib oladi va ularning yig'indisini hisoblaydi:
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# Bu funksiyani istalgancha parametr bilan chaqirish mumkin:
# print(summa(1,2,3,4,54))
# Natija: 64
# print(summa(4,5,6,7,8,3,1,34,564))
# Natija: 632

# *argsusulida barcha uzatilgan parametrlar (birdona bo'lsa ham) funksiya ichida o'zgarmas ro'yxatga (tuple) joylanadi. Bundan
# kelib chiqib yuqoridagi funksiyamizni yanada soddalashtirib yozishimiz mumkin:
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     return sum(sonlar)
# Funksiyani ishlatib ko'ramiz:
# print(summa(4,5,6,7))
# Natija: 22

# Agar funksiya bir nechta argument qabul qilsa, *args argumenti doim ohirida yoziladi:
# def summa(x, y, *sonlar):
#     """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
#     return x+y+sum(sonlar)
# Yuqoridagi funksiyamiz 2ta majburiy parametr qabul qiladi (x va y), undan keyingi qiymatlar esa ixtiyoriy bo'ladi:
# print(summa(2))
# Natija: TypeError: summa() missing 1 required positional argument: 'y'
# print(summa(9,10,11))
# Natija: 30
# print(summa(-10,10))
# Natija: 0


# **kwargs USULI.
# Agar funksiyaga kalit-qiymat ko'rinishida argumentlarni uzatish talab qilinsa va bunday oarametrlar soni noma'lum bo'lsa,
# argument oldidan ikkita yulduzcha qo'yiladi (**kwargs).

# **kwrgs - keyword argument (kalit so'zli argumentlar)

# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar

# Yuqoridagi funksiyamiz kompaniya va model degan ikki qiymatni qabul qiladi, undan keyin esa funksiyasiga istalgancha parametr
# uzatish mumkin. Bunday funksiyaga parametrlar KALIT = QIYMAT ko'rinishida uzatiladi.

# Funksiya ichida avval foydalanuvchi kiritgan QO'SHIMCHA qiymatlardan iborat ma'lumotlar deb nomlangan lug'at shakllantiriladi.
# Undan keyin esa majburiy parametrlarni lug'atga qo'shamiz.
# avto1 = avto_info("GM", "malibu", rang = "qora", yil = 2018)
# avto2 = avto_info("KIA", 'K5', rang = "qizil", narx = 35000)
# print(avto2)
# Natija: {'rang': 'qizil', 'narx': 35000, 'kompaniya': 'KIA', 'model': 'K5'}

# AMALIYOT TOPSHIRIQLARI.
#1 - Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing.
# def summa(*sonlar): # Funksiya yaratib olyapmiz (istalgancha parametr qabul qiladigan funksiya)
#     kopaytma = 1 # Boshlang'ich qiymat qilib 1 soni olinadi, mega aynan 1? Ko'paytma operatsiyasi 1 bilan boshlanadi (1 * n = n)
#     for son in sonlar: # Son degan o'zgaruvchi yaratib olinadi va u sonlar ichidagi har bir songa tenglanadi.
#         kopaytma *= son # Bu yerda kopaytma o'zgaruvchisiga har bir son ko'paytiriladi. Bu kopaytma = kopaytma * son deganidir.
#     return kopaytma # Funksiya oxirida kpaytma qiymatini tashqi kodga qaytaradi.
# print(summa(3,5,1,6,4,))
# Natija: 360

#2 - Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy
# argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
# def talaba_info(ism, familiya, **malumotlar):
#     malumotlar["ism"] = ism
#     malumotlar["familiya"] = familiya
#     return malumotlar
# talaba1 = talaba_info("Nurulloh", "Abdurashidov", t_yil = 1999, yoshi = 25)
# print(talaba1)
# Natija: {'t_yil': 1999, 'yoshi': 25, 'ism': 'Nurulloh', 'familiya': 'Abdurashidov'}

# 21 - DARS TUGADI.