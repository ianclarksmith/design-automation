
class Cylinder(object):
    
    create_by_plane = """
        base_point = base_plane[0]
        z_axis = _base._rsf.vector_cross_product(base_plane[1], base_plane[2])
        z_axis = _base._rsf.vector_unitize(z_axis)
        z_axis = _base._rsf.vector_scale(z_axis, height)
        height_point = _base._rsf.point_add( base_point, z_axis )
        _rhino_id = _base._rsf.add_cylinder(base_point, height_point, radius, cap)

        if _rhino_id:
            return Cylinder(_rhino_id)
        else:
            return None
"""


class Cone(object):
    
    create_by_plane = """
        base_point = base_plane[0]
        z_axis = _base._rsf.vector_cross_product(base_plane[1], base_plane[2])
        z_axis = _base._rsf.vector_unitize(z_axis)
        z_axis = _base._rsf.vector_scale(z_axis, height)
        height_point = _base._rsf.point_add( base_point, z_axis )
        _rhino_id = _base._rsf.add_cone(base_point, height_point, radius, cap)

        if _rhino_id:
            return Cylinder(_rhino_id)
        else:
            return None
"""