import tkinter as tk
def color_change():
     selected_color=color_var.get()
     label.config(fg=selected_color)
root=tk.Tk()
root.title("Text Color Changer")
label=tk.Label(root,text="hello, Welcome to Codehub Sodepur.",font=("Arial",16))
label.pack(pady=20)
color_var=tk.StringVar(value="black") # variable to hold selected color
colors=["pink","red","yellow","green","blue","orange","black","purple"]

for col in colors:
     rb=tk.Radiobutton(root,text=col.capitalize(),variable=color_var,value=col,command=color_change)
     rb.pack(anchor="w")

root.mainloop()