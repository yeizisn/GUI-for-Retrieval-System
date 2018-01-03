#!/usr/bin/python
# use PyQt to play an animated gif
# added buttons to start and stop animation
# tested with PyQt4.4 and Python 2.5
# also tested with PyQt4.5 and Python 3.0
# vegaseat

import sys 
# too lazy to keep track of QtCore or QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import * 

class MoviePlayer(QWidget): 
    def __init__(self, parent=None,command): 
        QWidget.__init__(self, parent) 
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("QMovie to show animated gif")
        
        # set up the movie screen on a label
        self.movie_screen = QLabel()
        # expand and center the label 
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, 
            QSizePolicy.Expanding)        
        self.movie_screen.setAlignment(Qt.AlignCenter) 

        btn_start = QPushButton("Start Animation")
        self.connect(btn_start, SIGNAL("clicked()"), self.start) 

        btn_stop = QPushButton("Stop Animation")
        self.connect(btn_stop, SIGNAL("clicked()"), self.stop)        

        main_layout = QVBoxLayout() 
        main_layout.addWidget(self.movie_screen)
        main_layout.addWidget(btn_start) 
        main_layout.addWidget(btn_stop)
        self.setLayout(main_layout) 
                
        # use an animated gif file you have in the working folder
        # or give the full file path
        self.movie = QMovie("try.gif", QByteArray(), self) 
        self.movie.setCacheMode(QMovie.CacheAll) 
        self.movie.setSpeed(100) 
        self.movie_screen.setMovie(self.movie) 
        #self.movie.start()
        self.comd = command
        
    def start(self):
        """sart animnation"""
        command = self.comd
        self.movie.start()
        child1 = subprocess.Popen(shlex.split(command),stdout=subprocess.PIPE,shell=False)
        child2 = subprocess.Popen(shlex.split(command),stdin=child1.stdout,stdout=subprocess.PIPE,shell=False)
        out = child2.communicate()
        result = str(str(out[0]).split("#############")[2])
        self.result = str(result.split("output")[0])
        self.movie.stop()
        
    def result(self):
        """stop the animation"""
        return self.result


# app = QApplication(sys.argv) 
# player = MoviePlayer() 
# player.show() 
# sys.exit(app.exec_())