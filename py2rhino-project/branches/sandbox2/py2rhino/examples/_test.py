#TESTING
#===============================================================================
# Curves
#===============================================================================
import py2rhino
from py2rhino.curve import Curve

co = Curve()
cv1 = co.add_line((0,0,0), (10,10,0))
length = co.curve_length(cv1)
print cv1
print length

cv2 = co.add_circle3_pt((0,0,0),(4,4,2),(1,2,3))
co.curve_area(cv2)

cv3 = co.add_curve(((0,0,0),(1,2,3),(3,4,5),(5,6,7)), 3)

