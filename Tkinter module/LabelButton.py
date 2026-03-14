from tkinter import *
class MyButtons:
     # constructor
     def __init__(self, root):

          # create a frame as child to root window 
          self.f = Frame(root, height=350, width=500)

          # let the frame will not shrink
          self.f.propagate (0)

          # attach the frame to root window 
          self.f.pack()

          # create a push button and bind it to buttonclick method 
          self.b1 = Button(self.f, text='Click Me', width=15, height=2, command=self.buttonClick)

          # create another button that closes the root window upon clicking 
          self.b2 = Button(self.f, text='close', width=15, height=2, command=quit)

          # attach buttons to the frame
          self.b1.grid(row=0, column=1)
          self.b2.grid(row=0, column=2)

     # the event handler method
     def buttonClick(self):

          # create a label with some text

          self.lbl = Label(self.f, text="Welcome to Python", width=20,height=2, font=('Courier', -30, 'bold underline '),fg='blue')
          
          # attach the label in the frame 
          self.lbl.grid(row=2, column=0)

# create root window 
root = Tk()

# create an object to MyButtons class 
mb = MyButtons(root)

# the root window handles the mouse click event 
root.mainloop()