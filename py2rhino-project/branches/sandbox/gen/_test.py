from win32com.client.dynamic import Dispatch
import time
from curve import Curve
from surface_and_polysurface import SurfaceAndPolysurface

#set up the connection
app = Dispatch("Rhino4.Interface")
time.sleep(1)
app.Visible = True
script_object = app.GetScriptObject

#test a simple method
cv = Curve(script_object)
print cv.add_line((0,0,0), (10,10,0))

#create some curves
cv1 = cv.add_curve(((0,0,0),(10,0,0),(20,0,0),(3,0,0)), 3)
cv2 = cv.add_curve(((0,0,10),(10,0,10),(20,0,10),(3,0,10)), 3)
cv3 = cv.add_curve(((0,0,20),(10,0,20),(20,0,20),(3,0,20)), 3)

#create a loft
sf = SurfaceAndPolysurface(script_object)
sf.add_loft_srf((cv1, cv2, cv3), (0,0,0), (0,0,20), 0, 0, 10, False )