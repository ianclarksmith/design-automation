from rhinoCOM.RhinoScript import IRhinoScript
import win32com
import time


def connect():
    """returns a connection to Rhino."""
    Rhino = win32com.client.Dispatch("Rhino4.Interface")
    time.sleep(1)
    Rhino.Visible = True
    return Rhino

def getScriptObject(RhinoConnection):
    """returns a Rhino script object, on which RhinoScript methods can be called."""      
    ScriptObject = RhinoConnection.GetScriptObject
    return IRhinoScript(ScriptObject)
    
global rhino
try:
    rhino
except NameError:
    rhino = getScriptObject(connect())

