# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:45:41 2024

@author: eren_
"""

from PyQt5.QtWidgets import * 
import sys
from partsStockAddmenuUI import Ui_MainWindow
import sqlite3
from database import *

class stokEkle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.veritabani = kayit()
        self.ui.pushButton_Anamenu.clicked.connect(self.ekrankapa)
        self.ui.pushButton_kaydet.clicked.connect(self.parcaekle)
        
    def parcaekle(self):
        parcaadi= self.ui.lineEdit_stokParcaadi.text()
        parcafiyat= self.ui.spinBox_stokParcafiyat.value()
        parcaadet= self.ui.spinBox_stokParcaadet.value()
        print(parcaadi,parcafiyat,parcaadet)
        
        deger = self.veritabani.ParcaEkle(parcaadi, parcafiyat, parcaadet)
        if deger:
            QMessageBox.information(self,"Bilgi","Kaydınız oluşturuldu")
        
        
    def ekrankapa(self):
        self.hide()    
    