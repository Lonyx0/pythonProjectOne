# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cihazKayit_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_marka = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_marka.setObjectName("comboBox_marka")
        self.comboBox_marka.addItem("")
        self.comboBox_marka.addItem("")
        self.comboBox_marka.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_marka)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.le_cihazModel = QtWidgets.QLineEdit(self.centralwidget)
        self.le_cihazModel.setObjectName("le_cihazModel")
        self.horizontalLayout_2.addWidget(self.le_cihazModel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.comboBox_marka_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_marka_2.setObjectName("comboBox_marka_2")
        self.comboBox_marka_2.addItem("")
        self.comboBox_marka_2.addItem("")
        self.comboBox_marka_2.addItem("")
        self.comboBox_marka_2.addItem("")
        self.comboBox_marka_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_marka_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.checkBox_garanti = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_garanti.setObjectName("checkBox_garanti")
        self.horizontalLayout_4.addWidget(self.checkBox_garanti)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.textEdit_cihazSikayet = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_cihazSikayet.setObjectName("textEdit_cihazSikayet")
        self.verticalLayout.addWidget(self.textEdit_cihazSikayet)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pb_kayitekranKaydet = QtWidgets.QPushButton(self.centralwidget)
        self.pb_kayitekranKaydet.setObjectName("pb_kayitekranKaydet")
        self.horizontalLayout_5.addWidget(self.pb_kayitekranKaydet)
        self.pb_kayitekranAnamenu = QtWidgets.QPushButton(self.centralwidget)
        self.pb_kayitekranAnamenu.setObjectName("pb_kayitekranAnamenu")
        self.horizontalLayout_5.addWidget(self.pb_kayitekranAnamenu)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cihaz Kayıt Ekranı"))
        self.label.setText(_translate("MainWindow", "Cihaz marka:"))
        self.comboBox_marka.setItemText(0, _translate("MainWindow", "Samsung"))
        self.comboBox_marka.setItemText(1, _translate("MainWindow", "Apple"))
        self.comboBox_marka.setItemText(2, _translate("MainWindow", "Xiaomi"))
        self.label_2.setText(_translate("MainWindow", "Cihaz model:"))
        self.label_5.setText(_translate("MainWindow", "Cihaz Hafıza:"))
        self.comboBox_marka_2.setItemText(0, _translate("MainWindow", "32"))
        self.comboBox_marka_2.setItemText(1, _translate("MainWindow", "64"))
        self.comboBox_marka_2.setItemText(2, _translate("MainWindow", "128"))
        self.comboBox_marka_2.setItemText(3, _translate("MainWindow", "256"))
        self.comboBox_marka_2.setItemText(4, _translate("MainWindow", "512"))
        self.label_3.setText(_translate("MainWindow", "Cihaz Garanti Durumu:"))
        self.checkBox_garanti.setText(_translate("MainWindow", "Var"))
        self.label_4.setText(_translate("MainWindow", "Cihaz Şikayeti:"))
        self.pb_kayitekranKaydet.setText(_translate("MainWindow", "Kaydet"))
        self.pb_kayitekranAnamenu.setText(_translate("MainWindow", "Ana Menü"))
