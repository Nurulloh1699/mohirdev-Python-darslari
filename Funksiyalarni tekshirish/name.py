# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:01:05 2025

@author: DavrServis
"""

def get_full_name(ism, familiya, otasi = ''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()