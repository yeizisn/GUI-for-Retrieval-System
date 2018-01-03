cd /System/Library/Frameworks/Python.framework/Versions/2.7/bin
#./pyuic4 -o /Users/Song/sastbx/gui/sasqt/superpose.py /Users/Song/sastbx/gui/sasqt/superpose.ui
./pyrcc4 -o /Users/Song/sastbx/gui/sasqt/resource_rc.py /Users/Song/sastbx/gui/sasqt/resource.qrc


python /Library/Python/2.7/site-packages/PyQt4/uic/pyuic.py -x superpose.ui -o superpose.py
