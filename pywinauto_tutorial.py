import time
from pywinauto.application import Application

app = Application(backend="uia").start("notepad.exe")
app.UntitledNotepad.type_keys("%FX")
time.sleep(10)