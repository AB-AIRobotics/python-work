import ImageWriter 
import time

'''
 Helpful functions
'''

def getCoordWhitePixel(initial_x,initial_y ,inputImg,img_height , image_width):
    
    for i in range(initial_x,img_height):
        for j in range(initial_y,image_width):
            pixel = inputImg.pic[i][j]
            if (pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255):
                return i,j

def getCoordBlackPixel(initial_x,initial_y ,inputImg,img_height , image_width):
    
    for i in range(initial_x,img_height):
        for j in range(initial_y,image_width):
            pixel = inputImg.pic[i][j]
            if (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0):
                return i,j

# ----------------------------------------------------------------------------------------------------------------


def convertBlackWhite(inputpicture):

    mypic = ImageWriter.loadPicture(inputpicture)
    w = ImageWriter.getWidth(mypic)
    h = ImageWriter.getHeight(mypic)

    print 'Image width: ' ,w
    print 'Image height: ',h

    for i in range(0,h):
        for j in range(0,w):
            pixel = mypic.pic[i][j]
            threshold = (pixel[0] + pixel[1] + pixel[2])/3
            if threshold < 55:
                ImageWriter.setColor(mypic,j,i,[0,0,0])
            else:
                ImageWriter.setColor(mypic,j,i,[255,255,255])

    ImageWriter.updatePicture(mypic)
    ImageWriter.savePicture(mypic,'barcode2c.jpg')

#convertBlackWhite("barcode2.jpg")


def searchForStartPoint(blackWhiteImg):
    
    mypic = ImageWriter.loadPicture(blackWhiteImg)

    w = ImageWriter.getWidth(mypic)
    h = ImageWriter.getHeight(mypic)

    for i in range(0,h):
        for j in range(0,w):
            pixel = mypic.pic[i][j]
            if (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0):
                return i,j

#print searchForStartPoint("barcode2c.jpg")

def getUnitWidth(inputpicture):

    mypic = ImageWriter.loadPicture(inputpicture)

    w = ImageWriter.getWidth(mypic)
    h = ImageWriter.getHeight(mypic)

    startCoordOfBar1 = searchForStartPoint(inputpicture)
    print "Start point coordinates: ",startCoordOfBar1

    x = startCoordOfBar1[0]
    y = startCoordOfBar1[1]

    endCoordOfBar1 = getCoordWhitePixel(x,y,mypic,h,w)

    x1 = endCoordOfBar1[0]
    y1 = endCoordOfBar1[1]
    
    startCoordOfBar2 = getCoordBlackPixel(x1,y1,mypic,h,w)

    x2 = startCoordOfBar2[0]
    y2 = startCoordOfBar2[1]

    print x2
    print y2 
    #bar1WidthInPxl = y1-y 
    #print bar1WidthInPxl

getUnitWidth("barcode2c.jpg")





    




