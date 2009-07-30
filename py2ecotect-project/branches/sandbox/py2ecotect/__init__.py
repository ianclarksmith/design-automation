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
# Populate the lists in the Model object
#===============================================================================
import py2ecotect as p2e
from py2ecotect.object import _Object
from py2ecotect.model import Model
from py2ecotect.zone import Zone 
from py2ecotect.node import Node 
from py2ecotect.select import Select 
from py2ecotect.selection import Selection
from py2ecotect.view import View 
from py2ecotect import _util

p2e.model._populate() 
