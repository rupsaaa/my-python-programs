from tkinter import *
class MyMessage:
      # constructor
      def __init__(self,root):
            
            # create a frame as child to root window
            self.f=Frame(root, height=350, width=500)

            # let the frame will not shrink
            self.f.propagate(0)

            # attach the frame to root window
            self.f.pack()

            # create a Message widget with some text
            self.m=Message(self.f,text='This is a message that has more than one line of text.',width=200,font=('Roman',20,'bold italic'),fg='dark goldenrod')

            # attach Message to the frame
            self.m.pack(side=LEFT)

# create root window
root=Tk()

# create an object to MyMessage class
mb=MyMessage(root)

# the root window handles the mouse click event
root.mainloop()