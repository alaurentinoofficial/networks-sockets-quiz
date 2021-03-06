# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/nickname_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

class NicknameDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 165)
        Dialog.setStyleSheet("QDialog {\n"
"    background: #000;\n"
"}")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 110, 101, 41))
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setStyleSheet("QPushButton {\n"
"    background-color: #1c7fe8;\n"
"    border: 2px solid #1c7fe8;\n"
"    border-radius: 20;\n"
"    color: #eee;\n"
"    height: 40px;\n"
"    width: 100px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(22, 108, 194);\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 19))
        self.label.setStyleSheet("QLabel {\n"
"    color: #fff;\n"
"    font-size: 16px;\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 501, 61))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background: #444;\n"
"    border: 2px solid #666;\n"
"    border-radius: 20;\n"
"    height: 30px;\n"
"    margin: 10px;\n"
"    padding-left: 15px;\n"
"    font-size: 14px;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #1c7fe8;\n"
"}"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1c7fe8;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nickname:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
