import ImageWriter
import time

mypic = ImageWriter.loadPicture("barcode2.jpg")
ImageWriter.showPicture(mypic)
time.sleep(3)
w = ImageWriter.getWidth(mypic)
print ('width' ,w)
for i in range (0,w):
    # set the color of row 40 to color (red = 50
    # green =5 and blue = 200)
    ImageWriter.setColor(mypic,i,200,[50,5,200])
# update the picture so you can see the changes
ImageWriter.updatePicture(mypic)

# save the picture as sav.jpg

ImageWriter.savePicture(mypic,'sav.jpg')



