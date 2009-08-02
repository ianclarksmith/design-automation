# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _ObjectRootFunctionsGroups(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def groups(self, ):

        return _rsf.object_groups(self.rhino_id)


    def top_group(self, ):

        return _rsf.object_top_group(self.rhino_id)

