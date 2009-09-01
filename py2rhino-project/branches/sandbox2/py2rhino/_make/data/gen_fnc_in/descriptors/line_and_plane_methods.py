#The data below will be used to generate the Rhinoscript function wrappers

#===============================================================================
# line
#===============================================================================
class line(object):    
    folder = "util"

    class Functions(object):
        
        line_plane = {
            "method_name": "line_pln",
            "method_parameters": (("line","array_of dbl","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        line_transform = {
            "method_name": "xform",
            "method_parameters": (("line","array_of dbl","REQ"),("xform","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }
        
        #distances
        line_closest_point = {
            "method_name": "closest_pnt",
            "method_parameters": (("line","array_of dbl","REQ"),("point","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }
        line_max_distance_to = {
            "method_name": "max_distance_to_pnt",
            "method_parameters": (("line","array_of dbl","REQ"),("point","array_of dbl","REQ")),
            "method_returns": ("bln","null")
            }
        line_max_distance_to_2 = {
            "method_name": "max_distance_to_line",
            "method_parameters": (("line_1","array_of dbl","REQ"),("line_2","array_of dbl","REQ")),
            "method_returns": ("bln","null")
            }
        line_min_distance_to = {
            "method_name": "min_distance_to_pnt",
            "method_parameters": (("line","array_of dbl","REQ"),("point","array_of dbl","REQ")),
            "method_returns": ("bln","null")
            }
        line_min_distance_to_2 = {
            "method_name": "min_distance_to_line",
            "method_parameters": (("line_1","array_of dbl","REQ"),("line_2","array_of dbl","REQ")),
            "method_returns": ("bln","null")
            }

        #intersection
        line_line_intersection = {
            "method_name": "intersect_2_lines",
            "method_parameters": (("line_1","array_of dbl","REQ"),("line_2","array_of dbl","REQ"),("planar","bln","OPT")),
            "method_returns": ("array_of dbl","null")
            }        
        line_plane_intersection = {
            "method_name": "intersect_pln",
            "method_parameters": (("line","array_of dbl","REQ"),("plane","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }


        """
        line_is_farther_than = {
            "method_name": "is_farther_than",
            "method_parameters": (("line","array_of dbl","REQ"),("distance","dbl","REQ"),("point","array_of dbl","REQ")),
            "method_returns": ("bln","null")
            }
        line_is_farther_than_2 = {
            "method_name": "is_farther_than_2",
            "method_parameters": (("line","array_of dbl","REQ"),("distance","dbl","REQ"),("line_2","array_of dbl","REQ")),
            "method_returns": ("bln","null")
            }
        """

#===============================================================================
# plane
#===============================================================================
class plane(object):    
    folder = "util"

    class Functions(object):
        
        
        distance_to_plane = {
            "method_name": "distance_to_pln",
            "method_parameters": (("plane","array_of dbl","REQ"),("point","array_of dbl","REQ")),
            "method_returns": ("dbl","null")
            }
        plane_closest_point = {
            "method_name": "closest_pnt",
            "method_parameters": (("plane","array_of dbl","REQ"),("point","array_of dbl","REQ"),("return_point","bln","OPT")),
            "method_returns": ("array_of dbl","null")
            }        
        evaluate_plane = {
            "method_name": "evaluate",
            "method_parameters": (("plane","array_of dbl","REQ"),("parameter","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }
        intersect_planes = {
            "method_name": "intersect_3_plns",
            "method_parameters": (("plane_1","array_of dbl","REQ"),("plane_2","array_of dbl","REQ"),("plane_3","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }
        plane_plane_intersection = {
            "method_name": "intersect_2_plns",
            "method_parameters": (("plane_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }
        
        #transform
        move_plane = {
            "method_name": "move",
            "method_parameters": (("plane","array_of dbl","REQ"),("origin","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }
        rotate_plane = {
            "method_name": "rotate",
            "method_parameters": (("plane","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }
        plane_transform = {
            "method_name": "xform",
            "method_parameters": (("plane","array_of dbl","REQ"),("xform","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }        

        
        #creation
        plane_equation = {
            "method_name": "equation",
            "method_parameters": (("plane","array_of dbl","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        plane_fit_from_points = {
            "method_name": "fit_from_pnts",
            "method_parameters": (("points","array_of dbl","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        plane_from_frame = {
            "method_name": "from_frame",
            "method_parameters": (("origin","array_of dbl","REQ"),("xaxis","array_of dbl","REQ"),("yaxis","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }
        plane_from_normal = {
            "method_name": "from_normal",
            "method_parameters": (("origin","array_of dbl","REQ"),("normal","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }
        plane_from_points = {
            "method_name": "from_pnts",
            "method_parameters": (("origin","array_of dbl","REQ"),("point_x","array_of dbl","REQ"),("point_y","array_of dbl","REQ")),
            "method_returns": ("array_of dbl","null")
            }


        
        
        world_x_y_plane = {
            "method_name": "world_x_y_plane",
            "method_parameters": (),
            "method_returns": ("array_of dbl",)
            }
        world_y_z_plane = {
            "method_name": "world_y_z_plane",
            "method_parameters": (),
            "method_returns": ("array_of dbl",)
            }
        world_z_x_plane = {
            "method_name": "world_z_x_plane",
            "method_parameters": (),
            "method_returns": ("array_of dbl",)
            }
