from PIL import Image,ImageFilter
image=Image.open("E:/python programs/Image Processing/imageproc.png")
blur=image.filter(ImageFilter.BLUR)
blur.save("E:/python programs/Image Processing/imageprocblur.png")
blur.show()