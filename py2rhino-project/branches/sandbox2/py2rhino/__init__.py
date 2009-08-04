from win32com.client import Dispatch
import time
app = Dispatch("Rhino4.Interface")
time.sleep(1)
app.Visible = True
_rso = app.GetScriptObject

from functions._rhinoscript_functions import _RhinoscriptFunctions
_rsf = _RhinoscriptFunctions(_rso)

import _util
_util._rsf = _rsf
import arc
arc._rsf = _rsf
from arc import Arc
import box
box._rsf = _rsf
from box import Box
import circle
circle._rsf = _rsf
from circle import Circle
import cone
cone._rsf = _rsf
from cone import Cone
import cylinder
cylinder._rsf = _rsf
from cylinder import Cylinder
import ellipse
ellipse._rsf = _rsf
from ellipse import Ellipse
import elliptical_arc
elliptical_arc._rsf = _rsf
from elliptical_arc import EllipticalArc
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
import nurbs_surface
nurbs_surface._rsf = _rsf
from nurbs_surface import NurbsSurface
import plane_surface
plane_surface._rsf = _rsf
from plane_surface import PlaneSurface
import poly_surface
poly_surface._rsf = _rsf
from poly_surface import PolySurface
import polyline
polyline._rsf = _rsf
from polyline import Polyline
import sphere
sphere._rsf = _rsf
from sphere import Sphere
import torus
torus._rsf = _rsf
from torus import Torus
