from tkinter import *
def render(parent,history,clean,after):
    t = 100
    label = Label(parent,text="Starting...",font=("Helvetica",40),bd=parent.winfo_screenheight()/2)
    history.append(label)
    label.pack(pady=0)
    label.after(1000,lambda : changeView("3","teal",label,parent))
    label.after(1500,lambda : changeView("2","magenta",label,parent))
    label.after(2000,lambda : changeView("1","dodgerblue",label,parent))
    label.after(2500,lambda : changeView("Siddhant Sharma","tomato",label,parent))
    label.after(3000+t,lambda : label.config(text="D"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Da"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Das"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dash"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashb"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashbo"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboa"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboar"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard | "))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard | N"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard | No"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard | Not"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard | Note"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard | Notes"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard | Notes A"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard | Notes Ap"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard | Notes App"))
    t = t + 100
    label.after(3000+t,lambda : label.config(text="Dashboard | Notes App..."))
    t = t + 100
    label.after(3000+t,lambda : clean(history))
    label.after(3000+t,after)
def changeView(title,color,label,parent):
    parent.title(title)
    label.config(text=title)
    parent.config(bg=color)