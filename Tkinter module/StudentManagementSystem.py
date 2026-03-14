import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Student Management System")
root.geometry("450x500")
root.configure(bg="lightblue")
students=[]

def add_student():
     name=name_entry.get()
     roll=roll_entry.get()
     course=course_entry.get()

     if name=="" or roll=="" or course=="":
          messagebox.showwarning("All fields are required!!")
          return
     
     student= f"{roll} - {name} - {course}"
     students.append(student)

     listbox.insert(tk.END,student)

     name_entry.delete(0,tk.END)
     roll_entry.delete(0,tk.END)
     course_entry.delete(0,tk.END)

def delete_student():
     selected=listbox.curselection()

     if selected:
          index=selected[0]
          listbox.delete(index)
          students.pop(index)
     else:
          messagebox.showwarning("Warning","Select a student first!")

def clear_all():
     listbox.delete(0,tk.END)
     students.clear()

title=tk.Label(root,text="Student Management System",font=("Tahoma",18,"bold"))
title.pack(pady=10)
frame=tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame,text="Reg No").grid(row=0,column=0,padx=5,pady=5)
roll_entry=tk.Entry(frame)
roll_entry.grid(row=0,column=1)

tk.Label(frame,text="Name").grid(row=1,column=0,padx=5,pady=5)
name_entry=tk.Entry(frame)
name_entry.grid(row=1,column=1)

tk.Label(frame,text="Course").grid(row=2,column=0,padx=5,pady=5)
course_entry=tk.Entry(frame)
course_entry.grid(row=2,column=1)

btn_frame=tk.Frame(root)
btn_frame.pack(pady=10)

add_btn=tk.Button(btn_frame,text="Add",width=10,command=add_student)
add_btn.grid(row=0,column=0,padx=5)

del_btn=tk.Button(btn_frame,text="Delete",width=10,command=delete_student)
del_btn.grid(row=0,column=1,padx=5)

clear_btn=tk.Button(btn_frame,text="Clear All",width=10,command=clear_all)
clear_btn.grid(row=0,column=2,padx=5)

listbox=tk.Listbox(root,width=45,height=12)
listbox.pack(pady=10)

root.mainloop()