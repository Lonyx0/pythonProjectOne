# -*- coding: utf-8 -*-
"""
Created on Mon May 27 01:43:58 2024

@author: eren_
"""

from PyQt5.QtWidgets import *
import sys
import sqlite3
from loginScreenUI import *
from register import kayitol
from database import *
from mainMenu import Anamenu


class pageLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.kayitsayfa = kayitol()
        self.veritabani = kayit()
        self.anamenusayfa = Anamenu()
        self.ui.pb_kaydol.clicked.connect(self.kaydol)
        self.ui.pb_giris.clicked.connect(self.girisYap)
    
        
    def girisYap(self):
        kullaniciAdi = self.ui.le_kullaniciAdi.text()
        sifre = self.ui.lineEdit_2.text()
        
        dogrulama = self.veritabani.KullaniciGetir()
        if kullaniciAdi == "" or sifre == "":
            QMessageBox.warning(self,"Hata","Giriş Bilgileri boş bıraklamaz!!!")
    
        else:
            bos = False
            for deger in dogrulama:
                if kullaniciAdi == deger[4] and sifre == deger[5]:
                    bos = True
                    break
                
            
        
        if bos:
            QMessageBox.information(self,"bilgi","Giris basarili")
            self.anamenusayfa.Listele()
            self.anamenusayfa.show()
        else:
            QMessageBox.information(self,"bilgi","Giris basarisiz")
        
        
        
    def kaydol(self):
        self.kayitsayfa.show()
    
        
        
        
if(__name__=="__main__"):
    app=QApplication(sys.argv)
    window=pageLogin()
    window.show()
    sys.exit(app.exec_())

