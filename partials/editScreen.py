from tkinter import *
import time
fm = None
id = None
data = None
def backAction(onBack,history):
    for i in history:
            i.pack_forget()
    onBack()
def render(parent,history,onBack):
    width = parent.winfo_screenwidth()
    height = parent.winfo_screenheight()
    data = fm.read(id)
    if 'lastModified' not in data:
        data['lastModified'] = time.ctime(time.time())
    parent.title(f"{data['title']} - edit | Last Modified - {data['lastModified']}")
    parent.configure(background=data["theme"])
    btn = Button(parent,command=lambda : backAction(onBack,history),text = "<---",bg = data["theme"])
    history.append(btn)
    btn.pack(side=TOP,fill=X)
    frame = Frame(parent)
    history.append(frame)
    inp = Entry(parent,bd=0,bg=data["theme"],cursor="dot",selectforeground="white",font=("TimesNewRoman",30,"italic"))
    history.append(inp)
    textArea = Text(parent,width=width,height=height,bg=data["theme"],font = ("TimesNewRoman",21),bd=0)
    history.append(textArea)
    Button(frame,text="  ",command = lambda:changeColor(parent,"#ff4444",data,inp,textArea,btn),bg="#ff4444",width=int(width/60)).pack(side=LEFT)
    Button(frame,text="  ",command = lambda:changeColor(parent,"#33b5e5",data,inp,textArea,btn),bg="#33b5e5",width=int(width/60)).pack(side=LEFT)
    Button(frame,text="  ",command = lambda:changeColor(parent,"#00C851",data,inp,textArea,btn),bg="#00C851",width=int(width/60)).pack(side=LEFT)
    Button(frame,text="  ",command = lambda:changeColor(parent,"#4B515D",data,inp,textArea,btn),bg="#4B515D",width=int(width/60)).pack(side=LEFT)
    Button(frame,text="  ",command = lambda:changeColor(parent,"#aa66cc",data,inp,textArea,btn),bg="#aa66cc",width=int(width/60)).pack(side=LEFT)
    Button(frame,text="  ",command = lambda:changeColor(parent,"#ffbb33",data,inp,textArea,btn),bg="#ffbb33",width=int(width/60)).pack(side=LEFT)
    Button(frame,text="  ",command = lambda:changeColor(parent,"#3F729B",data,inp,textArea,btn),bg="#3F729B",width=int(width/60)).pack(side=LEFT)
    Button(frame,text="  ",command = lambda:changeColor(parent,"magenta",data,inp,textArea,btn),bg="magenta",width=int(width/60)).pack(side=LEFT)
    frame.pack(side=BOTTOM)
    inp.bind("<Key>",lambda x: autosave(inp,textArea,data))
    inp.pack(fill=X)
    inp.delete(0,END)
    inp.insert(0,data["title"])
    textArea.bind("<Key>",lambda x: autosave(inp,textArea,data))
    textArea.delete(1.0,END)
    if "body" in data:
        textArea.insert(END,data["body"])
    scrollbar  = Scrollbar(parent,command=textArea.yview)
    history.append(scrollbar)
    scrollbar.pack(side=RIGHT,fill=Y)
    textArea.configure(yscrollcommand=lambda x0,x1: scrollbar.set(x0,x1))
    textArea.pack()

def changeColor(parent,color,data,inp,textArea,btn):
    parent.configure(background=color)
    data["theme"] = color
    fm.writeById(id,data)
    inp.configure(background=color)
    btn.configure(background=color)
    textArea.configure(background=color)

def autosave(inp,txt,data):
    data["title"] = inp.get()
    data["body"] = txt.get(1.0,END)
    data["lastModified"] = time.ctime(time.time())
    fm.writeById(data["_id"],data)