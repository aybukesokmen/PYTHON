#-*-coding: cp1254-*-
###Renk ve Sekil Algılama###
 
import numpy as np
import cv2
 
red_lower = np.array([0, 100, 100],np.uint8)
red_upper = np.array([10, 255, 255],np.uint8)
 

 
cam=cv2.VideoCapture(0)
 
def filtre(lower,upper):
	mask=None
	mask=cv2.inRange(hsv, lower, upper)
	mask=cv2.erode(mask,None,iterations=2)
	mask=cv2.dilate(mask,None,iterations=2)
	return mask
 
def detect(c):	
	peri=cv2.arcLength(c,True)
	approx=cv2.approxPolyDP(c,0.04*peri,True)
 
	if len(approx)==1:
		shape="Ucgen"
	else:
		shape="Tanimlanamayan"
	return shape
 
def algilama(mask,renk):
	cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	center= None
	if len(cnts)>0:
		c=max(cnts,key=cv2.contourArea)
		x,y,w,h=cv2.boundingRect(c)
 
		M = cv2.moments(c)
		cX = int((M["m10"] / M["m00"]))
		cY = int((M["m01"] / M["m00"]))
		shape = detect(c)
 
		c=c.astype("int")
		cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
		cv2.putText(frame, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
		cv2.putText(frame,renk,(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0))
 
 
 
while(cam.isOpened()):
	ret,frame=cam.read()
	if ret:
		blur=cv2.GaussianBlur(frame,(5,5),0)
		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	
		red=filtre(red_lower,red_upper)

 
		algilama(red,"kirmizi")

		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF ==27:
			break
	else:
		break
cam.release()
cv2.destroyAllWindows()