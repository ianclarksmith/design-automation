#The data below will be used to generate the Rhinoscript function wrappers
#===============================================================================
# PolySurface
#===============================================================================
class PolySurface(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_SurfaceRootDefm",                
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootModf",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object level
        "dupl": "_PolySurfaceDupl",#inherits from object level
        
        #holds
        "func": "_PolySurfaceFunc",
    }    
    class Constructors(object):
        extrude_surface = {#ed
            "method_name": "create_by_srf_extrude",
            "method_parameters": (("surface","_ObjectRoot._SurfaceRoot","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),("cap","bln","OPT"),),
            "method_returns": ("SELF","null")
            }   
        join_surfaces = {#ed
            "method_name": "create_by_srf_join",
            "method_parameters": (("surfaces","array_of _ObjectRoot._SurfaceRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("SELF","null")
            }        
#===============================================================================
# _PolySurfaceDupl
#===============================================================================
class _PolySurfaceDupl(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._SurfaceRoot.PolySurface","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._SurfaceRoot.PolySurface","null")         
            }
        """
        offset_surface = {#ed
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot.PolySurface","null")  #TODO: see what is returned
            }   """ 
#===============================================================================
# _PolySurfaceProp
#===============================================================================
class _PolySurfaceFunc(object):
    inherits = ("_SurfaceRootFuncClsd", )
    class Methods(object):
        explode_polysurfaces = {
            "method_name": "explode",
            "method_parameters": (("","SELF","REQ"),("delete","bln","OPT"),),#this was an array - hope it still works
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot.NurbsSurface","null")
            } 
#===============================================================================
# Box
#===============================================================================
class Box(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_SurfaceRootDefm",          
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
      
        "modf": "_SurfaceRootModf",
        "func": "_SurfaceRootFuncClsd", #TODO: closed?
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object level
        "dupl": "_BoxDupl",#inherits from object level
        
        #holds
        "prop": "_SurfaceRootPropClsd",           
    } 
    class Constructors(object):
        add_box = {#ed
            "method_name": "create",
            "method_parameters": (("corner_points","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
#===============================================================================
# _BoxDupl
#===============================================================================
class _BoxDupl(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._SurfaceRoot.Box","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._SurfaceRoot.Box","null")         
            }
        """
        offset_surface = {#ed
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot","null")  #TODO: see what is returned
            }      """  
#===============================================================================
# Cone
#===============================================================================
class Cone(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_SurfaceRootDefm",                 
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootModf",
        "func": "_SurfaceRootFuncClsd",#TODO: closed?
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object level
        "dupl": "_ConeDupl",#inherits from object level
        
        #arc holds
        "prop": "_ConeProp",       
    }     
    class Constructors(object):
        add_cone = {#ed
            "method_name": "create",
            "method_parameters": (("base_point","array_of dbl","REQ"),("height_point","array_of dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT"),),
            "method_returns": ("SELF","null")
            }
        add_cone_2 = {#ed
            "method_name": "create_by_plane",
            "method_parameters": (("base_plane","array_of dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT"),),
            "method_returns": ("SELF","null")
            }        
        
#===============================================================================
# _ConeDupl
#===============================================================================
class _ConeDupl(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._SurfaceRoot.Cone","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._SurfaceRoot.Cone","null")         
            }
        """
        offset_surface = {#ed
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot","null")  #TODO: see what is returned
            }    """
    
#===============================================================================
# _ConeProp
#===============================================================================
class _ConeProp(object):
    inherits = ("_SurfaceRootPropClsd", )         
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
        "defm": "_SurfaceRootDefm",                
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootModf",
        "func": "_SurfaceRootFuncClsd",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object level
        "dupl": "_NurbsSurfaceDupl",#inherits from object level
        
        "prop": "_SurfaceRootPropClsd",        
    }    
    class Constructors(object):
        add_cut_plane = {#ed
            "method_name": "create_by_cut_plane",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("normal_vector","array_of dbl","OPT"),),
            "method_returns": ("SELF","null")
            }
        add_edge_srf = {#ed
            "method_name": "create_by_edge",
            "method_parameters": (("edge_curves","array_of _ObjectRoot._CurveRoot","REQ"),),
            "method_returns": ("SELF","null")
            }
        add_loft_srf = {#ed
            "method_name": "create_by_loft",
            "method_parameters": (("section_curves","array_of _ObjectRoot._CurveRoot","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT"),("srf_type","int","OPT"),("style","int","OPT"),("value","n","OPT"),("closed","bln","OPT"),),
            "method_returns": ("first_in_array_of SELF","null")#returns array
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
            "method_name": "create_by_control_pnt_grid",
            "method_parameters": (("count","array_of int","REQ"),("points","array_of dbl","REQ"),("degree","array_of dbl","OPT"),),
            "method_returns": ("SELF","null")
            }
        add_srf_pt = {#ed
            "method_name": "create_by_corner_pnts",
            "method_parameters": (("points","array_of dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        add_srf_pt_grid = {#ed
            "method_name": "create_by_pnt_grid",
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
            "method_returns": ("array_of SELF","null")#returns array
            }  


        #these return arrays
        
        add_planar_srf = {#ed
            "method_name": "create_by_planar_crv",
            "method_parameters": (("planar_curves","array_of _ObjectRoot._CurveRoot","REQ"),),
            "method_returns": ("first_in_array_of SELF","null")#returns array
            }
        add_sweep_1 = {#ed
            "method_name": "create_by_sweep_1",
            "method_parameters": (("rail","_ObjectRoot._CurveRoot","REQ"),("shapes","array_of _ObjectRoot._CurveRoot","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT"),("closed","bln","OPT"),("style","int","OPT"),("style_arg","va","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT"),),
            "method_returns": ("first_in_array_of SELF","null")#returns array
            }
        add_sweep_2 = {#ed
            "method_name": "create_by_sweep_2",
            "method_parameters": (("rails","array_of _ObjectRoot._CurveRoot","REQ"),("shapes","array_of _ObjectRoot._CurveRoot","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT"),("closed","bln","OPT"),("simple_sweep","bln","OPT"),("maintain_height","bln","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT"),),
            "method_returns": ("first_in_array_of SELF","null")#returns array
            }

#===============================================================================
# _NurbsSurfaceDupl
#===============================================================================
class _NurbsSurfaceDupl(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._SurfaceRoot.NurbsSurface","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._SurfaceRoot.NurbsSurface","null")         
            }
        offset_surface = {#ed
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot.NurbsSurface","null")
            }    
#===============================================================================
# Cylinder
#===============================================================================
class Cylinder(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_SurfaceRootDefm",                
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootModf",
        "func": "_SurfaceRootFuncClsd",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object level
        "dupl": "_CylinderDupl",#inherits from object level
        
        #arc holds
        "prop": "_CylinderProp",        
    }    
    class Constructors(object):
        
        add_cylinder = {#ed
            0: {
            "method_name": "create",
            "method_parameters": (("base_point","array_of dbl","REQ"),("height_point","array_of dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
            "method_returns": ("SELF","null"),
            },
            1: {
            "method_name": "create_by_plane",
            "method_parameters": (("base_plane","array_of dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
            "method_returns": ("SELF","null")            
            }}

        '''
        add_cylinder_2 = {#ed
            "method_name": "create_by_plane",
            "method_parameters": (("base_plane","array_of dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
            "method_returns": ("SELF","null")
            }    '''  
            
#===============================================================================
# _CylinderDupl
#===============================================================================
class _CylinderDupl(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._SurfaceRoot.Cylinder","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._SurfaceRoot.Cylinder","null")         
            }
        """
        offset_surface = {#ed
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot","null")  #TODO: see what is returned
            }    """
#===============================================================================
# _CylinderProp
#===============================================================================
class _CylinderProp(object):
    inherits = ("_SurfaceRootPropClsd", )         
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
        "defm": "_SurfaceRootDefm",               
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootModf",
        "func": "_SurfaceRootFuncClsd",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object level
        "dupl": "_PlaneSurfaceDupl",#inherits from object level

        "prop": "_SurfaceRootProp",
    }    
    class Constructors(object):
        add_plane_surface = {#ed
            "method_name": "create",
            "method_parameters": (("base_plane","array_of dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ"),),
            "method_returns": ("SELF","null")
            }
        
#===============================================================================
# _PlaneSurfaceDupl
#===============================================================================
class _PlaneSurfaceDupl(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._SurfaceRoot.PlaneSurface","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._SurfaceRoot.PlaneSurface","null")         
            }
        offset_surface = {#ed
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot._PlaneSurface","null")  #TODO: see what is returned
            }    
#===============================================================================
# Sphere
#===============================================================================
class Sphere(object):
    inherits = ("_SurfaceRoot", )
    holds = {
                   
        #general object holds
        "defm": "_SurfaceRootDefm",                 
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootModf",
        "func": "_SurfaceRootFuncClsd",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object level
        "dupl": "_SphereDupl",#inherits from object level
        
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
#===============================================================================
# _SphereDupl
#===============================================================================
class _SphereDupl(object):
    inherits = None 
    class Methods(object):
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._SurfaceRoot.Sphere","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._SurfaceRoot.Sphere","null")         
            }
        """
        offset_surface = {#ed
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot","null")  #TODO: see what is returned
            }    """
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
        "defm": "_SurfaceRootDefm",                
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #general curve holds
        "modf": "_SurfaceRootModf",
        "func": "_SurfaceRootFuncClsd",
        "eval": "_SurfaceRootEval",
        "test": "_SurfaceRootTest",#inherits from object level
        "dupl": "_TorusDupl",#inherits from object level
        
        #arc holds
        "prop": "_TorusProp",      
    }    
    class Constructors(object):
        add_torus = {#ed
            "method_name": "create",
            "method_parameters": (("base_point","array_of dbl","REQ"),("major_radius","dbl","REQ"),("minor_radius","dbl","REQ"),("direction","array_of dbl","OPT")),
            "method_returns": ("SELF","null")
            }
        add_torus_2 = {#ed
            "method_name": "create_by_plane",
            "method_parameters": (("base_plane","array_of dbl","REQ"),("major_radius","dbl","REQ"),("minor_radius","dbl","REQ")),
            "method_returns": ("SELF","null")
            }
#===============================================================================
# _TorusDupl
#===============================================================================
class _TorusDupl(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","OPT"),("end_point","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._SurfaceRoot.Torus","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation_vector","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("_ObjectRoot._SurfaceRoot.Torus","null")         
            }
        """
        offset_surface = {#ed
            "method_name": "copy_by_offset",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot","null")  #TODO: see what is returned
            }    """
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
        


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        
#===============================================================================
# _SurfaceRootDefm
#===============================================================================
class _SurfaceRootDefm(object):
    inherits = None
    class Methods(object):
        box_morph_object = {#no plural version
            "method_name": "box_morph",
            "method_parameters": (("","SELF","REQ"),("box_points","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("_ObjectRoot._SurfaceRoot.NurbsSurface","null")# a slight simplification
            }          
        shear_object = {
            "method_name": "shear",
            "method_parameters": (("","SELF","REQ"),("origin","array_of dbl","REQ"),("ref_point","array_of dbl","REQ"),("angle","dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("_ObjectRoot._SurfaceRoot.NurbsSurface","null")# a slight simplification
            }
        transform_object = {
            "method_name": "transform",
            "method_parameters": (("","SELF","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),#what is this matrix
            "method_returns": ("_ObjectRoot._SurfaceRoot.NurbsSurface","null")# a slight simplification
            }
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
class _SurfaceRootModf(object):
    inherits = ("_ObjectRootModf",)
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
            "method_name": "derivatives",
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
# _SurfaceRootFunc
#===============================================================================
class _SurfaceRootFunc(object):
    inherits = ("_ObjectRootFunc",)
    class Methods(object):
        make_surface_non_periodic = {
            "method_name": "make_non_periodic",
            "method_parameters": (("","SELF","REQ"),("direction","int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot.NurbsSurface","null")
            }
        make_surface_periodic = {
            "method_name": "make_periodic",
            "method_parameters": (("","SELF","REQ"),("direction","int","REQ"),("delete","bln","OPT"),),
            "method_returns": ("_ObjectRoot._SurfaceRoot.NurbsSurface","null")
            }            
        surface_closest_point = {
            "method_name": "closest_pnt",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("array_of number","null")
            }
        
        #TODO: fix these mixed return values
        surface_surface_intersection = {
            0:{#TODO: needs more work - points can also be returned
            "method_name": "intersect_2_srfs",
            "method_parameters": (("","SELF","REQ"),("surface_a","_ObjectRoot._SurfaceRoot","REQ"),("tolerance","dbl","OPT"),("create","bln","OPT", "TRUE", "HIDE"),),
            "method_returns": ("array_of number","null")#returns curves
            },
            1:{
            "method_name": "intersect_2_srfs_test",
            "method_parameters": (("","SELF","REQ"),("surface_a","_ObjectRoot._SurfaceRoot","REQ"),("tolerance","dbl","OPT"),("create","bln","OPT"),),
            "method_returns": ("array_of number","null")#returns lots of crazy stuff               
            }}  
        
        """      
        intersect_breps = {
            "method_name": "intersect_2_breps",
            "method_parameters": (("","SELF","REQ"),("brep","_ObjectRoot._SurfaceRoot","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("array_of _ObjectRoot","null")#returns curves and points
            }"""
            
        brep_closest_point = {
            "method_name": "closest_pnt_brep",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),),
            "method_returns": ("array_of number","null")
            }
        
        split_brep = {#ed
            "method_name": "split",
            "method_parameters": (("","SELF","REQ"),("cutter","_ObjectRoot._SurfaceRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot","null")
            }
        
        #TODO: needs custom imp
        cap_planar_holes = {
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

        #booleans return surfaces or polysurfaces
        
        boolean_difference = {
            0:{
            "method_name": "boolean_difference_1",
            "method_parameters": (("","SELF","REQ"),("breps","array_of _ObjectRoot._SurfaceRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot.PolySurface","null")
            },
            1:{
            "method_name": "boolean_difference_2",
            "method_parameters": (("breps","array_of _ObjectRoot._SurfaceRoot","REQ"),("","SELF","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot.PolySurface","null")               
            }}
        boolean_intersection = {
            "method_name": "boolean_intersection",
            "method_parameters": (("","SELF","REQ"),("breps","array_of _ObjectRoot._SurfaceRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot.PolySurface","null")
            }
        boolean_union = {#TODO: this has no SELF
            "method_name": "boolean_union",
            "method_parameters": (("breps","array_of _ObjectRoot._SurfaceRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._SurfaceRoot.PolySurface","null")
            }


#===============================================================================
# _SurfaceRoot
#===============================================================================
class _SurfaceRoot(object):
    inherits = ("_ObjectRoot", )


















