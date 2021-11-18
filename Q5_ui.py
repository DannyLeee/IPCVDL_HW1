# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 205)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 119, 185))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Q5_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Q5_1.setStyleSheet("text-align:left;")
        self.Q5_1.setObjectName("Q5_1")
        self.verticalLayout.addWidget(self.Q5_1)
        self.Q5_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Q5_2.setStyleSheet("text-align:left;")
        self.Q5_2.setObjectName("Q5_2")
        self.verticalLayout.addWidget(self.Q5_2)
        self.Q5_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Q5_3.setStyleSheet("text-align:left;")
        self.Q5_3.setObjectName("Q5_3")
        self.verticalLayout.addWidget(self.Q5_3)
        self.Q5_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Q5_4.setStyleSheet("text-align:left;")
        self.Q5_4.setObjectName("Q5_4")
        self.verticalLayout.addWidget(self.Q5_4)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.img_index = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.img_index.setMinimum(1)
        self.img_index.setMaximum(10000)
        self.img_index.setObjectName("img_index")
        self.verticalLayout.addWidget(self.img_index)
        self.Q5_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Q5_5.setStyleSheet("text-align:left;")
        self.Q5_5.setObjectName("Q5_5")
        self.verticalLayout.addWidget(self.Q5_5)
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(130, 10, 491, 181))
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CVDL HW1 Q5"))
        self.Q5_1.setText(_translate("MainWindow", "5.1 Show Dataset"))
        self.Q5_2.setText(_translate("MainWindow", "5.2 HyperParameter"))
        self.Q5_3.setText(_translate("MainWindow", "5.3 Show Model"))
        self.Q5_4.setText(_translate("MainWindow", "5.4 Performance Curve"))
        self.label.setText(_translate("MainWindow", "Image Index:"))
        self.Q5_5.setText(_translate("MainWindow", "5.5 Test"))
        self.result.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
