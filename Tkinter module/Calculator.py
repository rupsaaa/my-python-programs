import tkinter as tk
root=tk.Tk()
root.title("Addition Program")
root.geometry("350x250")
root.configure(bg="pink")

def addition():
     try:
          a=int(num1.get())
          b=int(num2.get())
          result_label.config(text="Sum = "+str(a+b),fg="blue")
     except:
          result_label.config(text="Invalid input!",fg="red")

def product():
     try:
          a=int(num1.get())
          b=int(num2.get())
          result_label.config(text="Product = "+str(a*b),fg="blue")
     except:
          result_label.config(text="Invalid input!",fg="red")

tk.Label(root,text="Enter 1st Number: ",bg="pink").grid(row=0,column=0,padx=0,pady=10,sticky="w")
num1=tk.Entry(root)
num1.grid(row=0,column=1,padx=10)

tk.Label(root,text="Enter 2nd Number: ",bg="pink").grid(row=1,column=0,padx=10,pady=10,sticky="w")
num2=tk.Entry(root)
num2.grid(row=1,column=1,padx=10)

tk.Button(root,text="Addition",command=addition).grid(row=2,column=0,columnspan=2,pady=15)
result_label=tk.Label(root,text="",font=("Toshiba",14),bg='pink')
result_label.grid(row=3,column=0,columnspan=2,pady=10)

tk.Button(root,text="Product",command=product).grid(row=2,column=1,columnspan=2,pady=15)
result_label=tk.Label(root,text="",font=("Toshiba",14),bg="pink")
result_label.grid(row=3,column=0,columnspan=2,pady=10)

root.mainloop()