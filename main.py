import os
import eel

import sys
sys.path.append('engine\features.py')


eel.init("www")

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)