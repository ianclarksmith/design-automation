#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_named_c_plane = {
    "function_location": "view",
    "function_com_id": 280,
    "function_vb_name": "AddNamedCPlane",
    "function_name": "add_named_c_plane",
    "function_parameters": (("name","str","REQ"),("view","str","OPT")),
    "function_returns": ("string","null")
    }
add_named_view = {
    "function_location": "view",
    "function_com_id": 281,
    "function_vb_name": "AddNamedView",
    "function_name": "add_named_view",
    "function_parameters": (("name","str","REQ"),("view","str","OPT")),
    "function_returns": ("string","null")
    }
background_bitmap = {
    "function_location": "view",
    "function_com_id": 780,
    "function_vb_name": "BackgroundBitmap",
    "function_name": "background_bitmap",
    "function_parameters": (("view","str","OPT"),("file_name","str","OPT"),("point","array_of dbl","OPT"),("width","dbl","OPT")),
    "function_returns": ("string","string","null")
    }
current_detail = {
    "function_location": "view",
    "function_com_id": 923,
    "function_vb_name": "CurrentDetail",
    "function_name": "current_detail",
    "function_parameters": (("layout","str","REQ"),("detail","str","OPT"),("return_names","bln","OPT")),
    "function_returns": ("string","string","null")
    }
current_view = {
    "function_location": "view",
    "function_com_id": 251,
    "function_vb_name": "CurrentView",
    "function_name": "current_view",
    "function_parameters": (("view","str","OPT"),("return_name","bln","OPT")),
    "function_returns": ("string","string","null")
    }
delete_named_c_plane = {
    "function_location": "view",
    "function_com_id": 284,
    "function_vb_name": "DeleteNamedCPlane",
    "function_name": "delete_named_c_plane",
    "function_parameters": (("name","str","REQ"),),
    "function_returns": ("boolean","null")
    }
delete_named_view = {
    "function_location": "view",
    "function_com_id": 285,
    "function_vb_name": "DeleteNamedView",
    "function_name": "delete_named_view",
    "function_parameters": (("name","str","REQ"),),
    "function_returns": ("boolean","null")
    }
detail_names = {
    "function_location": "view",
    "function_com_id": 922,
    "function_vb_name": "DetailNames",
    "function_name": "detail_names",
    "function_parameters": (("layout","str","REQ"),("return_names","bln","OPT")),
    "function_returns": ("array","null")
    }
