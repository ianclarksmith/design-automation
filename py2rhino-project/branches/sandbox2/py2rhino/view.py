# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class View(p2r._Entity):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    def add_named_view(self, view=pythoncom.Empty):

        return p2r_f.add_named_view(self.rhino_id, view)


    def current_view(self, return_name=pythoncom.Empty):

        return p2r_f.current_view(self.rhino_id, return_name)


    def delete_named_view(self, ):

        return p2r_f.delete_named_view(self.rhino_id)


    def maximize_restore_view(self, ):

        return p2r_f.maximize_restore_view(self.rhino_id)


    def named_views(self):

        return p2r_f.named_views()


    def rename_view(self, new_title):

        return p2r_f.rename_view(self.rhino_id, new_title)


    def restore_named_view(self, view=pythoncom.Empty, restore_bitmap=pythoncom.Empty):

        return p2r_f.restore_named_view(self.rhino_id, view, restore_bitmap)


    def rotate_camera(self, direction=pythoncom.Empty, angle=pythoncom.Empty):

        return p2r_f.rotate_camera(self.rhino_id, direction, angle)


    def rotate_view(self, direction=pythoncom.Empty, angle=pythoncom.Empty):

        return p2r_f.rotate_view(self.rhino_id, direction, angle)


    def view_camera(self, camera=pythoncom.Empty):

        return p2r_f.view_camera(self.rhino_id, camera)


    def view_camera_lens(self, length=pythoncom.Empty):

        return p2r_f.view_camera_lens(self.rhino_id, length)


    def view_camera_plane(self, ):

        return p2r_f.view_camera_plane(self.rhino_id)


    def view_camera_target(self, camera=pythoncom.Empty, target=pythoncom.Empty):

        return p2r_f.view_camera_target(self.rhino_id, camera, target)


    def view_camera_up(self, up_vector=pythoncom.Empty):

        return p2r_f.view_camera_up(self.rhino_id, up_vector)


    def view_display_mode_ex(self, mode=pythoncom.Empty, return_names=pythoncom.Empty):

        return p2r_f.view_display_mode_ex(self.rhino_id, mode, return_names)


    def view_display_mode_name(self, ):

        return p2r_f.view_display_mode_name(self.rhino_id)


    def view_display_modes(self, return_name=pythoncom.Empty):

        return p2r_f.view_display_modes(return_name)


    def view_projection(self, mode=pythoncom.Empty):

        return p2r_f.view_projection(self.rhino_id, mode)


    def view_radius(self, radius=pythoncom.Empty):

        return p2r_f.view_radius(self.rhino_id, radius)


    def view_size(self, ):

        return p2r_f.view_size(self.rhino_id)


    def view_target(self, target=pythoncom.Empty):

        return p2r_f.view_target(self.rhino_id, target)


    def view_title(self, ):

        return p2r_f.view_title(self.rhino_id)

