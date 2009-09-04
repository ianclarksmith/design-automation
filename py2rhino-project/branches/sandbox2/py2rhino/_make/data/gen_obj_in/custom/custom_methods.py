
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
            return Cone(_rhino_id)
        else:
            return None
"""
class _CurveRootFuncClsd(object):
    
    boolean_union = """
        if type(curves) != list and type(curves) != tuple:
            curves = (self, curves)
        else:
            if type(curves) == tuple:
                curves = list(curves)
            curves.append(self)
        _rhino_ids = _base._rsf.curve_boolean_union(map(lambda i: i._rhino_id, curves))
        if _rhino_ids:
            return map(lambda i: p2r.obj.PolyCurve(i), _rhino_ids)
        else:
            return None
"""

class _SurfaceRootFunc(object):
    
    intersect_2_srfs = """
        result = _base._rsf.surface_surface_intersection(self._rhino_id, surface_a._rhino_id, tolerance, create)
        if result:
            curves = []
            for i in result:
                curves.append(p2r.obj.NurbsCurve(i[-1]))
            return curves
        else:
            return None
"""  
    cap_planar_holes = """
        result = _base._rsf.cap_planar_holes(self._rhino_id)
        if result:
            return p2r.obj.PolySurface(self._rhino_id)
        else:
            return None
"""
        
            
class _SurfaceRootFuncClsd(object):
    
    boolean_union = """
        if type(breps) != list and type(breps) != tuple:
            breps = (self, breps)
        else:
            if type(breps) == tuple:
                breps = list(breps)
            breps.append(self)            
        _rhino_ids = _base._rsf.boolean_union(map(lambda i: i._rhino_id, breps), delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.PolySurface(i), _rhino_ids)
        else:
            return None
"""   

     