is_background_bitmap = {
    "function_location": "view",
    "function_com_id": 779,
    "function_vb_name": "IsBackgroundBitmap",
    "function_name": "is_background_bitmap",
    "function_parameters": (("view","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_detail = {
    "function_location": "view",
    "function_com_id": 921,
    "function_vb_name": "IsDetail",
    "function_name": "is_detail",
    "function_parameters": (("layout","str","REQ"),("detail","str","REQ")),
    "function_returns": ("null",)
    }
is_layout = {
    "function_location": "view",
    "function_com_id": 920,
    "function_vb_name": "IsLayout",
    "function_name": "is_layout",
    "function_parameters": (("layout","str","REQ"),),
    "function_returns": ("null",)
    }
is_view = {
    "function_location": "view",
    "function_com_id": 252,
    "function_vb_name": "IsView",
    "function_name": "is_view",
    "function_parameters": (("view","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_view_current = {
    "function_location": "view",
    "function_com_id": 253,
    "function_vb_name": "IsViewCurrent",
    "function_name": "is_view_current",
    "function_parameters": (("view","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_view_maximized = {
    "function_location": "view",
    "function_com_id": 254,
    "function_vb_name": "IsViewMaximized",
    "function_name": "is_view_maximized",
    "function_parameters": (("view","str","OPT"),),
    "function_returns": ("boolean","null")
    }
is_view_perspective = {
    "function_location": "view",
    "function_com_id": 255,
    "function_vb_name": "IsViewPerspective",
    "function_name": "is_view_perspective",
    "function_parameters": (("view","str","OPT"),),
    "function_returns": ("boolean","null")
    }
is_view_title_visible = {
    "function_location": "view",
    "function_com_id": 256,
    "function_vb_name": "IsViewTitleVisible",
    "function_name": "is_view_title_visible",
    "function_parameters": (("view","str","OPT"),),
    "function_returns": ("boolean","null")
    }
is_wallpaper = {
    "function_location": "view",
    "function_com_id": 531,
    "function_vb_name": "IsWallpaper",
    "function_name": "is_wallpaper",
    "function_parameters": (("view","str","REQ"),),
    "function_returns": ("boolean","null")
    }
maximize_restore_view = {
    "function_location": "view",
    "function_com_id": 257,
    "function_vb_name": "MaximizeRestoreView",
    "function_name": "maximize_restore_view",
    "function_parameters": (("view","str","OPT"),),
    "function_returns": ()
    }
named_c_plane = {
    "function_location": "view",
    "function_com_id": 286,
    "function_vb_name": "NamedCPlane",
    "function_name": "named_c_plane",
    "function_parameters": (("name","str","REQ"),),
    "function_returns": ("array","null")
    }
named_c_planes = {
    "function_location": "view",
    "function_com_id": 258,
    "function_vb_name": "NamedCPlanes",
    "function_name": "named_c_planes",
    "function_parameters": (),
    "function_returns": ("array","null")
    }
named_views = {
    "function_location": "view",
    "function_com_id": 259,
    "function_vb_name": "NamedViews",
    "function_name": "named_views",
    "function_parameters": (),
    "function_returns": ("array","null")
    }
rename_view = {
    "function_location": "view",
    "function_com_id": 260,
    "function_vb_name": "RenameView",
    "function_name": "rename_view",
    "function_parameters": (("old_title","str","REQ"),("new_title","str","REQ")),
    "function_returns": ("string","null")
    }
restore_named_c_plane = {
    "function_location": "view",
    "function_com_id": 282,
    "function_vb_name": "RestoreNamedCPlane",
    "function_name": "restore_named_c_plane",
    "function_parameters": (("name","str","REQ"),("view","str","OPT")),
    "function_returns": ("string","null")
    }
restore_named_view = {
    "function_location": "view",
    "function_com_id": 283,
    "function_vb_name": "RestoreNamedView",
    "function_name": "restore_named_view",
    "function_parameters": (("name","str","REQ"),("view","str","OPT"),("restore_bitmap","bln","OPT")),
    "function_returns": ("string","null")
    }
rotate_camera = {
    "function_location": "view",
    "function_com_id": 519,
    "function_vb_name": "RotateCamera",
    "function_name": "rotate_camera",
    "function_parameters": (("view","str","OPT"),("direction","int","OPT"),("angle","dbl","OPT")),
    "function_returns": ("boolean","null")
    }
rotate_view = {
    "function_location": "view",
    "function_com_id": 650,
    "function_vb_name": "RotateView",
    "function_name": "rotate_view",
    "function_parameters": (("view","str","OPT"),("direction","int","OPT"),("angle","dbl","OPT")),
    "function_returns": ("boolean","null")
    }
show_grid = {
    "function_location": "view",
    "function_com_id": 738,
    "function_vb_name": "ShowGrid",
    "function_name": "show_grid",
    "function_parameters": (("view","str","OPT"),("show","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
show_grid_axes = {
    "function_location": "view",
    "function_com_id": 739,
    "function_vb_name": "ShowGridAxes",
    "function_name": "show_grid_axes",
    "function_parameters": (("view","str","OPT"),("show","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
show_view_title = {
    "function_location": "view",
    "function_com_id": 261,
    "function_vb_name": "ShowViewTitle",
    "function_name": "show_view_title",
    "function_parameters": (("view","str","OPT"),("state","bln","OPT")),
    "function_returns": ()
    }
show_world_axes = {
    "function_location": "view",
    "function_com_id": 740,
    "function_vb_name": "ShowWorldAxes",
    "function_name": "show_world_axes",
    "function_parameters": (("view","str","OPT"),("show","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
synchronize_c_planes = {
    "function_location": "view",
    "function_com_id": 289,
    "function_vb_name": "SynchronizeCPlanes",
    "function_name": "synchronize_c_planes",
    "function_parameters": (("view","str","OPT"),),
    "function_returns": ("boolean","null")
    }
tilt_view = {
    "function_location": "view",
    "function_com_id": 518,
    "function_vb_name": "TiltView",
    "function_name": "tilt_view",
    "function_parameters": (("view","str","OPT"),("direction","int","OPT"),("angle","dbl","OPT")),
    "function_returns": ("boolean","null")
    }
view_c_plane = {
    "function_location": "view",
    "function_com_id": 264,
    "function_vb_name": "ViewCPlane",
    "function_name": "view_c_plane",
    "function_parameters": (("view","str","OPT"),("plane","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
view_camera = {
    "function_location": "view",
    "function_com_id": 394,
    "function_vb_name": "ViewCamera",
    "function_name": "view_camera",
    "function_parameters": (("view","str","OPT"),("camera","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
view_camera_lens = {
    "function_location": "view",
    "function_com_id": 262,
    "function_vb_name": "ViewCameraLens",
    "function_name": "view_camera_lens",
    "function_parameters": (("view","str","OPT"),("length","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
view_camera_plane = {
    "function_location": "view",
    "function_com_id": 778,
    "function_vb_name": "ViewCameraPlane",
    "function_name": "view_camera_plane",
    "function_parameters": (("view","str","OPT"),),
    "function_returns": ("array","null")
    }
view_camera_target = {
    "function_location": "view",
    "function_com_id": 263,
    "function_vb_name": "ViewCameraTarget",
    "function_name": "view_camera_target",
    "function_parameters": (("view","str","OPT"),("camera","array_of dbl","OPT"),("target","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
view_camera_up = {
    "function_location": "view",
    "function_com_id": 517,
    "function_vb_name": "ViewCameraUp",
    "function_name": "view_camera_up",
    "function_parameters": (("view","str","OPT"),("up_vector","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
view_display_mode = {
    "function_location": "view",
    "function_com_id": 290,
    "function_vb_name": "ViewDisplayMode",
    "function_name": "view_display_mode",
    "function_parameters": (("view","str","OPT"),("mode","int","OPT")),
    "function_returns": ("number","number","null")
    }
view_display_mode_ex = {
    "function_location": "view",
    "function_com_id": 910,
    "function_vb_name": "ViewDisplayModeEx",
    "function_name": "view_display_mode_ex",
    "function_parameters": (("view","str","OPT"),("mode","str","OPT"),("return_names","bln","OPT")),
    "function_returns": ("number","number","null")
    }
view_display_mode_name = {
    "function_location": "view",
    "function_com_id": 909,
    "function_vb_name": "ViewDisplayModeName",
    "function_name": "view_display_mode_name",
    "function_parameters": (("mode","str","REQ"),),
    "function_returns": ("string","null")
    }
view_display_modes = {
    "function_location": "view",
    "function_com_id": 908,
    "function_vb_name": "ViewDisplayModes",
    "function_name": "view_display_modes",
    "function_parameters": (("return_name","bln","OPT"),),
    "function_returns": ("array","null")
    }
view_names = {
    "function_location": "view",
    "function_com_id": 265,
    "function_vb_name": "ViewNames",
    "function_name": "view_names",
    "function_parameters": (("return_names","bln","OPT"),("type","int","OPT")),
    "function_returns": ("array","null")
    }
view_near_corners = {
    "function_location": "view",
    "function_com_id": 823,
    "function_vb_name": "ViewNearCorners",
    "function_name": "view_near_corners",
    "function_parameters": (("view","str","OPT"),),
    "function_returns": ("array","null")
    }
view_projection = {
    "function_location": "view",
    "function_com_id": 266,
    "function_vb_name": "ViewProjection",
    "function_name": "view_projection",
    "function_parameters": (("view","str","OPT"),("mode","int","OPT")),
    "function_returns": ("number","number","null")
    }
view_radius = {
    "function_location": "view",
    "function_com_id": 824,
    "function_vb_name": "ViewRadius",
    "function_name": "view_radius",
    "function_parameters": (("view","str","OPT"),("radius","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
view_size = {
    "function_location": "view",
    "function_com_id": 267,
    "function_vb_name": "ViewSize",
    "function_name": "view_size",
    "function_parameters": (("view","str","OPT"),),
    "function_returns": ("array","null")
    }
view_target = {
    "function_location": "view",
    "function_com_id": 395,
    "function_vb_name": "ViewTarget",
    "function_name": "view_target",
    "function_parameters": (("view","str","OPT"),("target","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
view_title = {
    "function_location": "view",
    "function_com_id": 907,
    "function_vb_name": "ViewTitle",
    "function_name": "view_title",
    "function_parameters": (("mode","str","REQ"),),
    "function_returns": ("string","null")
    }
wallpaper = {
    "function_location": "view",
    "function_com_id": 532,
    "function_vb_name": "Wallpaper",
    "function_name": "wallpaper",
    "function_parameters": (("view","str","OPT"),("file_name","str","OPT")),
    "function_returns": ("string","string","null")
    }
wallpaper_gray_scale = {
    "function_location": "view",
    "function_com_id": 534,
    "function_vb_name": "WallpaperGrayScale",
    "function_name": "wallpaper_gray_scale",
    "function_parameters": (("view","str","OPT"),("gray_scale","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
wallpaper_hidden = {
    "function_location": "view",
    "function_com_id": 533,
    "function_vb_name": "WallpaperHidden",
    "function_name": "wallpaper_hidden",
    "function_parameters": (("view","str","OPT"),("hidden","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
zoom_bounding_box = {
    "function_location": "view",
    "function_com_id": 479,
    "function_vb_name": "ZoomBoundingBox",
    "function_name": "zoom_bounding_box",
    "function_parameters": (("corners","array_of dbl","REQ"),("view","str","OPT"),("all","bln","OPT")),
    "function_returns": ()
    }
zoom_extents = {
    "function_location": "view",
    "function_com_id": 375,
    "function_vb_name": "ZoomExtents",
    "function_name": "zoom_extents",
    "function_parameters": (("view","str","OPT"),("all","bln","OPT")),
    "function_returns": ()
    }
zoom_selected = {
    "function_location": "view",
    "function_com_id": 376,
    "function_vb_name": "ZoomSelected",
    "function_name": "zoom_selected",
    "function_parameters": (("view","str","OPT"),("all","bln","OPT")),
    "function_returns": ()
    }
