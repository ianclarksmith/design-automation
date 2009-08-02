# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _ObjectRootFunctionsState(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def flash(self, style=pythoncom.Empty):

        return _rsf.flash_object(self.rhino_id, style)


    def hide(self, ):

        return _rsf.hide_objects(self.rhino_id)


    def lock(self, ):

        return _rsf.lock_objects(self.rhino_id)


    def match_object_attributes(self, targets):

        return _rsf.match_object_attributes(map(lambda i: i.rhino_id, targets), self.rhino_id)


    def reset_object_attributes(self, source):

        return _rsf.match_object_attributes(self.rhino_id, source.rhino_id)


    def move_to_layout_space(self, layout=pythoncom.Empty, return_name=pythoncom.Empty):

        return _rsf.object_layout(self.rhino_id, layout, return_name)


    def select(self, ):

        return _rsf.select_objects(self.rhino_id)


    def show(self, ):

        return _rsf.show_objects(self.rhino_id)


    def unlock(self, ):

        return _rsf.unlock_objects(self.rhino_id)


    def unselect(self, ):

        return _rsf.unselect_objects(self.rhino_id)

