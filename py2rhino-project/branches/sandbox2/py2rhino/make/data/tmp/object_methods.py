#The data below will be used to generate the Rhinoscript function wrappers
#===============================================================================
# DocumentObjectFunctions
#===============================================================================
"""
class _DocumentObjectFunc(object):
    inherits = None
    class ClassMethods(object):
        #material
        object_material_source = {
            "method_name": "material_source",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")
            }
        #render mesh
        enable_object_mesh = {                  
            "method_name": "enable_render_mesh",#renamed
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("enable","bln","OPT")),
            "method_returns": ("bln","null")
            }
        #state
        select_objects = {
            "method_name": "select",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("number","null")
            }
        show_objects = {
            "method_name": "show",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("number","null")
            }
        unlock_objects = {
            "method_name": "unlock",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("number","null")
            }
        unselect_objects = {
            "method_name": "unselect",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("number","null")
            }
        match_object_attributes = {#Note that this one is different from the others
            "method_name": "reset_attributes",
            "method_parameters": (("targets","array_of _ObjectRoot","REQ"),("source","_ObjectRoot","OPT", "EMPTY", "HIDE")),
            "method_returns": ("number","null")
            }
        flash_object = {
            "method_name": "flash",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("style","bln","OPT")),
            "method_returns": ()
            }
        hide_objects = {
            "method_name": "hide",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("number","null")
            }
        lock_objects = {
            "method_name": "lock",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("number","null")
            }      
        #transforms
        copy_objects = {
            "method_name": "copy",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        copy_objects_2 = {
            "method_name": "copy_and_xform",#renamed
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        mirror_objects = {
            "method_name": "mirror",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("start_pt","array_of dbl","REQ"),("end_pt","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        move_objects = {
            "method_name": "move",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        move_objects_2 = {
            "method_name": "move_and_xform",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("translation","array_of dbl","REQ"),),#first param was missing here
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        rotate_objects = {
            "method_name": "rotate",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("point","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","OPT"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        scale_objects = {
            "method_name": "scale",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("origin","array_of dbl","REQ"),("scale","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        orient_objects = {
            "method_name": "orient",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("reference","array_of dbl","REQ"),("target","array_of dbl","REQ"),("flags","int","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        shear_objects = {
            "method_name": "shear",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("origin","array_of dbl","REQ"),("ref_pt","array_of dbl","REQ"),("scale","array_of int","REQ"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        transform_objects = {
            "method_name": "trfm",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),#what is this matrix
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        box_morph_object = {
            "method_name": "box_morph",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("box_points","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        remap_objects = {
            "method_name": "remap",
            "method_parameters": (("_ObjectRoot","array_of _ObjectRoot","REQ"),("src_plane","array_of dbl","REQ"),("dst_plane","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")#GenericObject
            }
        #properties
        object_color = {
            "method_name": "color",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("color","lng","OPT")),
            "method_returns": ("number","null")
            }
        object_color_source = {
            "method_name": "color_source",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")
            }
        object_layer = {
            "method_name": "layer",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("layer","_Entity.Layer","OPT")),
            "method_returns": ("number","null")
            }
        object_linetype = {
            "method_name": "linetype",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("layer","_Entity.Layer","OPT")),
            "method_returns": ("number","null")
            }
        object_linetype_source = {
            "method_name": "linetype_source",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")
            }
        object_names = {
            "method_name": "name",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("names","array_of str","OPT")),
            "method_returns": ("array_of str","null")
            }
        object_print_color = {
            "method_name": "print_color",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("color","lng","OPT")),
            "method_returns": ("number","null")
            }
        object_print_color_source = {
            "method_name": "print_color_source",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")
            }
        object_print_width = {
            "method_name": "print_width",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("width","dbl","OPT")),
            "method_returns": ("number","null")
            }
        object_print_width_source = {
            "method_name": "print_width_source",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")
            }
        '''
        object_u_r_l = {#this one has some other possibilities
            "method_name": "set_url",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("url","str","REQ")),
            "method_returns": ("number","null")
            }
        '''
        #object
        delete_objects = {
            "method_name": "delete",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("number","null")
            }
        is_object = {
            "method_name": "is_object",
            "method_parameters": (("rhino_id","str","REQ"),),
            "method_returns": ("bln", )
            }   """
#===============================================================================
# Object
#===============================================================================
class GenericObject(object):
    inherits = ("_ObjectRoot",)
    holds = {
        #general holds
        "defm": "_ObjectRootDefm",          
        "prop": "_ObjectRootProp",        
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",
        
        "test": "_ObjectRootTest",#will be inherited 
        "type": "_ObjectRootType",#exposed only here        
    }
#===============================================================================
# ObjectRoot
#===============================================================================
class _ObjectRoot(object):
    inherits = None
    
    pass
#===============================================================================
# ObjectGroups
#===============================================================================
class _ObjectRootMdfy(object):
    inherits = None
    
#===============================================================================
# ObjectFunc
#===============================================================================
class _ObjectRootFunc(object):    
    inherits = None
    class Methods(object):
        delete_objects = {
            "method_name": "delete",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")        
            }        
