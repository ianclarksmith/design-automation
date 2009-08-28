#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

add_named_c_plane = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "add_named_c_plane",
    "method_parameters": (("name","str","REQ"),("view","str","OPT")),
    "method_returns": ("string","null")
    }
add_named_view = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "add_named_view",
    "method_parameters": (("name","str","REQ"),("view","str","OPT")),
    "method_returns": ("string","null")
    }
background_bitmap = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "background_bitmap",
    "method_parameters": (("view","str","OPT"),("file_name","str","OPT"),("point","array_of dbl","OPT"),("width","dbl","OPT")),
    "method_returns": ("string","string","null")
    }
current_detail = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "current_detail",
    "method_parameters": (("layout","str","REQ"),("detail","str","OPT"),("return_names","bln","OPT")),
    "method_returns": ("string","string","null")
    }
current_view = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "current_view",
    "method_parameters": (("view","str","OPT"),("return_name","bln","OPT")),
    "method_returns": ("string","string","null")
    }
delete_named_c_plane = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "delete_named_c_plane",
    "method_parameters": (("name","str","REQ"),),
    "method_returns": ("boolean","null")
    }
delete_named_view = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "delete_named_view",
    "method_parameters": (("name","str","REQ"),),
    "method_returns": ("boolean","null")
    }
detail_names = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "detail_names",
    "method_parameters": (("layout","str","REQ"),("return_names","bln","OPT")),
    "method_returns": ("array","null")
    }
is_background_bitmap = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "is_background_bitmap",
    "method_parameters": (("view","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_detail = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "is_detail",
    "method_parameters": (("layout","str","REQ"),("detail","str","REQ")),
    "method_returns": ("null",)
    }
is_layout = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "is_layout",
    "method_parameters": (("layout","str","REQ"),),
    "method_returns": ("null",)
    }
is_view = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "is_view",
    "method_parameters": (("view","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_view_current = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "is_view_current",
    "method_parameters": (("view","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_view_maximized = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "is_view_maximized",
    "method_parameters": (("view","str","OPT"),),
    "method_returns": ("boolean","null")
    }
is_view_perspective = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "is_view_perspective",
    "method_parameters": (("view","str","OPT"),),
    "method_returns": ("boolean","null")
    }
is_view_title_visible = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "is_view_title_visible",
    "method_parameters": (("view","str","OPT"),),
    "method_returns": ("boolean","null")
    }
is_wallpaper = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "is_wallpaper",
    "method_parameters": (("view","str","REQ"),),
    "method_returns": ("boolean","null")
    }
maximize_restore_view = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "maximize_restore_view",
    "method_parameters": (("view","str","OPT"),),
    "method_returns": ()
    }
named_c_plane = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "named_c_plane",
    "method_parameters": (("name","str","REQ"),),
    "method_returns": ("array","null")
    }
named_c_planes = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "named_c_planes",
    "method_parameters": (),
    "method_returns": ("array","null")
    }
named_views = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "named_views",
    "method_parameters": (),
    "method_returns": ("array","null")
    }
rename_view = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "rename_view",
    "method_parameters": (("old_title","str","REQ"),("new_title","str","REQ")),
    "method_returns": ("string","null")
    }
restore_named_c_plane = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "restore_named_c_plane",
    "method_parameters": (("name","str","REQ"),("view","str","OPT")),
    "method_returns": ("string","null")
    }
restore_named_view = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "restore_named_view",
    "method_parameters": (("name","str","REQ"),("view","str","OPT"),("restore_bitmap","bln","OPT")),
    "method_returns": ("string","null")
    }
rotate_camera = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "rotate_camera",
    "method_parameters": (("view","str","OPT"),("direction","int","OPT"),("angle","dbl","OPT")),
    "method_returns": ("boolean","null")
    }
rotate_view = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "rotate_view",
    "method_parameters": (("view","str","OPT"),("direction","int","OPT"),("angle","dbl","OPT")),
    "method_returns": ("boolean","null")
    }
