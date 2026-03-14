from tkinter import *
class MyCheck:
     # constructor 
     def __init__(self,root):
          # create a frame as child to root window
          self.f=Frame(root,height=350,width=500)

          # let the frame will not shrink
          self.f.propagate(0)

          # attach the frame to root window 
          self.f.pack()

          # create IntVar class variables 
          self.var1=IntVar()
          self.var2=IntVar()
          self.var3=IntVar()

          # create check boxes and bind them to display method 
          self.c1=Checkbutton(self.f,bg='yellow',fg='green',font=('Georgia',20,'underline'),text='Java',variable=self.var1,command=self.display)
          self.c2=Checkbutton(self.f,text='Python',variable=self.var2,command=self.display)
          self.c3=Checkbutton(self.f,text='.NET',variable=self.var3,command=self.display)

          # attach check boxes to the frame
          self.c1.place(x=50,y=100)
          self.c2.place(x=200,y=100)
          self.c3.place(x=350,y=100)
     
     def display(self):
          # retrieve the control variable values
          x=self.var1.get()
          y=self.var2.get()
          z=self.var3.get()

          # string is empty initially
          str=''

          # catch user choice
          if x==1:
               str+=' Java '
          if y==1:
               str+=' Python '
          if z==1:
               str+=' .NET '

          # display the user selction as a label
          lbl=Label(text=str,fg='blue').place(x=50,y=150,width=200,height=20)

# create root window
root=Tk()

# create an object to MyButtons class
mb=MyCheck(root)

# the root window handles the mouse click event
root.mainloop()