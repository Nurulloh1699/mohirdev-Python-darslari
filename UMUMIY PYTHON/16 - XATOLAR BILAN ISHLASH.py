# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:24:30 2025

@author: DavrServis
"""

# 16 - DARS.
# XATOLAR BILAN ISHLASH.

# Har qanday dasturchi kod yozishda xatoga yo'l qo'yadi. Ko'p yozgan odam ko'p xato qiladi va bu tabiiy. Ba'zi xatolarimiz
# Python tomonidan dasturbajarilishidan avval aniqlanadi. Ba'zilari essa dastur bajarish jarayonida aniqlanib, dasturimiz
# to'xtab qoladi.

# Ushbu bobda dastavval dasturchilar ko'p yo'l qo'yadigan xatolar bilan tanishamiz. Keyin esa dastur bajarilishi davomida
# xatolik yuz berganda dastur to'xtab qolishining oldini olishni o'rganamiz.

# XATOLARNING TURLARI.
# SiyntaxError - SINTAKSIS XATOLIK.
# Biz bu xatolik turo nilan 2 - bobda tanishgan edik. SyntaxError eng ko'p uchraydigan xato bo'lib, odatda, dasturlash tili
# qoidalariga amal qilmaslik natijasida kelib chiqadi. Aksar dasturlash muhitlari bunday xatolikni dastur bajarilishidan oldin
# aniqlab, dasturchiga ishora beradi. Sintaksis xatolik bor dasturni Python bajarmaydi.
# print "Hello World!"
# SyntaxError: Missing parentheses in call to 'print'.
# Did you mean print("Hello World!")?

# Odatda, dasturlash mihiti xatoning turi bilan birga (SyntaxError) xato haqida qo'shimcha ma'lumot ham beradi:
# Missing parentheses in call to 'print'. Did you mean print("Hello World!")? shu ko'rinishda.

# Xatolar bilan ishlashda xatolik matnini sinchikovlik bilan o'qish va tahlil qilish juda muhim. Agar ingliz tilini bilmasangiz
# Google Translate yoki Yandex Tarjimon kabi onlayn xizmatlar yordamida xatolik matnini o'zingizga tushunarli (O'zbek yoki Rus)
# tilga tarjima qilib xatoni to'g'irlashingiz mumkin.

# EOL va EOF xatolik.
# EOL (End of Line - qator yakuni) xatoligi sintaksis xatoliklarning bir turi bo'lib, odatda, qator oxirida qo'shtirnoqni
# (bir tirnoq) yopish esdan chiqqanda yuzaga keladi.
# print("Hello World! 
# SyntaxError: Unterminated string literal (detectedat line 2752)


# EOF (End of function - funksitya yakuni) xatoligi esa funksiya oxirida qavsni yopish esdan chiqqanda yuzaga keladi.
# print("Hello World!"
# SyntaxError: '(' was never closed

# EOF xatoligining muammoli tarafi - Python aynan qaysi funksiya yopilmay qolganini ko'rsata olmaydi va dastur yakuniga
# ishora qiladi. Dasturingiz uzun bo'lsa, kodingizni sinchiklab ko'zdan kechirib chiqish talab etiladi.

# IndentationError - JOY TASHLASHDA XATOLIK.
# Python tilida vaziyatga qarab kodni qator boshidan joy tashlab yoki tashlamasdan yozish muhim ahamiyatga ega. Qator boshidan
# asossiz joy qoldirish IndentationError ga olib keladi.

# Quyidagi kodga e'tibor bering, qator boshida 1 dona bo'sh joy qolgani uchun dasturlash muhiti xatoni aniqlab, ╳ bilan belgilab
# qo'yadi.
# print("Hello World!") # Bu kod shunga misol.

# Ba'zi joylarda esa, aksincha, bo'sh joy tashlab yozish talab qilinadi. Masalan, for siklida yoki if-elif-else shartlarining
# ichida va hokazo.
# print("O'ngacha sanaymiz.")
# for n in range(11):
# print(n) # Bu qatorddagi xatolik bitta Tab yani 4ta harflik bo'sh joy tashlanmagan degani (IndentationError).

# Yana bir misol ko'ramiz:
# son = 50 
# if son >= 0:
#     print("Musbat son")
# else:
# print("Manfiy son") # Bu qarda ham xatolik qaytaradi yana print ni bir Tab surishni unutdik.

# QANDAY JOY TASHLASHIMIZ KERAK.
# Aslida, hech bo'lmaganda 1 harflik bo'sh joy qoldirish ham bizni IndentationError dan holos etadi. 

# ETIBOR BERING! Agar dastur boshidan beri bitta Tab dek joy tashlab kelgan bo'lsangiz ohirigacha shunday qiling va aksincha.

# RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK
# Run time error dastur bajarish jarayonida kelib chiqadi va dasturning ishlashini to'xtatadi. Sintaksis xatolikdan farqli ravishda 
# Python bunday xatolarni dasturni bajarishdan oldin aniqlay olmaydi. Bu xatoliklarning bir necha turi bor.
# Ulardan ba'zilari bilan tanishamiz:

# TypeError
# Biror funksiya yoki metodga noto'g'ri ma'lumot turini yuborish:
# son = input("Istalgan sonni kiriting: ")
# print(f"{son} ning kvadrati {son**2} ga teng.") 
# Yuqoridagi koddagi xatolik biz sonni butun son (int) yoki o'nlik son (float) ga o'tkazib olmaganimiz.

# NameError
# O'zgaruvchi funksiya, obyekt nomini noto'g'ri yozish natijasida kelib chiquvchi xatolik.
# Quyida bunga misol ko'ramiz.
# prit("Hello World!")
# Natijada xatolik beradi. Biz print funksiyasini yozishda xatolikka yo'l qo'ydik.

# Yana bir misol ko'ramiz:
# mevalar = ['olma', 'uzum', 'shaftoli', 'bexi']
# for meva in mvalar: # Xatolik shu qatorga to'g'ri keladi. mevalar degan o'zgaruvchini nomini yozishda xatoga yo'l qo'ydik.
#     print(meva)

# ValueError
# Funksiyaga noto'g'ri qiymatni yuborish natijasida xatolik.
# Quyida bunga misol ko'ramiz.
# son = int(input("Istalgan sonni kiriting: "))
# if son >= 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")
# Dasturni bajarishda xatolik yuz beradi qachon biz qiymat berishda adashsak. Masalan, biz 5.5 kiritdik, bu xato chunki yuqorida 
# biz son degan o'zgaruvchiga butun son deb (int) qiymatlaganmiz. Aytish mumkinki kodimiz universalroq bo'lishi uchun son ga
# o'nlik son deb (float) qiymat berishimiz kerak bo'ladi.

# IndexError
# Yangi dasturchilar yo'l qo'yadigan yan bir xato indeks xatolikdir. Ya'ni ro'yxat elementlariga murojaat etishda ineksini
# noto'g'ri kiritish (ro'yxatda mavjud bo'lmagan elementga murojaat qilish):
# Quyida bunga misol ko'ramiz:
# mevalar = ['olma', 'anor', 'uzum']
# print(mevalar[3]) # Xatolik shundan iboratki oldingi darslarimizda biz aytib o'tkanimizdek dasturlashda indekslash 0dan boshlanadi.
# Shu qoidaga asosan bizning ro'yxatimizda elementlar faqat 2gacha indekslangan shu sababli IndexError xatosi kelib chiqyapti.

# ZeroDivisionError
# Dastur jarayonida 0ga bo'lish natijasida yuzaga keladigan xatolik.
# x, y = 50, 50
# z = 250/(x-y) # x-y=0
# Yuqoridagi misolda qavsning ichidan 0 degan javob chiqadi va 0ga bo'lib bo'lmasligini inobatga olgan holda xato qayd etiladi.

# MANTIQIY XATOLAR.
# Mantiqiy xatolar - dasturchi tomonidan dastur algoritmini yozishda yo'l qo'yilgan xatolar. Bunday xatolar dastur bajarilishiga
# to'sqinlik qilmasa-da, dastur to'g'ri ishlashiga xalaqit qiladi va kutilgan natijani bermaydi.

# Mantiqiy xatolar eng ko'p uchraydigan va aniqlash qiyin bo'lgan xatolar hisoblanadi. Aksar holatlarda Python mantiqiy xatolarni
# aniqlamaydi va dastur bajarilaveradi (lekin kutilgan natija chiqmaydi). Bunday xatolarni oldini olish uchun dasturimizning har
#  bir  qadamida chiqayotgan natijalarni tekshirib borish kerak. Katta dasturlar o'nlab, balki yuzlab funksiyalardan iborat bo'ladi, 
# agar mantiqiy xatolar vaqtida topilmasa, minglab qator kodlarni ko'zdan kechirib chiqish talab qilinishi mumkin.

# Mantiqiy xatolar turli ko'rinishda bo'lishi mumkin, masalan, sonlar bilan ishlashda:
# radius = 5
# pi = 4.14
# aylana_yuzi = pi * radius ** 2
# print(aylana_yuzi)
# Kod bajariladi, natija ham chiqadi. Lekin natija xato. Nima uchun? Sababi, biz π = 4.14 deb xato yozib ketdik
# (to'g'ri qiymat: π = 3.14).

# Avval aytkanimizdek, mantiqiy xatolarning oldini olish uchun dasturimizning har bir qadamida chiqayotgan natijalarni
# tahlil qilib borish muhim. Sodda dasturlar qo'lda bajariladi, murakkabroq funksiyalar uchun esa maxsus test dasturlar yoziladi.
# Test dasturlar yozish haqida kelgusi boblarda alohida gaplashamiz. Hozir esa qo'lda tekshirishni ko'raylik:
# son = float(input("Istalgan son kiriting: ")) # 4 ni kiritamiz va 2 degan javobni olamiz.
# ildiz = son**1/2
# print(f"{son}ning ildizi {ildiz} ga teng.")
# Dasturimiz biz kutgan natijani berdi. Lekin yaxshi dasturchi bitta test bilan chegaralanmaydi. Dasturni qayta bajaramiz:
# son = float(input("Istalgan son kiriting: ")) # 9 ni kiritamiz va 4.5 degan javobni olamiz.
# ildiz = son**1/2
# print(f"{son}ning ildizi {ildiz} ga teng.")   
# Mana endi natija xato, 9 sonining ildizi 4.5 bo'lib chiqti. Kodni tahlil qilamiz: 2 - qatorda ildizni hisoblashda 1/2 qavs ichida
# yozilmagani xatolikka olib kelyapti. Natijada foydalanuvchi kiritgan son avval 1 - darajaga oshirildi va undan keyin 2ga bo'lindi.
# Kodni to'g'irlaymiz va dasturni 3-4 marta turli qiymatlar berib bajarib ko'ramiz:
# son = float(input("Istalgan son kiriting: ")) # 9 ni kiritamiz va 3 degan javobni olamiz.
# ildiz = son**(1/2)
# print(f"{son}ning ildizi {ildiz} ga teng.")

# Ba'zida noo'rin bo'sh joy qoldirish (yoki qoldirmaslik) ham mantiqiy xatoga olib kelishi mumkin:
# mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi")
# Yuqorida "Dastur tugadi" matni bir marta, dastur tugaganidan so'ng chiqishi kerak edi. Lekin o'ngga surilib qolgani uchun bir
# necha marta qaytarildi.
 
# Bundan boshqa ham mantiqiy xatoliklar juda ko'p uchraydi. Mantiqiy xatoliklar mutlaqo topilmasdan ham qolib ketishi va dastur
# bozorga chiqqanidan keyin aniqlanishi tabiiy hol. Shuning uchun ham aksar dasturlar tez-tez yangilanib turadi.

# Dasturlash jarayonida bundan boshqa xatolilklar ham ko'p uchraydi. Biz ulardan ba'zilari bilan tanishdik, xolos. Keyingi bo'limda
# Runtime xatoliklar  dastur davomida aniqlash va dastur to'xtab qolishining oldini olishni o'rganamiz.

# AMALIYOT TOPSHIRIQLARI.
#Quyidagi dasturlarda bir nechta xatolar bor ularni to'g'irlang:

#1
# son = float(input("Juft son kiriting: ")
# if son%2==0:
#     print("Bu son juft emas.') # shu qatorda xatolik bor (qo'shtirnoq va birtirnoq bilan bog'liq)
# else:
#     print("Rahmat!"))    

#2
# yosh = (input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18 # Xatolik shu qatorda elif sharti berkitilmagan ohirida ikkita nuqta qo'yilmagan.
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")

#3
# x = float(input("Birinchi sonni kiriting: ") # Shu qatorda qavs yopilmagan.
# y = float(input("Ikkinchi sonni kiriting: ") # Shu qatorda qavs yopilmagan.
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}") # shu qatorda xatolik bor (qo'shtirnoq va birtirnoq bilan bog'liq)
# else # Shu qatorda xatolik bor else funksiyasi yopilmagan.
#     print(f"{x}>{y}")

#4
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun' # shu qatorda xatolik bor ro'yxatning qavslari yopilmagan.

# # shu qatorga savat degan bo'sh ro'yxat qo'shishimiz kerak edi.

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat # shu qatorda xatolik bor for funksiyasi yopilmagan.
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")     

#5
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               # 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: ')) # shu qatorda xatolik bor f-string ichidagi matnni qo'shtirnoqqa
# # olish kerak edi yoki (') belgisi oldidan (\) belgisini qo'yish kerak edi.

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahslot) # shu qatorda xatolik bor (mahslot) bo'lib qolgan (mahsulot) bo'lishi kerak edi.
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas: # if deb shart berishta hamxatolik bor to'g'ri variantni quyirog'da keltirdim.
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda mavjud.")

#6
# users = ['alisher1983','aziza','yasina' 'umar'] # Shu qatorda ('yasina'(,) 'umar') belgisining tashlab ketilishi mantiqiy xatoga
# # sabab bo'ladi. 

# login = input("Yangi login tanlang:' ) # Yuqorida ko'rgan xatoligimiz qo'shtirnoq bilan bog'liq. Bu qatordagi yana bir xato 
# # .lower() metodi qo'shilmagan

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")

#7
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n): # Agar shu qatordagi ifodaga son % n == 0 ga deb qo'yilsa to'g'ri boladi.
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
        

# 16 - DARS TUGADI.