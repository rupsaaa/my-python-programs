import tkinter as tk
from tkinter import font
def font_size():
    selected_index=listbox.curselection() #get selected size from listbox
    if selected_index:
        size=listbox.get(selected_index)
        label.config(font=("Arial", size)) #change font size of label
root=tk.Tk()
root.title("Font Size Changer")
label=tk.Label(root,text="Hello, welcome to GUI Programming!",font=("Arial Black", 12))
root.geometry("450x300")
root.configure(bg="pink")
label.pack(pady=20)
listbox=tk.Listbox(root,height=6)
font_sizes=[6,8,10,12,14,16,18,20,24,28,32,36,40,72]
for size in font_sizes:
    listbox.insert(tk.END,size) #insert font sizes into listbox
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", lambda event: font_size()) #bind selection event to font_size function
root.mainloop()
