# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:38:39 2024

@author: eren_
"""
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
import sys
from partsStock_menuUI import Ui_parca_stok
import sqlite3
from database import *
from stockAdd import stokEkle

class parcaStok(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui=Ui_parca_stok()
        self.ui.setupUi(self)
        self.stokekle=stokEkle()
        self.veritabani = kayit()
        self.ui.pb_parcastokAnamenu.clicked.connect(self.ekrankapa)
        self.ui.pb_parcaEkle.clicked.connect(self.parcaekle)
        self.ui.pb_parcaTableGuncelle.clicked.connect(self.Listele)
        self.ui.pb_parcaSil.clicked.connect(self.parca_sil)
        
    def parcaekle(self):
        self.stokekle.show()
        
    def ekrankapa(self):
        self.hide()
        
    def Listele(self):
        """Fetch data from the database and populate the table widget."""
        veriler = self.veritabani.Parca()
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setRowCount(len(veriler))
        
        for i, item in enumerate(veriler):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(item[0])))  
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(item[1])))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(item[2])))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(item[3])))
            
            
    def parca_sil(self):
        selected_row = self.ui.tableWidget.currentRow()
        
        if selected_row >=0:
            try:
                id = int(self.ui.tableWidget.item(selected_row,0).text())
                self.veritabani.parca_sil(id)
                print(f"Veritabanından silindi: ID{id}")
                
                self.ui.tableWidget.removeRow(selected_row)
                print(f"Table widget tan silindi : ID{id}")
            except Exception as e:
                print(f"Silme sırasında hata oluştu: {e}")
        else:
            QMessageBox.warning(self,"Hata","Lütfen silinecek bir satır seçiniz!!!")
        
        
        
        
        
        
            
            
            
            
            
            
            
        