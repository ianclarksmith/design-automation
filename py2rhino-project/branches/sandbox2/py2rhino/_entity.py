# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class _Entity(p2r.object):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    def background_bitmap(self, file_name=pythoncom.Empty, point=pythoncom.Empty, width=pythoncom.Empty):

        return p2r_f.background_bitmap(self.rhino_id, file_name, point, width)


    def current_detail(self, detail=pythoncom.Empty, return_names=pythoncom.Empty):

        return p2r_f.current_detail(self.rhino_id, detail, return_names)


    def detail_names(self, return_names=pythoncom.Empty):

        return p2r_f.detail_names(self.rhino_id, return_names)


    def is_background_bitmap(self, ):

        return p2r_f.is_background_bitmap(self.rhino_id)


    def is_detail(self, detail):

        return p2r_f.is_detail(self.rhino_id, detail)


    def is_hatch(self, ):

        return p2r_f.is_hatch(self.rhino_id)


    def is_hatch_pattern(self, ):

        return p2r_f.is_hatch_pattern(self.rhino_id)


    def is_hatch_pattern_current(self, ):

        return p2r_f.is_hatch_pattern_current(self.rhino_id)


    def is_hatch_pattern_reference(self, ):

        return p2r_f.is_hatch_pattern_reference(self.rhino_id)


    def is_layer(self, ):

        return p2r_f.is_layer(self.rhino_id)


    def is_layer_changeable(self, ):

        return p2r_f.is_layer_changeable(self.rhino_id)


    def is_layer_child_of(self, test):

        return p2r_f.is_layer_child_of(self.rhino_id, test)


    def is_layer_current(self, ):

        return p2r_f.is_layer_current(self.rhino_id)


    def is_layer_empty(self, ):

        return p2r_f.is_layer_empty(self.rhino_id)


    def is_layer_expanded(self, ):

        return p2r_f.is_layer_expanded(self.rhino_id)


    def is_layer_locked(self, ):

        return p2r_f.is_layer_locked(self.rhino_id)


    def is_layer_on(self, ):

        return p2r_f.is_layer_on(self.rhino_id)


    def is_layer_parent_of(self, test):

        return p2r_f.is_layer_parent_of(self.rhino_id, test)


    def is_layer_reference(self, ):

        return p2r_f.is_layer_reference(self.rhino_id)


    def is_layer_selectable(self, ):

        return p2r_f.is_layer_selectable(self.rhino_id)


    def is_layer_visible(self, ):

        return p2r_f.is_layer_visible(self.rhino_id)


    def is_layout(self, ):

        return p2r_f.is_layout(self.rhino_id)


    def is_view(self, ):

        return p2r_f.is_view(self.rhino_id)


    def is_view_current(self, ):

        return p2r_f.is_view_current(self.rhino_id)


    def is_view_maximized(self, ):

        return p2r_f.is_view_maximized(self.rhino_id)


    def is_view_perspective(self, ):

        return p2r_f.is_view_perspective(self.rhino_id)


    def is_view_title_visible(self, ):

        return p2r_f.is_view_title_visible(self.rhino_id)


    def is_wallpaper(self, ):

        return p2r_f.is_wallpaper(self.rhino_id)


    def show_grid(self, show=pythoncom.Empty):

        return p2r_f.show_grid(self.rhino_id, show)


    def show_grid_axes(self, show=pythoncom.Empty):

        return p2r_f.show_grid_axes(self.rhino_id, show)


    def show_view_title(self, state=pythoncom.Empty):

        return p2r_f.show_view_title(self.rhino_id, state)


    def show_world_axes(self, show=pythoncom.Empty):

        return p2r_f.show_world_axes(self.rhino_id, show)


    def synchronize_c_planes(self, ):

        return p2r_f.synchronize_c_planes(self.rhino_id)


    def tilt_view(self, direction=pythoncom.Empty, angle=pythoncom.Empty):

        return p2r_f.tilt_view(self.rhino_id, direction, angle)


    def view_c_plane(self, plane=pythoncom.Empty):

        return p2r_f.view_c_plane(self.rhino_id, plane)


    def view_names(self, return_names=pythoncom.Empty, type=pythoncom.Empty):

        return p2r_f.view_names(return_names, type)


    def view_near_corners(self, ):

        return p2r_f.view_near_corners(self.rhino_id)


    def wallpaper(self, file_name=pythoncom.Empty):

        return p2r_f.wallpaper(self.rhino_id, file_name)


    def wallpaper_gray_scale(self, gray_scale=pythoncom.Empty):

        return p2r_f.wallpaper_gray_scale(self.rhino_id, gray_scale)


    def wallpaper_hidden(self, hidden=pythoncom.Empty):

        return p2r_f.wallpaper_hidden(self.rhino_id, hidden)


    def zoom_bounding_box(self, corners, view=pythoncom.Empty, all=pythoncom.Empty):

        return p2r_f.zoom_bounding_box(corners, view, all)


    def zoom_extents(self, all=pythoncom.Empty):

        return p2r_f.zoom_extents(self.rhino_id, all)


    def zoom_selected(self, all=pythoncom.Empty):

        return p2r_f.zoom_selected(self.rhino_id, all)

