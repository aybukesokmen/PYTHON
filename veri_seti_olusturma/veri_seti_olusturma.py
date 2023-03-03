import cv2
import numpy as np
import os

path="images"

imgWidth=180
imgHeight=120

cap=cv2.VideoCapture(1)
cap.set(180,640)
cap.set(180,180)

#klasor olusturma
global countFolser
def saveDataFunc():
    global countFolder
    countFolder=0
    while os.path.exists(path+str(countFolder)):
        countFolder+=1
    os.makedirs(path+str(countFolder))
saveDataFunc()

count =0
countSave=1
while True:
    success,img=cap.read()
    if success:
        img=cv2.resize(img,(imgWidth,imgHeight))
        
        if count%5==0:
            cv2.imwrite(path+str(countFolder)+"/"+str(countSave)+"_"+".png",img)
            countSave+=1
            print(countSave)
        count+=1
        
        cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0XFF==ord("q"):break
cap.release()
cv2.destroyAllWindows()
