# -*- coding: utf-8 -*-
"""
Created on Mon May 27 02:08:14 2024

@author: eren_
"""

from PyQt5.QtWidgets import *
import sys
from register_screenUI import *
import sqlite3
from database import *

class kayitol(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.veritabani = kayit()
        self.ui.pushButton.clicked.connect(self.kayitol)
    
    def kayitol(self):
        ad = self.ui.le_kayitAd.text()
        soyad = self.ui.le_kayitSoyad.text()
        telno = self.ui.le_kayitTelno.text()
        eposta = self.ui.le_kayitEposta.text()
        sifre = self.ui.le_kayitSifre.text()
        
        print(ad,soyad,telno,eposta,sifre)
        
        deger = self.veritabani.KullaniciEkle(ad, soyad, telno, eposta, sifre)
        if deger:
            QMessageBox.information(self,"Bilgi","Kaydınız oluşturuldu")
        