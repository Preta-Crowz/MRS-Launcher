# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import os
import launchcore
def mkdir(dir):
    if not(os.path.exists(dir)):
        os.makedirs(dir)
        return 1
    else:
        return 0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 575)
        MainWindow.setMinimumSize(QtCore.QSize(972, 575))
        MainWindow.setMaximumSize(QtCore.QSize(972, 575))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalFrame_3 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame_3.setGeometry(QtCore.QRect(0, 0, 971, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_3.setSizePolicy(sizePolicy)
        self.horizontalFrame_3.setObjectName("horizontalFrame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.horizontalFrame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget1 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.widget1)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.Button_check = QtWidgets.QPushButton(self.widget1)
        self.Button_check.setObjectName("Button_check")
        self.verticalLayout_2.addWidget(self.Button_check)
        self.horizontalLayout_2.addWidget(self.widget1)
        self.horizontalLayout_3.addWidget(self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget2 = QWebEngineView()
        self.widget2.setUrl(QUrl("https://gametowndev.tk/news.html"))
        self.widget2.setObjectName("widget2")
        self.verticalLayout.addWidget(self.widget2)
        self.widget3 = QtWidgets.QWidget(self.horizontalFrame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget3.sizePolicy().hasHeightForWidth())
        self.widget3.setSizePolicy(sizePolicy)
        self.widget3.setObjectName("widget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Button_option = QtWidgets.QPushButton(self.widget3)
        self.Button_option.setObjectName("Button_option")
        self.horizontalLayout.addWidget(self.Button_option)
        self.Button_launch = QtWidgets.QPushButton(self.widget3)
        self.Button_launch.setObjectName("Button_launch")
        self.horizontalLayout.addWidget(self.Button_launch)
        self.verticalLayout.addWidget(self.widget3)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        '''self.Button_check.clicked.connect()'''
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MRS Launcher"))
        self.label.setText(_translate("MainWindow", "모드팩 목록"))
        self.Button_check.setText(_translate("MainWindow", "새로고침"))
        self.Button_option.setText(_translate("MainWindow", "설정"))
        self.Button_launch.setText(_translate("MainWindow", "실행"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

