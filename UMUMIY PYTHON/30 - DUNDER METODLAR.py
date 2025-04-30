# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 08:48:55 2025

@author: DavrServis
"""

# 30 - DARS.
# DUNDER METODLAR.

# Bu metodlarni muisollar orqali ko'rib chiqamiz.
# class Avto:
#     __num_avto = 0
#     """Avto nomli klass"""
#     def __init__(self, make, model, rang, yil, narx, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model 
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         Avto.__num_avto += 1
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 40000, 1000)
# print(avto1)
# # Natija: <__main__.Avto object at 0x0000013267839430>

    # def __str__(self):
    #     return f"Avto: {self.make} {self.model}"

    # def __repr__(self):
    #     return f"Avto: {self.make} {self.model}"
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 40000, 1000)
# print(avto1)    
# Natija: Avto: GM Malibu.

# repr(avto1)
# Natija: Avto: GM Malibu

# Asosiy matn bilan ishlaydigan Dunder metodlar bilan tanishdik.

# Endi taqqoslash metodlari bilan tanishamiz.
# x.__lt__(self, y) = (x < y)
# x.__le__(self, y) = (x <= y)
# x.__gt__(self, y) = (x > y)
# x.__ge__(self, y) = (x >= y)
# x.__eq__(self, y) = (x == y)
# x.__ne__(self, y) = (x != y)

    # def __eq__(self, y):
    #     return self.narx == y.narx
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# print(avto1 == avto2)
# print(avto1 < avto2)
# Natija: False # Yuqorida funksiya yozganimiz uchun osongina ikki avto narxlari teng ekanini tekshirib olyabmz.
# Natija: TypeError: '<' not supported between instances of 'Avto' and 'Avto'

# Endi ikki avtolarning narxlari kicik yoki katta ekanini tekshiramiz.
    # def __lt__(self, y):
    #     return self.narx < y.narx
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# print(avto1 > avto2)
# print(avto1 < avto2)
# print(avto1 <= avto2)
# Natija: False
# Natija: True
# Natija: TypeError: '<=' not supported between instances of 'Avto' and 'Avto'
    # def __le__(self, y):
    #     return self.narx <= y.narx
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# print(avto1 <= avto2)
# print(avto1 <= avto2)
# Natija: True
# Natija: False

# Endi biz metodlarni uzunligini ko'rishni uchun nima qilishimizni ko'rib chiqamiz.
# class Avtosalon:
#     """Avtosalon klassi"""
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []
   
#     def __repr__(self):
#         return f"{self.name} avtosalon"

# salon1 = Avtosalon("MaxAvto")

# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)

# print(salon1)
# Natija: MaxAvto avtosalon\
    
# Shu o'rinda isinstance funksiyasi bilan tanishamiz. Bu funksiya ma'lum bir obyekt u yoki bu klassga tegishlimi yoki yo'q shuni aniqlab
# beradi.
# print(isinstance(4, int))
# Natija: True
    # def add_avto(self, * qiymat):
    #     for avto in qiymat:
    #         if isinstance(avto, Avto):
    #             self.avtolar.append(avto)
    #         else:
    #             print("Avto klassiga oid avto kiriting")
# Bu funksiya bilan tanishishimizdan maqsad yuqoridagi avtolar = [] ro'yxatimizga faqat Avto (va o'rniga boshqa klasslarni ham yozishimiz
# mumkin) klassiga tegishli avtolarni qo'shishga ruxsat beramiz holos.
# salon1 = Avtosalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.append(avto1, avto2, avto3)
    # def __getitem__(self, index):
    #     return self.avtolar[index]
    
# salon1 = Avtosalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)
# print(salon1[1])
# print(salon1[:])
# Natija: Avto: BMW M5
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]
# salon1[0] = Avto("Mercedes Benz", "S-klass", "Qora", 2024, 200000)
# Natija: TypeError: 'Avtosalon' object does not support item assignment

    # def __setitem__(self, index, qiymat):
    #    self.avtolar[index] = qiymat

# salon1 = Avtosalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)
# salon1[0] = Avto("Mercedes Benz", "S-klass", "Qora", 2024, 200000)
# print(salon1[0])
# Natija: Avto: Mercedes Benz S-klass

# salon1()
# Natija: TypeError: 'Avtosalon' object is not callable

# Endi shu xatoni bartaraf etishni ko'rib chiqamiz. Buning uchun:
    # def __call__(self):
    #     return [avto for avto in self.avtolar]
# Kerakli metodni yozib oldik va endi salon1 chaqirsak bo'ladi.
# salon1 = Avtosalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)    

# print(salon1())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]

# Bu __call__ metodiga biz istalgancha shart berishimiz mumkin va hozir bu metodga murojaat qilganimizda berilgan qiymatlarimiz
# chaqirilgan metodga qo'shilsin deb shart yozamiz: 
    # def __call__(self, * qiymat): # Biz call metodi orqali istalgancha metod chaqirsa bo'ladigan qilib qo'ydik. 
    #     if qiymat:
    #         for avto in qiymat:
    #             self.add_avto(avto)
    #     else:
    #         return [avto for avto in self.avtolar]

# salon1 = Avtosalon("MaxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)  

# avto4 = Avto("Mazda", "6", "Qizil", 2016, 25000)
# avto5 = Avto("Volkswagen", "Polo", "Oq", 2020, 18000)
# avto6 = Avto("Honda", "Accord", "Qora", 2018, 22000)
# print(salon1[:])
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]

# salon1(avto4, avto5)
# print(salon1[:])
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra, Avto: Mazda 6, Avto: Volkswagen Polo] # Mana yana 2ta mashina qo'shdik.
# salon1(avto6)
# print(salon1[:])
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra, Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord] # + yana 1ta mashina.
# salon1() # Klassimizni chaqirish uchun shu usulni qo'llash to'g'riroq bo'ladi.
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra, Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord]

# OPERATOR OVERLOADING.
# x, y = 5, 10

# print(x + y)
# Natija: 15
# print(x * 5)
# Natija: 25
# Yoki matnlar bilan har hil amallar.
# s1 = "Assalomu "
# s2 = "Aleykum"

# print(s1 + s2)
# Natija: Assalomu Aleykum
# print(s1 * 5)
# Natija: Assalomu Assalomu Assalomu Assalomu Assalomu 

# Shunga o'xshash. Va endi shu amallar aslida qanday ishlaydi shularni ko'rib chiqamiz.
# salon1 = Avtosalon("MaxAvto")
# salon2 = Avtosalon("LuxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)  

# avto4 = Avto("Mazda", "6", "Qizil", 2016, 25000)
# avto5 = Avto("Volkswagen", "Polo", "Oq", 2020, 18000)
# avto6 = Avto("Honda", "Accord", "Qora", 2018, 22000)
# salon2(avto4, avto5, avto6)
# print(salon1)
# Natija: MaxAvto avtosalon
# print(salon1())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]
# print(salon2)
# Natija: LuxAvto avtosalon
# print(salon2())
# Natija: [Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord]

# Endi biz bu ikki avtosalonni bir biriga qo'shib beradigan metod yozamiz (nomini, ichidagi avtomobillarni). Buning uchun maxsus
# metodlar bor avval ular bilan tanishamiz so'ngra metod yozamiz:
# __add__ - Qo'shish uchun 
# __sub__ - Ayirish uchun
# __mul__ - Ko'paytirish uchun
# __pow__ - Darajaga oshirish uchun
# __div__ - Bo'lish uchun

# Deamak endi biz metod yozishni boshlaymiz.
# class Avto:
#     __num_avto = 0
#     def __init__(self, make, model, rang, yil, narx, km=0):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         Avto.__num_avto += 1

#     def __str__(self):
#         return f"Avto: {self.make} {self.model}"

#     def __repr__(self):
#         return f"Avto: {self.make} {self.model}"

#     def __eq__(self, y):
#         return self.narx == y.narx

#     def __lt__(self, y):
#         return self.narx < y.narx

#     def __le__(self, y):
#         return self.narx <= y.narx


# class Avtosalon:
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosalon"

#     def add_avto(self, *qiymat):
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto klassiga oid avto kiriting")

#     def __getitem__(self, index):
#         return self.avtolar[index]

#     def __setitem__(self, index, qiymat):
#         self.avtolar[index] = qiymat

#     def __call__(self, *qiymat):
#         if qiymat:
#             for avto in qiymat:
#                 self.add_avto(avto)
#         else:
#             return [avto for avto in self.avtolar]

    # def __add__(self, boshqa_salon):
    #     if isinstance(boshqa_salon, Avtosalon):
    #         yangi_salon = Avtosalon(f"{self.name} {boshqa_salon.name}")
    #         yangi_salon.avtolar = self.avtolar + boshqa_salon.avtolar
    #         return yangi_salon


# salon1 = Avtosalon("MaxAvto")
# salon2 = Avtosalon("LuxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)

# avto4 = Avto("Mazda", "6", "Qizil", 2016, 25000)
# avto5 = Avto("Volkswagen", "Polo", "Oq", 2020, 18000)
# avto6 = Avto("Honda", "Accord", "Qora", 2018, 22000)
# salon2(avto4, avto5, avto6)

# Endi biz bu ikki salonni bir-biriga qo'shamiz:
# print(salon1())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]
# print(salon2())
# Natija: [Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord]

# salon3 = salon1 + salon2
# print(salon3())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra, Avto: Mazda 6, Avto: Volkswagen Polo, Avto: Honda Accord]    
# print(salon3.name)
# Natija: MaxAvto LuxAvto

# Endi keling biz yana shart qo'shaylik.
#     def __add__(self, y):
#         if isinstance(y, Avtosalon):
#            yangi_salon = Avtosalon(f"{self.name} {y.name}")
#            yangi_salon.avtolar = self.avtolar + y.avtolar
#            return yangi_salon
#         elif isinstance(y, Avto):
#            self.add_avto(y)

# salon1 = Avtosalon("MaxAvto")
# salon2 = Avtosalon("LuxAvto")
# avto1 = Avto("GM", "Malibu", "Qora", 2024, 35000)
# avto2 = Avto("BMW", "M5", "Yashil", 2022, 120000)
# avto3 = Avto("GM", "Jentra", "Oq", 2020, 13000)
# salon1.add_avto(avto1, avto2, avto3)

# avto4 = Avto("Mazda", "6", "Qizil", 2016, 25000)
# avto5 = Avto("Volkswagen", "Polo", "Oq", 2020, 18000)
# avto6 = Avto("Honda", "Accord", "Qora", 2018, 22000)
# salon2(avto4, avto5, avto6)

# print(salon1)
# Natija: MaxAvto avtosalon
# print(salon1())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra]
# print(avto4)
# Natija: Avto: Mazda 6
# salon1 + avto4
# print(salon1())
# Natija: [Avto: GM Malibu, Avto: BMW M5, Avto: GM Jentra, Avto: Mazda 6]

# Demak shunday usullar orqali o'zingizni obyektingizga qo'shimcha imkoniyatlar qo'shsangiz bo'ladi.

# AMALIYOT TOPSHIRIQLARI:
#1 - Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling. 

# Obyekt haqida ma'lumot (__rerp__)

# Talabalarni bosqichi bo'yicha solishtirish (__lt__,__eg__ va hokazo)
# class Shaxs:
#     """Shaxs degan klass yaratamiz"""
#     def __init__(self, ism, familiya, passport, email):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.email = email
#     def __repr__(self):
#         return f"{self.ism} {self.familiya}, {self.passport} {self.email}"
        
# shaxs1 = Shaxs("Nurulloh", "Abdurashidov", "AA002211", "nur2012@mail.ru")
# print(shaxs1)

# class Talaba:
#     def __init__(self, ism, familiya,idraqam):
#         self.ism = ism 
#         self.familiya = familiya
#         self.idraqam = idraqam
#     def __lt__(self, y):
#         return self.idraqam < y.idraqam

        
# talaba1 = Talaba("Nurulloh", "Abdurashidov", 123336)
# talaba2 = Talaba("Mavluda", "Abdurashidova", 15685)
# print(talaba1 > talaba2)
# print(talaba1 < talaba2)



#2 - Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga
# add_student(), __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.
# class Talaba:
#     def __init__(self, ism, familiya, idraqam):
#         self.ism = ism  # Talabaning ismini saqlash.
#         self.familiya = familiya  # Talabaning familiyasini saqlash.
#         self.idraqam = idraqam  # Talabaning ID raqamini saqlash.

#     def __repr__(self):
#         return f"{self.ism} {self.familiya} ({self.idraqam})"  # Talabaning matnli ko'rinishini qaytaradi.


# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi  # Fanning nomini saqlash.
#         self.talabalar = []  # Talabalar ro'yxatini bo'sh holda yaratish.

#     def add_student(self, talaba):
#         """Yangi talaba qo'shish."""
#         if isinstance(talaba, Talaba):  # Talaba obyektini tekshirish.
#             self.talabalar.append(talaba)  # Talabalar ro'yxatiga qo'shish.
#         else:
#             raise ValueError("Faqat Talaba obyekti qo'shilishi mumkin!")  # Noto'g'ri obyekt bo'lsa, xato chiqarish.

