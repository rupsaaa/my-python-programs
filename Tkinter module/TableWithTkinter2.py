from tkinter import *
class MyTable:
     def __init__(self,root):
          # code for creating the table
          for i in range(total_rows):
               for j in range(total_cols):
                    self.e=Entry(root,width=20,fg="blue",font=("Arial",16,"bold"))
                    self.e.grid(row=i,column=j)
                    self.e.insert(END,lst[i][j])

# take the data
lst=[(1001,'Geeta Kumari','Chandigarh',12078.88),
     (1002,'Vinod Teja','Hyderabad',20000.50),
     (1003,'Ravi Shankar','Bangalore',14500.75),
     (1004,'Lakshmi Prasanna','New Delhi',9500.00),
     (1005,'Nageswara Pillai','Chennai',21786.40)]

# find the no. of rows and cols in the list
total_rows=len(lst)
total_cols=len(lst[0])

# create root window
root=Tk()
mt=MyTable(root)
root.mainloop()