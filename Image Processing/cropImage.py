from PIL import Image
image=Image.open("E:/python programs/Image Processing/imageproc.png")
image.show()
box=(50,50,250,250) #left,upper,right,lower
crop_img=image.crop(box)
crop_img.show()