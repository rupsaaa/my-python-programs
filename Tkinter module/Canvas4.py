# create_arc : Creates an arc item, which can be a chord, a pieslice or a simple arc.
# coord = 10,50,240,219
# arc = canvas.create_arc(coord,start=0,extent=150,fill="blue")

from tkinter import *
top=Tk()
c=Canvas(top,bg="blue",height=250,width=300)
coord=10,50,240,210
arc=c.create_arc(coord,start=0,extent=180,fill="red")
c.pack()
top.mainloop()