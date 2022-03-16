import cv2 
import os
import numpy as np

#Card size
CARD_MIN_AREA = 1000
CARD_MAX_AREA = 5000

class Train_card_rank:
    def __init__(self):
        self.img = []
        self.name = ""

class Train_card_suit:
    def __init__(self): 
        self.img = []
        self.name = ""


def process_taken_image(image_path):
    #os path
    os_path = os.path.dirname(os.path.abspath(__file__))
    #taken picture path
    taken_picture = cv2.imread(os_path + image_path)

    #make picture to gray
    picGray = cv2.cvtColor(taken_picture, cv2.COLOR_BGR2GRAY)
    #make picture to blur
    picBlur = cv2.GaussianBlur(picGray, (7,7), 0)

    taken_picture_w, taken_picture_h = np.shape(taken_picture)[:2]
    h = picGray[int(taken_picture_h/100)][int(taken_picture_w/2)]
    #g = picGray[int(taken_picture_h/5000)][int(taken_picture_w/20)]
    
    thresh = cv2.threshold(picBlur,h,255,cv2.THRESH_BINARY)
    
    return thresh

def find_cards_in_picture(process_picture):
    #make a hierarchy tree with contours with simple method from end to end of a line
    hierarchy, contours = cv2.findContours(process_picture, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    index_sort = sorted(range(len(contours)), key=lambda i : cv2.contourArea(contours[i]),reverse=True)

    #checks for number of items in the contours list
    if len(contours) == 0:
        return [], []
    
    #initialize lists
    hierarchy_list = []
    contours_list = []

    for i in index_sort:
        hierarchy_list = hierarchy_list.append[hierarchy[i]]
        contours_list = contours_list.append[contours[i]]

    for i in range(len(contours_list)):
        size = cv2.contourArea(contours_list[i])
        perimeter = cv2.arcLength(contours_list[i],True)
        approximating_shape = cv2.approxPolyDP(contours_list[i],0.01*perimeter,True)
        
        if ((size < CARD_MAX_AREA) and (size > CARD_MIN_AREA)
            and (hierarchy_list[i][3] == -1) and (len(approximating_shape) == 4)):
            contours_list[i] = 1
        
    
    return contours
    


    