#===============================================================================
# ObjectGroups
#===============================================================================
class _ObjectRootGrps(object):
    inherits = None
    class Methods(object):
        object_groups = {
            "method_name": "groups",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of str","null") #this returns group names, but it should be converted to objects
            }
        object_top_group = {
            "method_name": "top_group",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("str","null")
            }
#===============================================================================
# ObjectMaterial
#===============================================================================
class _ObjectRootMtrl(object):
    inherits = None
    class Methods(object):
        object_material_index = {
            "method_name": "index",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")
            }
        object_material_source = {#dup in Document
            "method_name": "source",
            "method_parameters": (("","SELF","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")        
            }
#===============================================================================
# ObjectProperties - color, layer
#===============================================================================
class _ObjectRootProp(object):
    inherits = None
    class Methods(object):
        object_color = {
            "method_name": "color",
            "method_parameters": (("","SELF","REQ"),("color","lng","OPT")),
            "method_returns": ("number","null")        
            }
        object_color_source = {
            "method_name": "color_source",
            "method_parameters": (("","SELF","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")        
            }
        object_layer = {
            "method_name": "layer",
            "method_parameters": (("","SELF","REQ"),("layer","_Entity.Layer","OPT")),
            "method_returns": ("number","null")        
            }
        object_linetype = {
            "method_name": "linetype",
            "method_parameters": (("","SELF","REQ"),("layer","_Entity.Layer","OPT")),
            "method_returns": ("number","null")        
            }
        object_linetype_source = {
            "method_name": "linetype_source",
            "method_parameters": (("","SELF","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")        
            }
        object_names = {
            "method_name": "name",
            "method_parameters": (("","SELF","REQ"),("names","array_of str","OPT")),
            "method_returns": ("array_of str","null")        
            }
        object_print_color = {
            "method_name": "print_color",
            "method_parameters": (("","SELF","REQ"),("color","lng","OPT")),
            "method_returns": ("number","null")        
            }
        object_print_color_source = {
            "method_name": "print_color_source",
            "method_parameters": (("","SELF","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")        
            }
        object_print_width = {
            "method_name": "print_width",
            "method_parameters": (("","SELF","REQ"),("width","dbl","OPT")),
            "method_returns": ("number","null")        
            }
        object_print_width_source = {
            "method_name": "print_width_source",
            "method_parameters": (("","SELF","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")        
            }
        """ odd one with little use
        object_u_r_l = {
            "method_name": "url",
            "method_parameters": (("","SELF","REQ"),("url","str","OPT")),
            "method_returns": ("str","number","null")        
            }
        """
#===============================================================================
# _ObjectRootRndr
#===============================================================================
class _ObjectRootRndr(object):
    inherits = None
    class Methods(object):
        enable_object_mesh = {
            "method_name": "enable",#renamed
            "method_parameters": (("","SELF","REQ"),("enable","bln","OPT")),
            "method_returns": ("bln","null")        
            }
        add_object_mesh = {#note that this is not a constructor, despite the 'add' name
            "method_name": "add_mesh",
            "method_parameters": (("","SELF","REQ"),("quality","int","OPT"),("enable","bln","OPT")),
            "method_returns": ("bln","null")
            }
        object_has_mesh = {
            "method_name": "has_mesh",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        object_mesh_density = {
            "method_name": "density",
            "method_parameters": (("","SELF","REQ"),("density","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_max_angle = {
            "method_name": "max_angle",
            "method_parameters": (("","SELF","REQ"),("angle","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_max_aspect_ratio = {
            "method_name": "max_aspect_ratio",
            "method_parameters": (("","SELF","REQ"),("ratio","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_max_dist_edge_to_srf = {
            "method_name": "max_dist_edge_to_srf",
            "method_parameters": (("","SELF","REQ"),("distance","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_max_edge_length = {
            "method_name": "max_edge_length",
            "method_parameters": (("","SELF","REQ"),("length","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_min_edge_length = {
            "method_name": "min_edge_length",
            "method_parameters": (("","SELF","REQ"),("length","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_min_initial_grid_quads = {
            "method_name": "min_initial_grid_quads",
            "method_parameters": (("","SELF","REQ"),("quads","int","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_quality = {
            "method_name": "quality",
            "method_parameters": (("","SELF","REQ"),("quality","int","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_settings = {
            "method_name": "settings",
            "method_parameters": (("","SELF","REQ"),("settings","int","OPT")),
            "method_returns": ("bln","null")
            }
#===============================================================================
# ObjectState
#===============================================================================
class _ObjectRootStat(object):
    inherits = None
    class Methods(object):
        select_objects = {
            "method_name": "select",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")        
            }
        show_objects = {
            "method_name": "show",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")        
            }
        unlock_objects = {
            "method_name": "unlock",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")        
            }
        unselect_objects = {
            "method_name": "unselect",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")        
            }
        match_object_attributes = {#Note that this one is different from the others
            0: {
            "method_name": "match_object_attributes",
            "method_parameters": (("targets","array_of _ObjectRoot","REQ"),("","SELF","OPT")),
            "method_returns": ("number","null")        
            },
            1: {
            "method_name": "reset_object_attributes",
            "method_parameters": (("","SELF","OPT"),("source","_ObjectRoot","OMIT")),### Here is an OMIT statement 
            "method_returns": ("number","null")        
            }}
        flash_object = {
            "method_name": "flash",
            "method_parameters": (("","SELF","REQ"),("style","bln","OPT")),
            "method_returns": ()        
            }
        hide_objects = {
            "method_name": "hide",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")        
            }
        lock_objects = {
            "method_name": "lock",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")        
            }
        object_layout = {
            "method_name": "move_to_layout_space",#renamed
            "method_parameters": (("","SELF","REQ"),("layout","str","OPT"),("return_name","bln","OPT")),
            "method_returns": ("str","null")
            }     
#===============================================================================
# ObjectRootTest
#===============================================================================
class _ObjectRootTest(object):
    inherits = None
    class Methods(object):
        is_layout_object = {
            "method_name": "is_in_layout_space",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_hidden = {
            "method_name": "is_hidden",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_in_box = {
            "method_name": "is_in_box",
            "method_parameters": (("","SELF","REQ"),("box","array_of dbl","REQ"),("mode","bln","OPT")),
            "method_returns": ("bln", "null")
            }
        is_object_in_group = {
            "method_name": "is_in_group",
            "method_parameters": (("","SELF","REQ"),("group","str","OPT")),
            "method_returns": ("bln", "null")
            }
        is_object_locked = {
            "method_name": "is_locked",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_normal = {
            "method_name": "is_normal",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_reference = {
            "method_name": "is_reference",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_selectable = {
            "method_name": "is_selectable",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_selected = {
            "method_name": "is_selected",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_solid = {
            "method_name": "is_solid",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_valid = {
            "method_name": "is_valid",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_visible_in_view = {
            "method_name": "is_visible_in_view",
            "method_parameters": (("","SELF","REQ"),("view","str","OPT")),
            "method_returns": ("bln", "null")
            }
#===============================================================================
# ObjectTransform
#===============================================================================
class _ObjectRootTrfm(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy",
            "method_parameters": (("","SELF","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("SELF","null")        
            }
        copy_object_2 = {
            "method_name": "copy_by_vec",#renamed
            "method_parameters": (("","SELF","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("SELF","null")         
            }       
        mirror_object = {
            "method_name": "mirror",
            "method_parameters": (("","SELF","REQ"),("start_pt","array_of dbl","REQ"),("end_pt","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("SELF","null")   
            }
        move_object = {
            "method_name": "move",
            "method_parameters": (("","SELF","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
            "method_returns": ("SELF","null")   
            }
        move_object_2 = {
            "method_name": "move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation","array_of dbl","REQ"),),#first param was missing here
            "method_returns": ("SELF","null")       
            }
        rotate_object = {
            "method_name": "rotate",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","OPT"),("copy","bln","OPT")),
            "method_returns": ("SELF","null")         
            }
        scale_object = {
            "method_name": "scale",
            "method_parameters": (("","SELF","REQ"),("origin","array_of dbl","REQ"),("scale","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("SELF","null")          
            }
        orient_object = {
            "method_name": "orient",
            "method_parameters": (("","SELF","REQ"),("reference","array_of dbl","REQ"),("target","array_of dbl","REQ"),("flags","int","OPT")),
            "method_returns": ("SELF","null")       
            }
        remap_object = {
            "method_name": "remap",
            "method_parameters": (("","SELF","REQ"),("src_plane","array_of dbl","REQ"),("dst_plane","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("SELF","null")#GenericObject
            }
#===============================================================================
# ObjectTransform
#===============================================================================
class _ObjectRootDefm(object):
    inherits = None
    class Methods(object):
        box_morph_object = {#no plural version
            "method_name": "box_morph",
            "method_parameters": (("","SELF","REQ"),("box_points","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("_ObjectRoot","null")#GenericObject
            }          
        shear_object = {
            "method_name": "shear",
            "method_parameters": (("","SELF","REQ"),("origin","array_of dbl","REQ"),("ref_pt","array_of dbl","REQ"),("scale","array_of int","REQ"),("copy","bln","OPT")),
            "method_returns": ("_ObjectRoot","null")#GenericObject
            }
        transform_object = {
            "method_name": "trfm",
            "method_parameters": (("","SELF","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),#what is this matrix
            "method_returns": ("_ObjectRoot","null")#GenericObject
            }
#===============================================================================
# _ObjectRootType
#===============================================================================
class _ObjectRootType(object):
    inherits = None
    class Methods(object):     
        object_type = {
            "method_name": "object_type",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")
            }   

#===============================================================================
# ObjectUtil
#===============================================================================
class _ObjectRootUtil(object):
    inherits = None
    class Methods(object):
        object_dump = {
            "method_name": "dump",
            "method_parameters": (("","SELF","REQ"),("type","int","OPT")),
            "method_returns": ("str","null")
            }
        object_description = {
            "method_name": "description",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("str","null")
            }
   