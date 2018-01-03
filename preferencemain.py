#!/usr/bin/python
from PyQt4 import QtGui
from PyQt4 import QtCore
from preference import Ui_Preference
import os
import sys

 
base = str(os.path.split(sys.path[0])[0])

class PreferenceApp(QtGui.QMainWindow,Ui_Preference,QtCore.QEvent):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_Preference()
		self.ui.setupUi(self)
		#self.ui.actionQuit.triggered.connect(self.close)
		self.ui.browse_Button.connect(self.ui.browse_Button,QtCore.SIGNAL(( "clicked()")),self.pymolPath)
		self.ui.cancel_button.connect(self.ui.cancel_button,QtCore.SIGNAL((" clicked()")), self.cancel)
		self.ui.ok_button.connect(self.ui.ok_button,QtCore.SIGNAL((" clicked()")), self.ok)
		self.ui.SASTBX_path_Button.connect(self.ui.SASTBX_path_Button, QtCore.SIGNAL(( "clicked()" )),self.SASTBX_Path)


	def SASTBX_Path(self):
		self.dirname=str(QtGui.QFileDialog(self).getExistingDirectory())
		if os.path.isdir(self.dirname):
			self.ui.SASTBX_path_lineEdit.setText(self.dirname)

		dirs = []

		for d in os.listdir(self.dirname):
			dirs.append(d)

		if ("build" not in dirs) or  ("modules" not in dirs):
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			msgBox.setText("The SASTBX path is invalid")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False
			
	def pymolPath(self):
		self.filename=QtGui.QFileDialog(self).getOpenFileName()
		self.ui.pymol_path_lineEdit.setText(self.filename)

	def cancel(self):	
		self.close()

	def ok(self):
		SASTBXpathfile = os.path.join(base,"SASTBXpath.txt")
		with open(SASTBXpathfile,"w") as f1:
			print >> f1, self.ui.SASTBX_path_lineEdit.text()
		pymolpathfile = os.path.join(base,"pymolpath.txt")
		with open(pymolpathfile,"w") as f:
			if str(self.ui.pymol_path_lineEdit.text()).strip()=='':
				print >>f, "/Applications/MacPyMOL.app"
				self.pymolpath = "/Applications/MacPyMOL.app"
			else:
				print >>f, str(self.ui.pymol_path_lineEdit.text()).strip()	
				self.pymolpath = str(self.ui.pymol_path_lineEdit.text()).strip()
		self.close()	

if __name__ =="__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = PreferenceApp()
	myapp.show()
	app.exec_()







