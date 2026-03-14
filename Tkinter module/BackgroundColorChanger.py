import tkinter as tk
root=tk.Tk()
root.title("My color show")
root.geometry("400x300")

def redcolor():
     root.configure(bg="red")

def greencolor():
     root.configure(bg="green")

def bluecolor():
     root.configure(bg="blue")

def pinkcolor():
     root.configure(bg="pink")

def blackcolor():
     root.configure(bg="black")

def yellowcolor():
     root.configure(bg="yellow")

btn_red=tk.Button(root,text="Red",command=redcolor)
btn_red.pack(pady=5)

btn_green=tk.Button(root,text="Green",command=greencolor)
btn_green.pack(pady=5)

btn_blue=tk.Button(root,text="Blue",command=bluecolor)
btn_blue.pack(pady=5)

btn_pink=tk.Button(root,text="Pink",command=pinkcolor)
btn_pink.pack(pady=5)

btn_black=tk.Button(root,text="Black",command=blackcolor)
btn_black.pack(pady=5)

btn_yellow=tk.Button(root,text="Yellow",command=yellowcolor)
btn_yellow.pack(pady=5)

root.mainloop()