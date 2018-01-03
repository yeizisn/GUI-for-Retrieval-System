
rm -rf /Applications/SASTBX101/gui/sasqt/homemain/
rm -rf /Applications/SASTBX101/gui/sasqt/homemain.spec
rm -rf /Applications/SASTBX101/gui/sasqt/build/
rm -rf /Applications/SASTBX101/gui/sasqt/homemain.app

pyinstaller-2.7  -y $1  --distpath="." \
 -p "/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages" \
    -i "/Applications/SASTBX101/gui/sasqt/molecule.icns" \
    /Applications/SASTBX101/gui/sasqt/homemain.py




cp -r /Applications/SASTBX101/gui/sasqt/doc /Applications/SASTBX101/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX101/gui/sasqt/pictures /Applications/SASTBX101/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX101/gui/sasqt/sastbx_examples /Applications/SASTBX101/gui/sasqt/homemain.app/Contents/
