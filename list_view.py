# Form implementation generated from reading ui file 'list_view.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QWidget

from partner_types import Partner


class PartnerItemWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def setupUi(self, partner: Partner):

        self.type_fild = QtWidgets.QLabel(parent=self)
        self.type_fild.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.type_fild.setObjectName("type_fild")
        self.partner_name = QtWidgets.QLabel(parent=self)
        self.partner_name.setGeometry(QtCore.QRect(40, 10, 251, 16))
        self.partner_name.setObjectName("partner_name")
        self.director = QtWidgets.QLabel(parent=self)
        self.director.setGeometry(QtCore.QRect(10, 30, 231, 16))
        self.director.setObjectName("director")
        self.phone = QtWidgets.QLabel(parent=self)
        self.phone.setGeometry(QtCore.QRect(10, 50, 231, 16))
        self.phone.setObjectName("phone")
        self.rating_label = QtWidgets.QLabel(parent=self)
        self.rating_label.setGeometry(QtCore.QRect(10, 70, 49, 16))
        self.rating_label.setObjectName("rating_label")
        self.rating_field = QtWidgets.QLabel(parent=self)
        self.rating_field.setGeometry(QtCore.QRect(60, 70, 49, 16))
        self.rating_field.setObjectName("rating_field")
        self.line = QtWidgets.QFrame(parent=self)
        self.line.setGeometry(QtCore.QRect(30, 0, 16, 31))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.discount_field = QtWidgets.QLabel(parent=self)
        self.discount_field.setGeometry(QtCore.QRect(320, 10, 49, 16))
        self.discount_field.setObjectName("discount_field")

        self.retranslateUi(partner)

    def retranslateUi(self, partner: Partner):
        _translate = QtCore.QCoreApplication.translate

        self.type_fild.setText(partner.partner_type)
        self.partner_name.setText(partner.partner_name)
        self.director.setText(partner.partner_director)
        self.phone.setText(partner.partner_phone)
        self.rating_label.setText("Рейтинг:")
        self.rating_field.setText(f'{partner.partner_rating}')
        self.discount_field.setText(f"{partner.partner_discount}%")
