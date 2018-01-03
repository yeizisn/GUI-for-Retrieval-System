



rm -rf /Applications/SASTBX1.0.1/gui/sasqt/homemain/
rm -rf /Applications/SASTBX1.0.1/gui/sasqt/homemain.spec
rm -rf /Applications/SASTBX1.0.1/gui/sasqt/build/
rm -rf /Applications/SASTBX1.0.1/gui/sasqt/homemain.app

pyinstaller-2.7  -y $1  --distpath="." \
 -p "/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages" \
    -i "/Applications/SASTBX1.0.1/gui/sasqt/molecule.icns" \
    /Applications/SASTBX1.0.1/gui/sasqt/homemain.py




cp -r /Applications/SASTBX1.0.1/modules /Applications/SASTBX1.0.1/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX1.0.1/build /Applications/SASTBX1.0.1/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX1.0.1/gui/sasqt/doc /Applications/SASTBX1.0.1/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX1.0.1/gui/sasqt/pictures /Applications/SASTBX1.0.1/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX1.0.1/gui/sasqt/sastbx_examples /Applications/SASTBX1.0.1/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX1.0.1/base /Applications/SASTBX1.0.1/gui/sasqt/homemain.app/Contents/
