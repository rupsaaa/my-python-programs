from tkinter import *
from PIL import Image,ImageTk

def change_image():
     global current_index
     current_index=(current_index+1)%len(images)
     c.itemconfig(image_item,image=images[current_index])

top=Tk()
top.title("Canvas JPG Image Viewer")
top.geometry("600x600")
image_files=["E://My Python programs//Tkinter module//img1.jpg","E://My Python programs//Tkinter module//img2.jpg","E://My Python programs//Tkinter module//img3.jpg","E://My Python programs//Tkinter module//img4.jpg","E://My Python programs//Tkinter module//img5.jpg"]
images=[]
for file in image_files:
     img=Image.open(file)
     img=img.resize((300,300)) # resize image
     images.append(ImageTk.PhotoImage(img)) # coneverts image to Tkinter format
current_index=0
c=Canvas(top,bg="blue",height=500,width=500)
c.pack()
image_item=c.create_image(250,250,image=images[current_index]) # place first image
btn=Button(top,text="Next Image",command=change_image)
btn.pack(pady=10)
top.mainloop()