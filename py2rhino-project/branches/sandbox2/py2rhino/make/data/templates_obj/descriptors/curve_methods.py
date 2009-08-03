#The data below will be used to generate the Rhinoscript function wrappers
#TODO: what is an elliptical arc?? If you shear and arc, you get an elliptical arc
#===============================================================================
# Document
#===============================================================================
class _DocumentObjectFunctions(object):
    inherits = None
    class ClassMethods(object):
        project_curve_to_surface = {#split
            "method_name": "curves_project_to_surface",
            "method_parameters": (("curves","array_of _ObjectRoot._CurveRoot","REQ"),("surfaces","array_of _ObjectRoot._SurfaceRoot","REQ"),("direction","array_of dbl","REQ"),),###
            "method_returns": ("array_of _ObjectRoot._CurveRoot.GenericCurve","null")
            }
        explode_curves = {#this has the delete parameter - polys only             
            "method_name": "curves_explode",
            "method_parameters": (("objects","array_of _ObjectRoot._CurveRoot","REQ"),("delete","bln","OPT"),),###
            "method_returns": ("array_of _ObjectRoot._CurveRoot.GenericCurve","null")#GenericCirve
            }
#===============================================================================
# _CurveRoot
#===============================================================================
class _CurveRoot(object):
    inherits = ("_ObjectRoot", )
    
    #TODO: move these constructors
    class Constructors(object):
        #these constructors create curves of unknown type
        #e.g. offestting an arc will produce an arc, offestting a nurbs curve will produce a nurbs curve
        #e.g. a sub curve of a circle is an arc
        
        #one option is just to copy these constructors to all curve objects and manually adjust the return values
        """
        split_curve = {#this has the delete parameter
            "method_name": "create_by_split",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot","null")
        }
        add_sub_crv = {#ed
            "method_name": "create_by_sub",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot","null")
        } """
        offset_curve = {#ed
            "method_name": "create_by_offset",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("direction","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT"),),
            "method_returns": ("array_of SELF","null")
        } 
    
#===============================================================================
# GenericCurve
#===============================================================================
class GenericCurve(object):
    inherits = ("_ObjectRoot._CurveRoot", )
    holds = {
                   
        #general object holds
        "properties": "_ObjectRootProperties",        
        "groups": "_ObjectRootFunctionsGroups",
        "materials": "_ObjectRootFunctionsMaterial",
        "render": "_ObjectRootFunctionsRender",
        "state": "_ObjectRootFunctionsState",
        "transform": "_ObjectRootFunctionsTransform",
        "util": "_ObjectRootFunctionsUtil",        
  
        #general curve holds
        "intersect": "_CurveRootFunctionsIntersect",
        "modify": "_CurveRootFunctionsModify",
        "manipulate": "_CurveRootFunctionsManipulate",
        "evaluate": "_CurveRootFunctionsEvaluate",
        "area": "_CurveRootFunctionsArea",
        "poly": "_CurveRootFunctionsPoly",
        "test": "_CurveRootFunctionsTest",#inherits from object tests
        "type": "_CurveRootFunctionsType",#exposed only here
    }
    
   
