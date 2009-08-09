from win32com.client import Dispatch
import time
_app = Dispatch("Rhino4.Interface")
time.sleep(1)
_app.Visible = True

from functions._rhinoscript_functions import _RhinoscriptFunctions
_rsf = _RhinoscriptFunctions(_app.GetScriptObject)

import _rhinoscript_classes
_rhinoscript_classes._rsf = _rsf

import _util
import obj