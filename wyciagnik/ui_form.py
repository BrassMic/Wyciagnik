# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(856, 815)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 831, 761))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.kat_widget = QListWidget(self.verticalLayoutWidget)
        self.kat_widget.setObjectName(u"kat_widget")

        self.gridLayout.addWidget(self.kat_widget, 2, 1, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, -1, -1)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.min_line = QLineEdit(self.verticalLayoutWidget)
        self.min_line.setObjectName(u"min_line")

        self.horizontalLayout.addWidget(self.min_line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.max_line = QLineEdit(self.verticalLayoutWidget)
        self.max_line.setObjectName(u"max_line")

        self.horizontalLayout.addWidget(self.max_line)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.start_button = QPushButton(self.verticalLayoutWidget)
        self.start_button.setObjectName(u"start_button")

        self.gridLayout.addWidget(self.start_button, 4, 1, 1, 1)

        self.mkat_button = QPushButton(self.verticalLayoutWidget)
        self.mkat_button.setObjectName(u"mkat_button")

        self.gridLayout.addWidget(self.mkat_button, 0, 2, 1, 1)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.dkatline = QLineEdit(self.verticalLayoutWidget)
        self.dkatline.setObjectName(u"dkatline")

        self.gridLayout.addWidget(self.dkatline, 1, 1, 1, 1)

        self.mkatline = QLineEdit(self.verticalLayoutWidget)
        self.mkatline.setObjectName(u"mkatline")

        self.gridLayout.addWidget(self.mkatline, 0, 1, 1, 1)

        self.dkat_button = QPushButton(self.verticalLayoutWidget)
        self.dkat_button.setObjectName(u"dkat_button")

        self.gridLayout.addWidget(self.dkat_button, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Katalog g\u0142\u00f3wny", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Min files", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Max files", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.mkat_button.setText(QCoreApplication.translate("MainWindow", u"Wybierz", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Katalog docelowy", None))
        self.dkat_button.setText(QCoreApplication.translate("MainWindow", u"Wybierz", None))
    # retranslateUi

