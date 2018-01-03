#!/usr/bin/python
from PyQt4 import QtCore
from PyQt4 import QtGui
#superpose.py generate from superpose.ui
from superpose import Ui_Superpose
import sys
import subprocess
import shlex
import os
import shutil
import result_table
from filecontentmain import FileContentApp
from helpDocumentmain import helpDocumentApp
from preferencemain import PreferenceApp



############zernike_model/zalign.py################
#############Here maybe for the packaged file.....############
############But I'm not sure now.....##############

########run with console: this base is the same with base in homemain.py###########
base = sys.path[0]
#base = str(os.path.split(sys.path[0])[0])

# base = sys.path[0]
# print "base: ", base

class SuperposeApp(QtGui.QMainWindow,Ui_Superpose,QtCore.QEvent):
	def __init__(self,targetdir,parent=None):
		#super(SuperposeApp, self).__init__(parent)
		QtGui.QWidget.__init__(self,parent)

		self.ui = Ui_Superpose()
		self.ui.setupUi(self)
		self.preference = PreferenceApp()
		self.index_run = 0
		self.index_show = 0
		self.ui.Superpose_actionQuit.triggered.connect(self.projectClose)
		self.ui.actionShow.triggered.connect(self.show_pml)
		self.ui.Superpose_actionRun.triggered.connect(self.superpose)
		self.ui.superpose_tabWidget.setCurrentIndex(0)
		self.ui.Superpose_fix_pushButton.connect(self.ui.Superpose_fix_pushButton, QtCore.SIGNAL(( "clicked()" )),self.openfile_fix)
		self.ui.Superpose_mov_pushButton.connect(self.ui.Superpose_mov_pushButton, QtCore.SIGNAL(( "clicked()" )), self.openfile_mov)
		self.ui.superpose_statusbar.showMessage('Small Angle Scattering ToolBox  1.0.0                                Model Superposition')
		self.targetdir = targetdir
		self.icon1 = QtGui.QIcon()
		self.icon1.addPixmap(QtGui.QPixmap(":/image/imge/superpose.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)       
		self.superpose_toolButton = QtGui.QToolButton()
		self.superpose_toolButton.setObjectName('superpose')
		self.superpose_toolButton.setText("Model Superposition")
		#self.superpose_toolButton.setStyleSheet("font-size:30px;background-color:rgb(217,193,153,104);\
        #    :border 2pxsolid #333333")
		#self.superpose_toolButton.setStyleSheet("font-size:30px")
		#self.superpose_toolButton.setText("Superpose models at low resolutions")
		self.superpose_toolButton.setIcon(self.icon1)
		self.superpose_toolButton.setIconSize(QtCore.QSize(300,80))
		self.superpose_toolButton.setAutoRaise(True)
		self.superpose_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		
		self.ui.Superpose_actionQuit.triggered.connect(self.buttonClose)
		self.superpose_toolButton.connect(self.superpose_toolButton,QtCore.SIGNAL(( "clicked()" )),self.setwindowtop)
		
		self.icon2 = QtGui.QIcon()
		self.icon2.addPixmap(QtGui.QPixmap(":/image/imge/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)       
		self.project_toolButton = QtGui.QToolButton()
		self.project_toolButton.setText("CLOSE")
		#self.superpose_toolButton.setText("Superpose models at low resolutions")
		self.project_toolButton.setIcon(self.icon2)
		self.project_toolButton.setIconSize(QtCore.QSize(100,80))
		self.project_toolButton.setAutoRaise(True)
		self.project_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		
		self.result_table = result_table.SongTable()
		self.result_button = QtGui.QPushButton("show in pymol",self)
		self.result_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/image/imge/pymol.png")))
		self.result_button.setStyleSheet(""" 
		                background:gray;
		                """)

		self.result_button2 = QtGui.QPushButton("View the Content", self)
		self.result_button2.setIcon(QtGui.QIcon(QtGui.QPixmap(":/image/imge/directory.png")))
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
		self.helpDocument = helpDocumentApp()

		self.ui.Superpose_actionHelp.triggered.connect(self.helpDocumentShow)

		self.project_toolButton.connect(self.project_toolButton, QtCore.SIGNAL(( "clicked()" )), self.projectClose)
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
			out = open(self.superposedir,"r")
			lines = out.readlines()
			out.close()
			if lines!=buff:
				for sentence in lines:
					if sentence in buff:
						continue
					if sentence=='__END__':
						return
					self.ui.superpose_textBrowser.append(sentence)
					QtCore.QCoreApplication.processEvents()
				buff = lines
	
	def projectClose(self):
		self.project_toolButton.setParent(None)
		self.superpose_toolButton.setParent(None)
		self.close()

	def closeEvent(self, QCloseEvent):
		self.projectClose()

	def setwindowtop(self):
		self.hide()
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		self.show()

	def buttonClose(self):
		self.superpose_toolButton.setParent(None)

	def openfile_fix(self):
		self.filename=QtGui.QFileDialog(self).getOpenFileName()
		if os.path.isfile(self.filename):
			self.ui.Superpose_fix_lineEdit.setText(self.filename)
		fixfile = str(self.ui.Superpose_fix_lineEdit.displayText()).strip()
		typefix = str(fixfile.split(".")[-1]).strip()
		print typefix
		if (typefix!="pdb") and (typefix!="ent"):
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			msgBox.setText("The input file is invalid,please input a PDB file")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False
		


	def openfile_mov(self):
		self.filename=QtGui.QFileDialog(self).getOpenFileName()
		if os.path.isfile(self.filename):
			self.ui.Superpose_mov_lineEdit.setText(self.filename)

		movfile = str(self.ui.Superpose_mov_lineEdit.displayText()).strip()
		typemov = str(movfile.split(".")[-1])
		if typemov!="pdb" and typemov!="ent":
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			
			msgBox.setText("The input file is invalid,please input a PDB file")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False

	def run(self, command):
		import sys
		subprocess.Popen(shlex.split(command),stdout=sys.stdin,shell=False)

	

	def superpose(self):
		self.index_run += 1
		SASTBXpathfile = os.path.join(base,"SASTBXpath.txt")
		with open(SASTBXpathfile,"r") as f1:
			self.SASTBXpath = f1.read().strip()
		env = str(os.path.join(self.SASTBXpath, 'build', 'bin'))+ ':'
		##############Here add SASTBX101#############
		self.targetfile_SAS = os.path.join(self.SASTBXpath,"modules","cctbx_project","sastbx","targetpath_GUI.txt")
		with open(self.targetfile_SAS,"w") as f:
			print >> f, self.targetdir
		print "content in targetpath_GUI:", self.targetdir
		os.environ['PATH'] = env+os.environ['PATH']
		self.ui.superpose_textBrowser.clear()
		fixfile = str(self.ui.Superpose_fix_lineEdit.displayText()).strip()
		movfile = str(self.ui.Superpose_mov_lineEdit.displayText()).strip()
		nmax = str(self.ui.Superpose_nmax_comboBox.currentText()).strip()
		write_map = str(self.ui.writemap_comboBox.currentText()).strip()

		#targetdir = self.targetdir
		if fixfile=='' or movfile=='':
			msgBox = QtGui.QMessageBox()
			msgBox.setTextFormat(QtCore.Qt.RichText)
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			msgBox.setText("Please input the models")
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Ok:
				return False
		else:
			for file in fixfile,movfile:
				typefile = str(file.split(".")[-1])
				if typefile!="pdb" and typefile!="ent":
					msgBox = QtGui.QMessageBox()
					msgBox.setTextFormat(QtCore.Qt.RichText)
					msgBox.setIcon(QtGui.QMessageBox.Critical)
					
					msgBox.setText("The input file is invalid,please input a PDB file")
					msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
					ret = msgBox.exec_()
					if ret == QtGui.QMessageBox.Ok:
						return False
				if os.path.exists(file)==False:
					msgBox = QtGui.QMessageBox()
					msgBox.setTextFormat(QtCore.Qt.RichText)
					msgBox.setIcon(QtGui.QMessageBox.Critical)
					
					msgBox.setText("The file is is not exist")
					msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
					ret = msgBox.exec_()
					if ret == QtGui.QMessageBox.Ok:
						return False

			command = "sastbx.superpose"
			command = command+" fix=%s" %fixfile
			typef = str(fixfile.split(".")[-1])
	 		command = command+" typef=%s" %str(typef)
			command = command+ " mov=%s" %movfile
			typem = str(movfile.split(".")[-1])
			command = command+" typem=%s" %typem

			print "self.targetdir: ",self.targetdir
			if (typef=="pdb" or typef=="ent" ) and (typem=="pdb" or typem=="ent"):
				if os.path.isdir(os.path.join(self.targetdir,"Model_Superposition"))==False:
					os.mkdir(os.path.join(self.targetdir,"Model_Superposition"))
				self.posedir = os.path.join(self.targetdir,"Model_Superposition")


				##########copy input file to the output dir"##########
				shutil.copy(fixfile,self.posedir)
				shutil.copy(movfile,self.posedir)
				###############################################
				self.movie_screen = QtGui.QLabel()
				self.movie_screen.setText("The program is running, please wait about 2 seconds")		
				self.ui.superpose_tabWidget.setCurrentIndex(2)
				self.progdialog = QtGui.QProgressDialog(self)
				self.progdialog.setWindowTitle("Renaming Archives")
				self.progdialog.setWindowModality(QtCore.Qt.WindowModal)
				self.progdialog.setLabel(self.movie_screen)		
				self.progdialog.show()
				command = command+" nmax=%s" %str(nmax)
				command = command+" write_map=%s" %str(write_map)
				#self.superposedir = os.path.join(self.targetdir,"Model_Superposition","temp.txt")
				self.superposedir = os.path.join(self.SASTBXpath,"modules","cctbx_project","sastbx","superpose.txt")

				self.superpose_pml = os.path.join(self.targetdir,"Model_Superposition","superpose.pml")
				#command = command+" output=%s" %str(self.superposedir)

				#self.ui.superpose_tabWidget.setCurrentIndex(2)
				iner = open(self.superposedir,"w")
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
				#child1 = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE,shell=False)
				# child2 = subprocess.Popen(shlex.split(command),stdin=child1.stdout,stdout=subprocess.PIPE,shell=False)
				'''
				out = child1.communicate()
				result = str(out[0])
				# result = str(str(out[0]).split("#############")[2])
				# result = str(result.split("output")[0])
				explainStr = "The result files are saved in the following directory"
				self.ui.superpose_textBrowser.append(explainStr)
				self.ui.superpose_textBrowser.append(os.path.join(targetdir,"superpose"))
				self.ui.superpose_textBrowser.append(result)
				#child2 = subprocess.Popen(shlex.split(command),stdin=child1.stdout,stdout=subprocess.PIPE,shell=False)	
				# time2 = time.time()
				'''
				if self.ui.superpose_tabWidget.count()==4:
					self.ui.superpose_tabWidget.removeTab(3)
				filename_list = []
				with open(self.superposedir,"r") as f:
					tempf = f.read().split("OUTPUT files are : ")[-1]
					tempf = tempf.split("#############     END of SUMMARY     #############")[0]
					filename_list = tempf.split()



				for ii, file in enumerate(filename_list):
					file_type = file.split(".")[-1]
					file_size = '%.1fkb' %(os.path.getsize(file)/1024)
					self.result_table.setRowData(ii,[file,file_type,file_size])
				


				self.ui.superpose_tabWidget.addTab(self.result_widget,"result")
				self.ui.superpose_tabWidget.setCurrentIndex(2)
				self.progdialog.close()


				shutil.copy(self.superposedir,self.posedir)
				os.rename(os.path.join(self.posedir,"superpose.txt"),os.path.join(self.posedir,"log.txt"))

				#############add tablewidget to show page###########
	
	

				# self.summary_tab = QtGui.QTabWidget()
				# summarypage = QtGui.QWidget()
				# summarylayout = QtGui.QVBoxLayout(summarypage)

				# result_dir = os.path.join(self.targetdir,"superpose")
				# pml_file = os.path.join(result_dir,"pymol.pml")

				# os.system("pymol %s" %parameter)
				

					

				# file = output+"average.pr"
				# step_list,pr_list = self.getlist(file)

				# file2 =output+"best.pr"
				# step_list2,pr_list2 = self.getlist(file2)

				# sc1 = MyMplCanvas2(step_list,pr_list,step_list2,pr_list2,"step","pair distance","average pair distance","best pair distance","Pair_distance distribution" )
				# self.ntb1 = NavigationToolbar(sc1,self)



				# summarylayout.addWidget(self.ntb1)
				# summarylayout.addWidget(sc1)

				# self.summary_tab.addTab(summarypage,"show pdb")
				# ##########qii page###############

				# self.ui.superpose_tabWidget.addTab(self.summary_tab,"summary")

		
			else:
				msgBox = QtGui.QMessageBox()
				msgBox.setTextFormat(QtCore.Qt.RichText)
				msgBox.setIcon(QtGui.QMessageBox.Critical)
				
				msgBox.setText("File format error! The format of models must be pdb or ent")
				msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
				ret = msgBox.exec_()
				if ret == QtGui.QMessageBox.Ok:
					return False
		with open(self.targetfile_SAS,"w") as f:
			f.truncate()

	def show_pml(self):
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

		self.superpose_pml = os.path.join(self.targetdir,"Model_Superposition","superpose.pml")
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

			command = command +" "+self.superpose_pml

			try:
			
				#os.system("pymol")
				#command  = "open -a /Applications/WeChat.app"
				#command = "open -a /Users/Song/Desktop/MacPyMOL.app"
				##############This command is applicatable but Pymol can not open with out packages###############
				##############so try the pml script in pymol app then package them###############
				#command = "open -a /Users/Song/Desktop/MacPyMOL.app /Applications/SASTBX1.0.0/gui/sasqt/test.pml"
				
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
		typefile = filename.split(".")[-1]
		purename = str(filename.split(".")[0]).split('/')[-1]
		if typefile=="pdb":
			name = filename.split(".")[0]+".pml"
			name = str(name)
			self.pdb_pml = os.path.join(self.targetdir,"Model_Superposition",name)
			with open(self.pdb_pml,"w") as f:
				print >>f , "load %s" %filename
				print >>f , "show cartoon"
		elif typefile=="xplor":
			name = filename.split(".")[0]+".pml"
			name = str(name)
			self.pdb_pml = os.path.join(self.targetdir,"Model_Superposition",name)
			with open(self.pdb_pml,"w") as f:
				print >>f, "load %s, %s" %(filename,purename)
				print >>f, "volume %s, %s" %(str(purename+"_volume"), purename)
		else:
			self.pdb_pml = ''
		
		return self.pdb_pml


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
				#command = "source "
				command = self.pymolpath

	
			if len(self.item_list)>0:
				self.pdb_pml = self.write_pml(self.item_list[0])
				print "self.pdb_pml:" ,self.pdb_pml

				try:
					#command = "open -a "
					#command = command + self.pymolpath
					command = command +" "+self.pdb_pml
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
					
	                

if __name__ =="__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = SuperposeApp()
	myapp.show()
	app.exec_()