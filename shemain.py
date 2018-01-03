from PyQt4 import QtCore
from PyQt4 import QtGui
from she import Ui_She
import sys
import subprocess
import shlex
import os
from matplotlib import pyplot as plt
import math
import re
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib
from saxsshow import ApplicationWindow
from saxsshow import MyMplCanvas1
from saxsshow import MyMplCanvas2
from helpDocumentmain import helpDocumentApp
import shutil


#base = str(os.path.split(sys.path[0])[0])
base = sys.path[0]
###########intensity/sas_I.py#############
class SheApp(QtGui.QMainWindow,Ui_She,QtCore.QEvent):
	def __init__(self,targetdir,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_She()
		self.ui.setupUi(self)
		self.ui.actionQuit.triggered.connect(self.projectClose)
		self.ui.actionRun.triggered.connect(self.she)
		self.helpDocument = helpDocumentApp()

		self.ui.tabWidget.setCurrentIndex(0)
		self.ui.pdb_button.connect(self.ui.pdb_button,QtCore.SIGNAL(( "clicked()" )),self.openfile_pdb)
		self.ui.saxs_button.connect(self.ui.saxs_button,QtCore.SIGNAL(( "clicked()" )),self.openfile_saxs)
		self.ui.statusbar.showMessage('Small Angle Scattering ToolBox1.0.0              Intensity Calculation')
		self.ui.saxs_show_pushButton.connect(self.ui.saxs_show_pushButton,QtCore.SIGNAL(( "clicked()" )),self.show_saxs)
		self.targetdir = targetdir

		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/image/imge/she.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)       
	
		
		self.she_toolButton = QtGui.QToolButton()
		self.she_toolButton.setText("Compute theoretical scattering intensity curve")
		self.she_toolButton.setIcon(icon1)
		self.she_toolButton.setIconSize(QtCore.QSize(300,80))
		self.she_toolButton.setAutoRaise(True)
		self.she_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
	
		self.ui.actionQuit.triggered.connect(self.buttonclose)
		self.she_toolButton.connect(self.she_toolButton,QtCore.SIGNAL(( "clicked()" )),self.setwindowtop)
		self.icon2 = QtGui.QIcon()
		self.icon2.addPixmap(QtGui.QPixmap(":/image/imge/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)       
		self.project_toolButton = QtGui.QToolButton()
		self.project_toolButton.setText("CLOSE")
		#self.superpose_toolButton.setText("Superpose models at low resolutions")
		self.project_toolButton.setIcon(self.icon2)
		self.project_toolButton.setIconSize(QtCore.QSize(100,80))
		self.project_toolButton.setAutoRaise(True)
		self.project_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		self.project_toolButton.connect(self.project_toolButton, QtCore.SIGNAL(( "clicked()" )), self.projectClose)
		#self.ui.tabWidget.setTabEnabled(3,False)
		# self.ui.summary_tableWidget.setColumnCount(4)
		# self.ui.summary_tableWidget.setRowCount(2)
		# self.ui.summary_tableWidget.setHorizontalHeaderLabels(["File Path","type","Show","Compare"])
		# self.ui.summary_tableWidget.setColumnWidth(0, 400)
		# self.ui.summary_tableWidget.setColumnWidth(1, 80)
		# self.ui.summary_tableWidget.setColumnWidth(2, 80)
		# self.ui.summary_tableWidget.setColumnWidth(3, 105)
		self.ui.actionHelp.triggered.connect(self.helpDocumentShow)
		self.ui.starting_q_LineEdit.setText("0")
		self.ui.stopping_q_LineEdit.setText("0.5")
		self.ui.number_of_n_LineEdit.setText("51")


	def helpDocumentShow(self):
		self.helpDocument.show()

	def read(self):
		flag = True
		buff = []
		while flag:
			try:
				out = open(self.shefile,"r")
				lines = out.readlines()
				out.close()
			except:
				continue
			if lines!=buff:
				for sentence in lines:
					if sentence in buff:
						continue
					if sentence=='__END__':
						return
					self.ui.textBrowser.append(sentence)
					QtCore.QCoreApplication.processEvents()
				buff = lines
	

	def projectClose(self):
		self.project_toolButton.setParent(None)
		self.she_toolButton.setParent(None)
		self.close()

	def closeEvent(self, QCloseEvent):
			self.projectClose()
			
	def setwindowtop(self):
		self.hide()
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		self.show()

	def buttonclose(self):
		self.she_toolButton.setParent(None)

	def openfile_pdb(self):
		self.filename=QtGui.QFileDialog(self).getOpenFileName()
		if os.path.isfile(self.filename):
			self.ui.she_pdb_LineEdit.setText(self.filename)

	def openfile_saxs(self):
		self.filename=QtGui.QFileDialog(self).getOpenFileName()
		if os.path.isfile(self.filename):
			self.ui.she_saxs_LineEdit.setText(self.filename)



	def show_saxs(self):
		sasfile=str(self.ui.she_saxs_LineEdit.displayText())
		if sasfile=='':
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			
			msgBox.setText("The SAXS file is not exist!")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False
		else:
			typesas = str(sasfile.split(".")[-1])
			if typesas!="dat":
				msgBox = QtGui.QMessageBox()
				msgBox.setTextFormat(QtCore.Qt.RichText)
				msgBox.setIcon(QtGui.QMessageBox.Critical)
				
				msgBox.setText("The input file is invalid,please input a SAXS file")
				msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
				ret = msgBox.exec_()
				if ret == QtGui.QMessageBox.Ok:
					return False
			else:
				f = open(sasfile,"r")
				length = str(f.readline()).strip().split()
				if (length>=2):	
					q_list = []
					logi_list = []
					#sigma_list = []
					for line in f.readlines():
						list_qi = str(line).strip().split()	
						q, i = list_qi[0], list_qi[1]
						q_list.append(float(q))
						logi_list.append(math.log(float(i)))
						#sigma = sigma_list.append(float(sigma))
					self.plotcurve = ApplicationWindow(q_list,logi_list)
					self.plotcurve.show()
	 			else:
	 				msgBox = QtGui.QMessageBox()
					msgBox.setTextFormat(QtCore.Qt.RichText)
					msgBox.setIcon(QtGui.QMessageBox.Critical)
					
					msgBox.setText("The input file is invalid,please input a SAXS file")
					msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
					ret = msgBox.exec_()
					if ret == QtGui.QMessageBox.Ok:
						return False

	def run(self, command):
		import sys
		subprocess.Popen(shlex.split(command),stdout=sys.stdin,shell=False)

	def getlist(self,file):
		f = open(file,"r")
		length = str(f.readline()).strip().split()	
		q_list = []
		logi_list = []
		#sigma_list = []
		for line in f.readlines():
			list_qi = str(line).strip().split()	
			q, i = list_qi[0], list_qi[1]
			q_list.append(float(q))
			logi_list.append(math.log(float(i)))
		f.close()
		return	q_list, logi_list

	def she(self):
		SASTBXpathfile = os.path.join(base,"SASTBXpath.txt")
		with open(SASTBXpathfile,"r") as f1:
			self.SASTBXpath = f1.read().strip()
		env = str(os.path.join(self.SASTBXpath, 'build', 'bin'))+ ':'
		self.targetfile_SAS = os.path.join(self.SASTBXpath,"modules","cctbx_project","sastbx","targetpath_GUI.txt")
		with open(self.targetfile_SAS,"w") as f:
			print >> f, self.targetdir
		os.environ['PATH'] = env+os.environ['PATH']


		self.ui.textBrowser.clear()
		she_method = str(self.ui.she_method_comboBox.currentText())
		she_qstarting=str(self.ui.starting_q_LineEdit.displayText())
		she_qstopping=str(self.ui.stopping_q_LineEdit.displayText())
		she_nnumber=str(self.ui.number_of_n_LineEdit.displayText())
		she_structure=str(self.ui.she_pdb_LineEdit.displayText())
		she_expt_data=str(self.ui.she_saxs_LineEdit.displayText())
		if she_structure=='':
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			
			msgBox.setText("Please input the PDB file")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False

		else:
			command = "sastbx.she"
			command = command+" structure=%s" %she_structure


			dic = {"method":she_method,"experimental_data":she_expt_data,
			"q_start":she_qstarting,"q_stop":she_qstopping,"n_step":she_nnumber}

			for key in dic:
				if dic[key]!='':
					command = command+' '+key+"="+dic[key]

			
			# with open(str(sys.path[0])+"/tmp.txt","r") as f:
			# 	project=f.read().strip()
			project = self.targetdir
			outdir=os.path.join(project,"intensity_curve")

			filename = str(str(she_structure.split("/")[-1]).split(".")[0])
			output = os.path.join(outdir,filename+".iq")
			if os.path.isdir(outdir)==False:
				os.makedirs(outdir)
			#self.shefile = os.path.join(outdir,"temp.txt")
			self.shefile = os.path.join(self.SASTBXpath,"modules","cctbx_project","sastbx","she.txt")


			command = command+" output=%s" %output

			###########copy input file to outdir###########
			shutil.copy(she_structure,outdir)
			if she_expt_data!='':
				shutil.copy(she_expt_data,outdir)


			
			self.ui.tabWidget.setCurrentIndex(2)
			self.movie_screen = QtGui.QLabel()
			self.movie_screen.setText("The program is running, please wait")		
			progdialog = QtGui.QProgressDialog(self)
			progdialog.setWindowTitle("Renaming Archives")
			progdialog.setWindowModality(QtCore.Qt.WindowModal)
			progdialog.setLabel(self.movie_screen)		
			progdialog.show()
			iner = open(self.shefile,"w")
			iner.write("Start.")
			iner.close()
			import threading
			t = []
			t.append(threading.Thread(target=self.run(command)))
			t.append(threading.Thread(target=self.read()))
			for t1 in t:
				t1.setDaemon(True)
				t1.start()
				t1.join()
			# child1 = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE,shell=False)
			# out = child1.communicate()
			progdialog.close()
			# result = str(str(str(out[0]).split("__END__")[-1]).split("start running at")[0])
			# explainStr = "The result files are saved in the following directory"
			# self.ui.textBrowser.append(explainStr)
			# self.ui.textBrowser.append(os.path.join(project,"she"))
			# self.ui.textBrowser.append(result)
			self.ui.tabWidget.setCurrentIndex(2)
			self.summary_tab = QtGui.QTabWidget()
			summarypage = QtGui.QWidget()
			summarylayout = QtGui.QVBoxLayout(summarypage)
			q_list,logi_list = self.getlist(output)
			if she_expt_data =='':
				sc = MyMplCanvas1(q_list,logi_list)
			else:
				fitfile = output+".fit"
				fitq_list,fiti_list = self.getlist(fitfile)
				saxq_list,saxi_list = self.getlist(she_expt_data)
				sc = MyMplCanvas2(fitq_list,fiti_list,saxq_list,saxi_list,"q","Intensity","intensity curve fit saxs data","intensity curve for saxs data","Q-Intensity Curve Comparison")
			self.ntb = NavigationToolbar(sc,self)
			summarylayout.addWidget(self.ntb)
			summarylayout.addWidget(sc)
			self.summary_tab.addTab(summarypage,"Q-Intensity Curve")
			self.ui.tabWidget.addTab(self.summary_tab,"summary")
			# rowPosition = self.ui.summary_tableWidget.RowCount()
			# self.ui.summary_tableWidget.insertRow(rowPosition)
			# self.ui.summary_tableWidget.setItem()
			shutil.copy(self.shefile,outdir)
			os.rename(os.path.join(outdir,"she.txt"),os.path.join(outdir,"log.txt"))

		with open(self.targetfile_SAS,"w") as f:
			f.truncate()	



if __name__ =="__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = SheApp()
	myapp.show()
	app.exec_()


