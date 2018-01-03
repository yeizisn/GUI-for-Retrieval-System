#pregxs.py is generated from ui file.
from PyQt4 import QtCore
from PyQt4 import QtGui
from pregxs import Ui_Pregxs
import sys
import subprocess
import shlex
import os
import math
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib
from saxsshow import ApplicationWindow
from saxsshow import MyMplCanvas11
from saxsshow import MyMplCanvas2
from helpDocumentmain import helpDocumentApp
import shutil

#base = str(os.path.split(sys.path[0])[0])
base = sys.path[0]

#sastbx.pregxs pr/pergxs.py
#from pregxs import Ui_Pregxs
#pregxs.py is generated from ui file.
class PregxsApp(QtGui.QMainWindow,Ui_Pregxs,QtCore.QEvent):
	def __init__(self,targetdir,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_Pregxs()
		self.ui.setupUi(self)
		self.ui.actionQuit.triggered.connect(self.projectClose)
		self.ui.actionRun.triggered.connect(self.pregxs)
		self.ui.tabWidget.setCurrentIndex(0)
		self.ui.pushButton.connect(self.ui.pushButton, QtCore.SIGNAL(( "clicked()" )),self.openfile_dat)
		self.targetdir = targetdir
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/image/imge/pregxs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)       
		self.helpDocument = helpDocumentApp()

	
		self.refine_toolButton = QtGui.QToolButton()
		self.refine_toolButton.setText("P(r) Estimation")
		self.refine_toolButton.setIcon(icon1)
		self.refine_toolButton.setIconSize(QtCore.QSize(300,80))
		self.refine_toolButton.setAutoRaise(True)
		self.refine_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
	
		self.ui.statusbar.showMessage('Small Angle Scattering ToolBox1.0.0                  P(r) Estimation')

		self.ui.actionQuit.triggered.connect(self.buttonclose)
		self.refine_toolButton.connect(self.refine_toolButton,QtCore.SIGNAL(( "clicked()" )),self.setwindowtop)
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
		self.ui.pregxs_saxs_showButton.connect(self.ui.pregxs_saxs_showButton, QtCore.SIGNAL(( "clicked()")),self.showsaxs)
		
		self.ui.actionhelp.triggered.connect(self.helpDocumentShow)

	def helpDocumentShow(self):
		self.helpDocument.show()

	def showsaxs(self):
		sasfile = str(self.ui.dat_lineEdit.displayText()).strip()

		typesas = str(sasfile.split(".")[-1])
		
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

	def read(self):
		flag = True
		buff = []
		while flag:
			out = open(self.pregxsfile,"r")
			lines = out.readlines()
			out.close()
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
		self.refine_toolButton.setParent(None)
		self.close()

	def closeEvent(self, QCloseEvent):
		self.projectClose()
		
	def setwindowtop(self):
		self.hide()
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		self.show()

	def buttonclose(self):
		self.refine_toolButton.setParent(None)
	def openfile_dat(self):
		self.filename=QtGui.QFileDialog(self).getOpenFileName()
		if os.path.isfile(self.filename):
			self.ui.dat_lineEdit.setText(self.filename)

	def run(self, command):
		import sys
		print command
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

	def getlist_pr(self,file):
		f = open(file,"r")
		length = str(f.readline()).strip().split()	
		q_list = []
		i_list = []
		#sigma_list = []
		for line in f.readlines():
			list_qi = str(line).strip().split()	
			q, i = list_qi[0], list_qi[1]
			q_list.append(float(q))
			i_list.append(float(i))
			
		f.close()
		return	q_list, i_list

	def pregxs(self):
		if self.ui.tabWidget.count()==4:
			self.ui.tabWidget.removeTab(3)
		SASTBXpathfile = os.path.join(base,"SASTBXpath.txt")
		with open(SASTBXpathfile,"r") as f1:
			self.SASTBXpath = f1.read().strip()
		env = str(os.path.join(self.SASTBXpath, 'build', 'bin'))+ ':'
		self.targetfile_SAS = os.path.join(self.SASTBXpath,"modules","cctbx_project","sastbx","targetpath_GUI.txt")
		with open(self.targetfile_SAS,"w") as f:
			print >> f, self.targetdir
		os.environ['PATH'] = env+os.environ['PATH']

		self.ui.textBrowser.clear()
		datfile = str(self.ui.dat_lineEdit.displayText()).strip()
		dmax = str(self.ui.dmax_lineEdit.displayText()).strip()
		scan = str(self.ui.scan_comboBox.currentText())
		# with open(str(sys.path[0])+"/tmp.txt","r") as f:
		# 	project=f.read().strip()
		project = self.targetdir
		self.outdir=os.path.join(self.targetdir,"Pr_Estimation")
		datname = datfile.split(".")[0].split("/")[-1]
		output = os.path.join(self.outdir,datname)

		if os.path.isdir(self.outdir)==False:
			os.makedirs(self.outdir)


		if datfile=='':
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			
			msgBox.setText("Please input the dat file")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False

		elif dmax =='':
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			
			msgBox.setText("Please input dmax")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False
		else:
			command = "sastbx.pregxs"
			command = command+" data=%s" %datfile
			command = command+" d_max=%s" %dmax
			command = command+" scan=%s" %scan
			command = command+" output=%s" %str(output)
			self.movie_screen = QtGui.QLabel()
			self.movie_screen.setText("The program is running, please wait")		
			self.ui.tabWidget.setCurrentIndex(2)
			#self.pregxsfile = os.path.join(self.targetdir,"Pr_Estimation","temp.txt")
			self.pregxsfile = os.path.join(self.SASTBXpath,"modules","cctbx_project","sastbx","pregxs.txt")

			###########copy input file to out dir
			shutil.copy(datfile,self.outdir)


			progdialog = QtGui.QProgressDialog(self)
			progdialog.setWindowTitle("Renaming Archives")
			progdialog.setWindowModality(QtCore.Qt.WindowModal)
			progdialog.setLabel(self.movie_screen)		
			progdialog.show()
			# child = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE,shell=False)
			# out = child.communicate()
			iner = open(self.pregxsfile,"w")
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
			progdialog.close()
			# explainStr = "The result files are saved in the following directory"
			# self.ui.textBrowser.append(explainStr)
			# self.ui.textBrowser.append(os.path.join(project,"pregxs"))

			# result = str(str(out[0]).split()[3])
			# self.ui.textBrowser.append(str(out))
			self.ui.tabWidget.setCurrentIndex(2)
 			



			if scan=="False":
			######add widget to tabwidget############
			########pr page###########
			
				self.summary_tab = QtGui.QTabWidget()
				summarypage = QtGui.QWidget()
				summarylayout = QtGui.QVBoxLayout(summarypage)
				# file = output+"average.pr"
				# step_list,pr_list = self.getlist(file)

				
				file2 =output+"best.pr"
				step_list2,pr_list2 = self.getlist_pr(file2)

				
				sc1 = MyMplCanvas11(step_list2,pr_list2,"step","pair distance","best pair distance","Pair_distance distribution" )
				
				self.ntb1 = NavigationToolbar(sc1,self)
				summarylayout.addWidget(self.ntb1)
				summarylayout.addWidget(sc1)

				self.summary_tab.addTab(summarypage,"pair distance")
				##########qii page###############
				
				summarypage2 = QtGui.QWidget()
				summarylayout2 = QtGui.QVBoxLayout(summarypage2)
				
				inputq,inputi = self.getlist(datfile)
				bestqi_file = output+"best.qii"
				bestq,besti = self.getlist(bestqi_file)

				sc2 = MyMplCanvas2(inputq,inputi,bestq,besti,"q","intensity(log)","input saxs file","best intensity file","Intensity Comparison" )
				self.ntb2 = NavigationToolbar(sc2,self)
				summarylayout2.addWidget(self.ntb2)
				summarylayout2.addWidget(sc2)

				self.summary_tab.addTab(summarypage2,"Intensity")

				self.ui.tabWidget.addTab(self.summary_tab,"summary")
			
			else:

				self.summary_tab = QtGui.QTabWidget()
				summarypage = QtGui.QWidget()
				summarylayout = QtGui.QVBoxLayout(summarypage)
				# file = output+"average.pr"
				# step_list,pr_list = self.getlist(file)

				
				file2 =output+"best.pr"
				step_list2,pr_list2 = self.getlist_pr(file2)

				file3 = output+"average.pr"
				step_list3, pr_list3 = self.getlist_pr(file3)


				
				sc1 = MyMplCanvas2(step_list2,pr_list2,step_list3,pr_list3,"step","pair distance","best pair distance","average pair distance","Pair_distance distribution" )
				
				self.ntb1 = NavigationToolbar(sc1,self)
				summarylayout.addWidget(self.ntb1)
				summarylayout.addWidget(sc1)

				self.summary_tab.addTab(summarypage,"pair distance")
				

				##########qii page###############
				
				summarypage2 = QtGui.QWidget()
				summarylayout2 = QtGui.QVBoxLayout(summarypage2)
				
				inputq,inputi = self.getlist(datfile)
				bestqi_file = output+"best.qii"
				bestq,besti = self.getlist(bestqi_file)

				sc2 = MyMplCanvas2(inputq,inputi,bestq,besti,"q","intensity(log)","input saxs file","best intensity file","Intensity Comparison" )
				self.ntb2 = NavigationToolbar(sc2,self)
				summarylayout2.addWidget(self.ntb2)
				summarylayout2.addWidget(sc2)

				self.summary_tab.addTab(summarypage2,"Intensity")

				self.ui.tabWidget.addTab(self.summary_tab,"summary")
				# self.summary_tab = QtGui.QTabWidget()
				# summarypage = QtGui.QWidget()
				# summarylayout = QtGui.QVBoxLayout(summarypage)
				# file2 =output+"average.pr"
				# step_list2,pr_list2 = self.getlist_pr(file2)
				# sc1 = MyMplCanvas11(step_list2,pr_list2,"step","pair distance","average pair distance","Pair_distance distribution" )
				# self.ntb1 = NavigationToolbar(sc1,self)
				# summarylayout.addWidget(self.ntb1)
				# summarylayout.addWidget(sc1)

				# self.summary_tab.addTab(summarypage,"pair distance")
				# self.ui.tabWidget.addTab(self.summary_tab,"summary")

			shutil.copy(self.pregxsfile,self.outdir)
			os.rename(os.path.join(self.outdir,"pregxs.txt"),os.path.join(self.outdir,"log.txt"))


		with open(self.targetfile_SAS,"w") as f:
			f.truncate()



if __name__ =="__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = PregxsApp()
	myapp.show()
	app.exec_()









