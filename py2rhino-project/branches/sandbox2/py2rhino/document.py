# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class Document(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def objects_box_morph(cls, objects, box_points, copy=pythoncom.Empty):

        return _rsf.box_morph_object(map(lambda i: i.rhino_id, objects), box_points, copy)


    @classmethod
    def objects_copy(cls, objects, start=pythoncom.Empty, end=pythoncom.Empty):

        return _rsf.copy_objects(map(lambda i: i.rhino_id, objects), start, end)


    @classmethod
    def objects_copy_and_xform(cls, objects, translation=pythoncom.Empty):

        return _rsf.copy_objects_2(map(lambda i: i.rhino_id, objects), translation)


    @classmethod
    def objects_delete(cls, objects):

        return _rsf.delete_objects(map(lambda i: i.rhino_id, objects))


    @classmethod
    def objects_enable_render_mesh(cls, objects, enable=pythoncom.Empty):

        return _rsf.enable_object_mesh(map(lambda i: i.rhino_id, objects), enable)


    def curves_explode(self, objects, delete=pythoncom.Empty):

        return _rsf.explode_curves(map(lambda i: i.rhino_id, objects), delete)


    @classmethod
    def objects_flash(cls, objects, style=pythoncom.Empty):

        return _rsf.flash_object(map(lambda i: i.rhino_id, objects), style)


    @classmethod
    def objects_hide(cls, objects):

        return _rsf.hide_objects(map(lambda i: i.rhino_id, objects))


    @classmethod
    def objects_lock(cls, objects):

        return _rsf.lock_objects(map(lambda i: i.rhino_id, objects))


    @classmethod
    def objects_reset_attributes(cls, targets, source):

        return _rsf.match_object_attributes(map(lambda i: i.rhino_id, targets), source.rhino_id)


    @classmethod
    def objects_mirror(cls, objects, start_pt, end_pt, copy=pythoncom.Empty):

        return _rsf.mirror_objects(map(lambda i: i.rhino_id, objects), start_pt, end_pt, copy)


    @classmethod
    def objects_move(cls, objects, start, end):

        return _rsf.move_objects(map(lambda i: i.rhino_id, objects), start, end)


    @classmethod
    def objects_move_and_xform(cls, objects, translation):

        return _rsf.move_objects_2(map(lambda i: i.rhino_id, objects), translation)


    @classmethod
    def objects_color(cls, objects, color=pythoncom.Empty):

        return _rsf.object_color(map(lambda i: i.rhino_id, objects), color)


    @classmethod
    def objects_color_source(cls, objects, source=pythoncom.Empty):

        return _rsf.object_color_source(map(lambda i: i.rhino_id, objects), source)


    @classmethod
    def objects_layer(cls, objects, layer=pythoncom.Empty):

        return _rsf.object_layer(map(lambda i: i.rhino_id, objects), layer.rhino_id)


    @classmethod
    def objects_linetype(cls, objects, layer=pythoncom.Empty):

        return _rsf.object_linetype(map(lambda i: i.rhino_id, objects), layer.rhino_id)


    @classmethod
    def objects_linetype_source(cls, objects, source=pythoncom.Empty):

        return _rsf.object_linetype_source(map(lambda i: i.rhino_id, objects), source)


    @classmethod
    def objects_material_source(cls, objects, source=pythoncom.Empty):

        return _rsf.object_material_source(map(lambda i: i.rhino_id, objects), source)


    @classmethod
    def objects_name(cls, objects, names=pythoncom.Empty):

        return _rsf.object_names(map(lambda i: i.rhino_id, objects), names)


    @classmethod
    def objects_print_color(cls, objects, color=pythoncom.Empty):

        return _rsf.object_print_color(map(lambda i: i.rhino_id, objects), color)


    @classmethod
    def objects_print_color_source(cls, objects, source=pythoncom.Empty):

        return _rsf.object_print_color_source(map(lambda i: i.rhino_id, objects), source)


    @classmethod
    def objects_print_width(cls, objects, width=pythoncom.Empty):

        return _rsf.object_print_width(map(lambda i: i.rhino_id, objects), width)


    @classmethod
    def objects_print_width_source(cls, objects, source=pythoncom.Empty):

        return _rsf.object_print_width_source(map(lambda i: i.rhino_id, objects), source)


    @classmethod
    def objects_url(cls, objects, url=pythoncom.Empty):

        return _rsf.object_u_r_l(map(lambda i: i.rhino_id, objects), url)


    @classmethod
    def objects_orient(cls, objects, reference, target, flags=pythoncom.Empty):

        return _rsf.orient_objects(map(lambda i: i.rhino_id, objects), reference, target, flags)


    def curves_project_to_surface(self, curves, surfaces, direction):

        return _rsf.project_curve_to_surface(map(lambda i: i.rhino_id, curves), surfaces, direction)


    @classmethod
    def objects_remap(cls, _Object, src_plane, dst_plane, copy=pythoncom.Empty):

        return _rsf.remap_objects(map(lambda i: i.rhino_id, _Object), src_plane, dst_plane, copy)


    @classmethod
    def objects_rotate(cls, objects, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):

        return _rsf.rotate_objects(map(lambda i: i.rhino_id, objects), point, angle, axis, copy)


    @classmethod
    def objects_scale(cls, objects, origin, scale, copy=pythoncom.Empty):

        return _rsf.scale_objects(map(lambda i: i.rhino_id, objects), origin, scale, copy)


    @classmethod
    def objects_select(cls, objects):

        return _rsf.select_objects(map(lambda i: i.rhino_id, objects))


    @classmethod
    def objects_shear(cls, objects, origin, ref_pt, scale, copy=pythoncom.Empty):

        return _rsf.shear_objects(map(lambda i: i.rhino_id, objects), origin, ref_pt, scale, copy)


    @classmethod
    def objects_show(cls, objects):

        return _rsf.show_objects(map(lambda i: i.rhino_id, objects))


    @classmethod
    def objects_transform(cls, objects, matrix, copy=pythoncom.Empty):

        return _rsf.transform_objects(map(lambda i: i.rhino_id, objects), matrix, copy)


    @classmethod
    def objects_unlock(cls, objects):

        return _rsf.unlock_objects(map(lambda i: i.rhino_id, objects))


    @classmethod
    def objects_unselect(cls, objects):

        return _rsf.unselect_objects(map(lambda i: i.rhino_id, objects))

