from tkinter import *
from Design import fullscreen
from Design.clean import clean
from partials import fileManager as fm
from partials import editScreen
# Screens >>>
from partials import firstScreen
from partials import secondScreen
#__main__
History = []
window = Tk()
fullscreen.make(window)
secondScreen.fm = fm
secondScreen.editScreen = editScreen
firstScreen.render(window,History,clean,lambda : secondScreen.render(window,History))
# secondScreen.render(window,History)
window.mainloop()
