from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from main_menuUI import Ui_MainWindow  
from deviceAdd import cihazKayit
from partsStock import parcaStok
from database import kayit

class Anamenu(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.cihazkayit = cihazKayit()
        self.parcastok = parcaStok()
        self.veritabani = kayit()
        
        
        self.ui.pb_cihazKayitEkrani_4.clicked.connect(self.cihazKayit)
        self.ui.pb_parcaStok_4.clicked.connect(self.parcaStok)
        self.ui.pb_anamenuGuncelle_4.clicked.connect(self.Listele)
        self.ui.pb_cihazSil_4.clicked.connect(self.telefon_sil)
        self.ui.pb_anamenuCikis.clicked.connect(self.menukapat)
        
        
        self.ui.tableWidget.setItem(1, 1, QTableWidgetItem("NNABEERR"))
        
    def menukapat(self):
        self.hide()
    
    def parcaStok(self):
        
        self.parcastok.show()
        
    def cihazKayit(self):
        
        self.cihazkayit.show()
        
    def Listele(self):
        
        veriler = self.veritabani.Telefon()
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setRowCount(len(veriler))
        
        for i, item in enumerate(veriler):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(item[0])))  
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(item[1]))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(item[2]))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(item[3])))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(item[4])))
            self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(item[5]))


    def telefon_sil(self):
        selected_row = self.ui.tableWidget.currentRow()
        
        if selected_row >=0:
            try:
                id = int(self.ui.tableWidget.item(selected_row,0).text())
                self.veritabani.telefon_sil(id)
                print(f"Veritabanından silindi: ID{id}")
                
                self.ui.tableWidget.removeRow(selected_row)
                print(f"Table widget tan silindi : ID{id}")
            except Exception as e:
                print(f"Silme sırasında hata oluştu: {e}")
        else:
            QMessageBox.warning(self,"Hata","Lütfen silinecek bir satır seçiniz!!!")
