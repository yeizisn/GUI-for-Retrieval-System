from PyQt4 import QtGui 
from PyQt4 import QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib
from show import Ui_MainWindow


font = {'family' : 'serif',  
        'color'  : 'darkred',  
        'weight' : 'normal',  
        'size'   : 20,  
        } 

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self,q_list,logi_list, parent=None, width=7, height=7, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)

        #self.compute_initial_figure()

        self.q_list = q_list
        
        self.logi_list = logi_list
        #self.sigma_list = sigma_list
        self.compute_initial_figure()
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def compute_initial_figure(self):
        q = self.q_list
        i = self.logi_list
        #sigma =self.sigma_list
        qi_line, = self.axes.plot(q,i,color="lightcoral",linestyle='-',linewidth=2.0,label="q-Intensity(log)")
        #qs_line, = self.axes.plot(q,sigma,color="red",linestyle='-',linewidth=2.0,label="q-sigma")

        #.axes.plot(t, s)
        self.axes.grid(True, color='gray')
        self.axes.set_xlabel("q")
        self.axes.set_ylabel('intensity(log)')
        self.axes.legend(handles=[qi_line])

class MyMplCanvas1(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self,q_list,logi_list, parent=None, width=7, height=7, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)

        #self.compute_initial_figure()

        self.q_list = q_list
        self.logi_list = logi_list
        #self.sigma_list = sigma_list
        self.compute_initial_figure()
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def compute_initial_figure(self):
        q = self.q_list
        i = self.logi_list
        #sigma =self.sigma_list
        qi_line, = self.axes.plot(q,i,color="lightcoral",linestyle='-',linewidth=2.0,label="q-Intensity(log)")
        #qs_line, = self.axes.plot(q,sigma,color="red",linestyle='-',linewidth=2.0,label="q-sigma")

        #.axes.plot(t, s)
        self.axes.grid(True, color='gray')
        self.axes.set_xlabel("q")
        self.axes.set_ylabel('intensity(log)')
        self.axes.set_title("Q-Intensity Curve")
        self.axes.legend(handles=[qi_line])


class MyMplCanvas2(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self,q_list,logi_list,q_list2,logi_list2,x_label,y_label,label1,label2,title, parent=None, width=7, height=7, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)

        #self.compute_initial_figure()

        self.q_list = q_list
        self.logi_list = logi_list
        self.q_list2 = q_list2
        self.logi_list2 = logi_list2
        self.label1 = label1
        self.label2 = label2
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        #self.sigma_list = sigma_list
        self.compute_initial_figure()
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def compute_initial_figure(self):
       
        qi_line, = self.axes.plot(self.q_list,self.logi_list,color="lightcoral",linestyle='-',linewidth=2.0,label=self.label1)
        #qs_line, = self.axes.plot(q,sigma,color="red",linestyle='-',linewidth=2.0,label="q-sigma")
        qi_line2, = self.axes.plot(self.q_list2,self.logi_list2,color="blue",linestyle='-',linewidth=2.0,label=self.label2)

        #.axes.plot(t, s)
        self.axes.grid(True, color='gray')
        self.axes.set_xlabel(self.x_label)
        self.axes.set_ylabel(self.y_label)
        self.axes.set_title(self.title)
        self.axes.legend(handles=[qi_line,qi_line2])


class MyMplCanvas11(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self,q_list,logi_list,x_label,y_label,label,title, parent=None, width=7, height=7, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)

        #self.compute_initial_figure()

        self.q_list = q_list
        self.logi_list = logi_list
        
        self.label = label
       
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        #self.sigma_list = sigma_list
        self.compute_initial_figure()
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def compute_initial_figure(self):
       
        qi_line, = self.axes.plot(self.q_list,self.logi_list,color="lightcoral",linestyle='-',linewidth=2.0,label=self.label)
        #qs_line, = self.axes.plot(q,sigma,color="red",linestyle='-',linewidth=2.0,label="q-sigma")

        #.axes.plot(t, s)
        self.axes.grid(True, color='gray')
        self.axes.set_xlabel(self.x_label)
        self.axes.set_ylabel(self.y_label)
        self.axes.set_title(self.title)
        self.axes.legend(handles=[qi_line])


class MyMplCanvas3(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self,q_list,logi_list,q_list2,logi_list2,q_list3,logi_list3,x_label,y_label,label1,label2,label3,title, parent=None, width=7, height=7, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)

        #self.compute_initial_figure()

        self.q_list = q_list
        self.logi_list = logi_list
        self.q_list2 = q_list2
        self.logi_list2 = logi_list2
        self.q_list3 = q_list3
        self.logi_list3 = logi_list3
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        #self.sigma_list = sigma_list
        self.compute_initial_figure()
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def compute_initial_figure(self):
       
        qi_line, = self.axes.plot(self.q_list,self.logi_list,color="gray",linestyle='-',linewidth=1.5,label=self.label1)
        #qs_line, = self.axes.plot(q,sigma,color="red",linestyle='-',linewidth=2.0,label="q-sigma")
        qi_line2, = self.axes.plot(self.q_list2,self.logi_list2,color="royalblue",linestyle='-',linewidth=1.5,label=self.label2)
        qi_line3, = self.axes.plot(self.q_list3,self.logi_list3,color="orange",linestyle='-',linewidth=1.5,label=self.label3)

        #.axes.plot(t, s)
        self.axes.set_xlabel(self.x_label)
        self.axes.set_ylabel(self.y_label)
        self.axes.set_title(self.title)
        self.axes.grid(True, color='gray')
        self.axes.legend(handles=[qi_line,qi_line2,qi_line3])

class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self,q_list,logi_list):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_menu = QtGui.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)
        self.help_menu = QtGui.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)
        self.help_menu.addAction('&About', self.about)

        self.ui.main_widget = QtGui.QTextBrowser(self)
        self.q_list = q_list
        self.logi_list = logi_list
        #self.sigma_list = sigma_list


        l = QtGui.QVBoxLayout(self.ui.main_widget)
        sc = MyMplCanvas(self.q_list,self.logi_list,self.ui.main_widget)
        #sc = MyStaticMplCanvas(self.main_widget,q_list,logi_list,sigma_list, width=5, height=4, dpi=100)
        #dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        self.ntb = NavigationToolbar(sc,self)
        l.addWidget(self.ntb)
        l.addWidget(sc)
        #l.addWidget(dc)

        self.ui.main_widget.setFocus()
        self.setCentralWidget(self.ui.main_widget)

        self.statusBar().showMessage("Small Angle Scattering ToolBox  1.0.0                   Q-Intensity Curve")

        self.ui.actionQuit.triggered.connect(self.close)
      


    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtGui.QMessageBox.about(self)




if __name__ =="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ApplicationWindow()
    myapp.show()
    app.exec_()