# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _ObjectRootFunctionsMaterial(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def index(self, ):

        return _rsf.object_material_index(self.rhino_id)


    def source(self, source=pythoncom.Empty):

        return _rsf.object_material_source(self.rhino_id, source)

