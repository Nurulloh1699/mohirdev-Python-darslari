# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 16:59:18 2025

@author: DavrServis
"""

import pickle
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint as print

# Ma'lumotlarni o'qiymiz
with open('binolar_fixed.dat', 'rb') as file:
    binolar = pickle.load(file)
    hududlar = pickle.load(file)

print("Binolar va ularning qamrov hududlari:")
print(binolar)

# GREEDY algoritmi
yakuniy_binolar = set()

# Barcha hududlar kamida bitta bino tomonidan qamrab olinganligini tekshiramiz
qamrab_olingan_hududlar = set()
for bino_qamrovi in binolar.values():
    qamrab_olingan_hududlar |= bino_qamrovi

if qamrab_olingan_hududlar != hududlar:
    print("❌ Xatolik: Ba'zi hududlar hech qaysi bino tomonidan qamrab olinmagan!")
    print(f"Qamrab olinmagan hududlar: {hududlar - qamrab_olingan_hududlar}")
else:
    print("✅ Barcha hududlar kamida bitta bino tomonidan qamrab olingan.")
    
    # Algoritm har bir qadamni bosqichma-bosqich sharhlab boradi
    while hududlar:
        print("\n--- Yangi iteratsiya ---")
        best_bino = None
        qamralgan_hududlar = set()
        
        print("🔍 Har bir bino qamrovi tahlil qilinmoqda...")
        for bino, bino_qamrovi in binolar.items():
            qamrov = hududlar & bino_qamrovi  # Hozirgi bino qancha yangi hududni qamrab oladi?
            print(f"   {bino}: Qamrab olingan hududlar {qamrov}")
            
            # Eng ko'p yangi hududni qoplaydigan binoni tanlash
            if len(qamrov) > len(qamralgan_hududlar):
                best_bino = bino
                qamralgan_hududlar = qamrov
                print(f"   ✅ Hozircha eng yaxshi bino: {best_bino}, Qamrab olgan hududlari: {qamralgan_hududlar}")
        
        # Agar hech qanday bino tanlanmasa, algoritm to'xtaydi
        if best_bino is None:
            print("❌ Xatolik: Hududlarni to'liq qamrab olish imkonsiz!")
            print(f"Qamrab olinmagan hududlar: {hududlar}")
            break
        
        # Eng yaxshi binoni tanlaymiz va uning qamrab olgan hududlarini olib tashlaymiz
        hududlar -= qamralgan_hududlar
        yakuniy_binolar.add(best_bino)
        
        print(f"🏢 Tanlangan bino: {best_bino}")
        print(f"📉 Qolgan qoplanmagan hududlar: {hududlar}")
        print(f"✅ Hozirgacha tanlangan binolar: {yakuniy_binolar}")
    
    print("\n🎯 Yakuniy natija: Minimal binolar to'plami")
    print(yakuniy_binolar)
    
    # 📊 **Jadval shaklida natijalarni chiqarish**
    df = pd.DataFrame([(bino, binolar[bino]) for bino in yakuniy_binolar], columns=["Tanlangan bino", "Qamrab olingan hududlar"])
    print(df)
    
    # 📈 **Grafik shaklida natijalarni chiqarish**
    bino_names = list(binolar.keys())
    qamrov_miqdori = [len(binolar[bino]) for bino in bino_names]
    
    plt.figure(figsize=(10, 5))
    plt.bar(bino_names, qamrov_miqdori, color="skyblue")
    plt.xlabel("Binolar")
    plt.ylabel("Qamrab olingan hududlar soni")
    plt.title("Har bir binoning qamrov hududlari")
    plt.xticks(rotation=90)
    plt.show()
    
    # 📊 **Qamrov samaradorligini hisoblash**
    total_hudud = len(qamrab_olingan_hududlar)
    yakuniy_qamrov = sum(len(binolar[bino]) for bino in yakuniy_binolar)
    print(f"📊 Yakuniy binolar {yakuniy_qamrov} hududni qamrab oldi ({(yakuniy_qamrov / total_hudud) * 100:.2f}% samaradorlik).")

