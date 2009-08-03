# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util

_rsf = None

class _ObjectRootFunctionsTransform(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def box_morph(self, box_points, copy=pythoncom.Empty):
        rhino_id = _rsf.box_morph_object(self.rhino_id, box_points, copy)
        if rhino_id:
            return _util.wrap(rhino_id)
        else:
            return None

    def copy(self, start=pythoncom.Empty, end=pythoncom.Empty):
        rhino_id = _rsf.copy_object(self.rhino_id, start, end)
        if rhino_id:
            return _ObjectRootFunctionsTransform(rhino_id)
        else:
            return None

    def copy_and_xform(self, translation=pythoncom.Empty):
        rhino_id = _rsf.copy_object_2(self.rhino_id, translation)
        if rhino_id:
            return _ObjectRootFunctionsTransform(rhino_id)
        else:
            return None

    def mirror(self, start_pt, end_pt, copy=pythoncom.Empty):
        rhino_id = _rsf.mirror_object(self.rhino_id, start_pt, end_pt, copy)
        if rhino_id:
            return _ObjectRootFunctionsTransform(rhino_id)
        else:
            return None

    def move(self, start, end):
        rhino_id = _rsf.move_object(self.rhino_id, start, end)
        if rhino_id:
            return _ObjectRootFunctionsTransform(rhino_id)
        else:
            return None

    def move_and_xform(self, translation):
        rhino_id = _rsf.move_object_2(self.rhino_id, translation)
        if rhino_id:
            return _ObjectRootFunctionsTransform(rhino_id)
        else:
            return None

    def orient(self, reference, target, flags=pythoncom.Empty):
        rhino_id = _rsf.orient_object(self.rhino_id, reference, target, flags)
        if rhino_id:
            return _ObjectRootFunctionsTransform(rhino_id)
        else:
            return None

    def remap(self, src_plane, dst_plane, copy=pythoncom.Empty):
        rhino_id = _rsf.remap_object(self.rhino_id, src_plane, dst_plane, copy)
        if rhino_id:
            return _util.wrap(rhino_id)
        else:
            return None

    def rotate(self, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):
        rhino_id = _rsf.rotate_object(self.rhino_id, point, angle, axis, copy)
        if rhino_id:
            return _ObjectRootFunctionsTransform(rhino_id)
        else:
            return None

    def scale(self, origin, scale, copy=pythoncom.Empty):
        rhino_id = _rsf.scale_object(self.rhino_id, origin, scale, copy)
        if rhino_id:
            return _ObjectRootFunctionsTransform(rhino_id)
        else:
            return None

    def shear(self, origin, ref_pt, scale, copy=pythoncom.Empty):
        rhino_id = _rsf.shear_object(self.rhino_id, origin, ref_pt, scale, copy)
        if rhino_id:
            return GenericObject(rhino_id)
        else:
            return None

    def transform(self, matrix, copy=pythoncom.Empty):
        rhino_id = _rsf.transform_object(self.rhino_id, matrix, copy)
        if rhino_id:
            return _util.wrap(rhino_id)
        else:
            return None
