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
import document
document._rsf = _rsf
from document import Document
import ellipse
ellipse._rsf = _rsf
from ellipse import Ellipse
import line
line._rsf = _rsf
from line import Line
import nurbs_curve
nurbs_curve._rsf = _rsf
from nurbs_curve import NurbsCurve
import poly_curve
poly_curve._rsf = _rsf
from poly_curve import PolyCurve
import polyline
polyline._rsf = _rsf
from polyline import Polyline
import _curve_type
_curve_type._rsf = _rsf
from _curve_type import _CurveType
import _object
_object._rsf = _rsf
from _object import _Object
