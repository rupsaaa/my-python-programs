from tkinter import *
class MyEntry:
     # constructor
     def __init__(self,root):
          # create a frame as child to root window
          self.f=Frame(root,height=350,width=500)

          # let the frame will not shrink
          self.f.propagate(0)

          # attach the frame to root window
          self.f.pack()

          # labels
          self.l1=Label(text='Enter user name: ')
          self.l2=Label(text='Enter Password: ')

          # create Entry widget for user name
          self.e1=Entry(self.f,width=25,fg='blue',bg='yellow',font=('Arial',14))

          # create Entry widget for password. the text widget is replaced by stars (*)
          self.e2=Entry(self.f,width=25,fg='blue',bg='yellow',show='*')

          # when user presses Enter, bind that event to display method
          self.e2.bind("<Return>",self.display)

          # place labels and entry widgets in the frame
          self.l1.place(x=50,y=100)
          self.e1.place(x=200,y=100)
          self.l2.place(x=50,y=150)
          self.e2.place(x=200,y=150)
     
     def display(self,event):
          # retrieve the values from the entry widgets
          str1=self.e1.get()
          str2=self.e2.get()

          # display the values using labels
          lbl1=Label(text='Your name is: '+str1).place(x=50,y=200)
          lbl2=Label(text='Your password is: '+str2).place(x=50,y=220)

# create root window
root=Tk()

# create an object to MyButtons class
mb=MyEntry(root)

# the root window handles the mouse click event
root.mainloop()