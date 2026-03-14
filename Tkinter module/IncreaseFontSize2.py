import tkinter as tk
def ChangeFont(event):
     selection=listbox.curselection()
     if selection:
          size=listbox.get(selection[0]) # get the selected font size
          label.config(font=("Arial",size))

root=tk.Tk()
root.title("Font Size Selector")
root.geometry("400x250")
label=tk.Label(root,text="Hello Codehub Sodepur",font=("Arial",14))
label.pack(pady=20)
sizes=[10,12,14,16,18,20,24,28,32]
listbox=tk.Listbox(root,height=6)
for s in sizes:
     listbox.insert(tk.END,s)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>",ChangeFont)
root.mainloop()