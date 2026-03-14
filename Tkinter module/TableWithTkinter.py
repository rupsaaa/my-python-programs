import tkinter as tk
root=tk.Tk()
root.title("Table with Tkinter")
val=[
     ["Name","Age","Marks"],
     ["Arpan",24,78],
     ["Gopal",30,89],
     ["Naren",28,64],
     ["Ramani",21,97]
]
for i in range(len(val)): # create table using Labels
     for j in range(len(val[i])):
          cell=tk.Label(root,text=val[i][j],borderwidth=1,relief="ridge",width=15,anchor="center")
          cell.grid(row=i,column=j,padx=2,pady=2)
root.mainloop()