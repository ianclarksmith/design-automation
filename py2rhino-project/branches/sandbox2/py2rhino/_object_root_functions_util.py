# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _ObjectRootFunctionsUtil(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def description(self, ):

        return _rsf.object_description(self.rhino_id)


    def dump(self, type=pythoncom.Empty):

        return _rsf.object_dump(self.rhino_id, type)

