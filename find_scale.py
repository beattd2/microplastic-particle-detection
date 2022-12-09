'''
Functions allow user to submit images of any size and have the image's scale programatically determined. 
Implementation unfinished, for now it's assumed image sizes are correct.
'''

import numpy as np
import pytesseract
from PIL import Image
import detect_particles as dp
from itertools import chain


def image_to_text(image):
    """Takes in image and returns a 2d array of all characters detected and their respective positional data."""
    NUM_COLUMNS = 6
    img = Image.open(image)
    ocr_data = pytesseract.image_to_boxes(img)
    ocr_data = ocr_data.split()
    rows = int(len(ocr_data) / NUM_COLUMNS)
    ocr_data = np.asarray(ocr_data).reshape(rows, NUM_COLUMNS)
    return ocr_data

def find_center_of_scale(characters):
    """Returns position of first character of scale text ('500um')
    (center(x, y), (width, height), angle of rotation)--> don't believe this is correct
    Believe this is formatted x1, y1, x2, y2, angle of rotation."""
    scale_text = '500um'
    pos = "".join(str(x) for x in characters[:,0]).find(scale_text)
    return characters[pos,1:]

def get_position_of_scale(image):
    return find_center_of_scale(image_to_text(image))

def get_scale_contour(file, TESTING = False):
    """Use function to get the contour of the bounding box around the scale.
    When Testing == True, bounding box around scale contour will be drawn."""
    #Todo: fix img/file inconsistencies
    img, gray, thresh = dp.pre_process(file)
    contours = dp.get_contours(img, gray, thresh)
    pos = get_position_of_scale(file)
    result = img.copy()
    cont_tmp = list(chain.from_iterable(contours[1]))
    p1, p2, p3, p4 = cont_tmp[0], cont_tmp[1], cont_tmp[2], cont_tmp[3]

    for cont in contours:
        cont_simp = list(chain.from_iterable(cont))#list(chain.from_iterable(contours[1]))
        print(len(cont_simp))
        print(cont_simp)
        print('\n')
        if(len(cont_simp) < 0):
            p1, p2, p3, p4 = cont_simp[0], cont_simp[1], cont_simp[2], cont_simp[3]
            min_x, min_y = min(p1[0], p2[0], p3[0], p3[0]), min(p1[1], p2[1], p3[1], p3[1])
            max_x, max_y = max(p1[0], p2[0], p3[0], p3[0]), max(p1[1], p2[1], p3[1], p3[1])
            #cont = list(chain.from_iterable(cont))
            #is position of scale within bounding box?
            #print(sum(int(pos[0]), int(pos[2]))/2)
            avg_pos_x = (int(pos[0]) + int(pos[2])) / 2
            avg_pos_y = (int(pos[1]) + int(pos[3])) / 2
            print('MinX: {}, MaxX: {}'.format(min_x, max_x))
            print('MinY: {}, MaxY: {}'.format(min_y ,max_y))
            print(avg_pos_x, avg_pos_y)
            if avg_pos_x in range(min_x, max_x) and avg_pos_y in range(min_y, max_y):
                result = dp.draw_contour(result, cont)
                print('Found.')
                break
    if TESTING:
        dp.show_result(result)

def is_in_contour(contours, pos):
    None



