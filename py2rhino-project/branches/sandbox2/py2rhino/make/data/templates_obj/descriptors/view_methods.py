#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.
#===============================================================================
# ConstructionPlane
#===============================================================================
add_named_c_plane = {
    "method_location": "_Entity.ConstructionPlane",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("","self","REQ"),("view","str","OPT"),),
    "method_returns": ("string","null")
    }
delete_named_c_plane = {
    "method_location": "_Entity.ConstructionPlane",
    "method_type": "METHOD",
    "method_name": "delete_named_c_plane",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
named_c_planes = {
    "method_location": "_Entity.ConstructionPlane",
    "method_type": "METHOD",
    "method_name": "named_c_planes",
    "method_parameters": (),
    "method_returns": ("array of _Entity.ConstructionPlane","null")
    }
restore_named_c_plane = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "restore_named_c_plane",
    "method_parameters": (("","self","REQ"),("view","str","OPT"),),
    "method_returns": ("string","null")
    }
#===============================================================================
# View
#===============================================================================
add_named_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "add_named_view",
    "method_parameters": (("","self","REQ"),("view","str","OPT"),),
    "method_returns": ("string","null")
    }
current_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "current_view",
    "method_parameters": (("","self","OPT"),("return_name","bln","OPT"),),
    "method_returns": ("string","string","null")
    }
delete_named_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "delete_named_view",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
maximize_restore_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "maximize_restore_view",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("null")
    }
named_views = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "named_views",
    "method_parameters": (),
    "method_returns": ("array of _Entity.View","null")
    }
rename_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "rename_view",
    "method_parameters": (("","self","REQ"),("new_title","str","REQ"),),
    "method_returns": ("string","null")
    }
restore_named_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "restore_named_view",
    "method_parameters": (("","self","REQ"),("view","str","OPT"),("restore_bitmap","bln","OPT"),),
    "method_returns": ("string","null")
    }
rotate_camera = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "rotate_camera",
    "method_parameters": (("","self","OPT"),("direction","int","OPT"),("angle","dbl","OPT"),),
    "method_returns": ("boolean","null")
    }
rotate_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "rotate_view",
    "method_parameters": (("","self","OPT"),("direction","int","OPT"),("angle","dbl","OPT"),),
    "method_returns": ("boolean","null")
    }
view_display_mode_ex = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_display_mode_ex",
    "method_parameters": (("","self","OPT"),("mode","str","OPT"),("return_names","bln","OPT"),),
    "method_returns": ("number","number","null")
    }
view_display_mode_name = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_display_mode_name",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("string","null")
    }
view_display_modes = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_display_modes",
    "method_parameters": (("return_name","bln","OPT"),),
    "method_returns": ("array of dbl","null")
    }
view_title = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_title",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("string","null")
    }
view_projection = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_projection",
    "method_parameters": (("","self","OPT"),("mode","int","OPT"),),
    "method_returns": ("number","number","null")
    }
view_radius = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_radius",
    "method_parameters": (("","self","OPT"),("radius","dbl","OPT"),),
    "method_returns": ("number","number","null")
    }
view_size = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_size",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("array of dbl","null")
    }
view_target = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_target",
    "method_parameters": (("","self","OPT"),("target","array of dbl","OPT"),),
    "method_returns": ("array of dbl","array of dbl","null")
    }
view_camera = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_camera",
    "method_parameters": (("","self","OPT"),("camera","array of dbl","OPT"),),
    "method_returns": ("array of dbl","array of dbl","null")
    }
view_camera_lens = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_camera_lens",
    "method_parameters": (("","self","OPT"),("length","dbl","OPT"),),
    "method_returns": ("number","number","null")
    }
view_camera_plane = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_camera_plane",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("array of (array of dbl,array of dbl,array of dbl,array of dbl)","null")
    }
view_camera_target = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_camera_target",
    "method_parameters": (("","self","OPT"),("camera","array of dbl","OPT"),("target","array of dbl","OPT"),),
    "method_returns": ("array of dbl","array of dbl","null")
    }
