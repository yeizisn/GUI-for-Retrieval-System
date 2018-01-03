# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpDocument.ui'
#
# Created by: PyQt4 UI code generator 4.12
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

class Ui_Document(object):
    def setupUi(self, Document):
        Document.setObjectName(_fromUtf8("Document"))
        Document.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Document.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Document)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        Document.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Document)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Document.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Document)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Document.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Document)
        self.toolBar.setIconSize(QtCore.QSize(60, 60))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Document.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtGui.QAction(Document)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon1)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHome = QtGui.QAction(Document)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon2)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionHome)

        self.retranslateUi(Document)
        QtCore.QMetaObject.connectSlotsByName(Document)

    def retranslateUi(self, Document):
        Document.setWindowTitle(_translate("Document", "SASTBX Document", None))
        self.toolBar.setWindowTitle(_translate("Document", "toolBar", None))
        self.actionQuit.setText(_translate("Document", "quit", None))
        self.actionHome.setText(_translate("Document", "home", None))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Document = QtGui.QMainWindow()
    ui = Ui_Document()
    ui.setupUi(Document)
    Document.show()
    sys.exit(app.exec_())

