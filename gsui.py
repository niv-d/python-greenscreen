# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'greenscreen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 358)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonReset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReset.setGeometry(QtCore.QRect(10, 10, 150, 46))
        self.pushButtonReset.setObjectName("pushButtonReset")
        self.checkBoxGreenScreen = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxGreenScreen.setGeometry(QtCore.QRect(170, 20, 211, 29))
        self.checkBoxGreenScreen.setObjectName("checkBoxGreenScreen")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 200, 501, 131))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 231, 25))
        self.label.setObjectName("label")
        self.comboBoxNoise = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxNoise.setGeometry(QtCore.QRect(10, 60, 221, 41))
        self.comboBoxNoise.setObjectName("comboBoxNoise")
        self.comboBoxNoise.addItem("")
        self.comboBoxNoise.addItem("")
        self.comboBoxNoise.addItem("")
        self.horizontalSliderNoiseSize = QtWidgets.QSlider(self.groupBox)
        self.horizontalSliderNoiseSize.setGeometry(QtCore.QRect(260, 60, 181, 41))
        self.horizontalSliderNoiseSize.setMaximum(100)
        self.horizontalSliderNoiseSize.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderNoiseSize.setTickInterval(10)
        self.horizontalSliderNoiseSize.setObjectName("horizontalSliderNoiseSize")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(260, 30, 251, 25))
        self.label_2.setObjectName("label_2")
        self.labelSize = QtWidgets.QLabel(self.groupBox)
        self.labelSize.setGeometry(QtCore.QRect(450, 70, 41, 25))
        self.labelSize.setObjectName("labelSize")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 231, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(150, 30, 21, 25))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(80, 30, 21, 25))
        self.label_4.setObjectName("label_4")
        self.spinBoxRed = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxRed.setGeometry(QtCore.QRect(10, 60, 61, 41))
        self.spinBoxRed.setMaximum(255)
        self.spinBoxRed.setProperty("value", 255)
        self.spinBoxRed.setObjectName("spinBoxRed")
        self.spinBoxBlue = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxBlue.setGeometry(QtCore.QRect(150, 60, 61, 41))
        self.spinBoxBlue.setMaximum(255)
        self.spinBoxBlue.setProperty("value", 255)
        self.spinBoxBlue.setObjectName("spinBoxBlue")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 21, 25))
        self.label_3.setObjectName("label_3")
        self.spinBoxGreen = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxGreen.setGeometry(QtCore.QRect(80, 60, 61, 41))
        self.spinBoxGreen.setMaximum(255)
        self.spinBoxGreen.setProperty("value", 255)
        self.spinBoxGreen.setObjectName("spinBoxGreen")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 70, 261, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalSliderThresh = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSliderThresh.setGeometry(QtCore.QRect(20, 50, 181, 41))
        self.horizontalSliderThresh.setMaximum(100)
        self.horizontalSliderThresh.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderThresh.setObjectName("horizontalSliderThresh")
        self.labelThresh = QtWidgets.QLabel(self.groupBox_3)
        self.labelThresh.setGeometry(QtCore.QRect(210, 60, 41, 25))
        self.labelThresh.setObjectName("labelThresh")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 360, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.checkBoxGreenScreen.raise_()
        self.pushButtonReset.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.horizontalSliderThresh.valueChanged['int'].connect(self.labelThresh.setNum)
        self.horizontalSliderNoiseSize.valueChanged['int'].connect(self.labelSize.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Greenscreen"))
        self.pushButtonReset.setText(_translate("MainWindow", "Reset"))
        self.checkBoxGreenScreen.setText(_translate("MainWindow", "Hide Greenscreen"))
        self.groupBox.setTitle(_translate("MainWindow", "Noise Removal"))
        self.label.setText(_translate("MainWindow", "Type"))
        self.comboBoxNoise.setItemText(0, _translate("MainWindow", "Circle"))
        self.comboBoxNoise.setItemText(1, _translate("MainWindow", "Cross"))
        self.comboBoxNoise.setItemText(2, _translate("MainWindow", "Rectangle"))
        self.label_2.setText(_translate("MainWindow", "Size (0-100)"))
        self.labelSize.setText(_translate("MainWindow", "0"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Color of Greenscreen"))
        self.label_5.setText(_translate("MainWindow", "B:"))
        self.label_4.setText(_translate("MainWindow", "G:"))
        self.label_3.setText(_translate("MainWindow", "R:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Threshold"))
        self.labelThresh.setText(_translate("MainWindow", "0"))

