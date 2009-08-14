#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

#===============================================================================
# ConstructionPlane
#===============================================================================

#constructors

add_named_c_plane = {
    "method_location": "_Entity.ConstructionPlane",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_named_c_plane",
    "method_parameters": (("","self","REQ"),("view","str","OPT"),),
    "method_returns": ("_Entity.ConstructionPlane","null")
    }

#methods

delete_named_c_plane = {
    "method_location": "_Entity.ConstructionPlane",
    "method_type": "METHOD",
    "method_name": "delete",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
restore_named_c_plane = {
    "method_location": "View",
    "method_type": "METHOD",
    "method_name": "restore",
    "method_parameters": (("","self","REQ"),("view","str","OPT"),),
    "method_returns": ("str","null")
    }



#===============================================================================
# View
#===============================================================================

#constructors

add_named_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "create_named_view",
    "method_parameters": (("","self","REQ"),("view","str","OPT"),),
    "method_returns": ("_Entity.View","null")
    }



#methods 

delete_named_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "delete",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
rename_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "rename",
    "method_parameters": (("","self","REQ"),("new_title","str","REQ"),),
    "method_returns": ("str","null")
    }
restore_named_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "restore",
    "method_parameters": (("","self","REQ"),("view","str","OPT"),("restore_bitmap","bln","OPT"),),
    "method_returns": ("str","null")
    }
view_display_mode_name = { 
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "display_mode_name",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("str","null")
    }
view_title = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "title",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("str","null")
    }
is_view_current = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_current",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }

#------------------------------------------------------------------------------ 
#methods/function mix

current_view = { #TODO: this one is strange - it acts as both a method and a function
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "current_view",
    "method_parameters": (("","self","REQ"),("return_name","bln","OPT"),),
    "method_returns": ("str","str","null")
    }
current_detail = {#this looks like it is in the worng place
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "current_detail",
    "method_parameters": (("","self","REQ"),("detail","str","OPT"),("return_names","bln","OPT"),),
    "method_returns": ("str","str","null")
    }

#with these methods, you can either pass in the view id, or the 'active view'
#can be used. But this is not very object like - so I guess we should assume that
#the current ID has to be passed in. So with the methods below, we have change 
#self arg from OPT to REQ 

maximize_restore_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "maximize_restore",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null")
    }
rotate_camera = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "rotate_camera",
    "method_parameters": (("","self","REQ"),("direction","int","OPT"),("angle","dbl","OPT"),),
    "method_returns": ("bln","null")
    }
rotate_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "rotate",
    "method_parameters": (("","self","REQ"),("direction","int","OPT"),("angle","dbl","OPT"),),
    "method_returns": ("bln","null")
    }
view_display_mode_ex = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "display_mode_ex",
    "method_parameters": (("","self","REQ"),("mode","str","OPT"),("return_names","bln","OPT"),),
    "method_returns": ("number","number","null")
    }
view_projection = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "projection",
    "method_parameters": (("","self","REQ"),("mode","int","OPT"),),
    "method_returns": ("number","number","null")
    }
view_radius = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "radius",
    "method_parameters": (("","self","REQ"),("radius","dbl","OPT"),),
    "method_returns": ("number","number","null")
    }
view_size = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "size",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
    }
view_target = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "target",
    "method_parameters": (("","self","REQ"),("target","array_of dbl","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
    }
view_camera = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "camera",
    "method_parameters": (("","self","REQ"),("camera","array_of dbl","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
    }
view_camera_lens = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "camera_lens",
    "method_parameters": (("","self","REQ"),("length","dbl","OPT"),),
    "method_returns": ("number","number","null")
    }
view_camera_plane = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "camera_plane",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of (array_of dbl,array_of dbl,array_of dbl,array_of dbl)","null")
    }
view_camera_target = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "camera_target",
    "method_parameters": (("","self","REQ"),("camera","array_of dbl","OPT"),("target","array_of dbl","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
    }
view_camera_up = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "camera_up",
    "method_parameters": (("","self","REQ"),("up_vector","array_of dbl","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
    }

zoom_extents = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "zoom_extents",
    "method_parameters": (("","self","REQ"),("all","bln","OPT"),),
    "method_returns": ("null")
    }
zoom_selected = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "zoom_selected",
    "method_parameters": (("","self","REQ"),("all","bln","OPT"),),
    "method_returns": ("null")
    }
background_bitmap = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "background_bitmap",
    "method_parameters": (("","self","REQ"),("file_name","str","OPT"),("point","array_of dbl","OPT"),("width","dbl","OPT"),),
    "method_returns": ("str","str","null")
    }


is_view_maximized = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "is_maximized",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_view_perspective = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "is_perspective",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_view_title_visible = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "is_title_visible",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }


is_wallpaper = {#change to has_
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "has_wallpaper",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_background_bitmap = {#change to has_
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "has_background_bitmap",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_detail = {#change to has_
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "has_detail",
    "method_parameters": (("","self","REQ"),("detail","str","REQ"),),
    "method_returns": ("bln","null")
    }
is_layout = {#if we made layout an object, then this would change to is_layout
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "has_layout",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }

show_grid = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "show_grid",
    "method_parameters": (("","self","REQ"),("show","bln","OPT"),),
    "method_returns": ("bln","bln","null")
    }
show_grid_axes = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "show_grid_axes",
    "method_parameters": (("","self","REQ"),("show","bln","OPT"),),
    "method_returns": ("bln","bln","null")
    }
show_view_title = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "show_title",
    "method_parameters": (("","self","REQ"),("state","bln","OPT"),),
    "method_returns": ()
    }
show_world_axes = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "show_world_axes",
    "method_parameters": (("","self","REQ"),("show","bln","OPT"),),
    "method_returns": ("bln","bln","null")
    }
synchronize_c_planes = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "synchronize_c_planes",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
tilt_view = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "tilt",
    "method_parameters": (("","self","REQ"),("direction","int","OPT"),("angle","dbl","OPT"),),
    "method_returns": ("bln","null")
    }
view_c_plane = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "c_plane",
    "method_parameters": (("","self","REQ"),("plane","array_of dbl","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
    }
view_near_corners = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "near_corners",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
    }
wallpaper = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "wallpaper",
    "method_parameters": (("","self","REQ"),("file_name","str","OPT"),),
    "method_returns": ("str","str","null")
    }
wallpaper_gray_scale = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "wallpaper_gray_scale",
    "method_parameters": (("","self","REQ"),("gray_scale","bln","OPT"),),
    "method_returns": ("bln","bln","null")
    }
wallpaper_hidden = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "wallpaper_hidden",
    "method_parameters": (("","self","REQ"),("hidden","bln","OPT"),),
    "method_returns": ("bln","bln","null")
    }
detail_names = {#this only works for layour views
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "detail_names",
    "method_parameters": (("","self","REQ"),("return_names","bln","OPT"),),
    "method_returns": ("array_of _Entity","null")
    }

zoom_bounding_box = {#.... looks odd
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "zoom_bounding_box",
    "method_parameters": (("corners","array_of dbl","REQ"),("view","str","REQ"),("all","bln","OPT"),),
    "method_returns": ("null")
    }

#------------------------------------------------------------------------------ 
#functions

view_display_modes = { #TODO: function has been skipped that might be useful
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "view_display_modes",
    "method_parameters": (("return_name","bln","OPT"),),
    "method_returns": ("array_of dbl","null")
    }
named_views = {
    "method_location": "_Entity.View",
    "method_type": "METHOD",
    "method_name": "named_views",
    "method_parameters": (),
    "method_returns": ("array_of _Entity.View","null")
    }
#TODO: we need a function to get the active view

#===============================================================================
# _Entity
#===============================================================================

#methods

is_view = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_view",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }

#===============================================================================
# Document
#===============================================================================

view_names = {
    "method_location": "Document",
    "method_type": "METHOD",
    "method_name": "view_names",
    "method_parameters": (("return_names","bln","OPT"),("type","int","OPT"),),
    "method_returns": ("array_of dbl","null")
    }
named_c_planes = {
    "method_location": "Document",
    "method_type": "METHOD",
    "method_name": "named_c_planes",
    "method_parameters": (),
    "method_returns": ("array_of _Entity.ConstructionPlane","null")
    }