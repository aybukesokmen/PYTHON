
import cv2
 
kamera = cv2.VideoCapture(0)
 
while (True):
    ret, videoGoruntu = kamera.read()
    cv2.imshow("Bilgisayar Kamerasi", videoGoruntu)

    if cv2.waitKey(50) & 0xFF == ord('x'):
        break
 
kamera.release()
cv2.destroyAllWindows()