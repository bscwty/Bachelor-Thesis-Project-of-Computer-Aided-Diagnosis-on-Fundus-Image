# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bscwt\Desktop\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 751, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddressEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.AddressEdit.setObjectName("AddressEdit")
        self.horizontalLayout.addWidget(self.AddressEdit)
        self.SelectAddress = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SelectAddress.setObjectName("SelectAddress")
        self.horizontalLayout.addWidget(self.SelectAddress)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 120, 111, 31))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(360, 130, 20, 441))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(390, 130, 401, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.CAMView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.CAMView.setObjectName("CAMView")
        self.gridLayout.addWidget(self.CAMView, 1, 0, 1, 1)
        self.GuidedGradCAMView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.GuidedGradCAMView.setObjectName("GuidedGradCAMView")
        self.gridLayout.addWidget(self.GuidedGradCAMView, 4, 1, 1, 1)
        self.GradCAMPlusView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.GradCAMPlusView.setObjectName("GradCAMPlusView")
        self.gridLayout.addWidget(self.GradCAMPlusView, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.GradCAMView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.GradCAMView.setObjectName("GradCAMView")
        self.gridLayout.addWidget(self.GradCAMView, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 350, 111, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 350, 51, 31))
        self.label_7.setObjectName("label_7")
        self.OrgVIEW = QtWidgets.QGraphicsView(self.centralwidget)
        self.OrgVIEW.setGeometry(QtCore.QRect(40, 150, 196, 196))
        self.OrgVIEW.setObjectName("OrgVIEW")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(40, 380, 311, 192))
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SelectAddress.setText(_translate("MainWindow", "输入地址"))
        self.label.setText(_translate("MainWindow", "原始图片"))
        self.label_3.setText(_translate("MainWindow", "GradCAM++"))
        self.label_4.setText(_translate("MainWindow", "GradCAM"))
        self.label_5.setText(_translate("MainWindow", "Guided GradCAM"))
        self.label_2.setText(_translate("MainWindow", "CAM"))
        self.label_6.setText(_translate("MainWindow", "预测结果"))
        self.label_7.setText(_translate("MainWindow", "置信度"))
