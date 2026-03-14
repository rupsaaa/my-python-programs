import tkinter as tk
import random

def change_color():
     colors=["blue","red","green","purple","orange","brown","pink","yellow"]
     new_color=random.choice(colors) # pick a random color from the list
     mylabel.config(fg=new_color) # update the label foreground color

root=tk.Tk()
root.title("Color Changer")
root.geometry("300x150")
mylabel=tk.Label(root,text="Welcome to Codehub Sodepur",font=("Arial",20,"bold"),fg="black")
mylabel.pack(pady=30)
btn_action=tk.Button(root,text="Change Color",command=change_color)
btn_action.pack()
root.mainloop()