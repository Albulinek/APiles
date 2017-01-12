import sys
import pickle
import subprocess
import os.path
import re
from xml.etree import ElementTree as ET


# Start at ui/
# This code was provided by bc.Ladislav Dobrovský

ui_files = ['main', 'start', 'mainMasopust']
rc_files = ['icons']

path = sys.exec_prefix + '\\Scripts'

isForce = False
# isForce = True

# UIC\
"""
try:
    inFile = open('ui/.uiModifiyTimes', 'rb')
    modifyTimes = pickle.load(inFile)
    inFile.close()
except FileNotFoundError:
    modifyTimes = dict()

for ui_file in ui_files:
    filename = "ui/" + ui_file + ".ui"
    filenamePy = "ui/" + ui_file + ".py"
    mTime = os.path.getmtime(filename)

    if (filename in modifyTimes and mTime > modifyTimes[filename]) or not (filename in modifyTimes) or isForce:
        print('calling uic on', filename)
        if sys.platform == "win32":
            subprocess.call([path + "\\pyside-uic.exe", filename, "-o", filenamePy])
        else:
            subprocess.call(['/usr/bin/pyside-uic', filename, "-o", filenamePy])

    modifyTimes[filename] = mTime

for rc_file in rc_files:
    filename = "ui/"+rc_file+".qrc"
    # p = re.compile('.*\/(.*)')
    # rc_filePy = str(p.match(rc_file))
    # print(rc_filePy)
    filenamePy = rc_file+"_rc.py"
    mTime = os.path.getmtime(filename)

    if (filename in modifyTimes and mTime > modifyTimes[filename]) or not (filename in modifyTimes) or isForce:
        print('calling rcc on', filename)
        if sys.platform == "win32":
            path = sys.exec_prefix+'\\Lib\\site-packages\\PySide'
            subprocess.call([path + "\\pyside-rcc.exe", "-py3", filename, "-o", filenamePy])
        else:
            subprocess.call(['/usr/bin/pyrcc4', filename, "-o", filenamePy, "-py3"])

    modifyTimes[filename] = mTime

# save modification times
with open('ui/.uiModifiyTimes', 'wb') as output:
    pickle.dump(modifyTimes, output, 2)
"""