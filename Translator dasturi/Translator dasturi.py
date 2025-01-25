# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 08:36:25 2025

@author: DavrServis
"""

from googletrans import Translator
tarjimon = Translator()

msg = "Tarjima uchun so'z kiriting(chiqib ketish uchun 'q' deb yozing): "
while True:
    text = input(msg)
    if text == "q":
        break
    else:
        tarjima = tarjimon.translate(text, src = 'uz', dest = 'en')
        print(tarjima.text)