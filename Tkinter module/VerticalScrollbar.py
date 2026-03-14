from tkinter import*
class MyScrollbar:
    def __init__(self,root):
        self.t=Text(root,width=70,height=15,wrap=NONE)
        for i in range(50):
            self.t.insert(END,"This is some text\n")
        self.t.pack(side=LEFT,fill=Y)
        self.h=Scrollbar(root,orient=VERTICAL,command=self.t.yview)
        self.t.configure(yscrollcommand=self.h.set)
        self.h.pack(side=RIGHT,fill=Y)
root=Tk()
ms=MyScrollbar(root)
root.mainloop()