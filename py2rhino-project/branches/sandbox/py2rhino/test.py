from py2rhino.application import Application
import array


app = Application()
app.visible()
print app


rs = app.get_script_object()
print rs

for k in rs.__dict__.keys():
    print k, rs.__dict__[k]

print type(rs.AddLayer)

"""
from comtypes.client import GetModule
GetModule("C:\\Program Files\\Rhinoceros 4.0\\Plug-ins\\RhinoScript.tlb")
GetModule("C:\\Program Files\\Rhinoceros 4.0\\System\\Rhino4.tlb")
"""

print "done"
