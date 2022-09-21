from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    
    if file=="":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0,f.read())
        f.close()

def save():
        if file == None:
            saveAsFile()
        
        else:
            writer = open(file, 'w')
            writer.write(TextArea.get(1.0,END))
            writer.close()

def saveAsFile():
    global file
    
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt", 
        filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if file =="":
            file = None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")

    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()    

def exit():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))   

def selectAll():
    TextArea.tag_add(SEL,"1.0",END)
    TextArea.mark_set(INSERT,"1.0")
    TextArea.see(INSERT)
    return 'break'

def delete():
    TextArea.event_generate(('<Delete>'))

def about():
    showinfo("Notepad","A text editor platform")

if __name__ == '__main__':
    root=Tk()
    root.title("Untitled - Notepad")
    img = PhotoImage(file = "E:\\PythonProjects\\notepad\\pic.png")
    root.tk.call('wm', 'iconphoto', root._w, img)
    root.geometry("700x500")

    TextArea = Text(root,font="TimesNewRoman 11",undo=True)
    file = None
    TextArea.pack(expand=True,fill=BOTH)

    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)

    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Save", command=save)
    FileMenu.add_command(label="Save As", command=saveAsFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=exit)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu=Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Undo", command = TextArea.edit_undo)
    EditMenu.add_command(label="Redo", command = TextArea.edit_redo)
    EditMenu.add_separator()
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    EditMenu.add_command(label="Select All", command=selectAll)
    EditMenu.add_separator()
    EditMenu.add_command(label = 'Delete', command=delete)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)

    root.config(menu=MenuBar)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()