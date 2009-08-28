from win32com.client import Dispatch
import time
app = Dispatch("Rhino4.Interface")
time.sleep(1)
app.Visible = True
_rso = app.GetScriptObject

from _rhinoscript_functions import _RhinoscriptFunctions
_rsf = _RhinoscriptFunctions(_rso)

import application
application._rsf = _rsf
import block
block._rsf = _rsf
import curve
curve._rsf = _rsf
import dimension
dimension._rsf = _rsf
import document
document._rsf = _rsf
import geometry
geometry._rsf = _rsf
import group
group._rsf = _rsf
import hatch
hatch._rsf = _rsf
import layer
layer._rsf = _rsf
import light
light._rsf = _rsf
import line_and_plane
line_and_plane._rsf = _rsf
import linetype
linetype._rsf = _rsf
import material
material._rsf = _rsf
import math
math._rsf = _rsf
import mesh
mesh._rsf = _rsf
import object
object._rsf = _rsf
import object_grip
object_grip._rsf = _rsf
import point_and_vector
point_and_vector._rsf = _rsf
import selection
selection._rsf = _rsf
import surface_and_polysurface
surface_and_polysurface._rsf = _rsf
import transformation
transformation._rsf = _rsf
import user_data
user_data._rsf = _rsf
import user_interface
user_interface._rsf = _rsf
import utility
utility._rsf = _rsf
import view
view._rsf = _rsf
