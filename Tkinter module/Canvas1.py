# create_line : Creates a line item
# line = canvas.create_line(x0,y0,x1,y1,....,xn,yn,options)

from tkinter import *
top=Tk()
c=Canvas(top,bg="blue",height=250,width=300)
line=c.create_line(10,50,240,210,fill="red")
c.pack()
top.mainloop()