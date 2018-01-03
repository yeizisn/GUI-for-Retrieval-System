from PyQt4 import QtCore
from PyQt4 import QtGui
import sys
from shemain import SheApp


class runApp(QtGui.QWidget,QtCore.QEvent):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.she = SheApp()
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('run')

	def run(self):
		




if __name__ =="__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = runApp()
	myapp.show()
	app.exec_()
