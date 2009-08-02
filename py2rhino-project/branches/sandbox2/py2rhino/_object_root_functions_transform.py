# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _ObjectRootFunctionsTransform(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def box_morph(self, box_points, copy=pythoncom.Empty):

        return _rsf.box_morph_object(self.rhino_id, box_points, copy)


    def copy(self, start=pythoncom.Empty, end=pythoncom.Empty):

        return _rsf.copy_object(self.rhino_id, start, end)


    def copy_and_xform(self, translation=pythoncom.Empty):

        return _rsf.copy_object_2(self.rhino_id, translation)


    def mirror(self, start_pt, end_pt, copy=pythoncom.Empty):

        return _rsf.mirror_object(self.rhino_id, start_pt, end_pt, copy)


    def move(self, start, end):

        return _rsf.move_object(self.rhino_id, start, end)


    def move_and_xform(self, translation):

        return _rsf.move_object_2(self.rhino_id, translation)


    def orient(self, reference, target, flags=pythoncom.Empty):

        return _rsf.orient_object(self.rhino_id, reference, target, flags)


    def remap(self, src_plane, dst_plane, copy=pythoncom.Empty):

        return _rsf.remap_object(self.rhino_id, src_plane, dst_plane, copy)


    def rotate(self, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):

        return _rsf.rotate_object(self.rhino_id, point, angle, axis, copy)


    def scale(self, origin, scale, copy=pythoncom.Empty):

        return _rsf.scale_object(self.rhino_id, origin, scale, copy)


    def shear(self, origin, ref_pt, scale, copy=pythoncom.Empty):

        return _rsf.shear_object(self.rhino_id, origin, ref_pt, scale, copy)


    def transform(self, matrix, copy=pythoncom.Empty):

        return _rsf.transform_object(self.rhino_id, matrix, copy)

