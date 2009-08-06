from win32com.client import Dispatch
import time
_app = Dispatch("Rhino4.Interface")
time.sleep(1)
_app.Visible = True
_rso = _app.GetScriptObject

from functions._rhinoscript_functions import _RhinoscriptFunctions
_rsf = _RhinoscriptFunctions(_rso)

import _rhinoscript_classes
_rhinoscript_classes._rsf = _rsf

import _util
from _rhinoscript_classes import Arc
from _rhinoscript_classes import Box
from _rhinoscript_classes import Circle
from _rhinoscript_classes import Cone
from _rhinoscript_classes import Cylinder
from _rhinoscript_classes import Ellipse
from _rhinoscript_classes import EllipticalArc
from _rhinoscript_classes import GenericCurve
from _rhinoscript_classes import GenericObject
from _rhinoscript_classes import Line
from _rhinoscript_classes import NurbsCurve
from _rhinoscript_classes import NurbsSurface
from _rhinoscript_classes import PlaneSurface
from _rhinoscript_classes import PolySurface
from _rhinoscript_classes import Polyline
from _rhinoscript_classes import Sphere
from _rhinoscript_classes import Torus
