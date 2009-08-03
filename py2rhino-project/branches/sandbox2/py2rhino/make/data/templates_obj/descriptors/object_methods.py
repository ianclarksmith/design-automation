#The data below will be used to generate the Rhinoscript function wrappers
#===============================================================================
# DocumentObjectFunctions
#===============================================================================
class _DocumentObjectFunctions(object):
    inherits = None
    class StaticMethods(object):
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
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        copy_objects_2 = {
            "method_name": "copy_and_xform",#renamed
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        mirror_objects = {
            "method_name": "mirror",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("start_pt","array_of dbl","REQ"),("end_pt","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        move_objects = {
            "method_name": "move",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        move_objects_2 = {
            "method_name": "move_and_xform",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("translation","array_of dbl","REQ"),),#first param was missing here
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        rotate_objects = {
            "method_name": "rotate",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("point","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","OPT"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        scale_objects = {
            "method_name": "scale",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("origin","array_of dbl","REQ"),("scale","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        orient_objects = {
            "method_name": "orient",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("reference","array_of dbl","REQ"),("target","array_of dbl","REQ"),("flags","int","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        shear_objects = {
            "method_name": "shear",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("origin","array_of dbl","REQ"),("ref_pt","array_of dbl","REQ"),("scale","array_of int","REQ"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        transform_objects = {
            "method_name": "transform",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),#what is this matrix
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        box_morph_object = {
            "method_name": "box_morph",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("box_points","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
            }
        remap_objects = {
            "method_name": "remap",
            "method_parameters": (("_ObjectRoot","array_of _ObjectRoot","REQ"),("src_plane","array_of dbl","REQ"),("dst_plane","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("array_of _ObjectRoot.GenericObject","null")
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
        """
        object_u_r_l = {#this one has some other possibilities
            "method_name": "set_url",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),("url","str","REQ")),
            "method_returns": ("number","null")
            }
        """
        #object
        delete_objects = {
            "method_name": "delete",
            "method_parameters": (("objects","array_of _ObjectRoot","REQ"),),
            "method_returns": ("number","null")
            }
        is_object = {
            "method_name": "is_object",
            "method_parameters": (("rhino_id","str","REQ"),),
            "method_returns": ("bln")
            }   
#===============================================================================
# Object
#===============================================================================
class GenericObject(object):
    inherits = ("_ObjectRoot",)
    holds = {
        #general holds
        "properties": "_ObjectRootProperties",        
        "groups": "_ObjectRootFunctionsGroups",
        "materials": "_ObjectRootFunctionsMaterial",
        "render": "_ObjectRootFunctionsRender",
        "state": "_ObjectRootFunctionsState",
        "transform": "_ObjectRootFunctionsTransform",
        "utility": "_ObjectRootFunctionsUtil",
        
        "test": "_ObjectRootFunctionsTest",#will be inherited 
        "type": "_ObjectRootFunctionsType",#exposed only here        
    }
    class Methods(object):
        delete_objects = {
            "method_name": "delete",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("number","null")        
            }
#===============================================================================
# ObjectRoot
#===============================================================================
class _ObjectRoot(object):
    inherits = None
    class Methods(object):
        delete_objects = {
            "method_name": "delete",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("number","null")        
            }
#===============================================================================
# ObjectGroups
#===============================================================================
class _ObjectRootFunctionsGroups(object):
    inherits = None
    class Methods(object):
        object_groups = {
            "method_name": "groups",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("array_of str","null") #this returns group names, but it should be converted to objects
            }
        object_top_group = {
            "method_name": "top_group",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("str","null")
            }
#===============================================================================
# ObjectMaterial
#===============================================================================
class _ObjectRootFunctionsMaterial(object):
    inherits = None
    class Methods(object):
        object_material_index = {
            "method_name": "index",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("number","null")
            }
        object_material_source = {#dup in Document
            "method_name": "source",
            "method_parameters": (("","self","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")        
            }
#===============================================================================
# ObjectProperties - color, layer
#===============================================================================
class _ObjectRootProperties(object):
    inherits = None
    class Methods(object):
        object_color = {
            "method_name": "color",
            "method_parameters": (("","self","REQ"),("color","lng","OPT")),
            "method_returns": ("number","null")        
            }
        object_color_source = {
            "method_name": "color_source",
            "method_parameters": (("","self","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")        
            }
        object_layer = {
            "method_name": "layer",
            "method_parameters": (("","self","REQ"),("layer","_Entity.Layer","OPT")),
            "method_returns": ("number","null")        
            }
        object_linetype = {
            "method_name": "linetype",
            "method_parameters": (("","self","REQ"),("layer","_Entity.Layer","OPT")),
            "method_returns": ("number","null")        
            }
        object_linetype_source = {
            "method_name": "linetype_source",
            "method_parameters": (("","self","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")        
            }
        object_names = {
            "method_name": "name",
            "method_parameters": (("","self","REQ"),("names","array_of str","OPT")),
            "method_returns": ("array of str","null")        
            }
        object_print_color = {
            "method_name": "print_color",
            "method_parameters": (("","self","REQ"),("color","lng","OPT")),
            "method_returns": ("number","null")        
            }
        object_print_color_source = {
            "method_name": "print_color_source",
            "method_parameters": (("","self","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")        
            }
        object_print_width = {
            "method_name": "print_width",
            "method_parameters": (("","self","REQ"),("width","dbl","OPT")),
            "method_returns": ("number","null")        
            }
        object_print_width_source = {
            "method_name": "print_width_source",
            "method_parameters": (("","self","REQ"),("source","int","OPT")),
            "method_returns": ("number","null")        
            }
        """ odd one with little use
        object_u_r_l = {
            "method_name": "url",
            "method_parameters": (("","self","REQ"),("url","str","OPT")),
            "method_returns": ("str","number","null")        
            }
        """
#===============================================================================
# _ObjectRootFunctionsRender
#===============================================================================
class _ObjectRootFunctionsRender(object):
    inherits = None
    class Methods(object):
        enable_object_mesh = {
            "method_name": "enable",#renamed
            "method_parameters": (("","self","REQ"),("enable","bln","OPT")),
            "method_returns": ("bln","null")        
            }
        add_object_mesh = {#note that this is not a constructor, despite the 'add' name
            "method_name": "add_mesh",
            "method_parameters": (("","self","REQ"),("quality","int","OPT"),("enable","bln","OPT")),
            "method_returns": ("bln","null")
            }
        object_has_mesh = {
            "method_name": "has_mesh",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("bln","null")
            }
        object_mesh_density = {
            "method_name": "density",
            "method_parameters": (("","self","REQ"),("density","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_max_angle = {
            "method_name": "max_angle",
            "method_parameters": (("","self","REQ"),("angle","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_max_aspect_ratio = {
            "method_name": "max_aspect_ratio",
            "method_parameters": (("","self","REQ"),("ratio","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_max_dist_edge_to_srf = {
            "method_name": "max_dist_edge_to_srf",
            "method_parameters": (("","self","REQ"),("distance","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_max_edge_length = {
            "method_name": "max_edge_length",
            "method_parameters": (("","self","REQ"),("length","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_min_edge_length = {
            "method_name": "min_edge_length",
            "method_parameters": (("","self","REQ"),("length","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_min_initial_grid_quads = {
            "method_name": "min_initial_grid_quads",
            "method_parameters": (("","self","REQ"),("quads","int","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_quality = {
            "method_name": "quality",
            "method_parameters": (("","self","REQ"),("quality","int","OPT")),
            "method_returns": ("bln","null")
            }
        object_mesh_settings = {
            "method_name": "settings",
            "method_parameters": (("","self","REQ"),("settings","int","OPT")),
            "method_returns": ("bln","null")
            }
#===============================================================================
# ObjectState
#===============================================================================
class _ObjectRootFunctionsState(object):
    inherits = None
    class Methods(object):
        select_objects = {
            "method_name": "select",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("number","null")        
            }
        show_objects = {
            "method_name": "show",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("number","null")        
            }
        unlock_objects = {
            "method_name": "unlock",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("number","null")        
            }
        unselect_objects = {
            "method_name": "unselect",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("number","null")        
            }
        match_object_attributes = {#Note that this one is different from the others
            0: {
            "method_name": "match_object_attributes",
            "method_parameters": (("targets","array_of _ObjectRoot","REQ"),("","self","OPT")),
            "method_returns": ("number","null")        
            },
            1: {
            "method_name": "reset_object_attributes",
            "method_parameters": (("","self","OPT"),("source","_ObjectRoot","OMIT")),### Here is an OMIT statement 
            "method_returns": ("number","null")        
            }}
        flash_object = {
            "method_name": "flash",
            "method_parameters": (("","self","REQ"),("style","bln","OPT")),
            "method_returns": ()        
            }
        hide_objects = {
            "method_name": "hide",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("number","null")        
            }
        lock_objects = {
            "method_name": "lock",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("number","null")        
            }
        object_layout = {
            "method_name": "move_to_layout_space",#renamed
            "method_parameters": (("","self","REQ"),("layout","str","OPT"),("return_name","bln","OPT")),
            "method_returns": ("str","null")
            }     
#===============================================================================
# ObjectRootTest
#===============================================================================
class _ObjectRootFunctionsTest(object):
    inherits = None
    class Methods(object):
        is_layout_object = {
            "method_name": "is_in_layout_space",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_hidden = {
            "method_name": "is_hidden",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_in_box = {
            "method_name": "is_in_box",
            "method_parameters": (("","self","REQ"),("box","array_of dbl","REQ"),("mode","bln","OPT")),
            "method_returns": ("bln", "null")
            }
        is_object_in_group = {
            "method_name": "is_in_group",
            "method_parameters": (("","self","REQ"),("group","str","OPT")),
            "method_returns": ("bln", "null")
            }
        is_object_locked = {
            "method_name": "is_locked",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_normal = {
            "method_name": "is_normal",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_reference = {
            "method_name": "is_reference",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_selectable = {
            "method_name": "is_selectable",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_selected = {
            "method_name": "is_selected",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_solid = {
            "method_name": "is_solid",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_object_valid = {
            "method_name": "is_valid",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("bln", "null")
            }
        is_visible_in_view = {
            "method_name": "is_visible_in_view",
            "method_parameters": (("","self","REQ"),("view","str","OPT")),
            "method_returns": ("bln", "null")
            }
#===============================================================================
# ObjectTransform
#===============================================================================
class _ObjectRootFunctionsTransform(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy",
            "method_parameters": (("","self","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("self","null")        
            }
        copy_object_2 = {
            "method_name": "copy_and_xform",#renamed
            "method_parameters": (("","self","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
            "method_returns": ("self","null")         
            }       
        mirror_object = {
            "method_name": "mirror",
            "method_parameters": (("","self","REQ"),("start_pt","array_of dbl","REQ"),("end_pt","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("self","null")   
            }
        move_object = {
            "method_name": "move",
            "method_parameters": (("","self","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
            "method_returns": ("self","null")   
            }
        move_object_2 = {
            "method_name": "move_and_xform",
            "method_parameters": (("","self","REQ"),("translation","array_of dbl","REQ"),),#first param was missing here
            "method_returns": ("self","null")       
            }
        rotate_object = {
            "method_name": "rotate",
            "method_parameters": (("","self","REQ"),("point","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","OPT"),("copy","bln","OPT")),
            "method_returns": ("self","null")         
            }
        scale_object = {
            "method_name": "scale",
            "method_parameters": (("","self","REQ"),("origin","array_of dbl","REQ"),("scale","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("self","null")          
            }
        orient_object = {
            "method_name": "orient",
            "method_parameters": (("","self","REQ"),("reference","array_of dbl","REQ"),("target","array_of dbl","REQ"),("flags","int","OPT")),
            "method_returns": ("self","null")       
            }
        #these ones change the type of object that is returned
        #TODO: ????
        shear_object = {
            "method_name": "shear",
            "method_parameters": (("","self","REQ"),("origin","array_of dbl","REQ"),("ref_pt","array_of dbl","REQ"),("scale","array_of int","REQ"),("copy","bln","OPT")),
            "method_returns": ("_ObjectRoot.GenericObject","null")        
            }
        transform_object = {
            "method_name": "transform",
            "method_parameters": (("","self","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),#what is this matrix
            "method_returns": ("_ObjectRoot.GenericObjec","null")         
            }
        remap_object = {
            "method_name": "remap",
            "method_parameters": (("","self","REQ"),("src_plane","array_of dbl","REQ"),("dst_plane","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("_ObjectRoot.GenericObjec","null")        
            }
        box_morph_object = {#no plural version
            "method_name": "box_morph",
            "method_parameters": (("","self","REQ"),("box_points","array_of dbl","REQ"),("copy","bln","OPT")),
            "method_returns": ("_ObjectRoot.GenericObjec","null")          
            }        
#===============================================================================
# _ObjectRootFunctionsType
#===============================================================================
class _ObjectRootFunctionsType(object):
    inherits = None
    class Methods(object):     
        object_type = {
            "method_name": "object_type",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("number","null")
            }   

#===============================================================================
# ObjectUtil
#===============================================================================
class _ObjectRootFunctionsUtil(object):
    inherits = None
    class Methods(object):
        object_dump = {
            "method_name": "dump",
            "method_parameters": (("","self","REQ"),("type","int","OPT")),
            "method_returns": ("str","null")
            }
        object_description = {
            "method_name": "description",
            "method_parameters": (("","self","REQ"),),
            "method_returns": ("str","null")
            }
   