#===============================================================================
# NurbsCurve
#===============================================================================
class NurbsCurve(object):
    inherits = ("_ObjectRoot._CurveRoot", )
    holds = {
                   
        #general object holds
        "properties": "_ObjectRootProperties",        
        "groups": "_ObjectRootFunctionsGroups",
        "materials": "_ObjectRootFunctionsMaterial",
        "render": "_ObjectRootFunctionsRender",
        "state": "_ObjectRootFunctionsState",
        "transform": "_ObjectRootFunctionsTransform",
        "utility": "_ObjectRootFunctionsUtil",        
  
        #general curve holds
        "intersect": "_CurveRootFunctionsIntersect",
        "modify": "_CurveRootFunctionsModify",
        "manipulate": "_CurveRootFunctionsManipulate",
        "evaluate": "_CurveRootFunctionsEvaluate",
        "area": "_CurveRootFunctionsArea",
        "test": "_CurveRootFunctionsTest",#inherits from object tests
        
        #arc holds
        "attributes": "_ArcAttributes", 
    }
    class Constructors(object):
        add_curve = {#ed
            "method_name": "create_by_points",
            "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),),
            "method_returns": ("SELF","null")
        }
        add_nurbs_curve = {#ed
            "method_name": "create",
            "method_parameters": (("points","array_of dbl","REQ"),("knots","array_of int","REQ"),("degree","int","REQ"),("weights","array_of int","OPT"),),
            "method_returns": ("SELF","null")
        }
        add_interp_crv_on_srf = {#ed
            "method_name": "create_interp_curve_on_surface",
            "method_parameters": (("surface","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("points","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_interp_crv_on_srf_u_v = {#ed
            "method_name": "create_interp_curve_on_surface_uv",
            "method_parameters": (("surface","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("points","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_interp_curve = {#ed
            "method_name": "create_interp_curve",
            "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("start_tan","array_of dbl","OPT"),("end_tan","array_of dbl","OPT"),),
            "method_returns": ("SELF","null")
        }
        add_interp_curve_ex = {#ed
            "method_name": "create_interp_curve_ex",
            "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("sharp","bln","OPT"),("start_tangent","array_of dbl","OPT"),("end_tangent","array_of dbl","OPT"),),
            "method_returns": ("SELF","null")
        }
        offset_curve_on_surface = {#ed
            "method_name": "create_by_offset_on_surface",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("surface","str","REQ"),("distance","dbl","REQ"),("parameter","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        project_curve_to_surface = {#split
            "method_name": "create_by_projection_to_surface",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("surfaces","array_of str","REQ"),("direction","array_of dbl","REQ"),),###
            "method_returns": ("array_of SELF","null")
        }
        project_curve_to_mesh = {#ed
            "method_name": "create_by_projection_to_mesh",
            "method_parameters": (("curves","array_of _ObjectRoot","REQ"),("meshes","array_of str","REQ"),("direction","array_of dbl","REQ"),),
            "method_returns": ("array_of SELF","null")
        }
#===============================================================================
# NurbsCurveAttributes
#===============================================================================
class _NurbsCurveAttributes(object):
    inherits = ("_CurveRootAttributes", )

    #empty

#===============================================================================
# Arc
#===============================================================================
class Arc(object):
    inherits = ("_ObjectRoot._CurveRoot", )
    holds = {
                   
        #general object holds
        "properties": "_ObjectRootProperties",        
        "groups": "_ObjectRootFunctionsGroups",
        "materials": "_ObjectRootFunctionsMaterial",
        "render": "_ObjectRootFunctionsRender",
        "state": "_ObjectRootFunctionsState",
        "transform": "_ObjectRootFunctionsTransform",
        "utility": "_ObjectRootFunctionsUtil",        
  
        #general curve holds
        "intersect": "_CurveRootFunctionsIntersect",
        "modify": "_CurveRootFunctionsModify",
        "manipulate": "_CurveRootFunctionsManipulate",
        "evaluate": "_CurveRootFunctionsEvaluate",
        "test": "_CurveRootFunctionsTest",#inherits from object tests
        
        #arc holds
        "attributes": "_ArcAttributes",
    }    
    class Constructors(object):
        add_arc = {#ed
            "method_name": "create_arc",
            "method_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ"),("angle","dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_arc_3_pt = {#ed
            "method_name": "create_arc_3pt",
            "method_parameters": (("start","array_of dbl","REQ"),("end","array_of dbl","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_fillet_curve = {#ed
            "method_name": "create_arc_fillet",
            "method_parameters": (("curve_0","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("curve_1","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("radius","dbl","OPT"),("point_0","array_of dbl","OPT"),("point_1","array_of dbl","OPT"),),
            "method_returns": ("SELF","null")
        }
#===============================================================================
# _ArcAttributes
#===============================================================================
class _ArcAttributes(object):
    inherits = ("_CurveRootAttributes", )
    class Methods(object):    
        arc_angle = {#ed
            "method_name": "angle",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
        arc_center_point = {#ed
            "method_name": "center_point",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
        arc_mid_point = {#ed
            "method_name": "mid_point",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
        arc_radius = {#ed
            "method_name": "radius",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
#===============================================================================
# Circle
#===============================================================================
class Circle():
    inherits = ("_ObjectRoot._CurveRoot", )
    holds = {
                   
        #general object holds
        "properties": "_ObjectRootProperties",        
        "groups": "_ObjectRootFunctionsGroups",
        "materials": "_ObjectRootFunctionsMaterial",
        "render": "_ObjectRootFunctionsRender",
        "state": "_ObjectRootFunctionsState",
        "transform": "_ObjectRootFunctionsTransform",
        "utility": "_ObjectRootFunctionsUtil",        
  
        #general curve holds
        "intersect": "_CurveRootFunctionsIntersect",
        "modify": "_CurveRootFunctionsModify",
        "manipulate": "_CurveRootFunctionsManipulate",
        "evaluate": "_CurveRootFunctionsEvaluate",
        "area": "_CurveRootFunctionsArea",
        "test": "_CurveRootFunctionsTest",#inherits from object tests
        
        #circle holds
        "attributes": "_CircleAttributes",
    }      
    class Constructors(object):
        add_circle = {#ed
            "method_name": "create_circle",
            "method_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_circle_3_pt = {#ed
            "method_name": "create_circle_3pt",
            "method_parameters": (("first","array_of dbl","REQ"),("second","array_of dbl","REQ"),("third","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
#===============================================================================
# _CircleAttributes
#===============================================================================
class _CircleAttributes():
    inherits = ("_CurveRootAttributes", )
    class Methods(object):      
        circle_center_point = {#ed
            "method_name": "center_point",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
        circle_circumference = {#ed
            "method_name": "circumference",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
        circle_radius = {#ed
            "method_name": "radius",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
#===============================================================================
# Ellipse
#===============================================================================
class Ellipse(object):
    inherits = ("_ObjectRoot._CurveRoot", )
    holds = {
                   
        #general object holds
        "properties": "_ObjectRootProperties",        
        "groups": "_ObjectRootFunctionsGroups",
        "materials": "_ObjectRootFunctionsMaterial",
        "render": "_ObjectRootFunctionsRender",
        "state": "_ObjectRootFunctionsState",
        "transform": "_ObjectRootFunctionsTransform",
        "utility": "_ObjectRootFunctionsUtil",        
  
        #general curve holds
        "intersect": "_CurveRootFunctionsIntersect",
        "modify": "_CurveRootFunctionsModify",
        "manipulate": "_CurveRootFunctionsManipulate",
        "evaluate": "_CurveRootFunctionsEvaluate",
        "area": "_CurveRootFunctionsArea",
        "test": "_CurveRootFunctionsTest",#inherits from object tests
        
        #ellipse holds
        "attributes": "_EllipseAttributes",
    } 
    class Constructors(object):
        add_ellipse = {#ed
            "method_name": "create_ellipse",
            "method_parameters": (("plane","array_of dbl","REQ"),("x_radius","dbl","REQ"),("y_radius","dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_ellipse_3_pt = {#ed
            "method_name": "create_ellipse_3pt",
            "method_parameters": (("center","array_of dbl","REQ"),("second","array_of dbl","REQ"),("third","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
#===============================================================================
# EllipseAttributes
#===============================================================================
class _EllipseAttributes(object):
    inherits = ("_CurveRootAttributes", )
    class Methods(object):
        ellipse_center_point = {#ed
            "method_name": "center_point",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        ellipse_quad_points = {#ed
            "method_name": "quad_points",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
        } 
#===============================================================================
# Line
#===============================================================================
class Line(object):
    inherits = ("_ObjectRoot._CurveRoot", )
    holds = {
                   
        #general object holds
        "properties": "_ObjectRootProperties",        
        "groups": "_ObjectRootFunctionsGroups",
        "materials": "_ObjectRootFunctionsMaterial",
        "render": "_ObjectRootFunctionsRender",
        "state": "_ObjectRootFunctionsState",
        "transform": "_ObjectRootFunctionsTransform",
        "utility": "_ObjectRootFunctionsUtil",        
  
        #general curve holds
        "intersect": "_CurveRootFunctionsIntersect",
        "modify": "_CurveRootFunctionsModify",
        "manipulate": "_CurveRootFunctionsManipulate",
        "evaluate": "_CurveRootFunctionsEvaluate",
        "test": "_CurveRootFunctionsTest",#inherits from object tests
        
        #line holds
        #none
    }     
    class Constructors(object):
        add_line = {#ed
            "method_name": "create_line",
            "method_parameters": (("start","array_of dbl","REQ"),("end","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
#===============================================================================
# LineAttributes
#===============================================================================
    #empty
    
#===============================================================================
# Polyline
#===============================================================================
class Polyline(object):
    inherits = ("_ObjectRoot._CurveRoot", )
    holds = {
                   
        #general object holds
        "properties": "_ObjectRootProperties",        
        "groups": "_ObjectRootFunctionsGroups",
        "materials": "_ObjectRootFunctionsMaterial",
        "render": "_ObjectRootFunctionsRender",
        "state": "_ObjectRootFunctionsState",
        "transform": "_ObjectRootFunctionsTransform",
        "utility": "_ObjectRootFunctionsUtil",        
  
        #general curve holds
        "intersect": "_CurveRootFunctionsIntersect",
        "modify": "_CurveRootFunctionsModify",
        "manipulate": "_CurveRootFunctionsManipulate",
        "evaluate": "_CurveRootFunctionsEvaluate",
        "area": "_CurveRootFunctionsArea",
        "test": "_CurveRootFunctionsTest",#inherits from object tests
        
        #polyline holds
        "attributes": "_PolylineAttributes",
    }     
    class Constructors(object):
        add_polyline = {
            "method_name": "create_polyline",
            "method_parameters": (("points","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        convert_curve_to_polyline = {
            "method_name": "create_polyline_from_curve",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot","REQ"),("angle_tolerance","dbl","OPT"),("tolerance","dbl","OPT"),("delete_input","bln","OPT"),),
            "method_returns": ("SELF","null")
        } 
#===============================================================================
# PolylineAttributes
#===============================================================================
class _PolylineAttributes(object):
    inherits = ("_CurveRootAttributes",)
    class Methods(object):   
        polyline_vertices = {
            "method_name": "vertices",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
#===============================================================================
# PolyCurve - for the moment we will hide this class, since there are many complications
#===============================================================================

"""
class PolyCurve(object):
    inherits = ("_ObjectRoot._CurveRoot")
    holds = {
                   
        #general object holds
        "properties": "_ObjectRootProperties",        
        "groups": "_ObjectRootFunctionsGroups",
        "materials": "_ObjectRootFunctionsMaterial",
        "render": "_ObjectRootFunctionsRender",
        "state": "_ObjectRootFunctionsState",
        "transform": "_ObjectRootFunctionsTransform",
        "utility": "_ObjectRootFunctionsUtil",        
  
        #general curve holds
        "intersect": "_CurveRootFunctionsIntersect",
        "modify": "_CurveRootFunctionsModify",
        "manipulate": "_CurveRootFunctionsManipulate",
        "evaluate": "_CurveRootFunctionsEvaluate",
        "area": "_CurveRootFunctionsArea",
        "poly": "_CurveRootFunctionsPoly",
        "test": "_CurveRootFunctionsTest",#inherits from object tests
        
        #PolyCurve holds
        # none
    }     
    class Constructors(object):
        join_curves = {#ed
            "method_name": "create_poly_curve",
            "method_parameters": (("curves","array_of _ObjectRoot._CurveRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of SELF","null")
        }
    class Methods(object):
        #TODO: move method and fix index        
        poly_curve_count = {#ed
            "method_name": "count",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT"),),
            "method_returns": ("number","null")
        }
"""

#===============================================================================
# _PolyCurveAttributes
#===============================================================================

    # empty

#===============================================================================
# _CurveRootType
#===============================================================================
class _CurveRootFunctionsType(object):
    inherits = ("_ObjectRootFunctionsType",)
    class Methods(object):     
        is_arc = {#ed
            "method_name": "is_arc",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_circle = {#ed
            "method_name": "is_circle",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_curve = {#ed
            "method_name": "is_curve",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_ellipse = {#ed
            "method_name": "is_ellipse",
            "method_parameters": (("","SELF","REQ"),),#this is inconsistent - may be an error (cf is_circle)
            "method_returns": ("bln","null")
        }
        is_line = {#ed
            "method_name": "is_line",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_poly_curve = {#ed
            "method_name": "is_poly_curve",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_polyline = {#ed
            "method_name": "is_polyline",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
#===============================================================================
# _CurveRootTest
#===============================================================================
class _CurveRootFunctionsTest(object):
    inherits = ("_ObjectRootFunctionsTest", )
    class Methods(object):
        is_curve_in_plane = {#ed
            "method_name": "in_plane",
            "method_parameters": (("","SELF","REQ"),("plane","array_of dbl","OPT"),),
            "method_returns": ("bln","null")
        }
        is_curve_closable = {#ed
            "method_name": "is_curve_closable",
            "method_parameters": (("","SELF","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("bln","null")
        }
        is_curve_closed = {#ed
            "method_name": "is_curve_closed",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_curve_linear = {#ed
            "method_name": "is_curve_linear",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_curve_periodic = {#ed
            "method_name": "is_curve_periodic",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_curve_planar = {#ed
            "method_name": "is_curve_planar",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_curve_rational = {#ed
            "method_name": "is_curve_rational",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_point_on_curve = {#ed
            "method_name": "is_point_on_curve",
            "method_parameters": (("","SELF","REQ"),("point","array_of int","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
#===============================================================================
# _CurveRootModify
#===============================================================================
class _CurveRootFunctionsModify(object):
    inherits = None
    class Methods(object):
        curve_seam = {#ed
            "method_name": "seam",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),),
            "method_returns": ("bln","null")
        }
        fair_curve = {#ed
            "method_name": "fair_curve",
            "method_parameters": (("","SELF","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("bln","null")
        }
        insert_curve_knot = {#ed
            "method_name": "insert_curve_knot",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("symmetrical","bln","OPT"),),
            "method_returns": ("bln","null")
        }
        rebuild_curve = {#ed
            "method_name": "rebuild_curve",
            "method_parameters": (("","SELF","REQ"),("degree","int","OPT"),("point_count","int","OPT"),),
            "method_returns": ("bln","null")
        }
        remove_curve_knot = {#ed
            "method_name": "remove_curve_knot",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),),
            "method_returns": ("bln","null")
        }
        reverse_curve = {#ed
            "method_name": "reverse_curve",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
        }
        simplify_curve = {#ed
            "method_name": "simplify_curve",
            "method_parameters": (("","SELF","REQ"),("flags","int","OPT"),),
            "method_returns": ("bln","null")
        }
        
        #methods that return curves
        #the curves returned will be a modified version of the input curve - the id is the same
        #why this inconsistency??

        #the str return values will be converted to booleans
        
        close_curve = {# this only makes sense on open curves - so exclude form circle etc
            "method_name": "close_curve",
            "method_parameters": (("","SELF","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("str","null")
        }
        extend_curve = {#ed - open curves only
            "method_name": "extend_curve",
            "method_parameters": (("","SELF","REQ"),("type","int","REQ"),("side","int","REQ"),("objects","array_of str","REQ"),),
            "method_returns": ("str","null")
        }
        extend_curve_length = {#ed
            "method_name": "extend_curve_length",
            "method_parameters": (("","SELF","REQ"),("type","int","REQ"),("side","int","REQ"),("length","dbl","REQ"),),
            "method_returns": ("str","null")
        }
        extend_curve_point = {#ed
            "method_name": "extend_curve_point",
            "method_parameters": (("","SELF","REQ"),("side","int","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("str","null")
        }
        fit_curve = {#ed
            "method_name": "fit_curve",
            "method_parameters": (("","SELF","REQ"),("degree","int","OPT"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT"),),
            "method_returns": ("str","null")
        }
        make_curve_non_periodic = {#ed
            "method_name": "make_curve_non_periodic",
            "method_parameters": (("","SELF","REQ"),("delete","bln","OPT","FALSE","HIDE"),),
            "method_returns": ("str","null")
        }
        make_curve_periodic = {#ed
            "method_name": "make_curve_periodic",
            "method_parameters": (("","SELF","REQ"),("delete","bln","OPT","FALSE","HIDE"),),
            "method_returns": ("str","null")
        }
        trim_curve = {#ed
            "method_name": "trim_curve",
            "method_parameters": (("","SELF","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("str","null")
        }
#===============================================================================
# _CurveRootAttributes
#===============================================================================
class _CurveRootAttributes(object):
    inherits = None
    class Methods(object):
        curve_normal = {#ed
            "method_name": "normal",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_plane = {#ed
            "method_name": "plane",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_arrows = {#ed
            "method_name": "arrows",
            "method_parameters": (("","SELF","REQ"),("style","int","OPT"),),
            "method_returns": ("number","null")
        }
        curve_discontinuity = {#ed
            "method_name": "discontinuity",
            "method_parameters": (("","SELF","REQ"),("style","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_domain = {#ed
            "method_name": "domain",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot","null")
        }
        curve_degree = {#ed
            "method_name": "degree",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
        curve_dim = {#ed
            "method_name": "dim",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }

        curve_length = {#ed
            "method_name": "length",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),("sub_domain","array_of int","OPT"),),
            "method_returns": ("number","null")
        }
        curve_start_point = {#ed
            "method_name": "start_point",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }        
        curve_mid_point = {#TODO: test mid_point function
            "method_name": "mid_point",
            "method_parameters": (("","SELF","REQ"),),#no index - this looks inconsistent - may be an error?
            "method_returns": ("array_of dbl","null")
        }
        curve_end_point = {#ed
            "method_name": "end_point",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }        

        curve_weights = {#ed
            "method_name": "weights",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
        #knots
        curve_knot_count = {#ed
            "method_name": "knot_count",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
        curve_knots = {#ed
            "method_name": "knots",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
        #control points     
        curve_point_count = {#ed
            "method_name": "control_point_count",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
        curve_points = {#ed
            "method_name": "control_points",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
        #edit points
        curve_edit_points = {#ed
            "method_name": "edit_points",
            "method_parameters": (("","SELF","REQ"),("return_parameters","bln","OPT"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl", "null")
        }        
#===============================================================================
# _CurveRootIntersect
#===============================================================================
class _CurveRootFunctionsIntersect(object):
    inherits = None
    class Methods(object):
        curve_brep_intersect = {#TODO:can return either curve objects or point objects
            "method_name": "brep_intersection",
            "method_parameters": (("","SELF","REQ"),("brep","str","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot","null")
        }
        curve_curve_intersection = {#TODO: figure this one out
            "method_name": "curve_intersection",
            "method_parameters": (("","SELF","REQ"),("curve","str","OPT"),("tolerance","dbl","OPT"),),
            "method_returns": ("array_of dbl","null")#this is actually the wrong return value, but it works...
        }
        curve_surface_intersection = {#TODO: figure this one out
            "method_name": "surface_intersection",
            "method_parameters": (("","SELF","REQ"),("surface","str","REQ"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT"),),
            "method_returns": ("array_of dbl","null")#this is actually the wrong return value, but it works...
        }      
#===============================================================================
# _CurveRootManipulateFunctions
#===============================================================================
class _CurveRootFunctionsManipulate(object):
    inherits = None
    class Methods(object):
        divide_curve = {#ed
            "method_name": "divide_curve",
            "method_parameters": (("","SELF","REQ"),("segments","lng","REQ"),("create","bln","OPT"),("points","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
        }
        divide_curve_equidistant = {#ed
            "method_name": "divide_curve_equidistant",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
        }
        divide_curve_length = {#ed
            "method_name": "divide_curve_length",
            "method_parameters": (("","SELF","REQ"),("length","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
        }
        #TODO: fix these mixed return values
        """ 
        curve_closest_object = {#ed
            "method_name": "closest_ObjectRoot",
            "method_parameters": (("","SELF","REQ"),("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("array_of (_ObjectRoot._CurveRoot, array_of dbl, array_of dbl)","null")
        }
        """
        curve_arc_length_point = {#ed
            "method_name": "curve_arc_length_point",
            "method_parameters": (("","SELF","REQ"),("length","dbl","REQ"),("from_start","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_contour_points = {#ed
            "method_name": "contour_points",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_deviation = {#ed
            "method_name": "deviation",
            "method_parameters": (("","SELF","REQ"),("curve_a","str","REQ"),),
            "method_returns": ("array_of number","null")
        }
        line_fit_from_points = {#ed
            "method_name": "line_fit_from_points",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_directions_match = {#ed
            "method_name": "directions_match",
            "method_parameters": (("","SELF","REQ"),("curve_1","str","REQ"),),
            "method_returns": ("bln","null")
        }
        #TODO: fix these mixed return values
        """
        curve_fillet_points = {#TODO:documentation is not clear
            "method_name": "fillet_points",
            "method_parameters": (("","SELF","REQ"),("curve_0","str","REQ"),("radius","dbl","OPT"),("base_point_0","array_of dbl","OPT"),("base_point__1","array_of dbl","OPT"),),
            "method_returns": ("array_of (array_of dbl, array_of dbl, array_of dbl, array_of dbl, array_of dbl, array_of dbl)","_ObjectRoot._CurveRoot","null")
        }
        """
        curve_closest_point = {#ed
            "method_name": "closest_point",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
        curve_radius = {#ed
            "method_name": "radius",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }        
#===============================================================================
# _CurveRootClosedPlanarFunctions
#===============================================================================
class _CurveRootFunctionsArea(object):
    inherits = None
    class Methods(object):
        planar_curve_collision = {#TODO: confirm if this is in the right place
            "method_name": "planar_curve_collision",
            "method_parameters": (("","SELF","REQ"),("curve","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT"),),
            "method_returns": ("bln","null")
        }          
        curve_area = {#ed
            "method_name": "area",
            "method_parameters": (("","array_of _ObjectRoot","REQ"),),
            "method_returns": ("array_of int","null")
        }
        curve_area_centroid = {#ed
            "method_name": "curve_area_centroid",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        point_in_planar_closed_curve = {#ed
            "method_name": "point_in_planar_closed_curve",
            "method_parameters": (("point","array_of dbl","REQ"),("curve","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT"),),
            "method_returns": ("number","null")
        }
        planar_closed_curve_containment = {#ed
            "method_name": "planar_closed_curve_containment",
            "method_parameters": (("","SELF","REQ"),("curve__1","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT"),),
            "method_returns": ("number","null")
        }
        curve_boolean_difference = {#ed
            "method_name": "boolean_difference",
            "method_parameters": (("","SELF","REQ"),("curve","str","REQ"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot","null")
        }
        curve_boolean_intersection = {#ed
            "method_name": "boolean_intersection",
            "method_parameters": (("","SELF","REQ"),("curve_a","str","REQ"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot","null")
        }
        curve_boolean_union = {#ed
            "method_name": "boolean_union",
            "method_parameters": (("curves","array_of _ObjectRoot","REQ"),),#TODO: for this method, there is no SELF parameter
            "method_returns": ("array_of _ObjectRoot._CurveRoot","null")
        }
#===============================================================================
# _CurveRootFunctionsEvaluate
#===============================================================================
class _CurveRootFunctionsEvaluate(object):
    inherits = None
    class Methods(object):
        curve_evaluate = {#ed
            "method_name": "evaluate_derivatives",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("derivative","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_frame = {#ed
            "method_name": "frame",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_curvature = {#ed
            "method_name": "curvature",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_perp_frame = {#ed
            "method_name": "perp_frame",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        evaluate_curve = {#ed
            "method_name": "evaluate",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_tangent = {#ed
            "method_name": "tangent",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }        
#===============================================================================
# _CurveRootPolyFunctions
#===============================================================================
class _CurveRootFunctionsPoly(object):
    inherits = None
    class Methods(object):
        explode_curves = {#this has the delete parameter - polys only
            "method_name": "explode",
            "method_parameters": (("","SELF","REQ"),("delete","bln","OPT"),),###
            "method_returns": ("array_of _ObjectRoot._CurveRoot","null")
        }
#===============================================================================
# Mesh
#===============================================================================
"""
class PolygonMesh(object):
    inherits = ("_ObjectRoot._PolygonMeshRoot", )
    #TODO: move method
    class Methods(object):
        mesh_polyline = {#ed
            "method_name": "create_mesh_from_closed_polyline",
            "method_parameters": (("polyline","_ObjectRoot._CurveRoot.Polyline","REQ"),),
            "method_returns": ("_ObjectRoot._MeshRoot.PolygonMesh","null")
        }
        
"""
