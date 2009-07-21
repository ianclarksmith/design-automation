from win32com.client import Dispatch
import time 
"""
from object_grip import ObjectGrip
from user_interface import UserInterface
from geometry import Geometry
from hatch import Hatch
from layer import Layer
#from point_and_vector import PointAndVector
#from utility import Utility
from material import Material
from surface_and_polysurface import SurfaceAndPolysurface
from object import Object
from view import View
from block import Block
from light import Light
from user_data import UserData
from line_and_plane import LineAndPlane
from curve import Curve
from mesh import Mesh
from math import Math
from dimension import Dimension
from application import Application
from transformation import Transformation
from document import Document
from selection import Selection
from group import Group
from linetype import Linetype
"""
#Connect to Rhino
app = Dispatch("Rhino4.Interface")
time.sleep(1)
app.Visible = True
_rso = app.GetScriptObject