# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:19:55 2024

@author: eren_
"""

from PyQt5.QtWidgets import *
import sys
from device_registerScreenUI import Ui_MainWindow
import sqlite3
from database import *

class cihazKayit(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.veritabani = kayit()
        self.ui.pb_kayitekranKaydet.clicked.connect(self.telefonekle)
        self.ui.pb_kayitekranAnamenu.clicked.connect(self.ekrankapa)
        
    def ekrankapa(self):
        self.hide()
        
        
    
    
    def telefonekle(self):
        marka = self.ui.comboBox_marka.currentText()
        model = self.ui.le_cihazModel.text()
        hafiza = self.ui.comboBox_marka_2.currentText()
        garanti = self.ui.checkBox_garanti.isChecked()
        sikayet = self.ui.textEdit_cihazSikayet.toPlainText()
        
        print(marka,model,hafiza,garanti,sikayet)
        
        deger = self.veritabani.TelefonEkle(marka, model, hafiza, garanti, sikayet)
        if deger:
            QMessageBox.information(self,"Bilgi","Kaydınız oluşturuldu")
        