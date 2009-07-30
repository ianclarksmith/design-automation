# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Document(object):


    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    def objects_box_morph(self, objects, box_points, copy=pythoncom.Empty):

        return p2r_f.box_morph_object(map(lambda i: i.rhino_id, objects), box_points, copy)


    def objects_copy(self, objects, start=pythoncom.Empty, end=pythoncom.Empty):

        return p2r_f.copy_objects(map(lambda i: i.rhino_id, objects), start, end)


    def objects_copy_and_xform(self, objects, translation=pythoncom.Empty):

        return p2r_f.copy_objects_2(map(lambda i: i.rhino_id, objects), translation)


    def objects_delete(self, objects):

        return p2r_f.delete_objects(map(lambda i: i.rhino_id, objects))


    def objects_enable_render_mesh(self, objects, enable=pythoncom.Empty):

        return p2r_f.enable_object_mesh(map(lambda i: i.rhino_id, objects), enable)


    def curves_explode(self, objects, delete=pythoncom.Empty):

        return p2r_f.explode_curves(map(lambda i: i.rhino_id, objects), delete)


    def objects_flash(self, objects, style=pythoncom.Empty):

        return p2r_f.flash_object(map(lambda i: i.rhino_id, objects), style)


    def objects_hide(self, objects):

        return p2r_f.hide_objects(map(lambda i: i.rhino_id, objects))


    def objects_lock(self, objects):

        return p2r_f.lock_objects(map(lambda i: i.rhino_id, objects))


    def objects_reset_attributes(self, targets, source):

        return p2r_f.match_object_attributes(map(lambda i: i.rhino_id, targets), source.rhino_id)


    def objects_mirror(self, objects, start_pt, end_pt, copy=pythoncom.Empty):

        return p2r_f.mirror_objects(map(lambda i: i.rhino_id, objects), start_pt, end_pt, copy)


    def objects_move(self, objects, start, end):

        return p2r_f.move_objects(map(lambda i: i.rhino_id, objects), start, end)


    def objects_move_and_xform(self, objects, translation):

        return p2r_f.move_objects_2(map(lambda i: i.rhino_id, objects), translation)


    def objects_color(self, objects, color=pythoncom.Empty):

        return p2r_f.object_color(map(lambda i: i.rhino_id, objects), color)


    def objects_color_source(self, objects, source=pythoncom.Empty):

        return p2r_f.object_color_source(map(lambda i: i.rhino_id, objects), source)


    def objects_layer(self, objects, layer=pythoncom.Empty):

        return p2r_f.object_layer(map(lambda i: i.rhino_id, objects), layer.rhino_id)


    def objects_linetype(self, objects, layer=pythoncom.Empty):

        return p2r_f.object_linetype(map(lambda i: i.rhino_id, objects), layer.rhino_id)


    def objects_linetype_source(self, objects, source=pythoncom.Empty):

        return p2r_f.object_linetype_source(map(lambda i: i.rhino_id, objects), source)


    def objects_material_source(self, objects, source=pythoncom.Empty):

        return p2r_f.object_material_source(map(lambda i: i.rhino_id, objects), source)


    def objects_name(self, objects, names=pythoncom.Empty):

        return p2r_f.object_names(map(lambda i: i.rhino_id, objects), names)


    def objects_print_color(self, objects, color=pythoncom.Empty):

        return p2r_f.object_print_color(map(lambda i: i.rhino_id, objects), color)


    def objects_print_color_source(self, objects, source=pythoncom.Empty):

        return p2r_f.object_print_color_source(map(lambda i: i.rhino_id, objects), source)


    def objects_print_width(self, objects, width=pythoncom.Empty):

        return p2r_f.object_print_width(map(lambda i: i.rhino_id, objects), width)


    def objects_print_width_source(self, objects, source=pythoncom.Empty):

        return p2r_f.object_print_width_source(map(lambda i: i.rhino_id, objects), source)


    def objects_url(self, objects, url=pythoncom.Empty):

        return p2r_f.object_u_r_l(map(lambda i: i.rhino_id, objects), url)


    def objects_orient(self, objects, reference, target, flags=pythoncom.Empty):

        return p2r_f.orient_objects(map(lambda i: i.rhino_id, objects), reference, target, flags)


    def curves_project_to_surface(self, curves, surfaces, direction):

        return p2r_f.project_curve_to_surface(map(lambda i: i.rhino_id, curves), surfaces, direction)


    def objects_remap(self, _Object, src_plane, dst_plane, copy=pythoncom.Empty):

        return p2r_f.remap_objects(map(lambda i: i.rhino_id, _Object), src_plane, dst_plane, copy)


    def objects_rotate(self, objects, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):

        return p2r_f.rotate_objects(map(lambda i: i.rhino_id, objects), point, angle, axis, copy)


    def objects_scale(self, objects, origin, scale, copy=pythoncom.Empty):

        return p2r_f.scale_objects(map(lambda i: i.rhino_id, objects), origin, scale, copy)


    def objects_select(self, objects):

        return p2r_f.select_objects(map(lambda i: i.rhino_id, objects))


    def objects_shear(self, objects, origin, ref_pt, scale, copy=pythoncom.Empty):

        return p2r_f.shear_objects(map(lambda i: i.rhino_id, objects), origin, ref_pt, scale, copy)


    def objects_show(self, objects):

        return p2r_f.show_objects(map(lambda i: i.rhino_id, objects))


    def objects_transform(self, objects, matrix, copy=pythoncom.Empty):

        return p2r_f.transform_objects(map(lambda i: i.rhino_id, objects), matrix, copy)


    def objects_unlock(self, objects):

        return p2r_f.unlock_objects(map(lambda i: i.rhino_id, objects))


    def objects_unselect(self, objects):

        return p2r_f.unselect_objects(map(lambda i: i.rhino_id, objects))

