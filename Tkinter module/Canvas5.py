# create_image : Creates an image item, which can be an instance of either the BitmapImage or the PhotoImage classes
# filename = PhotoImage(file="filename.gif")
# image = canvas.create_image(x0,y0,options,image=filename)

from tkinter import *
top=Tk()
filename=PhotoImage(file="E://My Python programs//Tkinter module//image.gif")
c=Canvas(top,bg="blue",height=400,width=400)
image=c.create_image(100,100,image=filename)
c.pack()
top.mainloop()