from PIL import Image
image=Image.open("E:/python programs/Image Processing/imageproc.png")
image.show()
res_img=image.resize((300,200))
res_img.show()