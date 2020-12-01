# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import search


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(555, 415)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 30);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_area = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_area.setGeometry(QtCore.QRect(60, 70, 113, 21))
        self.lineEdit_area.setText("")
        self.lineEdit_area.setObjectName("lineEdit_area")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 250, 481, 61))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 130, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_month = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_month.setGeometry(QtCore.QRect(330, 70, 113, 21))
        self.lineEdit_month.setObjectName("lineEdit_month")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 210, 60, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 340, 151, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Comfirm"))
        self.label.setText(_translate("MainWindow", "Area Input"))
        self.label_2.setText(_translate("MainWindow", "Month Input"))
        self.label_3.setText(_translate("MainWindow", "Result"))
        self.pushButton_2.setText(_translate("MainWindow", "I want to see gragh!"))

    def result(self):
        area = self.lineEdit_area.text()
        month = self.lineEdit_month.text()
        ans = search.find(area,month)
        self.lineEdit_2.setText(ans)
        
    def plot(self):
        area = self.lineEdit_area.text()
        search.plot(area)

    def click(self):
        self.pushButton.clicked.connect(self.result)

    def click_plot(self):
        self.pushButton_2.clicked.connect(self.plot)
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.click()
    ui.click_plot()
    MainWindow.show()
    sys.exit(app.exec_())
