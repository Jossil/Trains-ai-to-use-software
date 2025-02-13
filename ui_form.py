# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(337, 196)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 2)

        self.textEdit_2 = QTextEdit(Widget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout.addWidget(self.textEdit_2, 3, 0, 1, 2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u8bb0\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u6267\u884c", None))
    # retranslateUi

