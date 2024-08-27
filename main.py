import os
import eel


from engine._pycache_.features import *
from engine._pycache_.command import *


eel.init("www")

playAssistantSound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)