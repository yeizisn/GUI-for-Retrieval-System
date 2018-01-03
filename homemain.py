#!/usr/bin/python
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtWebKit
from homepage import Ui_MainWindow
import sys
from posemain import SuperposeApp
from shapeupmain import ShapeupApp
from pregxsmain import PregxsApp
from shemain import SheApp
import os
from helpDocumentmain import helpDocumentApp
import shutil
import subprocess
import shlex
from preferencemain import PreferenceApp
#from retrieval import RetrievalApp



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
############add app path to envir path###############
###########################################################
#########Here base may be different for the packaged file and #########
#########the source file which running in console.....##########
##########So, take care to change the directory of 'base'###############



#base = '/Users/Song/sastbx/gui/sasqt/homemain.app/Contents/'
#base = str(os.path.split(sys.path[0])[0])

base = sys.path[0]
file_base  = str(os.path.split(sys.path[0])[0])
print "base of the SASTBXpath.txt: ", base
print "the content of SASTBXpath.txt:", file_base


# with open("/Users/songna/Desktop/dirpath.txt","w") as f:
# 	print >>f, file_base

#base = '/Users/songna/Downloads/software/sastbx/gui/sasqt/homemain.app/Contents/'
#path = os.path.dirname(base)
#env = str(os.path.join(base, 'build', 'bin'))+ ':'
#print env
#os.environ['PATH'] = env+os.environ['PATH']
# with open(os.path.join(base,"syspath.txt"),"w") as f:
# 	print >>f, os.environ['PATH']


with open(os.path.join(base,"SASTBXpath.txt"),"w") as f:
	print >>f, file_base

with open(os.path.join(base,"pymolpath.txt"),"w") as f:
	print >>f, "/Applications/MacPyMOL.app"
	
