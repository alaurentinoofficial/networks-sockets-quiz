# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\quiz.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    background: #000000;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("QLabel {\n"
"    color: #fff;\n"
"    font-size: 16px;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_g = QtWidgets.QPushButton(self.centralwidget)
        self.button_g.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_g.setStyleSheet("QPushButton {\n"
"    background-color: #555;\n"
"    border: 2px solid #666;\n"
"    border-radius: 20;\n"
"    color: #eee;\n"
"    height: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1c7fe8;\n"
"    border-color: #1c7fe8;\n"
"}"
"QPushButton:disabled {\n"
"    background-color: #111;\n"
"    border-color: #111;\n"
"}")
        self.button_g.setObjectName("button_g")
        self.gridLayout.addWidget(self.button_g, 3, 0, 1, 1)
        self.button_c = QtWidgets.QPushButton(self.centralwidget)
        self.button_c.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_c.setStyleSheet("QPushButton {\n"
"    background-color: #555;\n"
"    border: 2px solid #666;\n"
"    border-radius: 20;\n"
"    color: #eee;\n"
"    height: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1c7fe8;\n"
"    border-color: #1c7fe8;\n"
"}"
"QPushButton:disabled {\n"
"    background-color: #111;\n"
"    border-color: #111;\n"
"}")
        self.button_c.setObjectName("button_c")
        self.gridLayout.addWidget(self.button_c, 1, 0, 1, 1)
        self.button_f = QtWidgets.QPushButton(self.centralwidget)
        self.button_f.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_f.setStyleSheet("QPushButton {\n"
"    background-color: #555;\n"
"    border: 2px solid #666;\n"
"    border-radius: 20;\n"
"    color: #eee;\n"
"    height: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1c7fe8;\n"
"    border-color: #1c7fe8;\n"
"}"
"QPushButton:disabled {\n"
"    background-color: #111;\n"
"    border-color: #111;\n"
"}")
        self.button_f.setObjectName("button_f")
        self.gridLayout.addWidget(self.button_f, 2, 1, 1, 1)
        self.button_a = QtWidgets.QPushButton(self.centralwidget)
        self.button_a.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_a.setStyleSheet("QPushButton {\n"
"    background-color: #555;\n"
"    border: 2px solid #666;\n"
"    border-radius: 20;\n"
"    color: #eee;\n"
"    height: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1c7fe8;\n"
"    border-color: #1c7fe8;\n"
"}"
"QPushButton:disabled {\n"
"    background-color: #111;\n"
"    border-color: #111;\n"
"}")
        self.button_a.setObjectName("button_a")
        self.gridLayout.addWidget(self.button_a, 0, 0, 1, 1)
        self.button_d = QtWidgets.QPushButton(self.centralwidget)
        self.button_d.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_d.setStyleSheet("QPushButton {\n"
"    background-color: #555;\n"
"    border: 2px solid #666;\n"
"    border-radius: 20;\n"
"    color: #eee;\n"
"    height: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1c7fe8;\n"
"    border-color: #1c7fe8;\n"
"}"
"QPushButton:disabled {\n"
"    background-color: #111;\n"
"    border-color: #111;\n"
"}")
        self.button_d.setObjectName("button_d")
        self.gridLayout.addWidget(self.button_d, 1, 1, 1, 1)
        self.button_h = QtWidgets.QPushButton(self.centralwidget)
        self.button_h.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_h.setStyleSheet("QPushButton {\n"
"    background-color: #555;\n"
"    border: 2px solid #666;\n"
"    border-radius: 20;\n"
"    color: #eee;\n"
"    height: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1c7fe8;\n"
"    border-color: #1c7fe8;\n"
"}"
"QPushButton:disabled {\n"
"    background-color: #111;\n"
"    border-color: #111;\n"
"}")
        self.button_h.setObjectName("button_h")
        self.gridLayout.addWidget(self.button_h, 3, 1, 1, 1)
        self.button_e = QtWidgets.QPushButton(self.centralwidget)
        self.button_e.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_e.setStyleSheet("QPushButton {\n"
"    background-color: #555;\n"
"    border: 2px solid #666;\n"
"    border-radius: 20;\n"
"    color: #eee;\n"
"    height: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1c7fe8;\n"
"    border-color: #1c7fe8;\n"
"}"
"QPushButton:disabled {\n"
"    background-color: #111;\n"
"    border-color: #111;\n"
"}")
        self.button_e.setObjectName("button_e")
        self.gridLayout.addWidget(self.button_e, 2, 0, 1, 1)
        self.button_b = QtWidgets.QPushButton(self.centralwidget)
        self.button_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_b.setStyleSheet("QPushButton {\n"
"    background-color: #555;\n"
"    border: 2px solid #666;\n"
"    border-radius: 20;\n"
"    color: #eee;\n"
"    height: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1c7fe8;\n"
"    border-color: #1c7fe8;\n"
"}"
"QPushButton:disabled {\n"
"    background-color: #111;\n"
"    border-color: #111;\n"
"}")
        self.button_b.setCheckable(False)
        self.button_b.setObjectName("button_b")
        self.gridLayout.addWidget(self.button_b, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.button_g.setText(_translate("MainWindow", "PushButton"))
        self.button_c.setText(_translate("MainWindow", "PushButton"))
        self.button_f.setText(_translate("MainWindow", "PushButton"))
        self.button_a.setText(_translate("MainWindow", "PushButton"))
        self.button_d.setText(_translate("MainWindow", "PushButton"))
        self.button_h.setText(_translate("MainWindow", "PushButton"))
        self.button_e.setText(_translate("MainWindow", "PushButton"))
        self.button_b.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
