# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_size_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore,  QtWidgets


class Redact(object):
    def setupUi(self, Izmn_film):
        Izmn_film.setObjectName("Izmn_film")
        Izmn_film.resize(619, 333)
        self.verticalLayout = QtWidgets.QVBoxLayout(Izmn_film)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Izmn_film)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.nazvanie_edit = QtWidgets.QLineEdit(Izmn_film)
        self.nazvanie_edit.setObjectName("nazvanie_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nazvanie_edit)
        self.label_3 = QtWidgets.QLabel(Izmn_film)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.stepen_obj_edit = QtWidgets.QLineEdit(Izmn_film)
        self.stepen_obj_edit.setObjectName("stepen_obj_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.stepen_obj_edit)
        self.label = QtWidgets.QLabel(Izmn_film)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.opisanie_edit = QtWidgets.QLineEdit(Izmn_film)
        self.opisanie_edit.setObjectName("opisanie_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.opisanie_edit)
        self.label_4 = QtWidgets.QLabel(Izmn_film)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_6 = QtWidgets.QLabel(Izmn_film)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.price_edit = QtWidgets.QLineEdit(Izmn_film)
        self.price_edit.setObjectName("price_edit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.price_edit)
        self.molot_edit = QtWidgets.QLineEdit(Izmn_film)
        self.molot_edit.setObjectName("molot_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.molot_edit)
        self.label_7 = QtWidgets.QLabel(Izmn_film)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.obiom_edit = QtWidgets.QLineEdit(Izmn_film)
        self.obiom_edit.setObjectName("obiom_edit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.obiom_edit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(Izmn_film)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Izmn_film)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Izmn_film)
        QtCore.QMetaObject.connectSlotsByName(Izmn_film)

    def retranslateUi(self, Izmn_film):
        _translate = QtCore.QCoreApplication.translate
        Izmn_film.setWindowTitle(_translate("Izmn_film", "Dialog"))
        self.label_2.setText(_translate("Izmn_film", "Название"))
        self.label_3.setText(_translate("Izmn_film", " степень обжарки"))
        self.label.setText(_translate("Izmn_film", "молотый/в зернах"))
        self.label_4.setText(_translate("Izmn_film", "описание вкуса"))
        self.label_6.setText(_translate("Izmn_film", "цена"))
        self.label_7.setText(_translate("Izmn_film", " объем упаковки"))
        self.pushButton.setText(_translate("Izmn_film", "редактировать"))