class MyApp(QtGui.QMainWindow,Ui_MainWindow,QtCore.QEvent):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.statusBar.showMessage('Small Angle Scattering ToolBox1.0.0')
		self.vlayout = QtGui.QVBoxLayout(self.ui.groupBox)
		self.vlayout2 = QtGui.QVBoxLayout(self.ui.groupBox_2)
		self.helpDocument = helpDocumentApp()
		self.preference = PreferenceApp()

		#self.vlayout.setMargin(10)
		#self.vlayout.addStretch()
		self.vlayout.setAlignment(QtCore.Qt.AlignTop)
		self.vlayout2.setAlignment(QtCore.Qt.AlignTop)
		#self.currentdir = os.path.join(str(str(sys.path[0]).split("sastbx")[0]),"Desktop")
		self.currentdir = str(str(sys.path[0]).split("sastbx")[0])
		self.ui.lineEdit.setText('')
		
		self.ui.actionQuit.triggered.connect(QtGui.qApp.quit)
		self.ui.actionPreference.triggered.connect(self.preferenceShow)

		self.connect(self.ui.listWidget,QtCore.SIGNAL('itemClicked(QListWidgetItem *)'),self.itemClicked)
		self.ui.pushButton.connect(self.ui.pushButton,QtCore.SIGNAL(( "clicked()")),self.projectdir)
		self.ui.actionPymol.triggered.connect(self.start)
		self.tmp_targetdir = str(self.ui.lineEdit.displayText())
		self.ui.actionDocument.triggered.connect(self.helpDocumentShow)
		self.ui.actionHelp.triggered.connect(self.helpDocumentShow)
		self.ui.actionSASTBX.triggered.connect(self.exampleFile)
		self.ui.actionOpenProject.triggered.connect(self.projectdir)
		self.setStyleSheet(style)
		
		# self.superpose_close_button = QtGui.QPushButton("Close Project",self)
		# self.superpose_close_button.connect(self.close_button,QtCore.SIGNAL(( "clicked()" )),self.SuperposeClose)
	

	def closeEvent(self,event):
		QtGui.qApp.quit()

	def mouseEvent(self,event):
		if self.ui.label.underMouse():
			print 'under Mouse'
		return super(MyApp,self).mouseEvent(event)

	def helpDocumentShow(self):
		self.helpDocument.show()

	def preferenceShow(self):
		self.preference.show()
 
	def projectdir(self):
		self.dirname=QtGui.QFileDialog(self).getExistingDirectory()
		if os.path.isdir(self.dirname):
			self.ui.lineEdit.setText(self.dirname)
			#self.shapeup.outdir = self.dirname
			f = open("tmp.txt","w")
			f.write(self.dirname)
			f.close()
	
	def exampleFile(self):
		self.path = os.path.split(sys.path[0])[0]
		targetdir = str(self.ui.lineEdit.displayText())

		self.exampleDir = os.path.join(self.path,"sastbx_examples")
		shutil.copy(self.exampleDir,targetdir)
		#self.exampleDir = "/Users/Song/Downloads/cctbx/gui/sasqt/sastbx_examples"
		self.exampleFile=QtGui.QFileDialog.getExistingDirectory(self,"Example Files",self.exampleDir)

	def itemClicked(self):
		index = self.ui.listWidget.currentRow()
		targetdir = str(self.ui.lineEdit.displayText())
		if targetdir =='':
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			msgBox.setText("Please set the project location in the lineedit in the ")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False
		if os.path.isdir(targetdir)==False or (".app" in targetdir)==True:
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			msgBox.setText("The project location is invalid")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False
		
		#acurrent = str(self.ui.listWidget.currentItem().text()).strip()
		if index == 0:
			#self.ui.listWidget.currentItem().setBackgroundColor(QtGui.QColor('red'))
			try:
				self.superpose
				if not self.superpose.isVisible():
					self.superpose = SuperposeApp(targetdir)
					self.superpose.show()
					self.vlayout.addWidget(self.superpose.superpose_toolButton,QtCore.Qt.AlignTop)
					self.vlayout2.addWidget(self.superpose.project_toolButton,QtCore.Qt.AlignTop)
			except:
				self.superpose = SuperposeApp(targetdir)
				self.superpose.show()
				self.vlayout.addWidget(self.superpose.superpose_toolButton,QtCore.Qt.AlignTop)
				self.vlayout2.addWidget(self.superpose.project_toolButton,QtCore.Qt.AlignTop)
			
		elif index ==1:
			try:
				self.shapeup
				if not self.shapeup.isVisible():
					self.shapeup = ShapeupApp(targetdir)
					self.shapeup.show()
					self.vlayout.addWidget(self.shapeup.she_toolButton,QtCore.Qt.AlignTop)
					self.vlayout2.addWidget(self.shapeup.project_toolButton,QtCore.Qt.AlignTop)
			except:
				self.shapeup = ShapeupApp(targetdir)
				self.shapeup.show()
				self.vlayout.addWidget(self.shapeup.shapeup_toolButton,QtCore.Qt.AlignTop)
				self.vlayout2.addWidget(self.shapeup.project_toolButton,QtCore.Qt.AlignTop)

			
		elif index ==2:
			try:
				self.she
				if not self.she.isVisible():
					self.she = SheApp(targetdir)
					self.she.show()
					self.vlayout.addWidget(self.she.she_toolButton,QtCore.Qt.AlignTop)
					self.vlayout2.addWidget(self.she.project_toolButton,QtCore.Qt.AlignTop)
			except:
				self.she = SheApp(targetdir)
				self.she.show()
				self.vlayout.addWidget(self.she.she_toolButton,QtCore.Qt.AlignTop)
				self.vlayout2.addWidget(self.she.project_toolButton,QtCore.Qt.AlignTop)

			
		elif index ==3:
			try:
				self.pregxs
				if not self.pregxs.isVisible():
					self.pregxs = PregxsApp(targetdir)
					self.pregxs.show()
					self.vlayout.addWidget(self.pregxs.refine_toolButton,QtCore.Qt.AlignTop)
					self.vlayout2.addWidget(self.pregxs.project_toolButton,QtCore.Qt.AlignTop)
			except:
				self.pregxs = PregxsApp(targetdir)
				self.pregxs.show()
				self.vlayout.addWidget(self.pregxs.refine_toolButton,QtCore.Qt.AlignTop)
				self.vlayout2.addWidget(self.pregxs.project_toolButton,QtCore.Qt.AlignTop)
	
		
		##########retrieval
		elif index==4:
			try:
				self.retrieval
				if not self.retrieval.isVisible():
					self.retrieval = RetrievalApp(targetdir)
					self.retrieval.show()
					self.vlayout.addWidget(self.retrieval.retrieval_toolButton,QtCore.Qt.AlignTop)
					self.vlayout2.addWidget(self.retrieval.project_toolButton,QtCore.Qt.AlignTop)
			except:
				self.retrieval = RetrievalApp(targetdir)
				self.retrieval.show()
				self.vlayout.addWidget(self.retrieval.retrieval_toolButton,QtCore.Qt.AlignTop)
				self.vlayout2.addWidget(self.retrieval.project_toolButton,QtCore.Qt.AlignTop)
	

		else:
			print index


	def start(self):
		pymolpathfile = os.path.join(base,"pymolpath.txt")
		print "test pymol"
		print "pymolpathfile", pymolpathfile
		with open(pymolpathfile,"r") as f:
			temp_pymolpath = f.read().strip()
		
		if temp_pymolpath=='':
			self.pymolpath = "/Applications/MacPyMOL.app"
		else:
			self.pymolpath = temp_pymolpath

		if (self.pymolpath.find("pymol")!=-1) or (self.pymolpath.find("MacPyMOL.app")!=-1):
			if self.pymolpath.find(".app")!=-1:
				print "self.pymolpath is app: ",self.pymolpath
				command = "open -a "
				command = command+self.pymolpath
			else:
				print "self.pymolpath is command line", self.pymolpath
				#command = "source "
				command = self.pymolpath

			#try:
				#os.system("pymol")
				#command  = "open -a /Applications/WeChat.app"
				#command = "open -a /Users/Song/Desktop/MacPyMOL.app"
				##############This command is applicatable but Pymol can not open with out packages###############
				##############so try the pml script in pymol app then package them###############
				#command = "open -a /Users/Song/Desktop/MacPyMOL.app /Applications/SASTBX1.0.0/gui/sasqt/test.pml"
			try:
				process = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
				
				process_error =  process.stderr.read()
				print "process_error:",process_error
				if process_error !='':

					msgBox = QtGui.QMessageBox()
					msgBox.setTextFormat(QtCore.Qt.RichText)
					msgBox.setIcon(QtGui.QMessageBox.Critical)
					
					msgBox.setText("SASTBX couldn't locate MacPyMOL on your system\
						Please affirm the path configuration in preference is the MacPyMol path on your machine")
					msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
					ret = msgBox.exec_()
					if ret == QtGui.QMessageBox.Ok:
						return False
				else:
					print "process_error is NULL"


			except:

				msgBox = QtGui.QMessageBox()
				msgBox.setTextFormat(QtCore.Qt.RichText)
				msgBox.setIcon(QtGui.QMessageBox.Critical)
				
				msgBox.setText("SASTBX couldn't locate MacPyMOL on your system\
					Please affirm the path configuration in preference is the MacPyMol path on your machine")
				msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
				ret = msgBox.exec_()
				if ret == QtGui.QMessageBox.Ok:
					return False
		else:
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			
			msgBox.setText("The path is invaild\
				Please affirm the path configuration in preference is the MacPyMol path on your machine")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False
		

if __name__ =="__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyApp()
	myapp.show()
	app.exec_()
