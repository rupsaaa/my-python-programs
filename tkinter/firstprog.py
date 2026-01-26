import tkinter
from tkinter import messagebox
root=tkinter.Tk() #Tk() is a constructor of Tk class that creates object(root) representing main application window
root.title("Message Box Example")
def hellomsg():
    messagebox.showinfo("python","Python Programming")
b=tkinter.Button(root,text="python",command=hellomsg)
b.pack(pady=20) #pack sets geometric coordinates like pad y means yaxis coordinate 20
root.mainloop()
