import detect_particles as dp
import find_scale as fs
import os

#file = 'data/images/A.jpg'

# assign directory
dir = 'data/images'
 
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if 'Measured' not in f:
            print('Processing {}...'.format(f))
            img, gray, thresh, file_name = dp.pre_process(f)
            contours = dp.get_contours(img, gray, thresh)
            dp.draw_all_contours(img, contours, file_name, SHOW_RESULT=False)
            dp.draw_largest_contour(img, contours, file_name, SHOW_RESULT=False)

"""
img, gray, thresh, file_name = dp.pre_process(file)
contours = dp.get_contours(img, gray, thresh)
dp.draw_all_contours(img, contours, file_name, SHOW_RESULT=False)
dp.draw_largest_contour(img, contours, file_name, SHOW_RESULT=False)
"""


#find_scale.get_scale_contour(file, TESTING=False)