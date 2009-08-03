from win32com.client import Dispatch
import time
app = Dispatch("Rhino4.Interface")
time.sleep(1)
app.Visible = True
_rso = app.GetScriptObject

from functions._rhinoscript_functions import _RhinoscriptFunctions
_rsf = _RhinoscriptFunctions(_rso)

import arc
arc._rsf = _rsf
from arc import Arc
import circle
circle._rsf = _rsf
from circle import Circle
import ellipse
ellipse._rsf = _rsf
from ellipse import Ellipse
import generic_curve
generic_curve._rsf = _rsf
from generic_curve import GenericCurve
import generic_object
generic_object._rsf = _rsf
from generic_object import GenericObject
import line
line._rsf = _rsf
from line import Line
import nurbs_curve
nurbs_curve._rsf = _rsf
from nurbs_curve import NurbsCurve
import polyline
polyline._rsf = _rsf
from polyline import Polyline


