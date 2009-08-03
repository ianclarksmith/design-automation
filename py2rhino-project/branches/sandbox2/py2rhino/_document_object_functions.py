# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util


_rsf = None


class _DocumentObjectFunctions(object):

    # Class constructor
    def __init__(self, rhino_id, _class, _rsf_in):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    @classmethod
    def box_morph(cls, objects, box_points, copy=pythoncom.Empty):

    @classmethod
    def copy(cls, objects, start=pythoncom.Empty, end=pythoncom.Empty):

    @classmethod
    def copy_and_xform(cls, objects, translation=pythoncom.Empty):

    @classmethod
    def delete(cls, objects):

    @classmethod
    def enable_render_mesh(cls, objects, enable=pythoncom.Empty):

    @classmethod
    def curves_explode(cls, objects, delete=pythoncom.Empty):

    @classmethod
    def flash(cls, objects, style=pythoncom.Empty):

    @classmethod
    def hide(cls, objects):

    @classmethod
    def is_object(cls, rhino_id):

    @classmethod
    def lock(cls, objects):

    @classmethod
    def reset_attributes(cls, targets):

    @classmethod
    def mirror(cls, objects, start_pt, end_pt, copy=pythoncom.Empty):

    @classmethod
    def move(cls, objects, start, end):

    @classmethod
    def move_and_xform(cls, objects, translation):

    @classmethod
    def color(cls, objects, color=pythoncom.Empty):

    @classmethod
    def color_source(cls, objects, source=pythoncom.Empty):

    @classmethod
    def layer(cls, objects, layer=pythoncom.Empty):

    @classmethod
    def linetype(cls, objects, layer=pythoncom.Empty):

    @classmethod
    def linetype_source(cls, objects, source=pythoncom.Empty):

    @classmethod
    def material_source(cls, objects, source=pythoncom.Empty):

    @classmethod
    def name(cls, objects, names=pythoncom.Empty):

    @classmethod
    def print_color(cls, objects, color=pythoncom.Empty):

    @classmethod
    def print_color_source(cls, objects, source=pythoncom.Empty):

    @classmethod
    def print_width(cls, objects, width=pythoncom.Empty):

    @classmethod
    def print_width_source(cls, objects, source=pythoncom.Empty):

    @classmethod
    def orient(cls, objects, reference, target, flags=pythoncom.Empty):

    @classmethod
    def curves_project_to_surface(cls, curves, surfaces, direction):

    @classmethod
    def remap(cls, _ObjectRoot, src_plane, dst_plane, copy=pythoncom.Empty):

    @classmethod
    def rotate(cls, objects, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):

    @classmethod
    def scale(cls, objects, origin, scale, copy=pythoncom.Empty):

    @classmethod
    def select(cls, objects):

    @classmethod
    def shear(cls, objects, origin, ref_pt, scale, copy=pythoncom.Empty):

    @classmethod
    def show(cls, objects):

    @classmethod
    def transform(cls, objects, matrix, copy=pythoncom.Empty):

    @classmethod
    def unlock(cls, objects):

    @classmethod
    def unselect(cls, objects):
