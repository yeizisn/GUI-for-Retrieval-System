#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
 
from PyQt4 import QtCore, QtGui
from fawen import W2
 
style = """
        .QPushButton{
        border-style:none;
        border:1px solid #C2CCD8; 
        color:#F0F0F0;  
        padding:5px;
        min-height:20px;
        border-radius:5px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);
        }
    """
 
 
class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
      
        
        self.lineEdit = QtGui.QLineEdit()
        self.button = QtGui.QPushButton(u'子窗口',self)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.setWindowTitle(u'父窗口')
 
        self.button.clicked.connect(self.child)
        self.setStyleSheet(style)
 
    def child(self):
        print u'弹出子窗口'
        self.w2 = W2()
        self.connect(self.w2, QtCore.SIGNAL("myclicked()"), self.recv)
        self.w2.show()
       
         
    @QtCore.pyqtSlot(str) 
    def recv(self,s):
        print u'接受到子窗口值'
        print s
 
     
 
       
  
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())