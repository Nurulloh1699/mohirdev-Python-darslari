# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:56:13 2024

@author: DavrServis
"""

# import avto_info_mod # avto_info_mod modulini chaqiramiz.
# avto1 = avto_info_mod.avto_info("gm", "jentra", "qora", "avtomat", 2022, 15000)
# avto_info_mod.info_print(avto1)

import avto_info_mod as aim 

# avto_info funksiyasini chaqiramiz
avto1 = aim.avto_info("gm", "malibu", "qora", "avtomat", 2023, 40000)

# info_print funksiyasi yordamida ma'lumotlarni chiqaramiz
aim.info_print(avto1)

from avto_info_mod import avto_info, info_print
avto1 = avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
info_print(avto1)

from avto_info_mod import avto_info as ainfo
from avto_info_mod import info_print as iprint
avto1 = ainfo ("gm", "malibu", "qora", "avtomat", 2020, 40000)
iprint(avto1)

from avto_info_mod import * 
avto1 = avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
info_print(avto1)
