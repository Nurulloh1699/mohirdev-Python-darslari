# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:31:20 2025

@author: DavrServis
"""

import requests
import googletrans

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()['slip']['advice']
print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest = 'uz')
print(tarjima.text)