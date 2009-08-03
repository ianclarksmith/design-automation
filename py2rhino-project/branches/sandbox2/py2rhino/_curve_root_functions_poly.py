# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util

_rsf = None

class _CurveRootFunctionsPoly(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def explode(self, delete=pythoncom.Empty):

        return map(lambda i: _CurveRoot(i), rhino_id)

