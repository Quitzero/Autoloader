# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFontComboBox,
    QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 286)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.interface_tab = QWidget()
        self.interface_tab.setObjectName(u"interface_tab")
        self.verticalLayout_3 = QVBoxLayout(self.interface_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.theme_group = QGroupBox(self.interface_tab)
        self.theme_group.setObjectName(u"theme_group")
        self.verticalLayout = QVBoxLayout(self.theme_group)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.theme_layout = QHBoxLayout()
        self.theme_layout.setObjectName(u"theme_layout")
        self.light_theme_radio = QRadioButton(self.theme_group)
        self.light_theme_radio.setObjectName(u"light_theme_radio")
        self.light_theme_radio.setChecked(True)

        self.theme_layout.addWidget(self.light_theme_radio)

        self.dark_theme_radio = QRadioButton(self.theme_group)
        self.dark_theme_radio.setObjectName(u"dark_theme_radio")

        self.theme_layout.addWidget(self.dark_theme_radio)

        self.theme_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.theme_layout.addItem(self.theme_spacer)


        self.verticalLayout.addLayout(self.theme_layout)


        self.verticalLayout_3.addWidget(self.theme_group)

        self.text_group = QGroupBox(self.interface_tab)
        self.text_group.setObjectName(u"text_group")
        self.formLayout = QFormLayout(self.text_group)
        self.formLayout.setObjectName(u"formLayout")
        self.font = QLabel(self.text_group)
        self.font.setObjectName(u"font")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.font)

        self.typeface = QLabel(self.text_group)
        self.typeface.setObjectName(u"typeface")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.typeface)

        self.typefaceComboBox = QComboBox(self.text_group)
        self.typefaceComboBox.addItem("")
        self.typefaceComboBox.addItem("")
        self.typefaceComboBox.addItem("")
        self.typefaceComboBox.addItem("")
        self.typefaceComboBox.setObjectName(u"typefaceComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.typefaceComboBox)

        self.size = QLabel(self.text_group)
        self.size.setObjectName(u"size")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.size)

        self.sizeComboBox = QComboBox(self.text_group)
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.addItem("")
        self.sizeComboBox.setObjectName(u"sizeComboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sizeComboBox)

        self.fontComboBox = QFontComboBox(self.text_group)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fontComboBox)


        self.verticalLayout_3.addWidget(self.text_group)

        self.tabWidget.addTab(self.interface_tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.settings_confirmation_buttons_layout = QHBoxLayout()
        self.settings_confirmation_buttons_layout.setObjectName(u"settings_confirmation_buttons_layout")
        self.settings_buttons_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.settings_confirmation_buttons_layout.addItem(self.settings_buttons_spacer)

        self.accept_button = QPushButton(Dialog)
        self.accept_button.setObjectName(u"accept_button")

        self.settings_confirmation_buttons_layout.addWidget(self.accept_button)

        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.settings_confirmation_buttons_layout.addWidget(self.cancel_button)

        self.apply_button = QPushButton(Dialog)
        self.apply_button.setObjectName(u"apply_button")

        self.settings_confirmation_buttons_layout.addWidget(self.apply_button)


        self.verticalLayout_2.addLayout(self.settings_confirmation_buttons_layout)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.theme_group.setTitle(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043c\u0430", None))
        self.light_theme_radio.setText(QCoreApplication.translate("Dialog", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.dark_theme_radio.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043c\u043d\u0430\u044f", None))
        self.text_group.setTitle(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.font.setText(QCoreApplication.translate("Dialog", u"\u0428\u0440\u0438\u0444\u0442", None))
        self.typeface.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0435\u0440\u0442\u0430\u043d\u0438\u0435", None))
        self.typefaceComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u043d\u0434\u0440\u0430\u0442", None))
        self.typefaceComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u0416\u0438\u0440\u043d\u044b\u0439", None))
        self.typefaceComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u041a\u0443\u0440\u0441\u0438\u0432", None))
        self.typefaceComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u0416\u0438\u0440\u043d\u044b\u0439 \u043a\u0443\u0440\u0441\u0438\u0432", None))

        self.size.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u043c\u0435\u0440", None))
        self.sizeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"6", None))
        self.sizeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"8", None))
        self.sizeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"10", None))
        self.sizeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"12", None))
        self.sizeComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"14", None))
        self.sizeComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"16", None))
        self.sizeComboBox.setItemText(6, QCoreApplication.translate("Dialog", u"18", None))
        self.sizeComboBox.setItemText(7, QCoreApplication.translate("Dialog", u"20", None))
        self.sizeComboBox.setItemText(8, QCoreApplication.translate("Dialog", u"22", None))
        self.sizeComboBox.setItemText(9, QCoreApplication.translate("Dialog", u"24", None))
        self.sizeComboBox.setItemText(10, QCoreApplication.translate("Dialog", u"26", None))
        self.sizeComboBox.setItemText(11, QCoreApplication.translate("Dialog", u"28", None))
        self.sizeComboBox.setItemText(12, QCoreApplication.translate("Dialog", u"30", None))
        self.sizeComboBox.setItemText(13, QCoreApplication.translate("Dialog", u"32", None))
        self.sizeComboBox.setItemText(14, QCoreApplication.translate("Dialog", u"34", None))
        self.sizeComboBox.setItemText(15, QCoreApplication.translate("Dialog", u"36", None))
        self.sizeComboBox.setItemText(16, QCoreApplication.translate("Dialog", u"38", None))
        self.sizeComboBox.setItemText(17, QCoreApplication.translate("Dialog", u"40", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.interface_tab), QCoreApplication.translate("Dialog", u"\u0418\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"\u0425\u0440\u0430\u043d\u0438\u043b\u0438\u0449\u0435", None))
        self.accept_button.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.apply_button.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

