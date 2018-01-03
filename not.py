1.Qt Designer位置：/Developer/Applications/Qt
2.pyuic
位置：/Library/Python/2.7/site-packages/PyQt4/uic/pyuic.py
使用：python pyuic.py -x a.ui -o a.py
python /Library/Python/2.7/site-packages/PyQt4/uic/pyuic.py -x homepage.ui -o homepage.py
3./System/Library/Frameworks/Python.framework/Versions/2.7/bin
下面是有pyuic4 pyrcc等


python /Library/Python/2.7/site-packages/PyQt4/uic/pyuic.py -x homepage.ui -o homepage.py

python /Library/Python/2.7/site-packages/PyQt4/uic/pyuic.py -x shapeup.ui -o shapeup.py

python /Library/Python/2.7/site-packages/PyQt4/uic/pyuic.py -x pregxs.ui -o pregxs.py

python /Library/Python/2.7/site-packages/PyQt4/uic/pyuic.py -x she.ui -o she.py

python /Library/Python/2.7/site-packages/PyQt4/uic/pyuic.py -x Superpose.ui -o superpose.py

4. pymol 
/usr/local/Cellar/pymol/1.8.4.0/libexec/lib/python2.7/site-packages/pymol
5. matplotlib
/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
/usr/local/Cellar/matplotlib/2.0.2/lib/python2.7/site-packages

5. html
doc/example.html 338

<ul>
<li><a id="Functions" href="#">SASTBX Functions</a></li>
</ul>
<h1 id="test"><h1>
<script language="javascript">
var url = location.search;
url = url.split("?")[1].split("=")[1]
url = url+"gui.html"
// document.getElementById("test").innerHTML=url.split("?")[1].split("=")[1];
document.getElementById("Functions").href=url;
</script>

in helpdocument.html




"""
pyinstaller -y -w --distpath="." helpDocumentmain.py
cp -r /Users/Song/Downloads/cctbx/gui/sasqt/doc /Users/Song/Downloads/cctbx/gui/sasqt/helpDocumentmain.app/Contents/
"""

