from PyQt4 import QtCore
from PyQt4 import QtGui
from shapeup import Ui_Shapeup
import sys
import subprocess
import shlex
import os
import math
from saxsshow import ApplicationWindow
from helpDocumentmain import helpDocumentApp
import result_table
from filecontentmain import FileContentApp
from preferencemain import PreferenceApp
import shutil

############zernike_model/search_pdb.py################

#base = str(os.path.split(sys.path[0])[0])
base = sys.path[0]

class ShapeupApp(QtGui.QMainWindow,Ui_Shapeup,QtCore.QEvent):
	def __init__(self,targetdir,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_Shapeup()
		self.ui.setupUi(self)
		self.index_run = 0
		self.index_show = 0
		self.ui.shapeup_actionQuit.triggered.connect(self.projectClose)
		self.helpDocument = helpDocumentApp()
		self.preference = PreferenceApp()
		self.ui.shapeup_actionRun.triggered.connect(self.shapeup)
		self.ui.actionShow_maps.triggered.connect(self.showmaps)
		self.ui.shapeup_tabWidget.setCurrentIndex(0)
		self.ui.shapeup_sasfile_pushButton.connect(self.ui.shapeup_sasfile_pushButton, QtCore.SIGNAL(( "clicked()" )),self.openfile_sas)
		self.ui.shapeup_model_pushButton.connect(self.ui.shapeup_model_pushButton, QtCore.SIGNAL(( "clicked()")),self.openfile_model)
		#self.ui.shapeup_output_pushButton.connect(self.ui.shapeup_output_pushButton,QtCore.SIGNAL(( "clicked()")),self.opendir_output)
		self.ui.shapeup_saxs_showButton.connect(self.ui.shapeup_saxs_showButton,QtCore.SIGNAL(( "clicked()")),self.showsaxs)
		self.targetdir = targetdir
		self.ui.shapeup_statusbar.showMessage('Small Angle Scattering ToolBox1.0.0              Shape Search Engine')
		self.icon1 = QtGui.QIcon()
		self.icon1.addPixmap(QtGui.QPixmap(":/image/imge/shapeup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)       

		self.shapeup_toolButton = QtGui.QToolButton()
		self.shapeup_toolButton.setText("Shape Search Engine")
		self.shapeup_toolButton.setIcon(self.icon1)
		self.shapeup_toolButton.setIconSize(QtCore.QSize(300,80))
		self.shapeup_toolButton.setAutoRaise(True)
		self.shapeup_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		
		self.ui.shapeup_actionQuit.triggered.connect(self.buttonClose)
		self.shapeup_toolButton.connect(self.shapeup_toolButton,QtCore.SIGNAL(( "clicked()" )),self.setwindowtop)
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
		self.ui.shapeup_actionHelp.triggered.connect(self.helpDocumentShow)

		self.result_table = result_table.SongTable()
		self.result_button = QtGui.QPushButton("show in pymol",self)
		self.result_button.setIcon(QtGui.QIcon(":/image/imge/pymol.png"))
		self.result_button.setStyleSheet(""" 
		                background:gray;
		                """)

		self.result_button2 = QtGui.QPushButton("View the Content", self)
		self.result_button2.setIcon(QtGui.QIcon(":/image/imge/directory.png"))
		self.result_button2.setStyleSheet(""" 
		                background:gray;
		                """)

		self.button_layout = QtGui.QHBoxLayout()
		self.button_layout.addWidget(self.result_button)
		self.button_layout.addWidget(self.result_button2)

		self.button_widget = QtGui.QWidget()
		self.button_widget.setLayout(self.button_layout)


		self.result_layout = QtGui.QVBoxLayout()
		self.result_layout.addWidget(self.result_table)
		self.result_layout.addWidget(self.button_widget)
		self.result_widget = QtGui.QWidget()
		self.result_widget.setLayout(self.result_layout)

		self.filecontent = FileContentApp()
		self.result_table.table.cellClicked.connect(self.get_resultItem)
		self.result_button.connect(self.result_button,QtCore.SIGNAL(( "clicked()" )),self.view_inPymol)

		self.result_button2.connect(self.result_button2,QtCore.SIGNAL(( "clicked()" )),self.view_inDirectory)


		self.item_list = []


	def helpDocumentShow(self):
		self.helpDocument.show()


	def read(self):
		flag = True
		buff = []
		while flag:
			try:
				out = open(self.shapeupfile,"r")
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
					self.ui.shapeup_textBrowser.append(sentence)
					QtCore.QCoreApplication.processEvents()
				buff = lines
	
	def projectClose(self):
		self.project_toolButton.setParent(None)
		self.shapeup_toolButton.setParent(None)
		self.close()

	def closeEvent(self, QCloseEvent):
		self.projectClose()

	def setwindowtop(self):
		self.hide()
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		self.show()

	def buttonClose(self):
		self.shapeup_toolButton.setParent(None)


	def openfile_sas(self):
		self.filename=QtGui.QFileDialog(self).getOpenFileName()
		if os.path.isfile(self.filename):
			self.ui.shapeup_sasfile_lineEdit.setText(self.filename)
		sasfile = str(self.ui.shapeup_sasfile_lineEdit.displayText()).strip()
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
			if length<2:
				msgBox = QtGui.QMessageBox()
				msgBox.setTextFormat(QtCore.Qt.RichText)
				msgBox.setIcon(QtGui.QMessageBox.Critical)
				
				msgBox.setText("The input file is invalid,please input a SAXS file")
				msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
				ret = msgBox.exec_()
				if ret == QtGui.QMessageBox.Ok:
					return False

	def openfile_model(self):
		self.filename=QtGui.QFileDialog(self).getOpenFileName()
		if os.path.isfile(self.filename):
			self.ui.shapeup_model_lineEdit.setText(self.filename)



	# def opendir_output(self):
	# 	self.dirname=QtGui.QFileDialog(self).getExistingDirectory()
	# 	if os.path.isdir(self.dirname):
	# 		self.ui.shapeup_output_lineEdit.setText(self.dirname)	
	def run(self, command):
		import sys
		subprocess.Popen(shlex.split(command),stdout=sys.stdin,shell=False)

	def showsaxs(self):
		sasfile = str(self.ui.shapeup_sasfile_lineEdit.displayText()).strip()

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

	def shapeup(self):
		self.index_run += 1
		SASTBXpathfile = os.path.join(base,"SASTBXpath.txt")
		with open(SASTBXpathfile,"r") as f1:
			self.SASTBXpath = f1.read().strip()
		env = str(os.path.join(self.SASTBXpath, 'build', 'bin'))+ ':'
		self.targetfile_SAS = os.path.join(self.SASTBXpath,"modules","cctbx_project","sastbx","targetpath_GUI.txt")
		with open(self.targetfile_SAS,"w") as f:
			print >> f, self.targetdir
		os.environ['PATH'] = env+os.environ['PATH']

		self.ui.shapeup_textBrowser.clear()
		sasfile = str(self.ui.shapeup_sasfile_lineEdit.displayText()).strip()
		modelfile = str(self.ui.shapeup_model_lineEdit.displayText()).strip()
		namx = str(self.ui.shapeup_nmax_lineEdit.displayText()).strip()
		rmax = str(self.ui.shapeup_rmax_lineEdit.displayText()).strip()
		scan = str(self.ui.shapeup_scan_comboBox.currentText())
		buildmap = str(self.ui.shapeup_buildmap_comboBox.currentText())
		#output = str(self.ui.shapeup_output_lineEdit.displayText()).strip()

		dic = {"rmax":rmax,"nmax":namx,"scan":scan,"buildmap":buildmap,"pdb":modelfile}
		if sasfile=='':
			############################bug on msgBox#####################################
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			
			msgBox.setText("Please input the SAXS file")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False

		else:
			# with open(str(sys.path[0])+"/tmp.txt","r") as f:
			# 	project=f.read().strip()
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
				project = self.targetdir
				self.outdir=os.path.join(project,"Shape_Search_Engine")

				if os.path.isdir(self.outdir)==False:
					os.mkdir(self.outdir)

				##############copy input file to output dir###########
				shutil.copy(sasfile,self.outdir)
				if modelfile!='':
					shutil.copy(modelfile,self.outdir)
				##################################################


				filename = str(str(sasfile.split("/")[-1]).split(".")[0])
				output = os.path.join(self.outdir,filename)
			
				command = "sastbx.shapeup"
				command = command+" target=%s" %sasfile

				for key in dic:
					if(dic[key]!=''):
						command=command+" "+key+"="+dic[key]
				command = command+" prefix=%s" %output
				self.shapeupfile = os.path.join(self.SASTBXpath,"modules","cctbx_project","sastbx","shapeup.txt")
				self.ui.shapeup_tabWidget.setCurrentIndex(2)

				movie_screen = QtGui.QLabel()
				movie_screen.setText("The program is running, please wait")	
				progdialog = QtGui.QProgressDialog(self)
				progdialog.setWindowTitle("Program Running")
				progdialog.setWindowModality(QtCore.Qt.WindowModal)
				progdialog.setLabel(movie_screen)		
				progdialog.show()
				iner = open(self.shapeupfile,"w")
				iner.write("Start.")
				iner.close()

				explainStr = "The result files are saved in the following directory"
				self.ui.shapeup_textBrowser.append(explainStr)
				self.ui.shapeup_textBrowser.append(os.path.join(project,"Shape_Search_Engine"))
				
				import threading
				t = []
				t.append(threading.Thread(target=self.run(command)))
				t.append(threading.Thread(target=self.read()))
				for t1 in t:
					t1.setDaemon(True)
					t1.start()
					t1.join()


				#workThread = WorkThread(self.command)
				progdialog.close()
				if self.ui.shapeup_tabWidget.count()==4:
					self.ui.shapeup_tabWidget.removeTab(3)
				filename_list = []
				
				with open(os.path.join(self.SASTBXpath,"modules","cctbx_project","sastbx","outfilelog_shapeup.txt"),"r") as f:
					for line in f.readlines():
						filename_list.append(line.strip())



				print "filename_list: ", filename_list
				for ii, file in enumerate(filename_list):
					file_type = file.split(".")[-1]
					file_size = '%.1fkb' %(os.path.getsize(file)/1024)
					self.result_table.setRowData(ii,[file,file_type,file_size])


				self.ui.shapeup_tabWidget.addTab(self.result_widget,"result")
				self.ui.shapeup_tabWidget.setCurrentIndex(3)
		
			

				#self.ui.shapeup_tabWidget.setCurrentIndex(2)
				# workThread.run()
				# workThread.triggere.connect(progdialog.close())

				# child1 = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE,shell=False)
				# out = child1.communicate()
				# result = str(out[0])

				# explainStr = "The result files are saved in the following directory"
				# self.ui.shapeup_textBrowser.append(explainStr)
				# self.ui.shapeup_textBrowser.append(os.path.join(project,"shapeup"))
				#self.ui.shapeup_textBrowser.append(result)
					
				#self.ui.shapeup_tabWidget.setCurrentIndex(2)
				shutil.copy(self.shapeupfile,self.outdir)
				os.rename(os.path.join(self.outdir,"shapeup.txt"),os.path.join(self.outdir,"log.txt"))
		with open(self.targetfile_SAS,"w") as f:
			f.truncate()
	
	def get_resultItem(self):
		self.item_list =[]
		for item in self.result_table.table.selectedItems():
			print "item.text(): ", item.text()
			self.item_list.append(item.text())


	def view_inDirectory(self):
		self.filecontent.ui.textBrowser.clear()
		print self.item_list[0]
		if len(self.item_list)>0:
			try:
				with open(self.item_list[0],"r") as f:
					self.filecontent.ui.textBrowser.append(f.read())
				self.filecontent.setWindowTitle(self.item_list[0])
				self.filecontent.show()
			except Exception as e:
				print "error in "
				
		else:
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			
			msgBox.setText("Please Choose one file on the table!")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False

	def write_pml(self,filename):
		map_pml = filename.split(".")[0]+".pml"
		map_pml = str(map_pml)
		tmp_name = filename.split("/")[-1].split("_")[-1].split(".")[0]
		map_name = "map_%s" %(tmp_name)
		m_name = "m_%s" %(tmp_name)
		print "map_pml in shapeupmain: ", map_pml
		with open(map_pml,"w") as f:
			print >>f, "set bg_rgb,[1,1,1]"
			print >>f, 'load %s, %s'%(filename,map_name)
			print >> f, 'isosurface %s,%s,%s' %(m_name,map_name,str(1.0))

			
		return map_pml

	def view_inPymol(self):


		pymolpathfile = os.path.join(base,"pymolpath.txt")
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
				
				command = self.pymolpath		

			if len(self.item_list)>0:
				self.map_pml = self.write_pml(self.item_list[0])
				
				try:
					#command = "open -a "
					#command = command + self.pymolpath
					command = command + " "+self.map_pml
					print command
					process = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
					process_error =  process.stderr.read()
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

					#os.system("pymol %s" %self.item_list[0])
					#os.system("show cartoon")
				except Exception as e:
					print "no pymol found"
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
				
				msgBox.setText("Please Choose one file on the table!")
				msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
				ret = msgBox.exec_()
				if ret == QtGui.QMessageBox.Ok:
					return False
		else:
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			msgBox.setText("SASTBX couldn't locate MacPyMOL on your system\
					Please affirm the path configuration in preference is the MacPyMol path on your machine")

			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False

		                
		

	def showmaps(self):
		self.index_show +=1
		if self.index_run < self.index_show:
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			
			msgBox.setText("The Result can be seen after you run the program.")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False
		project = self.targetdir
		outdir=os.path.join(project,"Shape_Search_Engine")
		files = os.path.join(outdir,"maps.pml")
		pymolpathfile = os.path.join(base,"pymolpath.txt")
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
				
				command = self.pymolpath	
			command = command+" "+files	
			print "command: ",command
			try:
				#command = "open -a "
				#command = command + self.pymolpath

				process = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
				process_error =  process.stderr.read()
				print "process_error: ",process_error
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

				#os.system("pymol %s" %self.item_list[0])
				#os.system("show cartoon")
			except Exception as e:
				print "no pymol found"
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
			msgBox.setText("SASTBX couldn't locate MacPyMOL on your system\
					Please affirm the path configuration in preference is the MacPyMol path on your machine")

			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False


		

if __name__ =="__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = ShapeupApp()
	myapp.show()
	app.exec_()

