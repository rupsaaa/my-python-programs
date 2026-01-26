import tkinter as tk
root=tk.Tk()
root.title("Button click")
root.geometry("400x250")
root.configure(bg="lightblue")
msg_label=tk.Label(root,text="",font=("Arial black",20))
msg_label.pack(pady=20)
def display():
    msg_label.config(text="Codehub sodpur",fg="red")
button=tk.Button(root,text="Click here",command=display)
button.pack(pady=10)
root.mainloop()
