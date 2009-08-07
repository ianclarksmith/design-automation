#The data below will be used to generate the Rhinoscript function wrappers
#===============================================================================
# PolySurface
#===============================================================================
class PolySurface(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_ObjectRootDefm",                
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootMdfy",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object tests
        
        #holds
        "func": "_PolySurfaceFunc",
    }    
    class Constructors(object):
        extrude_surface = {#ed
            "method_name": "create_by_srf_extrude",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("curve","str","REQ"),("cap","bln","OPT"),),
            "method_returns": ("SELF","null")
            }   
        join_surfaces = {#ed
            "method_name": "create_by_srf_join",
            "method_parameters": (("surfaces","array_of _ObjectRoot._SurfaceRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("SELF","null")
            }
        
        offset_surface = {#ed
            "method_name": "create_by_offset",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }        
        
        copy_object = {
            "method_name": "create_copy_move",
            "method_parameters": (("object","_ObjectRoot","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("SELF","null")        
            }
        copy_object_2 = {
            "method_name": "create_copy_move_by_vec",
            "method_parameters": (("object","_ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("SELF","null")         
            }        
#===============================================================================
# _PolySurfaceProp
#===============================================================================
class _PolySurfaceFunc(object):
    inherits = ("_SurfaceRootFuncOorc", )
    class Methods(object):
        explode_polysurfaces = {
            "method_name": "explode",
            "method_parameters": (("objects","array_of _Object","REQ"),("delete","bln","OPT"),),#this was an array - hope it still works
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot.NurbsSurface","null")
            } 
#===============================================================================
# Box
#===============================================================================
class Box(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_ObjectRootDefm",          
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
      
        "modf": "_SurfaceRootMdfy",
        "func": "_SurfaceRootFuncOorc",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object tests
        
        #holds
        "prop": "_SurfaceRootPropClsd",           
    } 
    class Constructors(object):
        add_box = {#ed
            "method_name": "create",
            "method_parameters": (("corners","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        
        offset_surface = {#ed
            "method_name": "create_by_offset",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }        
        
        copy_object = {
            "method_name": "create_copy_move",
            "method_parameters": (("object","_ObjectRoot","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("SELF","null")        
            }
        copy_object_2 = {
            "method_name": "create_copy_move_by_vec",
            "method_parameters": (("object","_ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("SELF","null")         
            }        
#===============================================================================
# Cone
#===============================================================================
class Cone(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_ObjectRootDefm",                 
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootMdfy",
        "func": "_SurfaceRootFuncOorc",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object tests
        
        #arc holds
        "prop": "_ConeProp",       
    }     
    class Constructors(object):
        add_cone = {#ed
            "method_name": "create",
            "method_parameters": (("base","array_of dbl","REQ"),("height","array_of dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT"),),
            "method_returns": ("SELF","null")
            }
        add_cone_2 = {#ed
            "method_name": "create_by_plane",
            "method_parameters": (("plane","array_of dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT"),),
            "method_returns": ("SELF","null")
            }        
        
        offset_surface = {#ed
            "method_name": "create_by_offset",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }        
        
        copy_object = {
            "method_name": "create_copy_move",
            "method_parameters": (("object","_ObjectRoot","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("SELF","null")        
            }
        copy_object_2 = {
            "method_name": "create_copy_move_by_vec",
            "method_parameters": (("object","_ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("SELF","null")         
            }        
#===============================================================================
# _ConeProp
#===============================================================================
class _ConeProp(object):
    inherits = ("_SurfaceRootPropOorc", )         
    class Methods(object):
        surface_cone = {#ed
            "method_name": "cone_def",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
#===============================================================================
# NurbsSurface
#===============================================================================
class NurbsSurface(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_ObjectRootDefm",                
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootMdfy",
        "func": "_SurfaceRootFuncOorc",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object tests
        
        "prop": "_SurfaceRootPropOorc",        
    }    
    class Constructors(object):
        add_cut_plane = {#ed
            "method_name": "create_by_cut_plane",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("normal","array_of dbl","OPT"),),
            "method_returns": ("SELF","null")
            }
        add_edge_srf = {#ed
            "method_name": "create_by_edge",
            "method_parameters": (("objects","array_of _ObjectRoot._CurveRoot","REQ"),),
            "method_returns": ("SELF","null")
            }
        add_loft_srf = {#ed
            "method_name": "create_by_loft",
            "method_parameters": (("objects","array_of _ObjectRoot._CurveRoot","REQ"),("start_pt","array_of dbl","OPT"),("end_pt","array_of dbl","OPT"),("srf_type","int","OPT"),("style","int","OPT"),("value","n","OPT"),("closed","bln","OPT"),),
            "method_returns": ("array_of SELF","null")
            }
        add_nurbs_surface = {#ed
            "method_name": "create",
            "method_parameters": (("point_count","array_of int","REQ"),("points","array_of dbl","REQ"),("knots_u","array_of int","REQ"),("knots_v","array_of int","REQ"),("degree","array_of int","REQ"),("weights","array_of int","REQ"),),
            "method_returns": ("SELF","null")
            }
        add_rail_rev_srf = {#ed
            "method_name": "create_by_rail_rev",
            "method_parameters": (("profile","_ObjectRoot._CurveRoot","REQ"),("rail","_ObjectRoot._CurveRoot","REQ"),("axis","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        add_rev_srf = {#ed
            "method_name": "create_by_rev",
            "method_parameters": (("profile","_ObjectRoot._CurveRoot","REQ"),("axis","array_of dbl","REQ"),("start_angle","dbl","OPT"),("end_angle","dbl","OPT"),),
            "method_returns": ("SELF","null")
            }
        add_srf_control_pt_grid = {#ed
            "method_name": "create_by_control_pt_grid",
            "method_parameters": (("count","array_of int","REQ"),("points","array_of dbl","REQ"),("degree","array_of dbl","OPT"),),
            "method_returns": ("SELF","null")
            }
        add_srf_pt = {#ed
            "method_name": "create_by_corner_pts",
            "method_parameters": (("points","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        add_srf_pt_grid = {#ed
            "method_name": "create_by_pt_grid",
            "method_parameters": (("count","array_of int","REQ"),("points","array_of dbl","REQ"),("degree","array_of int","OPT"),("closed","array_of bln","OPT"),),
            "method_returns": ("SELF","null")
            }
        fit_surface = {#ed
            "method_name": "create_by_fit",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("degree","array_of int","OPT"),("tolerance","dbl","OPT"),),
            "method_returns": ("SELF","null")
            }
        
        #extruding a curve
        
        extrude_curve = {#ed
            "method_name": "create_by_extrude_crv",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot","REQ"),("path","str","REQ"),),
            "method_returns": ("SELF","null")
            }
        extrude_curve_point = {#ed
            "method_name": "create_by_extrude_crv_pnt",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        extrude_curve_straight = {#ed
            "method_name": "create_by_extrude_crv_straight",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        extrude_curve_tapered = {#ed
            "method_name": "create_by_extrude_crv_tapered",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot","REQ"),("distance","dbl","REQ"),("direction","array_of dbl","REQ"),("base_point","array_of dbl","REQ"),("angle","dbl","REQ"),("corner_type","int","OPT"),),
            "method_returns": ("array_of SELF","null")
            }  


        #these return arrays
        
        add_planar_srf = {#ed
            "method_name": "create_by_planar_crv",
            "method_parameters": (("objects","array_of _ObjectRoot._CurveRoot","REQ"),),
            "method_returns": ("array_of SELF","null")
            }
        add_sweep_1 = {#ed
            "method_name": "create_by_sweep_1",
            "method_parameters": (("rail","_ObjectRoot._CurveRoot","REQ"),("shapes","array_of _ObjectRoot._CurveRoot","REQ"),("start_pt","array_of dbl","OPT"),("end_pt","array_of dbl","OPT"),("closed","bln","OPT"),("style","int","OPT"),("style_arg","va","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT"),),
            "method_returns": ("array_of SELF","null")
            }
        add_sweep_2 = {#ed
            "method_name": "create_by_sweep_2",
            "method_parameters": (("rails","array_of _ObjectRoot._CurveRoot","REQ"),("shapes","array_of _ObjectRoot._CurveRoot","REQ"),("start_pt","array_of dbl","OPT"),("end_pt","array_of dbl","OPT"),("closed","bln","OPT"),("simple_sweep","bln","OPT"),("maintain_height","bln","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT"),),
            "method_returns": ("array_of SELF","null")
            }
        
        copy_object = {
            "method_name": "create_copy_move",
            "method_parameters": (("object","_ObjectRoot","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("SELF","null")        
            }
        copy_object_2 = {
            "method_name": "create_copy_move_by_vec",
            "method_parameters": (("object","_ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("SELF","null")         
            }
       
        offset_surface = {#ed
            "method_name": "create_by_offset",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }       
       
        copy_object = {
            "method_name": "create_copy_move",
            "method_parameters": (("object","_ObjectRoot","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("SELF","null")        
            }
        copy_object_2 = {
            "method_name": "create_copy_move_by_vec",
            "method_parameters": (("object","_ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("SELF","null")         
            }
#===============================================================================
# Cylinder
#===============================================================================
class Cylinder(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_ObjectRootDefm",                
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootMdfy",
        "func": "_SurfaceRootFuncOorc",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object tests
        
        #arc holds
        "prop": "_CylinderProp",        
    }    
    class Constructors(object):
        add_cylinder = {#ed
            "method_name": "create",
            "method_parameters": (("base","array_of dbl","REQ"),("height","array_of dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
            "method_returns": ("SELF","null")
            }
        add_cylinder_2 = {#ed
            "method_name": "create_by_plane",
            "method_parameters": (("plane","array_of dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
            "method_returns": ("SELF","null")
            }        
        
        offset_surface = {#ed
            "method_name": "create_by_offset",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }        
        
        copy_object = {
            "method_name": "create_copy_move",
            "method_parameters": (("object","_ObjectRoot","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("SELF","null")        
            }
        copy_object_2 = {
            "method_name": "create_copy_move_by_vec",
            "method_parameters": (("object","_ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("SELF","null")         
            }        
#===============================================================================
# _CylinderProp
#===============================================================================
class _CylinderProp(object):
    inherits = ("_SurfaceRootPropOorc", )         
    class Methods(object):
        surface_cylinder = {#ed
            "method_name": "cylinder_def",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
#===============================================================================
# PlaneSurface
#===============================================================================
class PlaneSurface(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_ObjectRootDefm",               
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootMdfy",
        "func": "_SurfaceRootFuncOorc",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object tests

        "prop": "_SurfaceRootPropOpen",
    }    
    class Constructors(object):
        add_plane_surface = {#ed
            "method_name": "create",
            "method_parameters": (("plane","array_of dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        
        offset_surface = {#ed
            "method_name": "create_by_offset",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }        
        
        copy_object = {
            "method_name": "create_copy_move",
            "method_parameters": (("object","_ObjectRoot","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("SELF","null")        
            }
        copy_object_2 = {
            "method_name": "create_copy_move_by_vec",
            "method_parameters": (("object","_ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("SELF","null")         
            }        
#===============================================================================
# Sphere
#===============================================================================
class Sphere(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_ObjectRootDefm",                 
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootMdfy",
        "func": "_SurfaceRootFuncOorc",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object tests
        
        #arc holds
        "prop": "_SphereProp",        
    }    
    class Constructors(object):
        add_sphere = {#ed
            "method_name": "create",
            "method_parameters": (("center","array_of dbl","REQ"),("radius","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        add_sphere_2 = {#ed
            "method_name": "create_by_plane",
            "method_parameters": (("center","array_of dbl","REQ"),("radius","dbl","REQ"),),
            "method_returns": ("SELF","null")
            } 
        
        offset_surface = {#ed
            "method_name": "create_by_offset",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }        
        
        copy_object = {
            "method_name": "create_copy_move",
            "method_parameters": (("object","_ObjectRoot","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("SELF","null")        
            }
        copy_object_2 = {
            "method_name": "create_copy_move_by_vec",
            "method_parameters": (("object","_ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("SELF","null")         
            }               
#===============================================================================
# _SphereProp
#===============================================================================
class _SphereProp(object):
    inherits = ("_SurfaceRootPropClsd", )         
    class Methods(object):
        surface_sphere = {#ed
            "method_name": "sphere_definition",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
#===============================================================================
# Torus
#===============================================================================
class Torus(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_ObjectRootDefm",                
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootMdfy",
        "func": "_SurfaceRootFuncOorc",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object tests
        
        #arc holds
        "prop": "_TorusProp",      
    }    
    class Constructors(object):
        add_torus = {#ed
            "method_name": "create",
            "method_parameters": (("base","array_of dbl","REQ"),("major_radius","dbl","REQ"),("minor_radius","dbl","REQ"),("direction","array_of dbl","OPT")),
            "method_returns": ("SELF","null")
            }
        add_torus_2 = {#ed
            "method_name": "create_by_plane",
            "method_parameters": (("plane","array_of dbl","REQ"),("major_radius","dbl","REQ"),("minor_radius","dbl","REQ")),
            "method_returns": ("SELF","null")
            }
        
        offset_surface = {#ed
            "method_name": "create_by_offset",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }        
        
        copy_object = {
            "method_name": "create_copy_move",
            "method_parameters": (("object","_ObjectRoot","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("SELF","null")        
            }
        copy_object_2 = {
            "method_name": "create_copy_move_by_vec",
            "method_parameters": (("object","_ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("SELF","null")         
            }        
#===============================================================================
# _TorusProp
#===============================================================================
class _TorusProp(object):
    inherits = ("_SurfaceRootPropClsd", )         
    class Methods(object):        
        surface_torus = {#ed
            "method_name": "torus_definition",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
#===============================================================================
# NurbsCurve
#===============================================================================
class NurbsCurve(object):
    inherits = ("_SurfaceRoot", )
    class Constructors(object):
        
        short_path = {#ed
            "method_name": "create_by_srf_short_path",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        
        #arrays of curves
                
        add_srf_contour_crvs = {#surface or polysurface
            "method_name": "create_by_srf_contour",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT")),
            "method_returns": ("array_of SELF","null")
            }
        add_srf_contour_crvs_2 = {#surface or polysurface
            "method_name": "create_by_srf_contour_cut_plane",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("plane","array_of dbl","REQ"),("interval","dbl","OPT")),
            "method_returns": ("array_of SELF","null")
            }        
        add_srf_section_crvs = {#surface or polysurface
            "method_name": "create_by_srf_section",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("plane","array_of dbl","REQ"),),
            "method_returns": ("array_of SELF","null")
            }
        duplicate_edge_curves = {#surface or polysurface
            "method_name": "create_by_srf_edge",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("select","bln","OPT"),),
            "method_returns": ("array_of SELF","null")
            }
        duplicate_surface_border = {#surface or polysurface
            "method_name": "create_by_srf_border",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),),
            "method_returns": ("array_of SELF","null")
            }
        extract_iso_curve = {#
            "method_name": "create_by_srf_iso_curve",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("parameter","array_of dbl","REQ"),("dir","int","REQ"),),
            "method_returns": ("array_of SELF","null")
            }
        surface_principal_curvature = {#ed
            "method_name": "create_by_srf_principal_curvature",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("array_of SELF","null")
            }
        pull_curve = {#ed
            "method_name": "create_by_srf_pull",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of SELF","null")
            } 
        
        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        
        
#===============================================================================
# _SurfaceRootType
#===============================================================================
class _SurfaceRootType(object):
    inherits = ("_ObjectRootTest", )
    class Methods(object):
        is_cone = {#ed
            "method_name": "is_cone",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        is_cylinder = {#ed
            "method_name": "is_cylinder",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        is_sphere = {#ed
            "method_name": "is_sphere",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        is_surface = {#ed
            "method_name": "is_surface",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        is_torus = {#ed
            "method_name": "is_torus",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
#===============================================================================
# _CurveRootTest
#===============================================================================
class _SurfaceRootTest(object):
    inherits = ("_ObjectRootTest",)
    class Methods(object):
        is_plane_surface = {#ed
            "method_name": "is_plane_surface",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        is_poly_surface_closed = {#ed
            "method_name": "is_poly_surface_closed",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }        
        is_brep = {#ed
            "method_name": "is_brep",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        is_brep_manifold = {#ed
            "method_name": "is_brep_manifold",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }        
        is_parameter_on_surface = {#ed
            "method_name": "is_parameter_on_srf",
            "method_parameters": (("","SELF","REQ"),("parameter","array_of dbl","REQ"),),
            "method_returns": ("bln","null")
            }
        is_point_in_surface = {#ed
            "method_name": "is_pnt_in_srf",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("bln","null")
            }
        is_point_on_surface = {#ed
            "method_name": "is_pnt_on_srf",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("bln","null")
            }
        is_surface_closed = {#ed
            "method_name": "is_srf_closed",
            "method_parameters": (("","SELF","REQ"),("direction","int","REQ"),),
            "method_returns": ("bln","null")
            }
        is_surface_periodic = {#ed
            "method_name": "is_srf_periodic",
            "method_parameters": (("","SELF","REQ"),("direction","int","REQ"),),
            "method_returns": ("bln","null")
            }
        is_surface_planar = {#ed
            "method_name": "is_srf_planar",
            "method_parameters": (("","SELF","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("bln","null")
            }
        is_surface_rational = {#ed
            "method_name": "is_srf_rational",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        is_surface_singular = {#ed
            "method_name": "is_srf_singular",
            "method_parameters": (("","SELF","REQ"),("direction","int","REQ"),),
            "method_returns": ("bln","null")
            }
        is_surface_trimmed = {#ed
            "method_name": "is_srf_trimmed",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        is_poly_surface = {#ed
            "method_name": "is_poly_srf",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        is_poly_surface_planar = {#ed
            "method_name": "is_poly_srf_planar",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }

#===============================================================================
# _CurveRootModify
#===============================================================================
class _SurfaceRootMdfy(object):
    inherits = ("_ObjectRootMdfy",)
    class Methods(object):
        rebuild_surface = {#ed
            "method_name": "rebuild",
            "method_parameters": (("","SELF","REQ"),("degree","array_of int","OPT"),("point_count","array_of int","OPT"),),
            "method_returns": ("bln","null")
            }
        remove_surface_knot = {#ed
            "method_name": "remove_knot",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("direction","int","REQ"),),
            "method_returns": ("bln","null")
            }
        reverse_surface = {#ed
            "method_name": "reverse",
            "method_parameters": (("","SELF","REQ"),("direction","int","REQ"),),
            "method_returns": ("bln","null")
            }
        shrink_trimmed_surface = {#ed
            "method_name": "shrink_trimmed",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        surface_seam = {#ed
            "method_name": "seam",
            "method_parameters": (("","SELF","REQ"),("direction","int","REQ"),("parameter","dbl","REQ"),),
            "method_returns": ("bln","null")
            }
        flip_surface = {#ed
            "method_name": "flip",
            "method_parameters": (("","SELF","REQ"),("flip","bln","OPT"),),
            "method_returns": ("bln","null")
            }
        insert_surface_knot = {#ed
            "method_name": "insert_knot",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("direction","int","REQ"),("symmetrical","bln","OPT"),),
            "method_returns": ("bln","null")
            }
#===============================================================================
# _SurfaceRootEval
#===============================================================================
class _SurfaceRootEval(object):
    inherits = None
    class Methods(object):
        surface_evaluate = {#ed
            "method_name": "evaluate_derivatives",
            "method_parameters": (("","SELF","REQ"),("parameter","array_of dbl","REQ"),("derivative","int","REQ"),),
            "method_returns": ("array_of number","null")
            }        
        evaluate_surface = {#ed
            "method_name": "evaluate",
            "method_parameters": (("","SELF","REQ"),("parameter","array_of dbl","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        surface_frame = {#ed
            "method_name": "evaluate_frame",
            "method_parameters": (("","SELF","REQ"),("parameter","array_of dbl","REQ"),),
            "method_returns": ("array_of dbl","null")
            }

#===============================================================================
# _SurfaceRootAttributes
#===============================================================================
class _SurfaceRootProp(object):
    inherits = ("_ObjectRootProp", )
    class Methods(object):
        surface_degree = {#ed
            "method_name": "degree",
            "method_parameters": (("","SELF","REQ"),("direction","int","OPT"),),
            "method_returns": ("array_of number","null")#this is not quite right
            }
        surface_weights = {#ed
            "method_name": "weights",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        surface_isocurve_density = {#ed
            "method_name": "isocurve_density",
            "method_parameters": (("","SELF","REQ"),("density","int","OPT"),),
            "method_returns": ("number","null")
            }
        surface_knot_count = {#ed
            "method_name": "knot_count",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of int","null")
            }
        surface_knots = {#ed
            "method_name": "knots",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        surface_normal = {#ed
            "method_name": "normal",
            "method_parameters": (("","SELF","REQ"),("parameter","array_of dbl","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        surface_point_count = {#ed
            "method_name": "pnt_count",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of int","null")
            }
        surface_points = {#ed
            "method_name": "pnts",
            "method_parameters": (("","SELF","REQ"),("return_all","bln","OPT"),),
            "method_returns": ("array_of int","null")
            }
        surface_contour_points = {#ed
            "method_name": "contour_pnts",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT"),("angle","dbl","OPT"),),
            "method_returns": ("array_of dbl","null")
            }
        surface_curvature = {#ed
            "method_name": "curvature",
            "method_parameters": (("","SELF","REQ"),("parameter","array_of dbl","REQ"),),
            "method_returns": ("array_of number","null")
            }
        surface_curvature_analysis = {#ed
            "method_name": "curvature_analysis",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
        surface_domain = {#ed
            "method_name": "domain",
            "method_parameters": (("","SELF","REQ"),("direction","int","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        surface_edit_points = {#ed
            "method_name": "edit_pnts",
            "method_parameters": (("","SELF","REQ"),("return_parameters","bln","OPT"),("return_all","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
            }
        surface_area = {#ed
            "method_name": "area",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
        surface_area_centroid = {#ed
            "method_name": "area_centroid",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
        surface_area_moments = {#ed
            "method_name": "area_moments",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
#===============================================================================
# _SurfaceRootPropClsd
#===============================================================================
class _SurfaceRootPropClsd(object):
    inherits = ('_SurfaceRootProp',)
    
    class Methods(object):       
        surface_volume = {#ed
            "method_name": "volume",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
        surface_volume_centroid = {#ed
            "method_name": "volume_centroid",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
        surface_volume_moments = {#ed
            "method_name": "volume_moments",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of number","null")
            }
#===============================================================================
# _SurfaceRootPropOpen
#===============================================================================
class _SurfaceRootPropOpen(object):
    inherits = ('_SurfaceRootProp',)
    
#===============================================================================
# _SurfaceRootPropOorc
#===============================================================================
class _SurfaceRootPropOorc(object):
    inherits = ('_SurfaceRootPropOpen','_SurfaceRootPropClsd', )
    
    
#===============================================================================
# _SurfaceRootFunc
#===============================================================================
class _SurfaceRootFunc(object):
    inherits = ("_ObjectRootFunc",)
    class Methods(object):
        make_surface_non_periodic = {#ed
            "method_name": "make_non_periodic",
            "method_parameters": (("","SELF","REQ"),("direction","int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot.NurbsSurface","null")
            }
        make_surface_periodic = {#ed
            "method_name": "make_periodic",
            "method_parameters": (("","SELF","REQ"),("direction","int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot.NurbsSurface","null")
            }            
        surface_closest_point = {#ed
            "method_name": "closest_pnt",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("array_of number","null")
            }
        
        #TODO: fix these mixed return values
        """        
        surface_surface_intersection = {#ed
            "method_name": "surface_surface_intersection",
            "method_parameters": (("","SELF","REQ"),("surface_a","str","REQ"),("tolerance","dbl","OPT"),("create","bln","OPT"),),
            "method_returns": ("array_of (array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl)","array_of (int, array_of _ObjectRoot._SurfaceRoot)","null")
            }
        """

    
#===============================================================================
# _SurfaceRootFuncOpen
#===============================================================================
class _SurfaceRootFuncOpen(object):
    inherits = ('_SurfaceRootFunc',)
    class Methods(object):    
        cap_planar_holes = {#ed
            "method_name": "cap_planar_holes",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
   

   
#===============================================================================
# _SurfaceRootFuncClsd
#===============================================================================
class _SurfaceRootFuncClsd(object):
    inherits = ('_SurfaceRootFunc',)
    
    class Methods(object):
        brep_closest_point = {#ed
            "method_name": "brep_closest_pnt",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("array_of number","null")
            }        
        
        #booleans return surfaces or polysurfaces
        
        boolean_difference = {
            "method_name": "boolean_difference",
            "method_parameters": (("","SELF","REQ"),("breps","array_of _ObjectRoot._SurfaceRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot.PolySurface","null")
            }
        boolean_intersection = {
            "method_name": "boolean_intersection",
            "method_parameters": (("","SELF","REQ"),("breps","array_of _ObjectRoot._SurfaceRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot.PolySurface","null")
            }
        boolean_union = {#TODO: this has no SELF
            "method_name": "boolean_union",
            "method_parameters": (("breps","array_of _ObjectRoot._SurfaceRoot","REQ"),("delete","bln","OPT"),),#TODO: for this method, there is no SELF parameter
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot.PolySurface","null")
            }
        split_brep = {#ed
            "method_name": "boolean_split",
            "method_parameters": (("","SELF","REQ"),("cutter","str","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot.PolySurface","null")
            }
        intersect_breps = {#ed
            "method_name": "intersect_breps",
            "method_parameters": (("","SELF","REQ"),("brep_1","str","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("array_of _ObjectRoot","null")
            }

#===============================================================================
# _SurfaceRootFuncOorc
#===============================================================================
class _SurfaceRootFuncOorc(object):
    inherits = ('_SurfaceRootFuncOpen','_SurfaceRootFuncClsd',)
    pass

#===============================================================================
# _SurfaceRoot
#===============================================================================
class _SurfaceRoot(object):
    inherits = ("_ObjectRoot", )


















