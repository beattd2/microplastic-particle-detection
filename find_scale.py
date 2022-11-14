"""

"""
import numpy as np
import pytesseract
from PIL import Image
import detect_particles as dp


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
    (center(x, y), (width, height), angle of rotation)"""
    scale_text = '500um'
    pos = "".join(str(x) for x in characters[:,0]).find(scale_text)
    return characters[pos,1:]

def get_position_of_scale(image):
    return find_center_of_scale(image_to_text(image))

def get_scale_contour(file):
    img, gray, thresh = dp.pre_process(file)
    contours = dp.get_contours(img, gray, thresh)

    print(get_position_of_scale(file))
    #for cont in contours:




