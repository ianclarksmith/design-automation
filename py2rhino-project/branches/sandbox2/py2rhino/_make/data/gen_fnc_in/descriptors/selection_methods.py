#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here
#===============================================================================
# 
#===============================================================================
class select(object):    
    folder = "doc"

    class Functions(object):
        all_objects = {
            "method_name": "all_objects",
            "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        first_object = {
            "method_name": "first_object",
            "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("str","null")
            }
        get_curve_object = {
            "method_name": "get_crv_object",
            "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        get_object = {
            "method_name": "get_object",
            "method_parameters": (("message","str","OPT"),("type","int","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","array_of str","OPT")),
            "method_returns": ("str","null")
            }
        get_object_ex = {
            "method_name": "get_object_ex",
            "method_parameters": (("message","str","OPT"),("type","int","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","array_of str","OPT")),
            "method_returns": ("array_of str","null")
            }
        get_objects = {
            "method_name": "get_objects",
            "method_parameters": (("message","str","OPT"),("type","int","OPT"),("group","bln","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","array_of str","OPT")),
            "method_returns": ("array_of str","null")
            }
        get_objects_ex = {
            "method_name": "get_objects_ex",
            "method_parameters": (("message","str","OPT"),("type","int","OPT"),("group","bln","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","array_of str","OPT")),
            "method_returns": ("array_of str","null")
            }
        get_point_coordinates = {
            "method_name": "get_point_coords",
            "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        get_surface_object = {
            "method_name": "get_srf_object",
            "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        hidden_objects = {
            "method_name": "hidden_objects",
            "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        invert_selected_objects = {
            "method_name": "invert_selected_objects",
            "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        last_created_objects = {
            "method_name": "last_created_objects",
            "method_parameters": (("select","bln","OPT"),),
            "method_returns": ("array_of str","null")
            }
        last_object = {
            "method_name": "last_object",
            "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("str","null")
            }
        locked_objects = {
            "method_name": "locked_objects",
            "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        next_object = {
            "method_name": "next_object",
            "method_parameters": (("object","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("str","null")
            }
        normal_objects = {
            "method_name": "normal_objects",
            "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        objects_by_color = {
            "method_name": "objects_by_color",
            "method_parameters": (("color","lng","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        objects_by_group = {
            "method_name": "objects_by_group",
            "method_parameters": (("group","str","REQ"),("select","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        objects_by_layer = {
            "method_name": "objects_by_layer",
            "method_parameters": (("layer","str","REQ"),("select","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        objects_by_name = {
            "method_name": "objects_by_name",
            "method_parameters": (("name","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        objects_by_type = {
            "method_name": "objects_by_type",
            "method_parameters": (("type","int","REQ"),("select","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        objects_by_u_r_l = {
            "method_name": "objects_by_url",
            "method_parameters": (("url","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        prev_selected_objects = {
            "method_name": "prev_selected_objects",
            "method_parameters": (("select","bln","OPT"),),
            "method_returns": ("array_of str","null")
            }
        reference_objects = {
            "method_name": "reference_objects",
            "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        selected_objects = {
            "method_name": "selected_objects",
            "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        unselect_all_objects = {
            "method_name": "unselect_all_objects",
            "method_parameters": (),
            "method_returns": ("number",)
            }
        unselected_objects = {
            "method_name": "unselected_objects",
            "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
        visible_objects = {
            "method_name": "visible_objects",
            "method_parameters": (("view","str","OPT"),("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
            "method_returns": ("array_of str","null")
            }
