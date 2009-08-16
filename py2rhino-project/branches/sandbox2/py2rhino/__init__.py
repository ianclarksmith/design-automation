
#version
_version = "0.1.3"
#===============================================================================
# Make a connection to Rhino
#===============================================================================
from win32com.client import Dispatch
import time
app = Dispatch("Rhino4.Interface")
time.sleep(1)
app.Visible = True
_rso = app.GetScriptObject

from wrappers._rhinoscript_functions import _RhinoscriptFunctions
_rsf = _RhinoscriptFunctions(_rso)

import _rhinoscript_classes
_rhinoscript_classes._rsf = _rsf
#===============================================================================
# Import modules
#===============================================================================
import _util
import obj
import ent
import doc
import app

import util.vector
util.vector._rsf = _rsf
