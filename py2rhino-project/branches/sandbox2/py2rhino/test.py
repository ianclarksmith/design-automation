from win32com.client import Dispatch
import time 
#===============================================================================
# Make the connection
#===============================================================================
app = Dispatch("Rhino4.Interface")
time.sleep(1)
app.Visible = True
script_object = app.GetScriptObject

#===============================================================================
# Curves
#===============================================================================
from py2rhino.curve import Curve
curve = Curve(script_object)
# draw a line



spl = u'b54d0963-0772-463e-b579-39770b5612e4'
pl = u'c0080928-ca3d-40fa-b1db-deeb9338c036'
box = u'8d5ec6ff-2ae7-4fc3-b798-779ce882ae04'

pt1 = curve.curve_mid_point(box)
print type(pt1)
print pt1
print "done"
l1 = curve.add_line((0,0,0),pt1)