# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_named_c_plane(name, view=pythoncom.Empty):

    return _rsf.add_named_c_plane(name, view)

def add_named_view(name, view=pythoncom.Empty):

    return _rsf.add_named_view(name, view)

def background_bitmap(view=pythoncom.Empty, file_name=pythoncom.Empty, point=pythoncom.Empty, width=pythoncom.Empty):

    return _rsf.background_bitmap(view, file_name, point, width)

def current_detail(layout, detail=pythoncom.Empty, return_names=pythoncom.Empty):

    return _rsf.current_detail(layout, detail, return_names)

def current_view(view=pythoncom.Empty, return_name=pythoncom.Empty):

    return _rsf.current_view(view, return_name)

def delete_named_c_plane(name):

    return _rsf.delete_named_c_plane(name)

def delete_named_view(name):

    return _rsf.delete_named_view(name)

def detail_names(layout, return_names=pythoncom.Empty):

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

def is_view_maximized(view=pythoncom.Empty):

    return _rsf.is_view_maximized(view)

def is_view_perspective(view=pythoncom.Empty):

    return _rsf.is_view_perspective(view)

def is_view_title_visible(view=pythoncom.Empty):

    return _rsf.is_view_title_visible(view)

def is_wallpaper(view):

    return _rsf.is_wallpaper(view)

def maximize_restore_view(view=pythoncom.Empty):

    return _rsf.maximize_restore_view(view)

def named_c_planes():

    return _rsf.named_c_planes()

def named_views():

    return _rsf.named_views()

def rename_view(old_title, new_title):

    return _rsf.rename_view(old_title, new_title)

def restore_named_c_plane(name, view=pythoncom.Empty):

    return _rsf.restore_named_c_plane(name, view)

def restore_named_view(name, view=pythoncom.Empty, restore_bitmap=pythoncom.Empty):

    return _rsf.restore_named_view(name, view, restore_bitmap)

def rotate_camera(view=pythoncom.Empty, direction=pythoncom.Empty, angle=pythoncom.Empty):

    return _rsf.rotate_camera(view, direction, angle)

def rotate_view(view=pythoncom.Empty, direction=pythoncom.Empty, angle=pythoncom.Empty):

    return _rsf.rotate_view(view, direction, angle)

def show_grid(view=pythoncom.Empty, show=pythoncom.Empty):

    return _rsf.show_grid(view, show)

def show_grid_axes(view=pythoncom.Empty, show=pythoncom.Empty):

    return _rsf.show_grid_axes(view, show)

def show_view_title(view=pythoncom.Empty, state=pythoncom.Empty):

    return _rsf.show_view_title(view, state)

def show_world_axes(view=pythoncom.Empty, show=pythoncom.Empty):

    return _rsf.show_world_axes(view, show)

def synchronize_c_planes(view=pythoncom.Empty):

    return _rsf.synchronize_c_planes(view)

def tilt_view(view=pythoncom.Empty, direction=pythoncom.Empty, angle=pythoncom.Empty):

    return _rsf.tilt_view(view, direction, angle)

def view_c_plane(view=pythoncom.Empty, plane=pythoncom.Empty):

    return _rsf.view_c_plane(view, plane)

def view_camera(view=pythoncom.Empty, camera=pythoncom.Empty):

    return _rsf.view_camera(view, camera)

def view_camera_lens(view=pythoncom.Empty, length=pythoncom.Empty):

    return _rsf.view_camera_lens(view, length)

def view_camera_plane(view=pythoncom.Empty):

    return _rsf.view_camera_plane(view)

def view_camera_target(view=pythoncom.Empty, camera=pythoncom.Empty, target=pythoncom.Empty):

    return _rsf.view_camera_target(view, camera, target)

def view_camera_up(view=pythoncom.Empty, up_vector=pythoncom.Empty):

    return _rsf.view_camera_up(view, up_vector)

def view_display_mode_ex(view=pythoncom.Empty, mode=pythoncom.Empty, return_names=pythoncom.Empty):

    return _rsf.view_display_mode_ex(view, mode, return_names)

def view_display_mode_name(mode):

    return _rsf.view_display_mode_name(mode)

def view_display_modes(return_name=pythoncom.Empty):

    return _rsf.view_display_modes(return_name)

def view_names(return_names=pythoncom.Empty, type=pythoncom.Empty):

    return _rsf.view_names(return_names, type)

def view_near_corners(view=pythoncom.Empty):

    return _rsf.view_near_corners(view)

def view_projection(view=pythoncom.Empty, mode=pythoncom.Empty):

    return _rsf.view_projection(view, mode)

def view_radius(view=pythoncom.Empty, radius=pythoncom.Empty):

    return _rsf.view_radius(view, radius)

def view_size(view=pythoncom.Empty):

    return _rsf.view_size(view)

def view_target(view=pythoncom.Empty, target=pythoncom.Empty):

    return _rsf.view_target(view, target)

def view_title(mode):

    return _rsf.view_title(mode)

def wallpaper(view=pythoncom.Empty, file_name=pythoncom.Empty):

    return _rsf.wallpaper(view, file_name)

def wallpaper_gray_scale(view=pythoncom.Empty, gray_scale=pythoncom.Empty):

    return _rsf.wallpaper_gray_scale(view, gray_scale)

def wallpaper_hidden(view=pythoncom.Empty, hidden=pythoncom.Empty):

    return _rsf.wallpaper_hidden(view, hidden)

def zoom_bounding_box(corners, view=pythoncom.Empty, all=pythoncom.Empty):

    return _rsf.zoom_bounding_box(corners, view, all)

def zoom_extents(view=pythoncom.Empty, all=pythoncom.Empty):

    return _rsf.zoom_extents(view, all)

def zoom_selected(view=pythoncom.Empty, all=pythoncom.Empty):

    return _rsf.zoom_selected(view, all)

