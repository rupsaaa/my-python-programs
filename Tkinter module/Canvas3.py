# create_oval : Creates a circle or an ellipse at the given coordinates. 
# oval = canvas.create_oval(x0,y0,x1,y1,options)

from tkinter import *
top=Tk()
c=Canvas(top,bg="blue",height=250,width=300)
oval=c.create_oval(80,100,150,200,fill="red")
c.pack()
top.mainloop()
