# create_polygon : Creates a polygon item that must have at least three vertices.
# polygon = canvas.create_polygon(x0,y0,x1,y1,.....,xn,yn,options)

from tkinter import *
top=Tk()
c=Canvas(top,bg="blue",height=250,width=300)
polygon=c.create_polygon(10,50,100,200,250,10,fill="red")
c.pack()
top.mainloop()