# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 569)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.widget.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.selectButton = QPushButton(self.widget)
        self.selectButton.setObjectName(u"selectButton")

        self.verticalLayout.addWidget(self.selectButton, 0, Qt.AlignmentFlag.AlignTop)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.loadButton = QPushButton(self.widget)
        self.loadButton.setObjectName(u"loadButton")

        self.verticalLayout.addWidget(self.loadButton)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(14)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setMaxCount(100)
        self.comboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox.setMinimumContentsLength(6)

        self.verticalLayout.addWidget(self.comboBox)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaxVisibleItems(10)
        self.comboBox_2.setMaxCount(100)
        self.comboBox_2.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox_2.setMinimumContentsLength(6)

        self.verticalLayout.addWidget(self.comboBox_2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.lowerRange = QSpinBox(self.widget)
        self.lowerRange.setObjectName(u"lowerRange")
        self.lowerRange.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.lowerRange)

        self.upperRange = QSpinBox(self.widget)
        self.upperRange.setObjectName(u"upperRange")
        self.upperRange.setMinimum(0)
        self.upperRange.setMaximum(999)
        self.upperRange.setValue(999)

        self.horizontalLayout_2.addWidget(self.upperRange)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.percentButton = QPushButton(self.widget)
        self.percentButton.setObjectName(u"percentButton")

        self.verticalLayout.addWidget(self.percentButton)

        self.directionButton = QPushButton(self.widget)
        self.directionButton.setObjectName(u"directionButton")

        self.verticalLayout.addWidget(self.directionButton)

        self.toggleAngles = QPushButton(self.widget)
        self.toggleAngles.setObjectName(u"toggleAngles")

        self.verticalLayout.addWidget(self.toggleAngles)

        self.rawButton = QPushButton(self.widget)
        self.rawButton.setObjectName(u"rawButton")

        self.verticalLayout.addWidget(self.rawButton)

        self.saveHeatmap = QPushButton(self.widget)
        self.saveHeatmap.setObjectName(u"saveHeatmap")

        self.verticalLayout.addWidget(self.saveHeatmap)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.messageBox = QLabel(self.widget)
        self.messageBox.setObjectName(u"messageBox")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(202, 227, 197, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(228, 241, 226, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(101, 113, 98, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(135, 151, 131, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(101, 113, 98, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush2)
        self.messageBox.setPalette(palette)
        self.messageBox.setFont(font)

        self.verticalLayout.addWidget(self.messageBox)


        self.horizontalLayout.addWidget(self.widget)

        self.graphWidget = GraphicsLayoutWidget(self.centralwidget)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setMinimumSize(QSize(500, 400))

        self.horizontalLayout.addWidget(self.graphWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 824, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SLP DI Analyzer", None))
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"Select Slippi File Directory", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load Slippi Files", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Your Connect Code:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Opponent's Character:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Bowser", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Captain Falcon", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Donkey Kong", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Dr. Mario", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Falco", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Fox", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Ganondorf", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Ice Climbers", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Jigglypuff", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Kirby", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Link", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Luigi", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"Mario", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"Marth", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"Mewtwo", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"Mr. Game & Watch", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"Ness", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"Peach", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"Pichu", None))
        self.comboBox.setItemText(19, QCoreApplication.translate("MainWindow", u"Pikachu", None))
        self.comboBox.setItemText(20, QCoreApplication.translate("MainWindow", u"Roy", None))
        self.comboBox.setItemText(21, QCoreApplication.translate("MainWindow", u"Samus", None))
        self.comboBox.setItemText(22, QCoreApplication.translate("MainWindow", u"Sheik", None))
        self.comboBox.setItemText(23, QCoreApplication.translate("MainWindow", u"Yoshi", None))
        self.comboBox.setItemText(24, QCoreApplication.translate("MainWindow", u"Young Link", None))
        self.comboBox.setItemText(25, QCoreApplication.translate("MainWindow", u"Zelda", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Opponent's Move:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Jab 1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Jab 2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Jab 3", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Rapid Jabs", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Dash Attack", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Forward Tilt", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Up Tilt", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Down Tilt", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Forward Smash", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Up Smash", None))
        self.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Down Smash", None))
        self.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Neutral Air", None))
        self.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"Forward Air", None))
        self.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"Back Air", None))
        self.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"Up Air", None))
        self.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"Down Air", None))
        self.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"Neutral Special", None))
        self.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"Side Special", None))
        self.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"Up Special", None))
        self.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"Down Special", None))
        self.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"Forward Throw", None))
        self.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"Back Throw", None))
        self.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"Up Throw", None))
        self.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"Down Throw", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Percentage Range:", None))
        self.percentButton.setText(QCoreApplication.translate("MainWindow", u"Update Percentage Range", None))
        self.directionButton.setText(QCoreApplication.translate("MainWindow", u"Change Knockback Direction", None))
        self.toggleAngles.setText(QCoreApplication.translate("MainWindow", u"Toggle Knockback Angle Display", None))
        self.rawButton.setText(QCoreApplication.translate("MainWindow", u"Display Magnitudes", None))
        self.saveHeatmap.setText(QCoreApplication.translate("MainWindow", u"Save Heatmap", None))
        self.messageBox.setText("")
    # retranslateUi

