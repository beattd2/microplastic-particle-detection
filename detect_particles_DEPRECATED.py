import cv2
import numpy as np


# read image
root = 'data/images/'
img_name = 'A.jpg'


#img = cv2.imread(root + img_name)
img = cv2.imread('data/images/A.jpg')

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# threshold
thresh = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)[1]

# get contours
result = img.copy()
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

"""
for cntr in contours:
    #x,y,w,h = cv2.boundingRect(cntr)
    cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 2)
    print("x,y,w,h:",x,y,w,h)
"""

for cntr in contours:
    #(center(x, y), (width, height), angle of rotation) = cv2.minAreaRect(points)
    #rect = cv2.minAreaRect(cntr)
    #box = cv2.boxPoints(rect) # cv2.boxPoints(rect) for OpenCV 3.x
    box = np.int0(box)
    cv2.drawContours(result,[box],0,(0,0,255),2)

# save resulting image
cv2.imwrite('rotated_two_blobs_result.jpg',result)      

# show thresh and result    
cv2.imshow("bounding_box", result)
cv2.waitKey(0)
cv2.destroyAllWindows()