import detect_particles as dp
import find_scale


file = 'data/images/A.jpg'

#print(find_scale.get_position_of_scale(file))
#img, gray, thresh = dp.pre_process(file)
#contours = dp.get_contours(img, gray, thresh)
#dp.draw_all_contours(img, contours, SHOW_RESULT=True)
find_scale.get_scale_contour(file)