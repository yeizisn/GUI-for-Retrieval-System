# rm -rf /Users/Song/sastbx/gui/sasqt/homemain/
# rm -rf /Users/Song/sastbx/gui/sasqt/homemain.spec
# rm -rf /Users/Song/sastbx/gui/sasqt/build/
# rm -rf /Users/Song/sastbx/gui/sasqt/homemain.app

# pyinstaller -y $1  --distpath="." \
# 	--hidden-import matplotlib \
# 	-p "/usr/local/opt/pymol/libexec/lib/python2.7/site-packages" \
# 	-i "/Users/Song/sastbx/gui/sasqt/molecule.icns" \
# 	/Users/Song/sastbx/gui/sasqt/homemain.py

# cp -r /Users/Song/sastbx/source /Users/Song/sastbx/gui/sasqt/homemain.app/Contents/
# cp -r /Users/Song/sastbx/build /Users/Song/sastbx/gui/sasqt/homemain.app/Contents/

rm -rf /Applications/SASTBX1.0.0/gui/sasqt/homemain/
rm -rf /Applications/SASTBX1.0.0/gui/sasqt/homemain.spec
rm -rf /Applications/SASTBX1.0.0/gui/sasqt/build/
rm -rf /Applications/SASTBX1.0.0/gui/sasqt/homemain.app

pyinstaller -y $1  --distpath="." \
	--hidden-import matplotlib \
	-p "/usr/local/opt/pymol/libexec/lib/python2.7/site-packages" \
	-i "/Applications/SASTBX1.0.0/gui/sasqt/molecule.icns" \
	/Applications/SASTBX1.0.0/gui/sasqt/homemain.py

cp -r /Applications/SASTBX1.0.0/modules /Applications/SASTBX1.0.0/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX1.0.0/build /Applications/SASTBX1.0.0/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX1.0.0/gui/sasqt/doc /Applications/SASTBX1.0.0/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX1.0.0/gui/sasqt/pictures /Applications/SASTBX1.0.0/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX1.0.0/gui/sasqt/sastbx_examples /Applications/SASTBX1.0.0/gui/sasqt/homemain.app/Contents/
cp -r /Applications/SASTBX1.0.0/base /Applications/SASTBX1.0.0/gui/sasqt/homemain.app/Contents/
