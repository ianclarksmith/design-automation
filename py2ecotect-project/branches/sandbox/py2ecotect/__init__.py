#win32 is required: http://python.net/crew/mhammond/win32/

#===============================================================================
# Make a connection to ecotect
#===============================================================================
import win32ui as _win32ui
import win32api as _win32api
import dde as _dde

#Create a conversation with Ecotect
_srv = _dde.CreateServer()
_srv.Create("Ecotect-Server") 
_app = _dde.CreateConversation(_srv)

#Create the connection
#Start Ecotect if necessary
try:
    _app.ConnectTo("Ecotect", "request")
except:
    _win32api.WinExec("C:\\Program Files\\Autodesk\\Ecotect 2009\\ecotect.exe")
    _app.ConnectTo("Ecotect", "request")
    
#print "conv = ", conversation
print "Connection with Ecotect successful..."
#===============================================================================
# Import classes
#===============================================================================

from _object import _Object
from _object import Point
from _object import Line
from _object import Roof
from _object import Floor
from _object import Ceiling
from _object import Wall
from _object import Partition
from _object import Void
from _object import Window
from _object import Panel
from _object import Door
from _object import Speaker
from _object import Light
from _object import Appliance
from _object import SolarCollector
from _object import Camera

from _application import Application
from _attribute import Attribute
from _calculation import Calculation
from _graph import Graph
from _grid import Grid
from _grid3d import Grid3D
from _masks import Masks
from _material import Material
from _model import Model
from _movie import Movie
from _node import Node
from _project_data import Project_Data
from _project import Project
from _radiance import Radiance
from _ray import Ray
from _rays import Rays
from _results import Results
from _schedule import Schedule
from _select import Select 
from _selection import Selection
from _shading import Shading
from _sunpath import Sunpath
from _timer import Timer
from _view import View 
from _weather import Weather
from _zone import Zone 

import _util

#===============================================================================
# Populate the lists in the Model object
#===============================================================================
import _model
_model._populate() 