#     def __getitem__(self, index):
#         """Index orqali talabani olish."""
#         return self.talabalar[index]  # Berilgan indeksdagi talabani qaytaradi.

#     def __setitem__(self, index, talaba):
#         """Index orqali talabani o'zgartirish."""
#         if isinstance(talaba, Talaba):  # Talaba obyektini tekshirish.
#             self.talabalar[index] = talaba  # Berilgan indeksdagi talabani almashtirish.
#         else:
#             raise ValueError("Faqat Talaba obyekti qo'shilishi mumkin!")  # Noto'g'ri obyekt bo'lsa, xato chiqarish.

#     def __len__(self):
#         """Talabalar ro'yxatining uzunligini aniqlash."""
#         return len(self.talabalar)  # Talabalar ro'yxatidagi talabalar sonini qaytarish.

#     def __add__(self, talaba):
#         """+ operatori orqali talaba qo'shish."""
#         if isinstance(talaba, Talaba):  # Talaba obyektini tekshirish.
#             yangi_fan = Fan(self.nomi)  # Yangi fan obyektini yaratish.
#             yangi_fan.talabalar = self.talabalar + [talaba]  # Talabalar ro'yxatiga yangi talabani qo'shish.
#             return yangi_fan  # Yangi fan obyektini qaytarish.
#         else:
#             raise ValueError("Faqat Talaba obyekti qo'shilishi mumkin!")  # Noto'g'ri obyekt bo'lsa, xato chiqarish.

