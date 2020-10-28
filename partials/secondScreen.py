from tkinter import *
fm = None
editScreen = None
bgcolor = "white"
fontColor = "black"
isDarkMode = False
isFullScreen = False
def askTitle(parent,history,isFirst = False):
    for i in history:
        i.pack_forget()
    history = []
    parent["bg"] = bgcolor;
    if(isFirst):
        firstNoteText = " First"
    else:
        firstNoteText = ""
    createFirstNote = Label(parent,text=f"Create{firstNoteText} Note",font=("TimesNewRoman",40),bg=bgcolor,fg = fontColor)
    history.append(createFirstNote)
    createFirstNote.pack(pady=2)

    mainFrame = Frame(parent,w=100,bg=bgcolor)
    history.append(mainFrame)

    label = Label(mainFrame,text = "Title",font=("TimesNewRoman",20),bg=bgcolor,fg = fontColor)
    label.pack(side=LEFT,padx=2)

    entry = Entry(mainFrame,text = "Create",bg=bgcolor,font=("TimesNewRoman",20),bd=0.5,fg = fontColor)
    entry.pack(side=RIGHT)
    entry.bind("<Return>",lambda x: createNote(entry.get(),history,parent))
    mainFrame.pack(pady=5)

    btn = Button(parent,text = "Create",bg = "#BFECE8",font=("Helvetica",20),command=lambda : createNote(entry.get(),history,parent),fg = fontColor)
    history.append(btn)
    btn.pack()
def render(parent,history):
    """
    Dark Mode
    """
    global isDarkMode
    global bgcolor
    global fontColor
    print("From File")
    print(fm.readUiMode())
    if(bool(fm.readUiMode())):
        isDarkMode = bool(fm.readUiMode())
        if(isDarkMode):
            #bgcolor = "#4B515D"
            bgcolor = "black"
            fontColor = "white"
    print(isDarkMode)
    """
    / Dark Mode
    """
    parent.title("Dashboard | Notes")
    parent.config(bg=bgcolor)
    if ifDock():
        createDock(parent,history)
    else:
        askTitle(parent,history,True)
def validate(text):
    if text == "":
        return False
    elif text[0] == " ":
        return False
    else:
        return True
def createNote(title,history,parent):
    if validate(title):
        obj = {"title":title,"theme":"teal"}
        id = fm.write(obj)
        for i in history:
            i.pack_forget()
        history = []
        createDock(parent,history)

def ifDock():
    return fm.isFilled()
def darkMode(history,parent):
    for i in history:
            i.pack_forget()
    global bgcolor,fontColor
    #bgcolor = "#4B515D"
    bgcolor = "black"
    fontColor = "white"
    render(parent,history)
def lightMode(history,parent):
    for i in history:
            i.pack_forget()
    global bgcolor,fontColor
    bgcolor = "white"
    fontColor = "black"
    render(parent,history)
def changeUiMode(history,parent):
    global isDarkMode
    if isDarkMode:
        isDarkMode = False
        fm.writeUiMode(isDarkMode)
        lightMode(history,parent)
    else:
        isDarkMode = True
        fm.writeUiMode(isDarkMode)
        darkMode(history,parent)
def toggleFullScreen(parent):
    global isFullScreen
    parent.overrideredirect(not isFullScreen)
    isFullScreen = not isFullScreen
def createDock(parent,history):
    mainTitle = Label(parent,text="Dashboards | Notes",font=("Helvetica",40),bg=bgcolor,fg = fontColor)
    history.append(mainTitle)
    mainTitle.pack()
    
    quitButton = Button(bd= 0,text = "X",font = ("Helvetica",15),bg=bgcolor,fg = fontColor,command = parent.quit,width = 200)
    quitButton.pack()
    history.append(quitButton)
    fullScreenModeButton = Button(bd= 0,text = "Full Screen",font = ("Helvetica",15),bg=bgcolor,fg = fontColor,command = lambda:toggleFullScreen(parent),width = 200)
    fullScreenModeButton.pack()
    history.append(fullScreenModeButton)
    changeModeButton = Button(bd= 0,text = "D@ark Mode",font = ("Helvetica",15),bg=bgcolor,fg = fontColor,command = lambda:changeUiMode(history,parent),width = 200)
    changeModeButton.pack()
    history.append(changeModeButton)
    
    dock = Frame(parent,bg=bgcolor)
    history.append(dock)
    data = fm.raw()

    row = 1
    column = 1
    rowCounter = 0
    columnCounter = 0
    for i in data:
        if(columnCounter%4==0):
            column = 1
            row += 1
        upper = Frame(dock,bg=i["theme"],bd=0,width=200)
        Label(upper,text = i["title"],font=("Helvetica",20),bg = i["theme"],fg = fontColor).pack(padx=5,pady=5)
        Button(upper,command = lambda agrid = i["_id"]: openNote(agrid,parent,history),text="Open",bg="#BFECE8",font=("Helvetica",20),bd=0).pack(padx=5,pady=5,fill=X)
        upper.grid(row=row,column=column,padx = 10,pady = 10)
        column += 1
        columnCounter += 1
    dock.pack()
    createbtn = Button(parent,bd=0,bg = "#BFECE8",text = "Create Note",font=("Helvetica",20),command = lambda : askTitle(parent,history))
    history.append(createbtn)
    createbtn.pack(side=BOTTOM,fill=X)
def openNote(id,parent,history):
    for i in history:
            i.pack_forget()
    history = []
    editScreen.fm = fm
    editScreen.id = id
    editScreen.render(parent,history,lambda : render(parent,history))
