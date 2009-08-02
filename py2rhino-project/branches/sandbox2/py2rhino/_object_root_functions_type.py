# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _ObjectRootFunctionsType(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def object_type(self, ):

        return _rsf.object_type(self.rhino_id)