#     def __sub__(self, talaba_id):
#         """- operatori orqali talaba olib tashlash."""
#         yangi_fan = Fan(self.nomi)  # Yangi fan obyektini yaratish.
#         yangi_fan.talabalar = [talaba for talaba in self.talabalar if talaba.idraqam != talaba_id]  
#         # Talabalar ro'yxatidan berilgan IDga ega talabani olib tashlash.
#         return yangi_fan  # Yangi fan obyektini qaytarish.

#     def __call__(self, talaba=None):
#         """Fanni chaqiriladigan qilish."""
#         if talaba:  # Agar talaba berilgan bo'lsa.
#             self.add_student(talaba)  # Talabani qo'shadi.
#         else:
#             return self.talabalar  # Aks holda talabalar ro'yxatini qaytaradi.

#     def __repr__(self):
#         """Fanni va ro'yxatdagi talabalarni ko'rsatish."""
#         talabalar_ro_yxati = ", ".join([str(t) for t in self.talabalar])  # Talabalar ro'yxatini matnli formatda tuzish.
#         return f"{self.nomi} fani: [{talabalar_ro_yxati}]"  # Fanning nomi va talabalar ro'yxatini qaytarish.


# Misol uchun ishlatish
# fan = Fan("Matematika")  # "Matematika" nomli fan obyektini yaratish.

