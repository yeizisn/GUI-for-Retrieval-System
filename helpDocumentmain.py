from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtWebKit
from helpDocument import Ui_Document
import sys
import os 

global filepath
#for APP

filepath =sys.path[0]
filepath = os.path.split(filepath)[0]
filepath = filepath + "/doc/"

#for terminal
#filepath = "/Users/Song/Downloads/cctbx/gui/sasqt/doc/"

class helpDocumentApp(QtGui.QMainWindow,Ui_Document,QtCore.QEvent):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_Document()
		self.ui.setupUi(self)
		self.ui.actionQuit.triggered.connect(self.projectclose)
		self.ui.actionHome.triggered.connect(self.sethome)
		self.ui.statusbar.showMessage('Small Angle Scattering ToolBox1.0.0                  SASTBX Document')
		self.layout = QtGui.QVBoxLayout()		
		self.ui.widget.setLayout(self.layout)
		self.view = QtWebKit.QWebView()
		self.htmlPath = "file://"+filepath+"helpdocument.html?path=%s" %filepath
		self.url = QtCore.QUrl(self.htmlPath)
		self.view.load(self.url)
		self.layout.addWidget(self.view)
		self.ui.widget.setLayout(self.layout)

	def projectclose(self):
		self.close()

	def sethome(self):
		self.htmlPath = "file://"+filepath+"helpdocument.html?path=%s" %filepath
		self.url = QtCore.QUrl(self.htmlPath)
		self.view.load(self.url)
		self.layout.addWidget(self.view)
		self.ui.widget.setLayout(self.layout)




if __name__ =="__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = helpDocumentApp()
	myapp.show()
	app.exec_()