#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

#===============================================================================
# ObjectModify
#===============================================================================

#methods

copy_objects = {
    0: {                
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_copy",
    "method_parameters": (("objects","array_of _Object","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
    "method_returns": ("array","null")
    },
    1: {
    "method_location": "ObjectModify",
    "method_type": "METHOD",
    "method_name": "copy",
    "method_parameters": (("","self","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
    "method_returns": ("array","null")        
    }}
copy_objects_2 = {
    0: {
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_copy_and_xform",#renamed
    "method_parameters": (("objects","array_of _Object","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
    "method_returns": ("array","null")
    },
    1: {
    "method_location": "ObjectModify",
    "method_type": "METHOD",
    "method_name": "copy_and_xform",#renamed
    "method_parameters": (("","self","REQ"),("translation","array_of dbl","OPT"),),#first was param is missing here
    "method_returns": ("array","null")        
    }}
delete_objects = {
    0: {
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_delete",
    "method_parameters": (("objects","array_of _Object","REQ"),),
    "method_returns": ("number","null")
    },
    1: {
    "method_location": "ObjectModify",
    "method_type": "METHOD",
    "method_name": "delete",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")        
    }}




#===============================================================================
# ObjectState
#===============================================================================

select_objects = {
    0: {                  
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_select",
    "method_parameters": (("objects","array_of _Object","REQ"),),
    "method_returns": ("number","null")
    },
    1: {
    "method_location": "ObjectState",
    "method_type": "METHOD",
    "method_name": "select",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")        
    }}
show_objects = {
    0: {                
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_show",
    "method_parameters": (("objects","array_of _Object","REQ"),),
    "method_returns": ("number","null")
    },
    1: {
    "method_location": "ObjectState",
    "method_type": "METHOD",
    "method_name": "show",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")        
    }}
unlock_objects = {
    0: {                  
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_unlock",
    "method_parameters": (("objects","array_of _Object","REQ"),),
    "method_returns": ("number","null")
    },
    1: {
    "method_location": "ObjectState",
    "method_type": "METHOD",
    "method_name": "unlock",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")        
    }}
unselect_objects = {
    0: {                    
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_unselect",
    "method_parameters": (("objects","array_of _Object","REQ"),),
    "method_returns": ("number","null")
    },
    1: {
    "method_location": "ObjectState",
    "method_type": "METHOD",
    "method_name": "unselect",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")        
    }}
match_object_attributes = {#Note that this one is different from the others
    0: {                           
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_reset_attributes",
    "method_parameters": (("targets","array_of _Object","REQ"),("source","_Object","OMIT")),
    "method_returns": ("number","null")
    },
    1: {
    "method_location": "ObjectState",
    "method_type": "METHOD",
    "method_name": "match_object_attributes",
    "method_parameters": (("targets","array_of _Object","REQ"),("","self","OPT")),
    "method_returns": ("number","null")        
    },
    2: {
    "method_location": "ObjectState",
    "method_type": "METHOD",
    "method_name": "reset_object_attributes",
    "method_parameters": (("","self","OPT"),("source","_Object","OMIT")),
    "method_returns": ("number","null")        
    }}
flash_object = {
    0: {                
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_flash",
    "method_parameters": (("objects","array_of _Object","REQ"),("style","bln","OPT")),
    "method_returns": ()
    },
    1: {
    "method_location": "ObjectState",
    "method_type": "METHOD",
    "method_name": "flash",
    "method_parameters": (("","self","REQ"),("style","bln","OPT")),
    "method_returns": ()        
    }}
hide_objects = {
    0: {                
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_hide",
    "method_parameters": (("objects","array_of _Object","REQ"),),
    "method_returns": ("number","null")
    },
    1: {
    "method_location": "ObjectState",
    "method_type": "METHOD",
    "method_name": "hide",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")        
    }}
lock_objects = {
    0: {                
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_lock",
    "method_parameters": (("objects","array_of _Object","REQ"),),
    "method_returns": ("number","null")
    },
    1: {
    "method_location": "ObjectState",
    "method_type": "METHOD",
    "method_name": "lock",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")        
    }}
object_layout = {
    "method_location": "ObjectState",
    "method_type": "METHOD",
    "method_name": "move_to_layout_space",#renamed
    "method_parameters": (("","self","REQ"),("layout","str","OPT"),("return_name","bln","OPT")),
    "method_returns": ("string","string","null")
    }
#===============================================================================
# ObjectProperties - color, layer
#===============================================================================
object_color = {
    0: {                
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_color",
    "method_parameters": (("objects","array_of _Object","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","number","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "color",
    "method_parameters": (("","self","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","number","null")        
    }}
object_color_source = {
    0: {                       
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_color_source",
    "method_parameters": (("objects","array_of _Object","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "color_source",
    "method_parameters": (("","self","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")        
    }}
object_layer = {
    0: {                
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_layer",
    "method_parameters": (("objects","array_of _Object","REQ"),("layer","_Entity.Layer","OPT")),
    "method_returns": ("number","number","number","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "layer",
    "method_parameters": (("","self","REQ"),("layer","_Entity.Layer","OPT")),
    "method_returns": ("number","number","number","null")        
    }}
object_linetype = {
    0: {                   
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_linetype",
    "method_parameters": (("objects","array_of _Object","REQ"),("layer","_Entity.Layer","OPT")),
    "method_returns": ("number","number","number","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "linetype",
    "method_parameters": (("","self","REQ"),("layer","_Entity.Layer","OPT")),
    "method_returns": ("number","number","number","null")        
    }}
object_linetype_source = {
    0: {                          
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_linetype_source",
    "method_parameters": (("objects","array_of _Object","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "linetype_source",
    "method_parameters": (("","self","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")        
    }}

object_names = {
    0: {                
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_name",
    "method_parameters": (("objects","array_of _Object","REQ"),("names","array_of str","OPT")),
    "method_returns": ("array","array","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "name",
    "method_parameters": (("","self","REQ"),("names","array_of str","OPT")),
    "method_returns": ("array","array","null")        
    }}
object_print_color = {
    0: {                      
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_print_color",
    "method_parameters": (("objects","array_of _Object","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","number","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "print_color",
    "method_parameters": (("","self","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","number","null")        
    }}
object_print_color_source = {
    0: {                             
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_print_color_source",
    "method_parameters": (("objects","array_of _Object","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "print_color_source",
    "method_parameters": (("","self","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")        
    }}
object_print_width = {
    0: {                      
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_print_width",
    "method_parameters": (("objects","array_of _Object","REQ"),("width","dbl","OPT")),
    "method_returns": ("number","number","number","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "print_width",
    "method_parameters": (("","self","REQ"),("width","dbl","OPT")),
    "method_returns": ("number","number","number","null")        
    }}
object_print_width_source = {
    0: {                             
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_print_width_source",
    "method_parameters": (("objects","array_of _Object","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "print_width_source",
    "method_parameters": (("","self","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")        
    }}
object_u_r_l = {
    0: {                
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_url",
    "method_parameters": (("objects","array_of _Object","REQ"),("url","str","OPT")),
    "method_returns": ("string","string","number","null")
    },
    1: {
    "method_location": "ObjectProperties",
    "method_type": "METHOD",
    "method_name": "url",
    "method_parameters": (("","self","REQ"),("url","str","OPT")),
    "method_returns": ("string","string","number","null")        
    }}
object_description = {
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "description",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("string","null")
    }
#===============================================================================
# ObjectTransform
#===============================================================================
mirror_objects = {
    0: {                  
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_mirror",
    "method_parameters": (("objects","array_of _Object","REQ"),("start_pt","array_of dbl","REQ"),("end_pt","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("string","null")
    },
    1: {
    "method_location": "ObjectTransform",
    "method_type": "METHOD",
    "method_name": "mirror",
    "method_parameters": (("","self","REQ"),("start_pt","array_of dbl","REQ"),("end_pt","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("string","null")        
    }}
move_objects = {
    0: {                
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_move",
    "method_parameters": (("objects","array_of _Object","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
    "method_returns": ("number","null")
    },
    1: {
    "method_location": "ObjectTransform",
    "method_type": "METHOD",
    "method_name": "move",
    "method_parameters": (("","self","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
    "method_returns": ("number","null")        
    }}
move_objects_2 = {
    0: {                  
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_move_and_xform",
    "method_parameters": (("objects","array_of _Object","REQ"),("translation","array_of dbl","REQ"),),#first param was missing here
    "method_returns": ("number","null")
    },
    1: {
    "method_location": "ObjectTransform",
    "method_type": "METHOD",
    "method_name": "move_and_xform",
    "method_parameters": (("","self","REQ"),("translation","array_of dbl","REQ"),),#first param was missing here
    "method_returns": ("number","null")        
    }}
rotate_objects = {
    0: {                  
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_rotate",
    "method_parameters": (("objects","array_of _Object","REQ"),("point","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","OPT"),("copy","bln","OPT")),
    "method_returns": ("string","null")
    },
    1: {
    "method_location": "ObjectTransform",
    "method_type": "METHOD",
    "method_name": "rotate",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","OPT"),("copy","bln","OPT")),
    "method_returns": ("string","null")        
    }}
scale_objects = {
    0: {                 
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_scale",
    "method_parameters": (("objects","array_of _Object","REQ"),("origin","array_of dbl","REQ"),("scale","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("array","null")
    },
    1: {
    "method_location": "ObjectTransform",
    "method_type": "METHOD",
    "method_name": "scale",
    "method_parameters": (("","self","REQ"),("origin","array_of dbl","REQ"),("scale","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("array","null")        
    }}
orient_objects = {
    0: {                  
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_orient",
    "method_parameters": (("objects","array_of _Object","REQ"),("reference","array_of dbl","REQ"),("target","array_of dbl","REQ"),("flags","int","OPT")),
    "method_returns": ("array","null")
    },
    1: {
    "method_location": "ObjectTransform",
    "method_type": "METHOD",
    "method_name": "orient",
    "method_parameters": (("","self","REQ"),("reference","array_of dbl","REQ"),("target","array_of dbl","REQ"),("flags","int","OPT")),
    "method_returns": ("array","null")        
    }}
shear_objects = {
    0: {                 
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_shear",
    "method_parameters": (("objects","array_of _Object","REQ"),("origin","array_of dbl","REQ"),("ref_pt","array_of dbl","REQ"),("scale","array_of int","REQ"),("copy","bln","OPT")),
    "method_returns": ("array","null")
    },
    1: {
    "method_location": "ObjectTransform",
    "method_type": "METHOD",
    "method_name": "shear",
    "method_parameters": (("","self","REQ"),("origin","array_of dbl","REQ"),("ref_pt","array_of dbl","REQ"),("scale","array_of int","REQ"),("copy","bln","OPT")),
    "method_returns": ("array","null")        
    }}
transform_objects = {
    0: {                     
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_transform",
    "method_parameters": (("objects","array_of _Object","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),#what is this matrix
    "method_returns": ("array","null")
    },
    1: {
    "method_location": "ObjectTransform",
    "method_type": "METHOD",
    "method_name": "transform",
    "method_parameters": (("","self","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),#what is this matrix
    "method_returns": ("array","null")        
    }}
box_morph_object = {
    0: {
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_box_morph",
    "method_parameters": (("objects","array_of _Object","REQ"),("box_points","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("string","array","null")
    },
    1: {
    "method_location": "ObjectTransform",
    "method_type": "METHOD",
    "method_name": "box_morph",
    "method_parameters": (("","self","REQ"),("box_points","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("string","array","null")        
    }}
remap_objects = {
    0: {                 
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_remap",
    "method_parameters": (("_Object","array_of _Object","REQ"),("src_plane","array_of dbl","REQ"),("dst_plane","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("array","null")
    },
    1: {
    "method_location": "ObjectTransform",
    "method_type": "METHOD",
    "method_name": "remap",
    "method_parameters": (("","self","REQ"),("src_plane","array_of dbl","REQ"),("dst_plane","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("array","null")        
    }}
#===============================================================================
# ObjectType
#===============================================================================

#methods

object_type = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "object_type",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }
is_layout_object = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_in_layout_space",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null",)
    }
is_object = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_object",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ()
    }
is_object_hidden = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_hidden",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null",)
    }
is_object_in_box = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_in_box",
    "method_parameters": (("","self","REQ"),("box","array_of dbl","REQ"),("mode","bln","OPT")),
    "method_returns": ("null",)
    }
is_object_in_group = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_in_group",
    "method_parameters": (("","self","REQ"),("group","str","OPT")),
    "method_returns": ("null",)
    }
is_object_locked = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_locked",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null",)
    }
is_object_normal = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_normal",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null",)
    }
is_object_reference = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_reference",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null",)
    }
is_object_selectable = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_selectable",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null",)
    }
is_object_selected = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_selected",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null",)
    }
is_object_solid = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_solid",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null",)
    }
is_object_valid = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_valid",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null",)
    }
is_visible_in_view = {
    "method_location": "ObjectType",
    "method_type": "METHOD",
    "method_name": "is_visible_in_view",
    "method_parameters": (("","self","REQ"),("view","str","OPT")),
    "method_returns": ("null",)
    }

#===============================================================================
# ObjectRenderMesh
#===============================================================================

enable_object_mesh = {
    0: {                      
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_enable_render_mesh",#renamed
    "method_parameters": (("objects","array_of _Object","REQ"),("enable","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    },
    1: {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "enable",#renamed
    "method_parameters": (("","self","REQ"),("enable","bln","OPT")),
    "method_returns": ("boolean","boolean","null")        
    }}
add_object_mesh = {#note that this is not a constructor, despite the 'add' name
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "add_mesh",
    "method_parameters": (("","self","REQ"),("quality","int","OPT"),("enable","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_has_mesh = {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "has_mesh",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
object_mesh_density = {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "density",
    "method_parameters": (("","self","REQ"),("density","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_max_angle = {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "max_angle",
    "method_parameters": (("","self","REQ"),("angle","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_max_aspect_ratio = {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "max_aspect_ratio",
    "method_parameters": (("","self","REQ"),("ratio","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_max_dist_edge_to_srf = {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "max_dist_edge_to_srf",
    "method_parameters": (("","self","REQ"),("distance","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_max_edge_length = {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "max_edge_length",
    "method_parameters": (("","self","REQ"),("length","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_min_edge_length = {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "min_edge_length",
    "method_parameters": (("","self","REQ"),("length","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_min_initial_grid_quads = {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "min_initial_grid_quads",
    "method_parameters": (("","self","REQ"),("quads","int","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_quality = {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "quality",
    "method_parameters": (("","self","REQ"),("quality","int","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_settings = {
    "method_location": "ObjectRenderMesh",
    "method_type": "METHOD",
    "method_name": "settings",
    "method_parameters": (("","self","REQ"),("settings","int","OPT")),
    "method_returns": ("boolean","boolean","null")
    }


#===============================================================================
# ObjectMaterial
#===============================================================================

object_material_index = {
    "method_location": "ObjectMaterial",
    "method_type": "METHOD",
    "method_name": "index",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }

object_material_source = {
    0: {                          
    "method_location": "Document",
    "method_type": "CLASS_METHOD",
    "method_name": "objects_material_source",
    "method_parameters": (("objects","array_of _Object","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")
    },
    1: {
    "method_location": "ObjectMaterial",
    "method_type": "METHOD",
    "method_name": "source",
    "method_parameters": (("","self","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")        
    }}
#===============================================================================
# ObjectGroups
#===============================================================================

object_groups = {
    "method_location": "ObjectGroups",
    "method_type": "METHOD",
    "method_name": "groups",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array","null")
    }
object_top_group = {
    "method_location": "ObjectGroups",
    "method_type": "METHOD",
    "method_name": "top_group",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("string","null")
    }

#===============================================================================
# ObjectUtil
#===============================================================================

object_dump = {
    "method_location": "ObjectUtil",
    "method_type": "METHOD",
    "method_name": "dump",
    "method_parameters": (("","self","REQ"),("type","int","OPT")),
    "method_returns": ("string","null")
    }







