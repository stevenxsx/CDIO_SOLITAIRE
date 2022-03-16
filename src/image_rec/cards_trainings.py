
import cv2 
import os

from cv2 import imread
import cards

os_path = os.path.dirname(os.path.abspath(__file__))
img_path = "/resources/androidparty.png"
process_picture = cards.process_taken_image(img_path)

img = imread( os_path + img_path)
#contours = cards.find_cards_in_picture(process_picture)
#canny = cv2.Canny(process_picture, 125, 175)
#print(process_picture)
cv2.imshow("process picture", process_picture[1])
cv2.imshow("nyt", img)
#cv2.imshow("picture", process_picture)
cv2.waitKey(10000)