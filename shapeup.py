# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shapeup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Shapeup(object):
    def setupUi(self, Shapeup):
        Shapeup.setObjectName(_fromUtf8("Shapeup"))
        Shapeup.resize(721, 622)
        self.shapeup_centralwidget = QtGui.QWidget(Shapeup)
        self.shapeup_centralwidget.setObjectName(_fromUtf8("shapeup_centralwidget"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.shapeup_centralwidget)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.shapeup_tabWidget = QtGui.QTabWidget(self.shapeup_centralwidget)
        self.shapeup_tabWidget.setObjectName(_fromUtf8("shapeup_tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_10 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Devanagari MT"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.tab)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_2.addWidget(self.label_22, 4, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.tab)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 5, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 6, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 7, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.tab)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 8, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 9, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_23 = QtGui.QLabel(self.tab)
        self.label_23.setMaximumSize(QtCore.QSize(50, 50))
        self.label_23.setText(_fromUtf8(""))
        self.label_23.setPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/play.png")))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_14.addWidget(self.label_23)
        self.label_24 = QtGui.QLabel(self.tab)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_14.addWidget(self.label_24)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_25 = QtGui.QLabel(self.tab)
        self.label_25.setMaximumSize(QtCore.QSize(55, 55))
        self.label_25.setText(_fromUtf8(""))
        self.label_25.setPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/help.png")))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_13.addWidget(self.label_25)
        self.label_26 = QtGui.QLabel(self.tab)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_13.addWidget(self.label_26)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.shapeup_tabWidget.addTab(self.tab, _fromUtf8(""))
        self.shapeup_tab = QtGui.QWidget()
        self.shapeup_tab.setObjectName(_fromUtf8("shapeup_tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.shapeup_tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_13 = QtGui.QLabel(self.shapeup_tab)
        self.label_13.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DecoType Naskh"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.shapeup_tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Devanagari MT"))
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout.addWidget(self.label_14)
        self.horizontalLayout_17.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.shapeup_tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.shapeup_sasfile_lineEdit = QtGui.QLineEdit(self.shapeup_tab)
        self.shapeup_sasfile_lineEdit.setObjectName(_fromUtf8("shapeup_sasfile_lineEdit"))
        self.horizontalLayout_3.addWidget(self.shapeup_sasfile_lineEdit)
        self.shapeup_sasfile_pushButton = QtGui.QPushButton(self.shapeup_tab)
        self.shapeup_sasfile_pushButton.setObjectName(_fromUtf8("shapeup_sasfile_pushButton"))
        self.horizontalLayout_3.addWidget(self.shapeup_sasfile_pushButton)
        self.shapeup_saxs_showButton = QtGui.QPushButton(self.shapeup_tab)
        self.shapeup_saxs_showButton.setObjectName(_fromUtf8("shapeup_saxs_showButton"))
        self.horizontalLayout_3.addWidget(self.shapeup_saxs_showButton)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtGui.QSpacerItem(165, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_15 = QtGui.QLabel(self.shapeup_tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Devanagari MT"))
        font.setPointSize(19)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_18.addWidget(self.label_15)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_16 = QtGui.QLabel(self.shapeup_tab)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_12.addWidget(self.label_16)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.shapeupDatabase_combobox = QtGui.QComboBox(self.shapeup_tab)
        self.shapeupDatabase_combobox.setObjectName(_fromUtf8("shapeupDatabase_combobox"))
        self.shapeupDatabase_combobox.addItem(_fromUtf8(""))
        self.shapeupDatabase_combobox.addItem(_fromUtf8(""))
        self.shapeupDatabase_combobox.addItem(_fromUtf8(""))
        self.horizontalLayout_12.addWidget(self.shapeupDatabase_combobox)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_12)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_18 = QtGui.QLabel(self.shapeup_tab)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_20.addWidget(self.label_18)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem9)
        spacerItem10 = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.shapeup_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.shapeup_model_lineEdit = QtGui.QLineEdit(self.shapeup_tab)
        self.shapeup_model_lineEdit.setObjectName(_fromUtf8("shapeup_model_lineEdit"))
        self.horizontalLayout_4.addWidget(self.shapeup_model_lineEdit)
        self.shapeup_model_pushButton = QtGui.QPushButton(self.shapeup_tab)
        self.shapeup_model_pushButton.setObjectName(_fromUtf8("shapeup_model_pushButton"))
        self.horizontalLayout_4.addWidget(self.shapeup_model_pushButton)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)
        spacerItem11 = QtGui.QSpacerItem(165, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.shapeup_tab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.shapeup_nmax_lineEdit = QtGui.QLineEdit(self.shapeup_tab)
        self.shapeup_nmax_lineEdit.setObjectName(_fromUtf8("shapeup_nmax_lineEdit"))
        self.horizontalLayout_5.addWidget(self.shapeup_nmax_lineEdit)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)
        spacerItem12 = QtGui.QSpacerItem(54, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.shapeup_tab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.shapeup_rmax_lineEdit = QtGui.QLineEdit(self.shapeup_tab)
        self.shapeup_rmax_lineEdit.setObjectName(_fromUtf8("shapeup_rmax_lineEdit"))
        self.horizontalLayout_6.addWidget(self.shapeup_rmax_lineEdit)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_6 = QtGui.QLabel(self.shapeup_tab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        self.shapeup_scan_comboBox = QtGui.QComboBox(self.shapeup_tab)
        self.shapeup_scan_comboBox.setObjectName(_fromUtf8("shapeup_scan_comboBox"))
        self.shapeup_scan_comboBox.addItem(_fromUtf8(""))
        self.shapeup_scan_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.shapeup_scan_comboBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem14 = QtGui.QSpacerItem(123, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_7 = QtGui.QLabel(self.shapeup_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_8.addWidget(self.label_7)
        self.shapeup_buildmap_comboBox = QtGui.QComboBox(self.shapeup_tab)
        self.shapeup_buildmap_comboBox.setObjectName(_fromUtf8("shapeup_buildmap_comboBox"))
        self.shapeup_buildmap_comboBox.addItem(_fromUtf8(""))
        self.shapeup_buildmap_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.shapeup_buildmap_comboBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.shapeup_tabWidget.addTab(self.shapeup_tab, _fromUtf8(""))
        self.shapeup_tab_2 = QtGui.QWidget()
        self.shapeup_tab_2.setObjectName(_fromUtf8("shapeup_tab_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.shapeup_tab_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_9 = QtGui.QLabel(self.shapeup_tab_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.shapeup_textBrowser = QtGui.QTextBrowser(self.shapeup_tab_2)
        self.shapeup_textBrowser.setObjectName(_fromUtf8("shapeup_textBrowser"))
        self.gridLayout.addWidget(self.shapeup_textBrowser, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.shapeup_tabWidget.addTab(self.shapeup_tab_2, _fromUtf8(""))
        self.horizontalLayout_21.addWidget(self.shapeup_tabWidget)
        Shapeup.setCentralWidget(self.shapeup_centralwidget)
        self.shapeup_menubar = QtGui.QMenuBar(Shapeup)
        self.shapeup_menubar.setGeometry(QtCore.QRect(0, 0, 721, 22))
        self.shapeup_menubar.setObjectName(_fromUtf8("shapeup_menubar"))
        Shapeup.setMenuBar(self.shapeup_menubar)
        self.shapeup_statusbar = QtGui.QStatusBar(Shapeup)
        self.shapeup_statusbar.setObjectName(_fromUtf8("shapeup_statusbar"))
        Shapeup.setStatusBar(self.shapeup_statusbar)
        self.shapeup_toolBar = QtGui.QToolBar(Shapeup)
        self.shapeup_toolBar.setIconSize(QtCore.QSize(60, 60))
        self.shapeup_toolBar.setObjectName(_fromUtf8("shapeup_toolBar"))
        Shapeup.addToolBar(QtCore.Qt.TopToolBarArea, self.shapeup_toolBar)
        self.shapeup_actionQuit = QtGui.QAction(Shapeup)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.shapeup_actionQuit.setIcon(icon)
        self.shapeup_actionQuit.setObjectName(_fromUtf8("shapeup_actionQuit"))
        self.shapeup_actionRun = QtGui.QAction(Shapeup)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shapeup_actionRun.setIcon(icon1)
        self.shapeup_actionRun.setObjectName(_fromUtf8("shapeup_actionRun"))
        self.shapeup_actionHelp = QtGui.QAction(Shapeup)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shapeup_actionHelp.setIcon(icon2)
        self.shapeup_actionHelp.setObjectName(_fromUtf8("shapeup_actionHelp"))
        self.actionShow_maps = QtGui.QAction(Shapeup)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/show.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionShow_maps.setIcon(icon3)
        self.actionShow_maps.setObjectName(_fromUtf8("actionShow_maps"))
        self.shapeup_toolBar.addAction(self.shapeup_actionQuit)
        self.shapeup_toolBar.addAction(self.shapeup_actionRun)
        self.shapeup_toolBar.addAction(self.shapeup_actionHelp)
        self.shapeup_toolBar.addAction(self.actionShow_maps)

        self.retranslateUi(Shapeup)
        self.shapeup_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Shapeup)

    def retranslateUi(self, Shapeup):
        Shapeup.setWindowTitle(_translate("Shapeup", "SASTBX Shape Search Engine", None))
        self.label_10.setText(_translate("Shapeup", "Shape Search Engine", None))
        self.label_11.setText(_translate("Shapeup", "Fast Retrieval 3D models for the given saxs experimental profile", None))
        self.label.setText(_translate("Shapeup", "SAXS File: The intensity profile is the only required input file.", None))
        self.label_8.setText(_translate("Shapeup", "Optional control parameters:", None))
        self.label_22.setText(_translate("Shapeup", "Database: The database used for SAXS file  fast retrieval", None))
        self.label_20.setText(_translate("Shapeup", "Model : any pdb model to be compared, and the maps will be aligned to the first pdb file", None))
        self.label_17.setText(_translate("Shapeup", " Nmax: maximum order of the zernike polynomial expansion (<=20 for precomputed database; 10 is the default)", None))
        self.label_12.setText(_translate("Shapeup", " Rmax : radius of the molecule (default: guessed from Rg)", None))
        self.label_19.setText(_translate("Shapeup", "Buildmap: build electron density map in xplor format, all the map will be aligned, default True", None))
        self.label_21.setText(_translate("Shapeup", "Scan:scan for different rmax,default True", None))
        self.label_24.setText(_translate("Shapeup", "Start the program", None))
        self.label_26.setText(_translate("Shapeup", "To obtain the example of  input and output files", None))
        self.shapeup_tabWidget.setTabText(self.shapeup_tabWidget.indexOf(self.tab), _translate("Shapeup", "Introduction", None))
        self.label_13.setText(_translate("Shapeup", "Shape Search Engine", None))
        self.label_14.setText(_translate("Shapeup", "Fast Retrieve 3D models for the given saxs experimental profile", None))
        self.label_2.setText(_translate("Shapeup", "SAS File", None))
        self.shapeup_sasfile_pushButton.setText(_translate("Shapeup", "Brower", None))
        self.shapeup_saxs_showButton.setText(_translate("Shapeup", "Show", None))
        self.label_15.setText(_translate("Shapeup", "Optional", None))
        self.label_16.setText(_translate("Shapeup", "Database", None))
        self.shapeupDatabase_combobox.setItemText(0, _translate("Shapeup", "pisa", None))
        self.shapeupDatabase_combobox.setItemText(1, _translate("Shapeup", "pdb", None))
        self.shapeupDatabase_combobox.setItemText(2, _translate("Shapeup", "3Dcomplex", None))
        self.label_18.setText(_translate("Shapeup", "Compare to PDB Coordinate File:", None))
        self.label_3.setText(_translate("Shapeup", "Model", None))
        self.shapeup_model_pushButton.setText(_translate("Shapeup", "Brower", None))
        self.label_4.setText(_translate("Shapeup", "Nmax", None))
        self.label_5.setText(_translate("Shapeup", "Rmax", None))
        self.label_6.setText(_translate("Shapeup", "Scan", None))
        self.shapeup_scan_comboBox.setItemText(0, _translate("Shapeup", "True", None))
        self.shapeup_scan_comboBox.setItemText(1, _translate("Shapeup", "False", None))
        self.label_7.setText(_translate("Shapeup", "Buildmap", None))
        self.shapeup_buildmap_comboBox.setItemText(0, _translate("Shapeup", "True", None))
        self.shapeup_buildmap_comboBox.setItemText(1, _translate("Shapeup", "Flase", None))
        self.shapeup_tabWidget.setTabText(self.shapeup_tabWidget.indexOf(self.shapeup_tab), _translate("Shapeup", "Input", None))
        self.label_9.setText(_translate("Shapeup", "Result", None))
        self.shapeup_tabWidget.setTabText(self.shapeup_tabWidget.indexOf(self.shapeup_tab_2), _translate("Shapeup", "Output", None))
        self.shapeup_toolBar.setWindowTitle(_translate("Shapeup", "toolBar", None))
        self.shapeup_actionQuit.setText(_translate("Shapeup", "quit", None))
        self.shapeup_actionRun.setText(_translate("Shapeup", "run", None))
        self.shapeup_actionHelp.setText(_translate("Shapeup", "help", None))
        self.actionShow_maps.setText(_translate("Shapeup", "Show maps in pymol", None))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Shapeup = QtGui.QMainWindow()
    ui = Ui_Shapeup()
    ui.setupUi(Shapeup)
    Shapeup.show()
    sys.exit(app.exec_())

