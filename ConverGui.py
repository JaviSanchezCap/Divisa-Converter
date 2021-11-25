from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ComboDinero1 = QtWidgets.QComboBox(self.centralwidget)
        self.ComboDinero1.setGeometry(QtCore.QRect(170, 170, 181, 51))
        self.ComboDinero1.setMouseTracking(False)
        self.ComboDinero1.setObjectName("ComboDinero1")
        self.ComboDinero1.addItem("")
        self.ComboDinero1.addItem("")
        self.ComboDinero1.addItem("")
        self.ComboDinero1.addItem("Dolar Canadiense")
        self.ComboDinero1.addItem("Rupia")
        self.ComboDinero2 = QtWidgets.QComboBox(self.centralwidget)
        self.ComboDinero2.setGeometry(QtCore.QRect(420, 170, 181, 51))
        self.ComboDinero2.setMouseTracking(True)
        self.ComboDinero2.setAutoFillBackground(False)
        self.ComboDinero2.setObjectName("ComboDinero2")
        self.ComboDinero2.addItem("")
        self.ComboDinero2.addItem("")
        self.ComboDinero2.addItem("")
        self.ComboDinero2.addItem("Dolar Canadiense")
        self.ComboDinero2.addItem("Rupia")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/money2.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 431, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imgs/divisa2.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 180, 16, 31))
        self.label_4.setObjectName("label_4")
        self.Cantidad = QtWidgets.QTextEdit(self.centralwidget)
        self.Cantidad.setGeometry(QtCore.QRect(360, 240, 121, 41))
        self.Cantidad.setObjectName("Cantidad")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 240, 141, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 330, 161, 41))
        self.label_5.setObjectName("label_5")
        self.Resultado = QtWidgets.QTextEdit(self.centralwidget)
        self.Resultado.setGeometry(QtCore.QRect(400, 330, 121, 41))
        self.Resultado.setObjectName("Resultado")
        self.DoBut = QtWidgets.QPushButton(self.centralwidget)
        self.DoBut.setGeometry(QtCore.QRect(500, 240, 51, 41))
        self.DoBut.setFlat(False)
        self.DoBut.setObjectName("DoBut")
        self.label.raise_()
        self.ComboDinero1.raise_()
        self.ComboDinero2.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.Cantidad.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.Resultado.raise_()
        self.DoBut.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.ComboDinero1.setItemText(0, _translate("MainWindow", "Dolar"))
        self.ComboDinero1.setItemText(1, _translate("MainWindow", "Euro"))
        self.ComboDinero1.setItemText(2, _translate("MainWindow", "Libra"))
        self.ComboDinero2.setItemText(0, _translate("MainWindow", "Dolar"))
        self.ComboDinero2.setItemText(1, _translate("MainWindow", "Euro"))
        self.ComboDinero2.setItemText(2, _translate("MainWindow", "Libra"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">A</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Cantidad:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#005500;\">Resultado:</span></p></body></html>"))
        self.DoBut.setText(_translate("MainWindow", "Do it!"))



