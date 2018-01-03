from PyQt4 import QtCore
from PyQt4 import QtGui
from filecontent import Ui_MainWindow
import sys

class FileContentApp(QtGui.QMainWindow,Ui_MainWindow,QtCore.QEvent):
	def __init__(self,parent=None):
		#super(SuperposeApp, self).__init__(parent)
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.actionClose.triggered.connect(self.projectClose)

	def projectClose(self):
		self.close()


if __name__ =="__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = FileContentApp()
	myapp.show()
	app.exec_()