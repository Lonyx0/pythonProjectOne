# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pb_cihazKayitEkrani_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cihazKayitEkrani_4.setObjectName("pb_cihazKayitEkrani_4")
        self.horizontalLayout_4.addWidget(self.pb_cihazKayitEkrani_4)
        self.pb_anamenuGuncelle_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_anamenuGuncelle_4.setObjectName("pb_anamenuGuncelle_4")
        self.horizontalLayout_4.addWidget(self.pb_anamenuGuncelle_4)
        self.pb_cihazSil_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cihazSil_4.setObjectName("pb_cihazSil_4")
        self.horizontalLayout_4.addWidget(self.pb_cihazSil_4)
        self.pb_parcaStok_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_parcaStok_4.setObjectName("pb_parcaStok_4")
        self.horizontalLayout_4.addWidget(self.pb_parcaStok_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pb_anamenuCikis = QtWidgets.QPushButton(self.centralwidget)
        self.pb_anamenuCikis.setObjectName("pb_anamenuCikis")
        self.verticalLayout.addWidget(self.pb_anamenuCikis)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ana Menü"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Marka"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Model"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Hafıza"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Garanti Durumu"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Şikayet"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Onarım Durumu"))
        self.pb_cihazKayitEkrani_4.setText(_translate("MainWindow", "Cihaz Kayıt Ekranı"))
        self.pb_anamenuGuncelle_4.setText(_translate("MainWindow", "Güncelle"))
        self.pb_cihazSil_4.setText(_translate("MainWindow", "Cihaz sil"))
        self.pb_parcaStok_4.setText(_translate("MainWindow", "Parça Stoğu"))
        self.pb_anamenuCikis.setText(_translate("MainWindow", "Çıkış"))