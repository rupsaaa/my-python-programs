from tkinter import *
class MyText:
     # constructor
     def __init__(self,root):
          # create a Text widget with 20 chars width and 10 lines height 
          self.t=Text(root,width=20,height=10,font=('Verdana',14,'bold'),fg='blue',bg='yellow',wrap=WORD)

          # insert some text into the text widget
          self.t.insert(END,'Text widget\nThis text is inserted into the Text widget.\nThis is second line\nand this is third line\n')

          # attach Text to the root
          self.t.pack(side=LEFT)

          # show image in the Text widget
          self.img=PhotoImage(file='E://My Python programs//Tkinter module//image.gif')
          self.t.image_create(END,image=self.img)

          # create a tag with the name 'start'
          self.t.tag_add('start','1.0','1.11')

          # apply colors to the tag
          self.t.tag_config('start',background='red',foreground='white',font=('Lucida console',20,'bold italic'))

          # create a Scrollbar widget to move the text vertically
          self.s=Scrollbar(root,orient=VERTICAL,command=self.t.yview)

          # attach the scroll bar to the Text widget
          self.t.configure(yscrollcommand=self.s.set)

          # attach the scroll bar to the root window
          self.s.pack(side=RIGHT,fill=Y)

# create root window 
root=Tk()

# create an object to MyText class
mt=MyText(root)

# the root window handles the mouse click event
root.mainloop()
