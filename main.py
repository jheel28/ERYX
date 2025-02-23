import os
import eel

eel.init("frontend")
os.system('start msedge.exe --app="http://localhost:5500/index.html"')
eel.start('index.html', mode=None, host='localhost', port=5500)