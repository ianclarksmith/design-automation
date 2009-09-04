#The data below will be used to generate the Rhinoscript function wrappers
#===============================================================================
# Document
#===============================================================================
"""
class _DocumentObjectFunc(object):
    inherits = None
    class ClassMethods(object):
        project_curve_to_surface = {#split
            "method_name": "crvs_project_to_srf",
            "method_parameters": (("curves","array_of _ObjectRoot._CurveRoot","REQ"),("surfaces","array_of _ObjectRoot._SurfaceRoot","REQ"),("direction_point","array_of dbl","REQ"),),###
            "method_returns": ("array_of _ObjectRoot._CurveRoot.GenericCurve","null")
            }
        explode_curves = {#this has the delete parameter - polys only             
            "method_name": "crvs_explode",
            "method_parameters": (("curves","array_of _ObjectRoot._CurveRoot","REQ"),("delete","bln","OPT"),),###
            "method_returns": ("array_of _ObjectRoot._CurveRoot.GenericCurve","null")#GenericCirve
            }
"""
   
#===============================================================================
# NurbsCurve
#===============================================================================
class NurbsCurve(object):
    inherits = ("_CurveRoot", )
    holds = {
                   
        #general object holds
        "defm": "_CurveRootDefm",          
        "prop": "_ObjectRootProp",        
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_CurveRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_NurbsCurveModf",
        "eval": "_CurveRootEval",
        "test": "_CurveRootTest",#inherits from object level
        "dupl": "_NurbsCurveDupl",#inherits from object level
        
        #properties
        "prop": "_CurveRootProp",
        "func": "_CurveRootFuncClsd",
    }
    class Constructors(object):
        add_nurbs_curve = {#ed
            "method_name": "create",
            "method_parameters": (("points","array_of dbl","REQ"),("knots","array_of int","REQ"),("degree","int","REQ"),("weights","array_of int","OPT"),),
            "method_returns": ("SELF","null")
        }        
        add_curve = {#ed
            "method_name": "create_by_pnts",
            "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),),
            "method_returns": ("SELF","null")
        }
        add_interp_crv_on_srf = {#ed
            "method_name": "create_interp_crv_on_srf",
            "method_parameters": (("surface","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("points","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_interp_crv_on_srf_u_v = {#ed
            "method_name": "create_interp_crv_on_srf_uv",
            "method_parameters": (("surface","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("points","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_interp_curve = {#ed
            "method_name": "create_interp_crv",
            "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("start_tan","array_of dbl","OPT"),("end_tan","array_of dbl","OPT"),),
            "method_returns": ("SELF","null")
        }
        add_interp_curve_ex = {#ed
            "method_name": "create_interp_crv_ex",
            "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("sharp","bln","OPT"),("start_tangent","array_of dbl","OPT"),("end_tangent","array_of dbl","OPT"),),
            "method_returns": ("SELF","null")
        }        
        fit_curve = {
            "method_name": "create_by_fit",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot","REQ"),("degree","int","OPT"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT"),),
            "method_returns": ("SELF","null")
        }
        
        project_curve_to_surface = {
            "method_name": "create_by_projection_to_srf",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("surfaces","array_of _ObjectRoot._SurfaceRoot","REQ"),("direction_vector","array_of dbl","REQ"),),
            "method_returns": ("array_of SELF","null")#returns array
        }
        project_curve_to_mesh = {
            "method_name": "create_by_projection_to_mesh",
            "method_parameters": (("curves","array_of _ObjectRoot","REQ"),("meshes","array_of _ObjectRoot._SurfaceRoot","REQ"),("direction_vector","array_of dbl","REQ"),),
            "method_returns": ("array_of SELF","null")#returns array
        }
        
        
        #FROM SURFACE METHODS
        
        short_path = {#ed
            "method_name": "create_by_srf_short_path",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        
        #arrays of curves
                
        add_srf_contour_crvs = {#surface or polysurface
            "method_name": "create_by_srf_contour",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT")),
            "method_returns": ("array_of SELF","null")#returns array
            }

        add_srf_section_crvs = {#surface or polysurface
            "method_name": "create_by_srf_section",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("cut_plane","array_of dbl","REQ"),),
            "method_returns": ("array_of SELF","null")#returns array
            }
        duplicate_edge_curves = {#surface or polysurface
            "method_name": "create_by_srf_edge",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("select","bln","OPT"),),
            "method_returns": ("array_of SELF","null")#returns array
            }
        duplicate_surface_border = {#surface or polysurface
            "method_name": "create_by_srf_border",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),),
            "method_returns": ("array_of SELF","null")#returns array
            }
        extract_iso_curve = {
            "method_name": "create_by_srf_iso_curve",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("parameter","array_of dbl","REQ"),("dir","int","REQ"),),
            "method_returns": ("array_of SELF","null")#returns array
            }
        surface_principal_curvature = {#ed
            "method_name": "create_by_srf_principal_curvature",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("array_of SELF","null")#returns array
            }
        
        
        pull_curve = {#ed
            "method_name": "create_by_srf_pull",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of SELF","null") #returns array
            } 
        
        ''' This calls add_srf_contour_crvs_2 - does not work due to args confusion
        add_srf_contour_crvs_2 = {#surface or polysurface
            "method_name": "create_by_srf_contour_cut_plane",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("cut_plane","array_of dbl","REQ"),("interval","dbl","OPT")),
            "method_returns": ("array_of SELF","null")#returns array
            }        '''
        
        
        
        
        
