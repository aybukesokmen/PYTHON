import cv2
import numpy as np

resim1=cv2.imread("1.png")
resim2=cv2.imread("2.png")

bit_and=cv2.bitwise_and(resim1,resim2)
bit_or=cv2.bitwise_or(resim1,resim2)
bit_xor=cv2.bitwise_xor(resim1,resim2)




cv2.imshow("ilk resim:",resim1)
cv2.imshow("ikinci resim",resim2)
cv2.imshow("bitwise and:",bit_and)
cv2.imshow("bitwise or",bit_or)
cv2.imshow("bitwise xor",bit_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()