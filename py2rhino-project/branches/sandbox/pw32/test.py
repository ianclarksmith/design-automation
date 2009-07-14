"""from pw32 import RhinoConnection
RhinoConnection.rhino.AddText("Hello Rhino", (0,0,0))
RhinoConnection.rhino.AddPoint((5,5,5))
RhinoConnection.rhino.AddLine((0,0,0), (10,10,0))
"""

import win32com
import time
from pw32.rhinoscript2 import IRhinoScript


app = win32com.client.Dispatch("Rhino4.Interface")
time.sleep(1)
app.Visible = True
rhino = IRhinoScript(app.GetScriptObject)
rhino.AddLine((0,0,0), (10,-10,0))



print "done"