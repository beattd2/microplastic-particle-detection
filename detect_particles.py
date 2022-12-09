import cv2
import numpy as np

#TODO: implement functions to save to file

def pre_process(file):
    img = cv2.imread(file)
    # convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)[1]
    return img, gray, thresh

#Following contour methods used to draw boxes around detected particles
def get_contours(img, gray, thresh):
    result = img.copy()
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    return contours

def draw_contour(img, cntr):
    result = img.copy()
    rect = cv2.minAreaRect(cntr)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(result,[box],0,(0,0,255),2)
    return result

def draw_largest_contour(img, contours, SHOW_RESULT = False):
    max_area = 0
    largest_contour = None
    for cont in contours:
        area = cv2.contourArea(cont)
        if area > max_area:
            largest_contour = cont
            max_area = area
    print(max_area)
    img = draw_contour(img, largest_contour)
    if SHOW_RESULT:
        show_result(img)

def draw_all_contours(img, contours, SHOW_RESULT = False):
    for cont in contours:
        img = draw_contour(img, cont)
    if SHOW_RESULT:
        show_result(img)
    return img

def show_result(result):   
    cv2.imshow("bounding_box", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#end contour methods

def write_image(result, fn):
    cv2.imwrite(fn,result) 

