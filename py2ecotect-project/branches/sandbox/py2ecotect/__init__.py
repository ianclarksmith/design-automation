#win32 is required: http://python.net/crew/mhammond/win32/

#version
_version = "0.1.1"
#===============================================================================
# Make a connection to ecotect
#===============================================================================
import win32ui as _win32ui
import win32api as _win32api
import dde as _dde
import os as _os
import sys as _sys

#Check version
_eco_is_2009 = _os.path.exists("C:\\Program Files\\Autodesk\\Ecotect 2009\\ecotect.exe")
if not _eco_is_2009:
    print """
    The version of Ecotect cannot be detected. Please make sure you are using 
    version 2009, and start Ecotect before running your script.
    """

#Create a conversation with Ecotect
_srv = _dde.CreateServer()
_srv.Create("Ecotect-Server") 
_app = _dde.CreateConversation(_srv)

#Create the connection and start Ecotect if necessary
try:
    _app.ConnectTo("Ecotect", "request")
except:
    if _eco_is_2009:
        _win32api.WinExec("C:\\Program Files\\Autodesk\\Ecotect 2009\\ecotect.exe")
        _app.ConnectTo("Ecotect", "request")
    else:
        print "\n\nERROR: No connection possible."
        _sys.exit()
    
print "Connection with Ecotect successful..."
#===============================================================================
# Import modules
#===============================================================================
import _base

import app
import doc
import ent
import obj
#===============================================================================
# Populate the lists in the Model object
#===============================================================================
doc._populate() 
