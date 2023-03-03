import cv2
path="cascade.xml"
objectName="hastalikli"
frameWidth=280
frameHeight=360

color=(255,0,255)

cap=cv2.VideoCapture(1)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):pass

cv2.namedWindow("sonuc")
cv2.resizeWindow("sonuc",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","sonuc",400,1000,empty)
cv2.createTrackbar("Neighbor","sonuc",4,50,empty)

cascade=cv2.CascadeClassifier(path)

while True:
    success,img=cap.read()
    
    if success:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        scaleVal=1+(cv2.getTrackbarPos("Scale","sonuc")/1000)
        neighbor=cv2.getTrackbarPos("Neighbor", "sonuc")
        rects=cascade.detectMultiScale(gray,scaleVal,neighbor)
        if scaleVal==0:
            scaleVal=1
        
        for(x,y,w,h) in rects:
            cv2.rectangle(img,(x,y),(x+w,y+h), color,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color,2)
        cv2.imshow("sonuc",img)
    if cv2.waitKey(1) & 0xFF==ord("q"): break
        

        