# talaba1 = Talaba("Nurulloh", "Abdurashidov", 123336)  # 1-talaba obyekti.
# talaba2 = Talaba("Mavluda", "Abdurashidova", 15685)  # 2-talaba obyekti.
# talaba3 = Talaba("Jasur", "To'raev", 987654)  # 3-talaba obyekti.

# Talabalarni qo'shish
# fan.add_student(talaba1)  # "Nurulloh Abdurashidov"ni ro'yxatga qo'shish.
# fan.add_student(talaba2)  # "Mavluda Abdurashidova"ni ro'yxatga qo'shish.
# fan.add_student(talaba3)  # "Jasur To'raev"ni ro'yxatga qo'shish.

# + operatori orqali talaba qo'shish
# talaba4 = Talaba("Shaxzod", "Nazarov", 54321)  # Yangi talaba.
# fan = fan + talaba4  # "Shaxzod Nazarov"ni ro'yxatga qo'shish.

# - operatori orqali talaba olib tashlash
# fan = fan - 15685  # ID raqami 15685 bo'lgan talabani olib tashlash.

# __call__ orqali fanni chaqirish va talaba qo'shish
# talaba5 = Talaba("Aziz", "Karimov", 112233)  # Yangi talaba.
# fan(talaba5)  # "Aziz Karimov"ni ro'yxatga qo'shish.

# Talabalarni ko'rish
# print(fan())  # Fanga qo'shilgan barcha talabalar ro'yxatini chiqaradi.
# print(fan)  # Fanning nomi va talabalar ro'yxatini chiqaradi.

# 30 - DARS TUGADI.