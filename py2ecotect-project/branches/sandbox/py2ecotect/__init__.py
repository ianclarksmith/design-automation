#win32 is required: http://python.net/crew/mhammond/win32/

#===============================================================================
# Make a connection to ecotect
#===============================================================================
import win32ui
import win32api
import dde

#Create a conversation with Ecotect
server = dde.CreateServer()
server.Create("Ecotect-Server") 
conversation = dde.CreateConversation(server)

#Create the connection
#Start Ecotect if necessary
try:
    conversation.ConnectTo("Ecotect", "request")
except:
    win32api.WinExec("C:\\Program Files\\Autodesk\\Ecotect 2009\\ecotect.exe")
    conversation.ConnectTo("Ecotect", "request")
    
#print "conv = ", conversation
print "Connection with Ecotect successful..."
#===============================================================================
# Import classes
#===============================================================================

from object import _Object
from object import Point
from object import Line
from object import Roof
from object import Floor
from object import Ceiling
from object import Wall
from object import Partition
from object import Void
from object import Window
from object import Panel
from object import Door
from object import Speaker
from object import Light
from object import Appliance
from object import SolarCollector
from object import Camera

from application import Application
from attribute import Attribute
from calculation import Calculation
from graph import Graph
from grid import Grid
from grid3d import Grid3D
from masks import Masks
from material import Material
from model import Model
from node import Node
from project_data import Project_Data
from project import Project
from radiance import Radiance
from ray import Ray
from rays import Rays
from results import Results
from schedule import Schedule
from select import Select 
from selection import Selection
from shading import Shading
from sunpath import Sunpath
from timer import Timer
from view import View 
from weather import Weather
from zone import Zone 

import _util

#===============================================================================
# Populate the lists in the Model object
#===============================================================================
import model
model._populate() 
