import tkinter as tk
import tkinter.ttk as view
root = tk.Tk()
root.title("Notes App")
width  = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')
root.overrideredirect(True)
def setScrollBar(x0,x1):
    scrollbar.set(x0,x1)
    print(x0,x1)
    val = None
    if(x0==0.0):
        value = x0
    else:
        value = x1
    progress["value"] = value
def changeColor(name):
    root.configure(background=name)
    inp.configure(background=name)
    textArea.configure(background=name)

progress = view.Progressbar(root,mode="determinate")
progress["value"] = 0.0
progress["maximum"] = 1
progress.pack(fill=tk.X)
btn = tk.Button(root,command=root.quit,text = "<---")
btn.pack(side=tk.TOP,fill=tk.X)
frame = tk.Frame(root)
tk.Button(frame,text="  ",command = lambda:changeColor("tomato"),bg="tomato",width=int(width/50)).pack(side=tk.LEFT)
tk.Button(frame,text="  ",command = lambda:changeColor("mediumseagreen"),bg="mediumseagreen",width=int(width/50)).pack(side=tk.LEFT)
tk.Button(frame,text="  ",command = lambda:changeColor("dodgerblue"),bg="dodgerblue",width=int(width/50)).pack(side=tk.LEFT)
tk.Button(frame,text="  ",command = lambda:changeColor("teal"),bg="teal",width=int(width/50)).pack(side=tk.LEFT)
tk.Button(frame,text="  ",command = lambda:changeColor("magenta"),bg="magenta",width=int(width/50)).pack(side=tk.LEFT)
frame.pack(side=tk.BOTTOM)
inp = tk.Entry(root,bd=0,bg="dodgerblue",cursor="dot",selectforeground="white",font=("TimesNewRoman",30,"italic"))
inp.pack(fill=tk.X)

root.configure(background="dodgerblue")

# background_image=tk.PhotoImage(file=r"D:\A Trp Tech Assests\trp tech.PNG")
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

textArea = tk.Text(root,width=width,height=height,bg="dodgerblue",font = ("TimesNewRoman",21),bd=0)


scrollbar  = tk.Scrollbar(root,command=textArea.yview,highlightcolor = "dodgerblue")
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
textArea.configure(yscrollcommand=setScrollBar)
textArea.pack()



tk.mainloop()