#===============================================================================
# _NurbsCurveDupl
#===============================================================================
class _NurbsCurveDupl(object):
    inherits = None
    class Methods(object):  
        
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")         
            }         
        offset_curve = {
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("direction_point","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }

        add_sub_crv = {#ed
            "method_name": "copy_by_sub",
            "method_parameters": (("","SELF","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }        
        trim_curve = {#ed
            "method_name": "copy_by_trim",
            "method_parameters": (("","SELF","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }
        
        split_curve = {#this has the delete parameter
            "method_name": "copy_by_split",
            "method_parameters": (("","SELF","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot.NurbsCurve","null")
        }
        
        
        offset_curve_on_surface = {#ed
            "method_name": "copy_by_offset_on_srf",
            "method_parameters": (("","SELF","REQ"),("surface","_ObjectRoot._SurfaceRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }
        offset_curve_on_surface_2 = {#ed
            "method_name": "copy_by_offset_on_srf_by_param",
            "method_parameters": (("","SELF","REQ"),("surface","_ObjectRoot._SurfaceRoot","REQ"),("parameter","array_of dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }
#===============================================================================
# _NurbsCurveModf
#===============================================================================
class _NurbsCurveModf(object):
    inherits = ('_CurveRootModf',)
    class Methods(object):
        close_curve = {
            "method_name": "close",
            "method_parameters": (("","SELF","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }        
        extend_curve = {
            "method_name": "extend",
            "method_parameters": (("","SELF","REQ"),("crv_type","int","REQ"),("side","int","REQ"),("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }
        extend_curve_length = {
            "method_name": "extend_length",
            "method_parameters": (("","SELF","REQ"),("crv_type","int","REQ"),("side","int","REQ"),("length","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }
        extend_curve_point = {
            "method_name": "extend_pnt",
            "method_parameters": (("","SELF","REQ"),("side","int","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }        
#===============================================================================
# Arc
#===============================================================================
class Arc(object):
    inherits = ("_CurveRoot", )
    holds = {
                   
        #general object holds
        "defm": "_CurveRootDefm",          
        "prop": "_ObjectRootProp",        
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_CurveRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_ArcModf",
        "eval": "_CurveRootEval",
        "test": "_CurveRootTest",#inherits from object level
        "dupl": "_ArcDupl",#inherits from object level
        
        #arc holds
        "prop": "_ArcProp",
        "func": "_CurveRootFunc",        
    }    
    class Constructors(object):
        add_arc = {#ed
            "method_name": "create",
            "method_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ"),("angle","dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_arc_3_pt = {#ed
            "method_name": "create_by_3pt",#inconsistent naming
            "method_parameters": (("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_fillet_curve = {#ed
            "method_name": "create_by_fillet",
            "method_parameters": (("curve_0","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("curve_1","_ObjectRoot._CurveRoot.NurbsCurve","REQ"),("radius","dbl","OPT"),("point_0","array_of dbl","OPT"),("point_1","array_of dbl","OPT"),),
            "method_returns": ("SELF","null")
        }
      
               
#===============================================================================
# _ArcFunc
#===============================================================================
class _ArcDupl(object):
    inherits = None
    class Methods(object):  
        
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")         
            }         
        offset_curve = {
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("direction_point","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")
        } 
        add_sub_crv = {#ed
            "method_name": "copy_by_sub",
            "method_parameters": (("","SELF","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")
        } 
        trim_curve = {#ed
            "method_name": "copy_by_trim",
            "method_parameters": (("","SELF","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")
        }
        
        #returns arrays
        split_curve = {#this has the delete parameter
            "method_name": "copy_by_split",
            "method_parameters": (("","SELF","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot.Arc","null")
        }
        
#===============================================================================
# _ArcProp
#===============================================================================
class _ArcProp(object):
    inherits = ("_CurveRootProp", )
    class Methods(object):    
        arc_angle = {#ed
            "method_name": "angle",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
        arc_center_point = {#ed
            "method_name": "center_pnt",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
        arc_mid_point = {#ed
            "method_name": "mid_pnt",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
        arc_radius = {#ed
            "method_name": "radius",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
#===============================================================================
# ArcModf
#===============================================================================
class _ArcModf(object):
    inherits = ('_CurveRootModf',)
    class Methods(object):
        close_curve = {
            "method_name": "close",
            "method_parameters": (("","SELF","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")
        }        
        extend_curve = {
            "method_name": "extend",
            "method_parameters": (("","SELF","REQ"),("crv_type","int","REQ"),("side","int","REQ"),("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")
        }
        extend_curve_length = {
            "method_name": "extend_length",
            "method_parameters": (("","SELF","REQ"),("crv_type","int","REQ"),("side","int","REQ"),("length","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")
        }
        extend_curve_point = {
            "method_name": "extend_pnt",
            "method_parameters": (("","SELF","REQ"),("side","int","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")
        }
#===============================================================================
# EllipticalArc
#===============================================================================
class EllipticalArc(object):
    inherits = ("_CurveRoot", )
    holds = {
                   
        #general object holds
        "defm": "_CurveRootDefm",          
        "prop": "_ObjectRootProp",        
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_CurveRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_EllipticalArcModf",
        "eval": "_CurveRootEval",
        "test": "_CurveRootTest",#inherits from object level
        "dupl": "_EllipticalArcDupl",#inherits from object level
        
        #ell arc holds
        "prop": "_CurveRootProp",
        "func": "_CurveRootFunc",        
    }    

        
#===============================================================================
# _EllipticalArcDupl
#===============================================================================
class _EllipticalArcDupl(object):
    inherits = None
    class Methods(object):   
        
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")         
            }         
        offset_curve = {
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("direction_point","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")
        } 
        split_curve = {#this has the delete parameter
            "method_name": "copy_by_split",
            "method_parameters": (("","SELF","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot.EllipticalArc","null")
        }
        add_sub_crv = {#ed
            "method_name": "copy_by_sub",
            "method_parameters": (("","SELF","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")
        } 
        trim_curve = {#ed
            "method_name": "copy_by_trim",
            "method_parameters": (("","SELF","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")
        }   
        
#===============================================================================
# _EllipticalArcModf
#===============================================================================
class _EllipticalArcModf(object):
    inherits = ('_CurveRootModf',)
    class Methods(object):
        close_curve = {
            "method_name": "close",
            "method_parameters": (("","SELF","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")
        }        
        extend_curve = {
            "method_name": "extend",
            "method_parameters": (("","SELF","REQ"),("crv_type","int","REQ"),("side","int","REQ"),("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")
        }
        extend_curve_length = {
            "method_name": "extend_length",
            "method_parameters": (("","SELF","REQ"),("crv_type","int","REQ"),("side","int","REQ"),("length","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")
        }
        extend_curve_point = {
            "method_name": "extend_pnt",
            "method_parameters": (("","SELF","REQ"),("side","int","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")
        }
#===============================================================================
# Circle
#===============================================================================
class Circle():
    inherits = ("_CurveRoot", )
    holds = {
                   
        #general object holds
        "defm": "_CurveRootDefm",          
        "prop": "_ObjectRootProp",        
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_CurveRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_CurveRootModf",
        "eval": "_CurveRootEval",
        "test": "_CurveRootTest",#inherits from object level
        "dupl": "_CircleDupl",#inherits from object level
        
        #circle holds
        "prop": "_CircleProp",
        "func": "_CurveRootFuncClsd",        
    }      
    class Constructors(object):
        add_circle = {#ed
            "method_name": "create",
            "method_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_circle_3_pt = {#ed
            "method_name": "create_by_3pt",#inconsistent naming
            "method_parameters": (("first_point","array_of dbl","REQ"),("second_point","array_of dbl","REQ"),("third_point","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
                  
#===============================================================================
# _CircleDupl
#===============================================================================
class _CircleDupl(object):
    inherits = None
    class Methods(object):
        
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._CurveRoot.Circle","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._CurveRoot.Circle","null")         
            }         
        offset_curve = {
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("direction_point","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Circle","null")
        }         
        add_sub_crv = {#ed
            "method_name": "copy_by_sub",
            "method_parameters": (("","SELF","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")
        }
        trim_curve = {#ed
            "method_name": "copy_by_trim",
            "method_parameters": (("","SELF","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Arc","null")
        }
        
        split_curve = {#this has the delete parameter
            "method_name": "copy_by_split",
            "method_parameters": (("","SELF","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot.Arc","null")
        }
#===============================================================================
# _CircleProp
#===============================================================================
class _CircleProp():
    inherits = ("_CurveRootProp", )
    class Methods(object):      
        circle_center_point = {#ed
            "method_name": "center_pnt",
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
    inherits = ("_CurveRoot", )
    holds = {
                   
        #general object holds
        "defm": "_CurveRootDefm",          
        "prop": "_ObjectRootProp",        
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_CurveRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_CurveRootModf",
        "eval": "_CurveRootEval",
        "test": "_CurveRootTest",#inherits from object level
        "dupl": "_EllipseDupl",#inherits from object level
        
        #ellipse holds
        "prop": "_EllipseProp",
        "func": "_CurveRootFuncClsd",        
    } 
    class Constructors(object):
        add_ellipse = {#ed
            "method_name": "create",
            "method_parameters": (("plane","array_of dbl","REQ"),("x_radius","dbl","REQ"),("y_radius","dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        add_ellipse_3_pt = {#ed
            "method_name": "create_by_3pt",#inconsistent naming
            "method_parameters": (("center","array_of dbl","REQ"),("second","array_of dbl","REQ"),("third","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
                
#===============================================================================
# _EllipseDupl
#===============================================================================
class _EllipseDupl(object):     
    inherits = None
    class Methods(object):     
        
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._CurveRoot.Ellipse","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._CurveRoot.Ellipse","null")         
            }         
        offset_curve = {
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("direction_point","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Ellipse","null")
        }         
        add_sub_crv = {#ed
            "method_name": "copy_by_sub",
            "method_parameters": (("","SELF","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")
        }
        trim_curve = {#ed
            "method_name": "copy_by_trim",
            "method_parameters": (("","SELF","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.EllipticalArc","null")
        }
        
        split_curve = {#this has the delete parameter
            "method_name": "copy_by_split",
            "method_parameters": (("","SELF","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot.EllipticalArc","null")
        }        
#===============================================================================
# _EllipseProp
#===============================================================================
class _EllipseProp(object):
    inherits = ("_CurveRootProp", )
    class Methods(object):
        ellipse_center_point = {#ed
            "method_name": "center_pnt",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        ellipse_quad_points = {#ed
            "method_name": "quad_pnts",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
        } 
        
#===============================================================================
# Line
#===============================================================================
class Line(object):
    inherits = ("_CurveRoot", )
    holds = {
                   
        #general object holds
        "defm": "_CurveRootDefm",          
        "prop": "_ObjectRootProp",        
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_CurveRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_LineModf",
        "eval": "_CurveRootEval",
        "test": "_CurveRootTest",#inherits from object level
        "dupl": "_LineDupl",#inherits from object level
        
        #properties
        "prop": "_CurveRootProp",
        "func": "_CurveRootFunc",        
    }     
    class Constructors(object):
        add_line = {#ed
            "method_name": "create",
            "method_parameters": (("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        
         
        
#===============================================================================
# _LineDupl
#===============================================================================
class _LineDupl(object):
    inherits = None
    class Methods(object):     
        
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._CurveRoot.Line","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._CurveRoot.Line","null")         
            }         
        offset_curve = {
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("direction_point","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Line","null")
        }
                
        add_sub_crv = {#ed
            "method_name": "copy_by_sub",
            "method_parameters": (("","SELF","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Line","null")
        }
        trim_curve = {#ed
            "method_name": "copy_by_trim",
            "method_parameters": (("","SELF","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Line","null")
        }
             
        split_curve = {#this has the delete parameter
            "method_name": "copy_by_split",
            "method_parameters": (("","SELF","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot.Line","null")
        }
#===============================================================================
# _LineModf
#===============================================================================
class _LineModf(object):
    inherits = ('_CurveRootModf',)
    class Methods(object):       
        extend_curve = {
            "method_name": "extend",
            "method_parameters": (("","SELF","REQ"),("crv_type","int","REQ"),("side","int","REQ"),("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Line","null")
        }
        extend_curve_length = {
            "method_name": "extend_length",
            "method_parameters": (("","SELF","REQ"),("crv_type","int","REQ"),("side","int","REQ"),("length","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Line","null")
        }
        extend_curve_point = {
            "method_name": "extend_pnt",
            "method_parameters": (("","SELF","REQ"),("side","int","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Line","null")
        }        
#===============================================================================
# Polyline
#===============================================================================
class Polyline(object):
    inherits = ("_CurveRoot", )
    holds = {
                   
        #general object holds
        "defm": "_CurveRootDefm",          
        "prop": "_ObjectRootProp",        
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_CurveRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_PolylineModf",
        "eval": "_CurveRootEval",
        "test": "_CurveRootTest",#inherits from object level
        "dupl": "_PolylineDupl",#inherits from object level
        
        #polyline holds
        "prop": "_PolylineProp",
        "func": "_CurveRootFuncClsd",
    }     
    class Constructors(object):
        add_polyline = {
            "method_name": "create",
            "method_parameters": (("points","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
        }
        convert_curve_to_polyline = {
            "method_name": "create_by_crv",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot","REQ"),("angle_tolerance","dbl","OPT"),("tolerance","dbl","OPT"),("delete_input","bln","OPT"),),
            "method_returns": ("SELF","null")
        } 
        
        #FROM MESH METHODS
        duplicate_mesh_border = {#ed
            "method_name": "create_by_mesh_border",
            "method_parameters": (("mesh","_ObjectRoot._MeshRoot","REQ"),),
            "method_returns": ("SELF","null")
            }  
        pull_curve_to_mesh = {#ed
            "method_name": "create_by_mesh_pull",
            "method_parameters": (("mesh","_ObjectRoot._MeshRoot","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),),
            "method_returns": ("SELF","null")
            }
          
#===============================================================================
# _PolylineDupl
#===============================================================================
class _PolylineDupl(object):
    inherits = None
    class Methods(object):     

        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._CurveRoot.Polyline","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._CurveRoot.Polyline","null")         
            }         
        offset_curve = {
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("direction_point","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Polyline","null")
        }
        trim_curve = {#ed
            "method_name": "copy_by_trim",
            "method_parameters": (("","SELF","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Polyline","null")#TODO: this could return a line
        }         
        add_sub_crv = {#ed
            "method_name": "copy_by_sub",
            "method_parameters": (("","SELF","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Polyline","null")#TODO: this could return a line
        } 
        
        split_curve = {#this has the delete parameter
            "method_name": "copy_by_split",
            "method_parameters": (("","SELF","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot.Polyline","null")#TODO: this could return a line
        }
#===============================================================================
# _PolylineProp
#===============================================================================
class _PolylineProp(object):
    inherits = ("_CurveRootProp",)
    class Methods(object):   
        polyline_vertices = {
            "method_name": "vertices",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
#===============================================================================
# _PolylineModf
#===============================================================================
class _PolylineModf(object):
    inherits = ('_CurveRootModf',)
    class Methods(object):
        close_curve = {
            "method_name": "close",
            "method_parameters": (("","SELF","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Polyline","null")
        }        
        extend_curve = {
            "method_name": "extend",
            "method_parameters": (("","SELF","REQ"),("crv_type","int","REQ"),("side","int","REQ"),("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Polyline","null")
        }
        extend_curve_length = {
            "method_name": "extend_length",
            "method_parameters": (("","SELF","REQ"),("crv_type","int","REQ"),("side","int","REQ"),("length","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Polyline","null")
        }
        extend_curve_point = {
            "method_name": "extend_pnt",
            "method_parameters": (("","SELF","REQ"),("side","int","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.Polyline","null")
        }
#===============================================================================
# PolyCurve - for the moment we will hide this class, since there are many complications
#===============================================================================

class PolyCurve(object):
    inherits = ("_CurveRoot",)
    holds = {
                   
        #general object holds
      
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_CurveRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        #"modf": "_CurveRootModf",
        #"test": "_CurveRootTest",#inherits from object tests        

        #polcurve holds
        "func": "_PolyCurveFunc",
        "dupl": "_PolyCurveDupl",
        "prop": "_PolyCurveProp",
        "eval": "_PolyCurveEval",
        
    }     
    class Constructors(object):
        join_curves = {#ed
            "method_name": "create",
            "method_parameters": (("curves","array_of _ObjectRoot._CurveRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("first_in_array_of SELF","null")
        }
        

#===============================================================================
# _PolyCurveFunc
#===============================================================================
class _PolyCurveFunc(object):
    inherits = ("_CurveRootFuncClsd",)
    class Methods(object):  
        explode_curves = {#this has the delete parameter - polys only
            "method_name": "explode",
            "method_parameters": (("","SELF","REQ"),("delete","bln","OPT"),),###
            "method_returns": ("array_of _ObjectRoot._CurveRoot.NurbsCurve","null")
        }   
#===============================================================================
# _PolyCurveDupl
#===============================================================================
class _PolyCurveDupl(object):
    inherits = None
    class Methods(object):     

        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._CurveRoot.PolyCurve","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._CurveRoot.PolyCurve","null")         
            }         
        offset_curve = {
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("direction_point","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.PolyCurve","null")
        }
        trim_curve = {#ed
            "method_name": "copy_by_trim",
            "method_parameters": (("","SELF","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._CurveRoot.PolyCurve","null")#TODO: this could return something else
        }         
        add_sub_crv = {#ed
            "method_name": "copy_by_sub",
            "method_parameters": (("","SELF","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._CurveRoot.PolyCurve","null")#TODO: this could return something else
        } 
        
        split_curve = {#this has the delete parameter
            "method_name": "copy_by_split",
            "method_parameters": (("","SELF","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot.PolyCurve","null")#TODO: this could return something else
        }
#===============================================================================
# _PolyCurveEval
#===============================================================================
class _PolyCurveEval(object):
    inherits = None
    class Methods(object):

        evaluate_curve = {#ed
            "method_name": "evaluate",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("index","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_tangent = {#ed
            "method_name": "tangent",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("index","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
#===============================================================================
# _PolyCurveProp
#===============================================================================
class _PolyCurveProp(object):
    inherits = None
    class Methods(object):
        
        #TODO: move method and fix index 
               
        poly_curve_count = {#ed
            "method_name": "segment_count",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT"),),
            "method_returns": ("number","null")
        }
        curve_domain = {#ed
            "method_name": "domain",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_degree = {#ed
            "method_name": "degree",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),),
            "method_returns": ("number","null")
        }
        curve_dim = {#ed
            "method_name": "dim",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),),
            "method_returns": ("number","null")
        }
        curve_length = {#ed
            "method_name": "length",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),("sub_domain","array_of int","OPT"),),
            "method_returns": ("number","null")
        }
        curve_start_point = {#ed
            "method_name": "start_pnt",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }        
        curve_mid_point = {#TODO: test mid_point function
            "method_name": "mid_pnt",
            "method_parameters": (("","SELF","REQ"),),#no index - this looks inconsistent - may be an error?
            "method_returns": ("array_of dbl","null")
        }
        curve_end_point = {#ed
            "method_name": "end_pnt",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }        

        curve_weights = {#ed
            "method_name": "weights",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        #knots
        curve_knot_count = {#ed
            "method_name": "knot_count",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),),
            "method_returns": ("number","null")
        }
        curve_knots = {#ed
            "method_name": "knots",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        #control points     
        curve_point_count = {#ed
            "method_name": "control_pnt_count",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),),
            "method_returns": ("number","null")
        }
        curve_points = {#ed
            "method_name": "control_pnts",
            "method_parameters": (("","SELF","REQ"),("index","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        #edit points
        curve_edit_points = {#ed
            "method_name": "edit_pnts",
            "method_parameters": (("","SELF","REQ"),("return_parameters","bln","REQ"),("index","int","REQ"),),
            "method_returns": ("array_of dbl", "null")
        } 
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#===============================================================================
# _CurveRootDefm
#===============================================================================
class _CurveRootDefm(object):
    inherits = None
    class Methods(object):
        box_morph_object = {#no plural version
            "method_name": "box_morph",
            "method_parameters": (("","SELF","REQ"),("box_points","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")# a slight simplification
            }          
        shear_object = {
            "method_name": "shear",
            "method_parameters": (("","SELF","REQ"),("origin","array_of dbl","REQ"),("ref_point","array_of dbl","REQ"),("angle","dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")# a slight simplification
            }
        transform_object = {
            "method_name": "transform",
            "method_parameters": (("","SELF","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),#what is this matrix
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")# a slight simplification
            }
#===============================================================================
# _CurveRootType
#===============================================================================
class _CurveRootType(object):
    inherits = ("_ObjectRootType",)
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
            "method_name": "is_crv",
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
            "method_name": "is_poly_crv",
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
class _CurveRootTest(object):
    inherits = ("_ObjectRootTest", )
    class Methods(object):
        is_curve_in_plane = {#ed
            "method_name": "in_plane",
            "method_parameters": (("","SELF","REQ"),("plane","array_of dbl","OPT"),),
            "method_returns": ("bln","null")
        }
        is_curve_closable = {#ed
            "method_name": "is_closable",
            "method_parameters": (("","SELF","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("bln","null")
        }
        is_curve_closed = {#ed
            "method_name": "is_closed",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_curve_linear = {#ed
            "method_name": "is_linear",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_curve_periodic = {#ed
            "method_name": "is_periodic",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_curve_planar = {#ed
            "method_name": "is_planar",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_curve_rational = {#ed
            "method_name": "is_rational",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        is_point_on_curve = {#ed
            "method_name": "is_pnt_on_crv",
            "method_parameters": (("","SELF","REQ"),("point","array_of int","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("bln","null")
        }
        planar_curve_collision = {
            "method_name": "planar_crv_collision",
            "method_parameters": (("","SELF","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT"),),
            "method_returns": ("bln","null")
        } 
#===============================================================================
# _CurveRootModf
#===============================================================================
class _CurveRootModf(object):
    inherits = ('_ObjectRootModf', )
    class Methods(object):
        curve_seam = {#ed
            "method_name": "seam",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),),
            "method_returns": ("bln","null")
        }
        fair_curve = {#ed
            "method_name": "fair",
            "method_parameters": (("","SELF","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("bln","null")
        }
        insert_curve_knot = {#ed
            "method_name": "insert_knot",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("symmetrical","bln","OPT"),),
            "method_returns": ("bln","null")
        }
        rebuild_curve = {#ed
            "method_name": "rebuild",
            "method_parameters": (("","SELF","REQ"),("degree","int","OPT"),("point_count","int","OPT"),),
            "method_returns": ("bln","null")
        }
        remove_curve_knot = {#ed
            "method_name": "remove_knot",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),),
            "method_returns": ("bln","null")
        }
        reverse_curve = {#ed
            "method_name": "reverse",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
        }
        simplify_curve = {#ed
            "method_name": "simplify",
            "method_parameters": (("","SELF","REQ"),("flags","int","OPT"),),
            "method_returns": ("bln","null")
        }

#===============================================================================
# _CurveRootStat
#===============================================================================
class _CurveRootStat(object):
    inherits = ("_ObjectRootStat",)
    
    class Methods(object):
        curve_arrows = {#ed
            "method_name": "arrows",
            "method_parameters": (("","SELF","REQ"),("style","int","OPT"),),
            "method_returns": ("number","null")
        }
#===============================================================================
# _CurveRootEval
#===============================================================================
class _CurveRootEval(object):
    inherits = None
    class Methods(object):
        curve_evaluate = {#ed
            "method_name": "derivatives",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("derivative","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        evaluate_curve = {#ed
            "method_name": "evaluate",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("index","int","OPT","EMPTY","HIDE"),),
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
        curve_tangent = {#ed
            "method_name": "tangent",
            "method_parameters": (("","SELF","REQ"),("parameter","dbl","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }

#===============================================================================
# _CurveRootProp
#===============================================================================
class _CurveRootProp(object):
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
        curve_discontinuity = {#ed
            "method_name": "discontinuity",
            "method_parameters": (("","SELF","REQ"),("style","int","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_domain = {#ed
            "method_name": "domain",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
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
            "method_name": "start_pnt",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }        
        curve_mid_point = {#TODO: test mid_point function
            "method_name": "mid_pnt",
            "method_parameters": (("","SELF","REQ"),),#no index - this looks inconsistent - may be an error?
            "method_returns": ("array_of dbl","null")
        }
        curve_end_point = {#ed
            "method_name": "end_pnt",
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
            "method_name": "control_pnt_count",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
        curve_points = {#ed
            "method_name": "control_pnts",
            "method_parameters": (("","SELF","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl","null")
        }
        #edit points
        curve_edit_points = {#ed
            "method_name": "edit_pnts",
            "method_parameters": (("","SELF","REQ"),("return_parameters","bln","OPT"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("array_of dbl", "null")
        } 
#===============================================================================
# _CurveRootPropOpen
#===============================================================================
class _CurveRootPropOpen(object):
    inherits = ('_CurveRootProp',)
    class Methods(object):
        pass
    
#===============================================================================
# _CurveRootPropClsd
#===============================================================================
class _CurveRootPropClsd(object):
    inherits = ('_CurveRootProp',)
    class Methods(object):
        pass
    
#===============================================================================
# _CurveRootPropOorC
#===============================================================================
class _CurveRootPropOorC(object):
    inherits = ('_CurveRootPropOpen', '_CurveRootPropClsd',)
    class Methods(object):
        pass
    
#===============================================================================
# _CurveRootFunc
#===============================================================================
class _CurveRootFunc(object):
    inherits = ("_ObjectRootFunc",)
    class Methods(object):
        
        divide_curve = {#ed
            "method_name": "divide_crv",
            "method_parameters": (("","SELF","REQ"),("segments","lng","REQ"),("create","bln","OPT"),("points","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
        }
        divide_curve_equidistant = {#ed
            "method_name": "divide_crv_equidistant",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
        }
        divide_curve_length = {#ed
            "method_name": "divide_crv_length",
            "method_parameters": (("","SELF","REQ"),("length","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_arc_length_point = {#ed
            "method_name": "crv_arc_length_pnt",
            "method_parameters": (("","SELF","REQ"),("length","dbl","REQ"),("from_start","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_contour_points = {#ed
            "method_name": "contour_pnts",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_deviation = {#ed
            "method_name": "deviation",
            "method_parameters": (("","SELF","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),),
            "method_returns": ("array_of number","null")
        }
        line_fit_from_points = {#ed
            "method_name": "line_fit_from_pnts",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        curve_directions_match = {#ed
            "method_name": "directions_match",
            "method_parameters": (("","SELF","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),),
            "method_returns": ("bln","null")
        }
        curve_closest_point = {#ed
            "method_name": "closest_pnt",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        }
        curve_radius = {#ed
            "method_name": "radius",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),("index","int","OPT","EMPTY","HIDE"),),
            "method_returns": ("number","null")
        } 
        
        
        
        make_curve_non_periodic = {
            "method_name": "make_non_periodic",
            "method_parameters": (("","SELF","REQ"),("delete","bln","OPT","FALSE","HIDE"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }
        make_curve_periodic = {
            "method_name": "make_periodic",
            "method_parameters": (("","SELF","REQ"),("delete","bln","OPT","FALSE","HIDE"),),
            "method_returns": ("_ObjectRoot._CurveRoot.NurbsCurve","null")
        }
        
        #TODO: fix these mixed return values
        """ 
        curve_closest_object = {#ed
            "method_name": "closest_ObjectRoot",
            "method_parameters": (("","SELF","REQ"),("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("array_of (_ObjectRoot._CurveRoot, array_of dbl, array_of dbl)","null")
        }
        """
        #TODO: fix these mixed return values
        """
        curve_fillet_points = {#TODO:documentation is not clear
            "method_name": "fillet_pnts",
            "method_parameters": (("","SELF","REQ"),("curve_0","str","REQ"),("radius","dbl","OPT"),("base_point_0","array_of dbl","OPT"),("base_point__1","array_of dbl","OPT"),),
            "method_returns": ("array_of (array_of dbl, array_of dbl, array_of dbl, array_of dbl, array_of dbl, array_of dbl)","_ObjectRoot._CurveRoot","null")
        }
        """    
        
        
        #intersections    
        #TODO: fix these mixed return values
        """
        curve_brep_intersect = {#TODO:can return either curve objects or point objects
            "method_name": "brep_intersection",
            "method_parameters": (("","SELF","REQ"),("brep","str","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot","null")
        }
        """
        curve_curve_intersection = {#TODO: figure this one out
            "method_name": "crv_intersection",
            "method_parameters": (("","SELF","REQ"),("curve","_ObjectRoot._CurveRoot","OPT"),("tolerance","dbl","OPT"),),
            "method_returns": ("array_of number","null")#check return values...
        }
        curve_surface_intersection = {#TODO: figure this one out
            "method_name": "srf_intersection",
            "method_parameters": (("","SELF","REQ"),("surface","_ObjectRoot._SurfaceRoot","REQ"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT"),),
            "method_returns": ("array_of number","null")#check return values...
        } 
#===============================================================================
# _CurveRootClosedFuncClsd - exclude arcs and lines
#===============================================================================
class _CurveRootFuncClsd(object):
    inherits = ('_CurveRootFunc',)
    class Methods(object):
         
        curve_area = {#TODO: no self
            "method_name": "area",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("array_of int","null")
        }
        curve_area_centroid = {#TODO: no self
            "method_name": "area_centroid",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("array_of dbl","null")
        }
        point_in_planar_closed_curve = {
            "method_name": "pnt_inside",
            "method_parameters": (("point","array_of dbl","REQ"),("","SELF","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT"),),
            "method_returns": ("number","null")
        }
        planar_closed_curve_containment = {
            "method_name": "containment",
            "method_parameters": (("","SELF","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT"),),
            "method_returns": ("number","null")
        }
        
        #booleans return curves or polycurves        
        
        curve_boolean_difference = {#ed
            "method_name": "boolean_difference",
            "method_parameters": (("","SELF","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot.PolyCurve","null")
        }
        curve_boolean_intersection = {#TODO: fix error
            "method_name": "boolean_intersection",
            "method_parameters": (("","SELF","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),),
            "method_returns": ("array_of _ObjectRoot._CurveRoot.PolyCurve","null")
        }
        curve_boolean_union = {#this has no self
            "method_name": "boolean_union",
            "method_parameters": (("curves","array_of _ObjectRoot._CurveRoot","REQ"),),#TODO: for this method, there is no SELF parameter
            "method_returns": ("array_of _ObjectRoot._CurveRoot.PolyCurve","null")
        }

#===============================================================================
# _CurveRoot
#===============================================================================
class _CurveRoot(object):
    inherits = ("_ObjectRoot", )
    #empty

#===============================================================================
# Mesh
#===============================================================================

class Mesh(object):
    inherits = ("_MeshRoot", )
    class Constructors(object):
        mesh_polyline = {#ed
            "method_name": "create_by_polyline",
            "method_parameters": (("polyline","_ObjectRoot._CurveRoot.Polyline","REQ"),),
            "method_returns": ("SELF","null")
        }


