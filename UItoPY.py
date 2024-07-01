# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:09:11 2024

@author: eren_
"""

from PyQt5 import uic
with open("parcaStokEkle_menuUI.py","w",encoding="utf-8") as fout:
    uic.compileUi("parcaStokEkle_menu.ui", fout)