show_grid = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "show_grid",
    "method_parameters": (("view","str","OPT"),("show","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
show_grid_axes = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "show_grid_axes",
    "method_parameters": (("view","str","OPT"),("show","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
show_view_title = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "show_view_title",
    "method_parameters": (("view","str","OPT"),("state","bln","OPT")),
    "method_returns": ()
    }
show_world_axes = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "show_world_axes",
    "method_parameters": (("view","str","OPT"),("show","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
synchronize_c_planes = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "synchronize_c_planes",
    "method_parameters": (("view","str","OPT"),),
    "method_returns": ("boolean","null")
    }
tilt_view = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "tilt_view",
    "method_parameters": (("view","str","OPT"),("direction","int","OPT"),("angle","dbl","OPT")),
    "method_returns": ("boolean","null")
    }
view_c_plane = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_c_plane",
    "method_parameters": (("view","str","OPT"),("plane","array_of dbl","OPT")),
    "method_returns": ("array","array","null")
    }
view_camera = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_camera",
    "method_parameters": (("view","str","OPT"),("camera","array_of dbl","OPT")),
    "method_returns": ("array","array","null")
    }
view_camera_lens = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_camera_lens",
    "method_parameters": (("view","str","OPT"),("length","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
view_camera_plane = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_camera_plane",
    "method_parameters": (("view","str","OPT"),),
    "method_returns": ("array","null")
    }
view_camera_target = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_camera_target",
    "method_parameters": (("view","str","OPT"),("camera","array_of dbl","OPT"),("target","array_of dbl","OPT")),
    "method_returns": ("array","array","null")
    }
view_camera_up = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_camera_up",
    "method_parameters": (("view","str","OPT"),("up_vector","array_of dbl","OPT")),
    "method_returns": ("array","array","null")
    }
view_display_mode = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_display_mode",
    "method_parameters": (("view","str","OPT"),("mode","int","OPT")),
    "method_returns": ("number","number","null")
    }
view_display_mode_ex = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_display_mode_ex",
    "method_parameters": (("view","str","OPT"),("mode","str","OPT"),("return_names","bln","OPT")),
    "method_returns": ("number","number","null")
    }
view_display_mode_name = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_display_mode_name",
    "method_parameters": (("mode","str","REQ"),),
    "method_returns": ("string","null")
    }
view_display_modes = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_display_modes",
    "method_parameters": (("return_name","bln","OPT"),),
    "method_returns": ("array","null")
    }
view_names = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_names",
    "method_parameters": (("return_names","bln","OPT"),("type","int","OPT")),
    "method_returns": ("array","null")
    }
view_near_corners = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_near_corners",
    "method_parameters": (("view","str","OPT"),),
    "method_returns": ("array","null")
    }
view_projection = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_projection",
    "method_parameters": (("view","str","OPT"),("mode","int","OPT")),
    "method_returns": ("number","number","null")
    }
view_radius = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_radius",
    "method_parameters": (("view","str","OPT"),("radius","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
view_size = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_size",
    "method_parameters": (("view","str","OPT"),),
    "method_returns": ("array","null")
    }
view_target = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_target",
    "method_parameters": (("view","str","OPT"),("target","array_of dbl","OPT")),
    "method_returns": ("array","array","null")
    }
view_title = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "view_title",
    "method_parameters": (("mode","str","REQ"),),
    "method_returns": ("string","null")
    }
wallpaper = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "wallpaper",
    "method_parameters": (("view","str","OPT"),("file_name","str","OPT")),
    "method_returns": ("string","string","null")
    }
wallpaper_gray_scale = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "wallpaper_gray_scale",
    "method_parameters": (("view","str","OPT"),("gray_scale","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
wallpaper_hidden = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "wallpaper_hidden",
    "method_parameters": (("view","str","OPT"),("hidden","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
zoom_bounding_box = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "zoom_bounding_box",
    "method_parameters": (("corners","array_of dbl","REQ"),("view","str","OPT"),("all","bln","OPT")),
    "method_returns": ()
    }
zoom_extents = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "zoom_extents",
    "method_parameters": (("view","str","OPT"),("all","bln","OPT")),
    "method_returns": ()
    }
zoom_selected = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "zoom_selected",
    "method_parameters": (("view","str","OPT"),("all","bln","OPT")),
    "method_returns": ()
    }
