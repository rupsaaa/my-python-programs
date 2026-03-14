from tkinter import *
from tkinter import filedialog

# GLOBAL TEXT WIDGET 
t = None   # global function

def new_file():
    global t
    t.delete(1.0, END)

def open_file():
    global t
    filename = filedialog.askopenfilename(
        title='Select a file',
        filetypes=(("Text files", "*.txt"),
                   ("Python files", "*.py"),
                   ("All files","."))
    )

    if filename:
        with open(filename, 'r') as f:
            contents = f.read()

        t.delete(1.0, END)
        t.insert(1.0, contents)

def save_file_as():
    global t
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=(("Text files", "*.txt"),
                   ("All files","."))
    )

    if filename:
        contents = t.get(1.0, END)
        with open(filename, 'w') as f:
            f.write(contents)



root = Tk()
root.title("A Menu Example.")
root.geometry('600x350')

# create global Text widget
t = Text(root, width=80, height=20, wrap=WORD)
t.pack(expand=True, fill=BOTH)

# create menubar
menubar = Menu(root)
root.config(menu=menubar)

# File menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save as", command=save_file_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="File", menu=filemenu)

# Edit menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>"))
editmenu.add_command(label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>"))
editmenu.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))

menubar.add_cascade(label="Edit", menu=editmenu)

root.mainloop()