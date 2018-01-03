# SASTBX APP Document
## configuration
Platform：MAC   
Packaged software: pyinstaller  
Programming language：pyqt4

**About the selection of programming language：**
swift is the most commonly used language for the development of mac app, and jave is the most popular language for cross-platform application. This two language maight be more professional choice for the app development. 
## Compile SASTBX with the latest version of CCTBX
Download CCTBX from <http://cci.lbl.gov/cctbx_build/>




## Quick start in sastbx
If you want to know the functions of a class in sastbx, the most convenient method is using dir(class_name) in sastbx.python, here is an example:
![comparison](/Users/Song/Downloads/cctbx/gui/sasqt/md_resource/example.png)
all the function will be listed in a list.

##Traps in packaging the software
As for the packaged software for python:
![comparison](/Users/Song/Downloads/cctbx/gui/sasqt/md_resource/comparison.png)

bbFreeze, pyInstaller, cx_Freeze and py2app can be used on OSX platform. And the documents of pyInsaller and cx_Freeze is more complete. Recommending you to use these two tools.
I use pyInstaller to packag the software.

###Do not open a file without its absolute path in your project

If you write or read a file without absolute path in your project, it works well with console. But when you try to package the project into one file as an app, you can not find any error here but the app just has no response. Beacuse the app's work path is the root directory, no matter where you store this app.

**Solution:**
Try to get the absolute path you need form gui.
And write the file in an appropriate space.

###Deal with the program runs for a long time which makes the app looks like no response
Running a long time program, the gui will looks like no response.
When a program's run time is pretty long and the time is not exact, it is different with copy or paste program which is actually a for loop and can be indicated by a progressbar or progresswidget.

**Solution:**
In this project, the long time used program is called by subprocess Popen.  We use the real-time log output to show the program is running.

```
out = subprocess.Popen(shlex.split(command),stdout=sys.stdin,shell=False)
```
here, out is a address in memory, so you can get it and get its change. You can add a new thread to get the change of this change.

Output every line in out to GUI directly is invalid.
Since adding text to the GUI (eg. ```textBrowser.append```)is blocking.

And ```read```,```readline```,```readlines```,```write```,etc are all blocking, so even if you try to get the changes in the log in another thead, you will still get the complete log at the end of the program running.

So, here we redirect the output from sys.out to a log in all the scripts in the project. In a thread, we run the program and write to a log and close the log after writing every time avoid of blocking, and in the end write an end identifying. In another thread, we try to open and read the log, distinguishs the new change, if there is something new add to the log, we read out it add to GUI, and flush the corresponding tool in the GUI, when read the end identifying, end the listening.

Another attention:
Since  ```read``` and  ```write``` are blocking,and  write and read is not one to one correspondence, so the threading may compete for resources, thread conflict will makes the program down. So, when write to the log in the program, use ```with open ``` instead ```open``` . And take care of open and close file in read an write thread.

Here gives an example in the program:

* Read thread

```
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
					self.ui.shapeup_textBrowser.append(sentence)
					QtCore.QCoreApplication.processEvents()
				buff = lines
```
* Write thread

```
def run(self, command):
		import sys
		subprocess.Popen(shlex.split(command),stdout=sys.stdin,shell=False)

```
* Join

```
import threading
	t = []
	t.append(threading.Thread(target=self.run(command)))
	t.append(threading.Thread(target=self.read()))
	for t1 in t:
		t1.setDaemon(True)
		t1.start()
		t1.join()
```
### import packages can not be found by pyinstaller although using -p to indicate
Although you use **-p $PATH** to force indicate the import package which can not package directly by pyinstaller, It is still no use.

**Solution:**
Add **--hidden-import PackegeName** and  **-p $PATH** to indicate this packege.


##Other Attentions
###Take care of app's robustness
* invalid inputs

	* examine suffix of the file.
	* examine whether the path of the file exist.
* the validity of the file content
	* use a light and quick program to examine the content of the file(eg. build_map to examine whether a pdb file content is right)
* users running the same project many times

	* Uplate the log and the module in GUI.

###Output file
* store the output files in a place where the user preference.
* Show the result in a proper way.
	* Show the iq and pr file with matplotlib.
	


	
	


 







