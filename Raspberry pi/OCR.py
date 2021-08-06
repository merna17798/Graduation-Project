from cv2 import cv2
import numpy as np
import imutils
import easyocr

img=cv2.imread("one.jpeg",0)
def Verfy(img):
    bfilter=cv2.bilateralFilter(img,11,17,17)
    edges=cv2.Canny(bfilter,30,200)
    keypoints=cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=imutils.grab_contours(keypoints)
    contours=sorted(contours,key=cv2.contourArea,reverse=True)[:10]
    location = None
    for cont in contours:
        approx=cv2.approxPolyDP(cont , 10 ,True)
        if(len(approx)==4):
            location=approx
            break
    mask=np.zeros(img.shape,np.uint8)
    new_img=cv2.drawContours(mask,[location],0,255,-1)
    new_img=cv2.bitwise_and(img,img,mask=mask)
    (x,y)=np.where(mask==255)
    (x1,y1)=(np.min(x),np.min(y))
    (x2,y2)=(np.max(x),np.max(y))
    cropped_img=img[x1:x2+1,y1:y2+1]
    reader=easyocr.Reader(['en'])
    result=reader.readtext(cropped_img)
    number=result[0][-2]
    print(number)
    return number

Verfy(img)