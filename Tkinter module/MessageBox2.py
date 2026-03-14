import tkinter as tk
root=tk.Tk()

root.title("Button Click")
root.geometry("400x250")

root.configure(bg="lightblue")

message_label=tk.Label(root,text="",font=("Arial black",20))
message_label.pack(pady=20)

def display_message():
     message_label.config(text="Code Hub Sodepur",fg="red")

button=tk.Button(root,text="Click Here",command=display_message)
button.pack(pady=10) # 10 pixels of empty space above and below vertical direction

root.mainloop() # the application run