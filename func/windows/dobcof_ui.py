# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_size_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore,  QtWidgets


class Ui_dob_cof_dialog(object):
    def setupUi(self, dob_film_dialog):
        dob_film_dialog.setObjectName("dob_film_dialog")
        dob_film_dialog.resize(619, 333)
        self.verticalLayout = QtWidgets.QVBoxLayout(dob_film_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(dob_film_dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.nazvanie_edit = QtWidgets.QLineEdit(dob_film_dialog)
        self.nazvanie_edit.setObjectName("nazvanie_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nazvanie_edit)
        self.label_3 = QtWidgets.QLabel(dob_film_dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.stepen_obj_edit = QtWidgets.QLineEdit(dob_film_dialog)
        self.stepen_obj_edit.setObjectName("stepen_obj_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.stepen_obj_edit)
        self.label = QtWidgets.QLabel(dob_film_dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.opisanie_edit = QtWidgets.QLineEdit(dob_film_dialog)
        self.opisanie_edit.setObjectName("opisanie_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.opisanie_edit)
        self.label_4 = QtWidgets.QLabel(dob_film_dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_6 = QtWidgets.QLabel(dob_film_dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.price_edit = QtWidgets.QLineEdit(dob_film_dialog)
        self.price_edit.setObjectName("price_edit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.price_edit)
        self.molot_edit = QtWidgets.QLineEdit(dob_film_dialog)
        self.molot_edit.setObjectName("molot_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.molot_edit)
        self.label_7 = QtWidgets.QLabel(dob_film_dialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.obiom_edit = QtWidgets.QLineEdit(dob_film_dialog)
        self.obiom_edit.setObjectName("obiom_edit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.obiom_edit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(dob_film_dialog)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(dob_film_dialog)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dob_film_dialog)
        QtCore.QMetaObject.connectSlotsByName(dob_film_dialog)

    def retranslateUi(self, dob_film_dialog):
        _translate = QtCore.QCoreApplication.translate
        dob_film_dialog.setWindowTitle(_translate("dob_film_dialog", "Dialog"))
        self.label_2.setText(_translate("dob_film_dialog", "????????????????"))
        self.label_3.setText(_translate("dob_film_dialog", " ?????????????? ??????????????"))
        self.label.setText(_translate("dob_film_dialog", "??????????????/?? ????????????"))
        self.label_4.setText(_translate("dob_film_dialog", "???????????????? ??????????"))
        self.label_6.setText(_translate("dob_film_dialog", "????????"))
        self.label_7.setText(_translate("dob_film_dialog", " ?????????? ????????????????"))
        self.pushButton.setText(_translate("dob_film_dialog", "????????????????"))
