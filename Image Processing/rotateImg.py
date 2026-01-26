from PIL import Image
image=Image.open("E:/python programs/Image Processing/imageproc.png")
rot_img=image.rotate(180)
flipped=image.transpose(Image.FLIP_LEFT_RIGHT)
rot_img.show()
flipped.show()
