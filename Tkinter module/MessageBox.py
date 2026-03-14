import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.title("Message Box Example")

def hellomsg():
     messagebox.showinfo("Python","Python Programming")

b=tkinter.Button(root,text="python",command=hellomsg)
b.pack(pady=20)

root.mainloop()

# Tk() is a constructor of the Tk Class
# That object represents the main application window. You store that object in a variable like root

'''
Tkinter has 3 layout managers

Grid is one of them:
1. pack() – simple, top/bottom/left/right
2. place() – fixed x, y coordinates
3. grid() – table style layout (most used)

grid means → place the widget in a specific row and column just like a table.

The word grid in Tkinter means a layout manager that arranges widgets in a table-like structure using rows and columns.
'''
