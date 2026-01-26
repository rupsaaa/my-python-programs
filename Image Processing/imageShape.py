import numpy as np
from PIL import Image
image=Image.open("E:/python programs/Image Processing/imageproc.png")
image_arr=np.array(image) 
print("Image shape:",image_arr.shape)#prints array of pixels..3 fields for coloured image height,width,color and 2 field for gray scale image