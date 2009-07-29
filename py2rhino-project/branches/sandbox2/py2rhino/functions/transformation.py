# Auto-generated module that wraps the RhinoscriptFunctions class

_rsf = None

def is_xform_identity(xform):

    return _rsf.is_xform_identity(xform)

def is_xform_similarity(xform):

    return _rsf.is_xform_similarity(xform)

def is_xform_zero(xform):

    return _rsf.is_xform_zero(xform)

def xform_c_plane_to_world(point, plane):

    return _rsf.xform_c_plane_to_world(point, plane)

def xform_change_basis(plane_1, plane_2):

    return _rsf.xform_change_basis(plane_1, plane_2)

def xform_change_basis_2(x_0, y_0, z_0, x_1, y_1, z_1):

    return _rsf.xform_change_basis_2(x_0, y_0, z_0, x_1, y_1, z_1)

def xform_compare(xform_1, xform_2):

    return _rsf.xform_compare(xform_1, xform_2)

def xform_determinant(xform):

    return _rsf.xform_determinant(xform)

def xform_diagonal(value):

    return _rsf.xform_diagonal(value)

def xform_identity():

    return _rsf.xform_identity()

def xform_inverse(xform):

    return _rsf.xform_inverse(xform)

def xform_mirror(point, normal):

    return _rsf.xform_mirror(point, normal)

def xform_multiply(xform_1, xform_2):

    return _rsf.xform_multiply(xform_1, xform_2)

def xform_planar_projection(plane):

    return _rsf.xform_planar_projection(plane)

def xform_rotation(plane_1, plane_2):

    return _rsf.xform_rotation(plane_1, plane_2)

def xform_rotation_2(angle, axis, point):

    return _rsf.xform_rotation_2(angle, axis, point)

def xform_rotation_3(start_dir, end_dir, point):

    return _rsf.xform_rotation_3(start_dir, end_dir, point)

def xform_rotation_4(x_0, y_0, z_0, x_1, y_1, z_1):

    return _rsf.xform_rotation_4(x_0, y_0, z_0, x_1, y_1, z_1)

def xform_scale(plane, x_scale, y_scale, z_scale):

    return _rsf.xform_scale(plane, x_scale, y_scale, z_scale)

def xform_scale_2(x_scale, y_scale, z_scale):

    return _rsf.xform_scale_2(x_scale, y_scale, z_scale)

def xform_scale_3(vector):

    return _rsf.xform_scale_3(vector)

def xform_scale_4(point, scale):

    return _rsf.xform_scale_4(point, scale)

def xform_screen_to_world(point, view=None, convert=None):

    return _rsf.xform_screen_to_world(point, view, convert)

def xform_shear(plane, x_1, y_1, z_1):

    return _rsf.xform_shear(plane, x_1, y_1, z_1)

def xform_translation(vector):

    return _rsf.xform_translation(vector)

def xform_world_to_c_plane(point, plane):

    return _rsf.xform_world_to_c_plane(point, plane)

def xform_world_to_screen(point, view=None, convert=None):

    return _rsf.xform_world_to_screen(point, view, convert)

def xform_zero():

    return _rsf.xform_zero()

