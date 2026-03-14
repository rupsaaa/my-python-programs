import tkinter as tk
from tkinter import ttk,messagebox

def ProgressBar():
     if prog["value"] < 100:
          prog["value"]+=10
          root.after(250,ProgressBar) # call again after 250 ms
     else:
          root.withdraw() # hide the main window
          messagebox.showinfo("Alert","100% job completed")
root=tk.Tk()
root.title("My Progress Bar")
root.geometry("300x200")
prog=ttk.Progressbar(root,orient="horizontal",length=300,mode="determinate")
prog.pack(pady=20)
button=tk.Button(root,text="Start",command=ProgressBar)
button.pack()
root.mainloop()