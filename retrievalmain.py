from PyQt4 import QtCore
from PyQt4 import QtGui 
import sys
import os
from retrieval import Ui_Retrieval
import subprocess
import shlex
import shutil
from filecontentmain import FileContentApp
from helpDocumentmain import helpDocumentApp
from preferencemain import PreferenceApp


############zernike_model/retrieval.py################
base = str(os.path.split(sys.path[0])[0])


class RetrievalApp(QtGui.QMainWindow,Ui_Retrieval,QtCore.QEvent):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_Retrieval()
		self.ui.setupUi(self)
		self.preference = PreferenceApp()
		self.filecontent = FileContentApp()
		self.helpDocument = helpDocumentApp()

		self.index_run = 0
		self.index_show = 0
		self.ui.actionQuit.triggered.connect(self.projectClose)
		
		self.ui.actionRun.triggered.connect(self.run)
		self.ui.actionHelp.triggered.connect(self.helpDocumentShow)
		self.icon1 = QtGui.QIcon()
		self.icon1.addPixmap(QtGui.QPixmap(":/image/imge/retrieval.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)       
		self.retrieval_toolButton = QtGui.QToolButton()
		self.retrieval_toolButton.setObjectName('retrieval')
		self.retrieval_toolButton.setText("Protein Retrieval")
		self.retrieval_toolButton.setIcon(self.icon1)
		self.retrieval_toolButton.setIconSize(QtCore.QSize(300,80))
		self.retrieval_toolButton.setAutoRaise(True)
		self.retrieval_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		

		self.ui.actionQuit.triggered.connect(self.buttonClose)
		self.retrieval_toolButton.connect(self.retrieval_toolButton,QtCore.SIGNAL(( "clicked()" )),self.setwindowtop)

		
		self.icon2 = QtGui.QIcon()
		self.icon2.addPixmap(QtGui.QPixmap(":/image/imge/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)       
		self.project_toolButton = QtGui.QToolButton()
		self.project_toolButton.setText("CLOSE")
		self.project_toolButton.setIcon(self.icon2)
		self.project_toolButton.setIconSize(QtCore.QSize(100,80))
		self.project_toolButton.setAutoRaise(True)
		self.project_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		
		self.ui.protein_Button.connect(self.ui.protein_Button,QtCore.SIGNAL(( "clicked()" )),self.openpdb)
		self.ui.database_Button.connect(self.ui.database_Button, QtCore.SIGNAL(( "clicked()" )), self.opendb)
		##########change for different platform############
		#######for console test##########
		self.default_database = "/Users/Song/Desktop/smalldatabase"
		self.ui.database_lineEdit.setText(self.default_database)
	

	def helpDocumentShow(self):
		self.helpDocument.show()

	def projectClose(self):
		self.project_toolButton.setParent(None)
		self.retrieval_toolButton.setParent(None)
		self.close()

	def setwindowtop(self):
		self.hide()
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		self.show()

	def buttonClose(self):
		self.retrieval_toolButton.setParent(None)

	def openpdb(self):
		self.filename=QtGui.QFileDialog(self).getOpenFileName()
		if os.path.isfile(self.filename):
			self.ui.protein_lineEdit.setText(self.filename)

		pdbfile = str(self.ui.protein_lineEdit.displayText()).strip()
		typefile = str(pdbfile.split(".")[-1]).strip()
		if (typefile!="pdb") and (typefile!="ent"):
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			msgBox.setText("The input file is invalid,please input a PDB file")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False

	def opendb(self):
		self.ui.database_lineEdit.clear()
		self.dirname=str(QtGui.QFileDialog(self).getExistingDirectory())
		flag_nlm = False
		flag_codes = False

		for rt, dirs, files in os.walk(self.dirname):
			for f in files:
				typef = f.split(".")[-1].strip()
				if typef =="codes":
					flag_codes=True
				if typef =="nlm":
					flag_nlm=True
		
		if flag_codes==True and flag_nlm==True:
			self.ui.database_lineEdit.setText(self.dirname)

		else:
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			msgBox.setText("The database path is invalid,please verify the directory")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False




if __name__ =="__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = RetrievalApp()
	myapp.show()
	app.exec_()

