# Auto-generated module that wraps the RhinoscriptFunctions class

_rsf = None

def add_named_c_plane(name, view=None):

    return _rsf.add_named_c_plane(name, view)

def add_named_view(name, view=None):

    return _rsf.add_named_view(name, view)

def background_bitmap(view=None, file_name=None, point=None, width=None):

    return _rsf.background_bitmap(view, file_name, point, width)

def current_detail(layout, detail=None, return_names=None):

    return _rsf.current_detail(layout, detail, return_names)

def current_view(view=None, return_name=None):

    return _rsf.current_view(view, return_name)

def delete_named_c_plane(name):

    return _rsf.delete_named_c_plane(name)

def delete_named_view(name):

    return _rsf.delete_named_view(name)

def detail_names(layout, return_names=None):

    return _rsf.detail_names(layout, return_names)

def is_background_bitmap(view):

    return _rsf.is_background_bitmap(view)

def is_detail(layout, detail):

    return _rsf.is_detail(layout, detail)

def is_layout(layout):

    return _rsf.is_layout(layout)

def is_view(view):

    return _rsf.is_view(view)

def is_view_current(view):

    return _rsf.is_view_current(view)

def is_view_maximized(view=None):

    return _rsf.is_view_maximized(view)

def is_view_perspective(view=None):

    return _rsf.is_view_perspective(view)

def is_view_title_visible(view=None):

    return _rsf.is_view_title_visible(view)

def is_wallpaper(view):

    return _rsf.is_wallpaper(view)

def maximize_restore_view(view=None):

    return _rsf.maximize_restore_view(view)

def named_c_planes():

    return _rsf.named_c_planes()

def named_views():

    return _rsf.named_views()

def rename_view(old_title, new_title):

    return _rsf.rename_view(old_title, new_title)

def restore_named_c_plane(name, view=None):

    return _rsf.restore_named_c_plane(name, view)

def restore_named_view(name, view=None, restore_bitmap=None):

    return _rsf.restore_named_view(name, view, restore_bitmap)

def rotate_camera(view=None, direction=None, angle=None):

    return _rsf.rotate_camera(view, direction, angle)

def rotate_view(view=None, direction=None, angle=None):

    return _rsf.rotate_view(view, direction, angle)

def show_grid(view=None, show=None):

    return _rsf.show_grid(view, show)

def show_grid_axes(view=None, show=None):

    return _rsf.show_grid_axes(view, show)

def show_view_title(view=None, state=None):

    return _rsf.show_view_title(view, state)

def show_world_axes(view=None, show=None):

    return _rsf.show_world_axes(view, show)

def synchronize_c_planes(view=None):

    return _rsf.synchronize_c_planes(view)

def tilt_view(view=None, direction=None, angle=None):

    return _rsf.tilt_view(view, direction, angle)

def view_c_plane(view=None, plane=None):

    return _rsf.view_c_plane(view, plane)

def view_camera(view=None, camera=None):

    return _rsf.view_camera(view, camera)

def view_camera_lens(view=None, length=None):

    return _rsf.view_camera_lens(view, length)

def view_camera_plane(view=None):

    return _rsf.view_camera_plane(view)

def view_camera_target(view=None, camera=None, target=None):

    return _rsf.view_camera_target(view, camera, target)

def view_camera_up(view=None, up_vector=None):

    return _rsf.view_camera_up(view, up_vector)

def view_display_mode_ex(view=None, mode=None, return_names=None):

    return _rsf.view_display_mode_ex(view, mode, return_names)

def view_display_mode_name(mode):

    return _rsf.view_display_mode_name(mode)

def view_display_modes(return_name=None):

    return _rsf.view_display_modes(return_name)

def view_names(return_names=None, type=None):

    return _rsf.view_names(return_names, type)

def view_near_corners(view=None):

    return _rsf.view_near_corners(view)

def view_projection(view=None, mode=None):

    return _rsf.view_projection(view, mode)

def view_radius(view=None, radius=None):

    return _rsf.view_radius(view, radius)

def view_size(view=None):

    return _rsf.view_size(view)

def view_target(view=None, target=None):

    return _rsf.view_target(view, target)

def view_title(mode):

    return _rsf.view_title(mode)

def wallpaper(view=None, file_name=None):

    return _rsf.wallpaper(view, file_name)

def wallpaper_gray_scale(view=None, gray_scale=None):

    return _rsf.wallpaper_gray_scale(view, gray_scale)

def wallpaper_hidden(view=None, hidden=None):

    return _rsf.wallpaper_hidden(view, hidden)

def zoom_bounding_box(corners, view=None, all=None):

    return _rsf.zoom_bounding_box(corners, view, all)

def zoom_extents(view=None, all=None):

    return _rsf.zoom_extents(view, all)

def zoom_selected(view=None, all=None):

    return _rsf.zoom_selected(view, all)

