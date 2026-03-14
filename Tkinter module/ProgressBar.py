from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

def progress_bar():
     prog["value"]+=10
     if prog["value"]>100:
          root.withdraw() # hide the main window
          messagebox.showinfo("Alert","100% job completed")

root=tk.Tk()
root.title("My Progress Bar")
root.geometry("300x200")
prog=ttk.Progressbar(root,orient="horizontal",length=200,mode="determinate")
prog.pack(pady=20)
button=tk.Button(root,text="Increase",command=progress_bar)
button.pack()
root.mainloop()