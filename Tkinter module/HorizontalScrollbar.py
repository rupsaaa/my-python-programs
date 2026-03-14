from tkinter import *
class MyScrollbar:

     # constructor
     def __init__(self,root):

          # create a Text widget with 70 chars width and 15 lines height
          self.t=Text(root,width=70,height=15,wrap=NONE)

          # insert some text into the Text widget
          for i in range(50):
               self.t.insert(END,"This is some text")
          
          # attach Text widget to root window at the top
          self.t.pack(side=TOP,fill=X)

          # create a horizontal scroll bar and attach it to Text widget
          self.h=Scrollbar(root,orient=HORIZONTAL,command=self.t.xview)

          # attach Text widget to the horizontal scroll bar
          self.t.configure(xscrollcommand=self.h.set)

          # attach Scrollbar to root window at the bottom
          self.h.pack(side=BOTTOM,fill=X)
     
# create root window
root=Tk()

# create an object to MyScrollbar class
ms=MyScrollbar(root)
# the root window handles the mouse click event
root.mainloop()