view_camera_up = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_camera_up",
    "method_parameters": (("","self","OPT"),("up_vector","array of dbl","OPT"),),
    "method_returns": ("array of dbl","array of dbl","null")
    }
zoom_bounding_box = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "zoom_bounding_box",
    "method_parameters": (("corners","array of dbl","REQ"),("view","str","OPT"),("all","bln","OPT"),),
    "method_returns": ("null")
    }
zoom_extents = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "zoom_extents",
    "method_parameters": (("","self","OPT"),("all","bln","OPT"),),
    "method_returns": ("null")
    }
zoom_selected = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "zoom_selected",
    "method_parameters": (("","self","OPT"),("all","bln","OPT"),),
    "method_returns": ("null")
    }
#===============================================================================
# _Entity
#===============================================================================

background_bitmap = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "background_bitmap",
    "method_parameters": (("","self","OPT"),("file_name","str","OPT"),("point","array of dbl","OPT"),("width","dbl","OPT"),),
    "method_returns": ("string","string","null")
    }
current_detail = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "current_detail",
    "method_parameters": (("","self","REQ"),("detail","str","OPT"),("return_names","bln","OPT"),),
    "method_returns": ("string","string","null")
    }
detail_names = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "detail_names",
    "method_parameters": (("","self","REQ"),("return_names","bln","OPT"),),
    "method_returns": ("array of _Entity","null")
    }
is_background_bitmap = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_background_bitmap",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_detail = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_detail",
    "method_parameters": (("","self","REQ"),("detail","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_layout = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layout",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_view = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_view",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_view_current = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_view_current",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_view_maximized = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_view_maximized",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("boolean","null")
    }
is_view_perspective = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_view_perspective",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("boolean","null")
    }
is_view_title_visible = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_view_title_visible",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("boolean","null")
    }
is_wallpaper = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_wallpaper",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
show_grid = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "show_grid",
    "method_parameters": (("","self","OPT"),("show","bln","OPT"),),
    "method_returns": ("boolean","boolean","null")
    }
show_grid_axes = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "show_grid_axes",
    "method_parameters": (("","self","OPT"),("show","bln","OPT"),),
    "method_returns": ("boolean","boolean","null")
    }
show_view_title = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "show_view_title",
    "method_parameters": (("","self","OPT"),("state","bln","OPT"),),
    "method_returns": ()
    }
show_world_axes = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "show_world_axes",
    "method_parameters": (("","self","OPT"),("show","bln","OPT"),),
    "method_returns": ("boolean","boolean","null")
    }
synchronize_c_planes = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "synchronize_c_planes",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("boolean","null")
    }
tilt_view = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "tilt_view",
    "method_parameters": (("","self","OPT"),("direction","int","OPT"),("angle","dbl","OPT"),),
    "method_returns": ("boolean","null")
    }
view_c_plane = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "view_c_plane",
    "method_parameters": (("","self","OPT"),("plane","array of dbl","OPT"),),
    "method_returns": ("array of dbl","array of dbl","null")
    }
view_names = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "view_names",
    "method_parameters": (("return_names","bln","OPT"),("type","int","OPT"),),
    "method_returns": ("array of dbl","null")
    }
view_near_corners = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "view_near_corners",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("array of dbl","null")
    }
wallpaper = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "wallpaper",
    "method_parameters": (("","self","OPT"),("file_name","str","OPT"),),
    "method_returns": ("string","string","null")
    }
wallpaper_gray_scale = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "wallpaper_gray_scale",
    "method_parameters": (("","self","OPT"),("gray_scale","bln","OPT"),),
    "method_returns": ("boolean","boolean","null")
    }
wallpaper_hidden = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "wallpaper_hidden",
    "method_parameters": (("","self","OPT"),("hidden","bln","OPT"),),
    "method_returns": ("boolean","boolean","null")
    }