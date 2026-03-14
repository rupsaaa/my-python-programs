from tkinter import *
msgs=["You have clicked me!","Welcome to codehub sodepur","Welcome to Tapas Sir's theka.",""]
i=0
def buttonClick(self):
     global i
     message_label.config(text=msgs[i%3])
     i+=1

def clearscreen(self):
     message_label.config(text=msgs[3])

root=Tk()
f=Frame(root,height=200,width=200)
f.propagate(0)
f.pack()
b=Button(f,text='MyButton',width=15,height=2,bg='yellow',fg='blue',activebackground='green',activeforeground='red')
b.pack()
b1=Button(f,text='Clear',width=15,height=2,bg='yellow',fg='blue',activebackground='green',activeforeground='red')
b1.pack()

message_label=Label(root,text="",font=("Arial black",20))
message_label.pack(pady=200,padx=100)

b.bind("<Button-1>",buttonClick)
b1.bind("<Button-1>",clearscreen)
root.mainloop()