# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class _Object(p2r.object):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    def bounding_box(self, objects, view=pythoncom.Empty, world_coords=pythoncom.Empty):

        return p2r_f.bounding_box(objects, view, world_coords)


    def compare_geometry(self, object_0):

        return p2r_f.compare_geometry(self.rhino_id, object_0)


    def is_arc(self, index=pythoncom.Empty):

        return p2r_f.is_arc(self.rhino_id, index)


    def is_brep(self, ):

        return p2r_f.is_brep(self.rhino_id)


    def is_brep_manifold(self, ):

        return p2r_f.is_brep_manifold(self.rhino_id)


    def is_circle(self, index=pythoncom.Empty):

        return p2r_f.is_circle(self.rhino_id, index)


    def is_clipping_plane(self, ):

        return p2r_f.is_clipping_plane(self.rhino_id)


    def is_cone(self, ):

        return p2r_f.is_cone(self.rhino_id)


    def is_curve(self, index=pythoncom.Empty):

        return p2r_f.is_curve(self.rhino_id, index)


    def is_curve_closable(self, tolerance=pythoncom.Empty):

        return p2r_f.is_curve_closable(self.rhino_id, tolerance)


    def is_curve_closed(self, index=pythoncom.Empty):

        return p2r_f.is_curve_closed(self.rhino_id, index)


    def in_plane(self, plane=pythoncom.Empty):

        return p2r_f.is_curve_in_plane(self.rhino_id, plane)


    def is_curve_linear(self, index=pythoncom.Empty):

        return p2r_f.is_curve_linear(self.rhino_id, index)


    def is_curve_periodic(self, index=pythoncom.Empty):

        return p2r_f.is_curve_periodic(self.rhino_id, index)


    def is_curve_planar(self, index=pythoncom.Empty):

        return p2r_f.is_curve_planar(self.rhino_id, index)


    def is_curve_rational(self, index=pythoncom.Empty):

        return p2r_f.is_curve_rational(self.rhino_id, index)


    def is_cylinder(self, ):

        return p2r_f.is_cylinder(self.rhino_id)


    def is_ellipse(self, ):

        return p2r_f.is_ellipse(self.rhino_id)


    def is_group(self, ):

        return p2r_f.is_group(self.rhino_id)


    def is_line(self, index=pythoncom.Empty):

        return p2r_f.is_line(self.rhino_id, index)


    def is_parameter_on_surface(self, parameter):

        return p2r_f.is_parameter_on_surface(self.rhino_id, parameter)


    def is_plane_surface(self, ):

        return p2r_f.is_plane_surface(self.rhino_id)


    def is_point(self, ):

        return p2r_f.is_point(self.rhino_id)


    def is_point_cloud(self, ):

        return p2r_f.is_point_cloud(self.rhino_id)


    def is_point_in_surface(self, point):

        return p2r_f.is_point_in_surface(self.rhino_id, point)


    def is_point_on_curve(self, point, index=pythoncom.Empty):

        return p2r_f.is_point_on_curve(self.rhino_id, point, index)


    def is_point_on_surface(self, point):

        return p2r_f.is_point_on_surface(self.rhino_id, point)


    def is_poly_curve(self, index=pythoncom.Empty):

        return p2r_f.is_poly_curve(self.rhino_id, index)


    def is_poly_surface(self, ):

        return p2r_f.is_poly_surface(self.rhino_id)


    def is_poly_surface_closed(self, ):

        return p2r_f.is_poly_surface_closed(self.rhino_id)


    def is_poly_surface_planar(self, ):

        return p2r_f.is_poly_surface_planar(self.rhino_id)


    def is_polyline(self, index=pythoncom.Empty):

        return p2r_f.is_polyline(self.rhino_id, index)


    def is_sphere(self, ):

        return p2r_f.is_sphere(self.rhino_id)


    def is_surface(self, ):

        return p2r_f.is_surface(self.rhino_id)


    def is_surface_closed(self, direction):

        return p2r_f.is_surface_closed(self.rhino_id, direction)


    def is_surface_periodic(self, direction):

        return p2r_f.is_surface_periodic(self.rhino_id, direction)


    def is_surface_planar(self, tolerance=pythoncom.Empty):

        return p2r_f.is_surface_planar(self.rhino_id, tolerance)


    def is_surface_rational(self, ):

        return p2r_f.is_surface_rational(self.rhino_id)


    def is_surface_singular(self, direction):

        return p2r_f.is_surface_singular(self.rhino_id, direction)


    def is_surface_trimmed(self, ):

        return p2r_f.is_surface_trimmed(self.rhino_id)


    def is_text(self, ):

        return p2r_f.is_text(self.rhino_id)


    def is_text_dot(self, ):

        return p2r_f.is_text_dot(self.rhino_id)


    def is_torus(self, ):

        return p2r_f.is_torus(self.rhino_id)


    def remove_from_all_groups(self, ):

        return p2r_f.remove_object_from_all_groups(self.rhino_id)

